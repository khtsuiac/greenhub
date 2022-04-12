# user_db/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
import uuid
from .models import Record,User
from clients.models import Client
from asgiref.sync import async_to_sync

class QRRequestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        Client.objects.filter(channel_name=self.channel_name).delete()

    def receive(self, text_data):
        data_json = json.loads(text_data)
        user_id = data_json['user_id']

        pid = str(uuid.uuid4())
        
        user = User.objects.get(id =user_id)
        Client.objects.create(channel_name=self.channel_name,pid=pid)
        
        self.send(text_data=json.dumps({
            'response_type' : 'RECEIVED'
            'pid': pid 
            }
        )) 

        


       