# user_db/consumers.py
import json
import logging
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer
import uuid
from channels.db import database_sync_to_async
from .lottery import lottery

import django
django.setup()

from .models import Record,User
from clients.models import Client
from restaurants_db.models import Restaurant
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

DEPOSIT = 10    

class QRRequestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        Client.objects.filter(channel_name=self.channel_name).delete()

    def receive(self, text_data):
        data_json = json.loads(text_data)
        user_id = data_json['user_id']
        logging.debug(user_id)


        pid = uuid.uuid4()
        pid_str = str(pid)

        user = User.objects.get(id=user_id)
        client = Client(channel_name=self.channel_name,pid=pid,user=user)
        client.save()
        
        self.send(text_data=json.dumps({
            'response_type' : 'RECEIVED',
            'pid': pid_str 
            }
        ))   
    def request_result(self,event):
        self.send(text_data=event["text"])   

class QRVerificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data_json = json.loads(text_data)
        pid_str = data_json['pid']
        r_id_str = data_json['r_id']
        mode = data_json['mode']
        if mode != "COUPON":
            amount =data_json['amount']
        
        try:
           restaurant= Restaurant.objects.get(id =uuid.UUID(r_id_str)) 
        except:
            self.send(text_data=json.dumps({
                'result': "failed",
                "reason": "Invalid restaurant account"
            }))

        try:
            client = Client.objects.get(pid=uuid.UUID(pid_str))
        except:
            self.send(text_data=json.dumps({
                'result': "failed",
                "reason": "Invalid QR code "
            }))

        record = Record()
        if (mode=="TOP UP"):
            record.balance_delta = int(amount)
            record.record_type = 'T'
            record.g_cash_delta= 0
        elif (mode == "LEND"):
            record.balance_delta = int(amount) * -1 *DEPOSIT
            record.record_type='B'
            record.g_cash_delta = 0
        else:
            record.balance_delta = int (amount)*DEPOSIT
            record.record_type='R'
            record.g_cash_delta = lottery()
            

        record.user = client.user
        record.date_time = datetime.now()
        record.restaurant = restaurant  

        record.save()

        self.send(text_data=json.dumps({
            'result' : 'success',
            }
        ))
        channel_layer = get_channel_layer()
        message = {
            "response_type" : "COMPLETED",
            "mode":mode,
            "r_name":restaurant.name,
            "r_id": str(restaurant.id),
            "amount": amount,
            "g_cash": record.g_cash_delta,

        }
        async_to_sync(channel_layer.send)(client.channel_name, {
            "type": "request.result",
            "text": json.dumps(message)
            })      
        
        Client.objects.filter(channel_name=self.channel_name).delete()



       