# user_db/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class BorrowRequestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, data):
        data_json = json.loads(data)
        id = text_data_json['id']

        self.send(text_data=json.dumps({
            'id': id
        }))
