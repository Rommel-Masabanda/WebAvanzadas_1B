import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Mensaje
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
         
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username': user.username,
            }
        )
    
    def chat_message(self, event):
        message = event['message']
        username = event['username']

        if self.scope['user'].username == username:
            
                user = User.objects.get(username=username)
                Mensaje.objects.create(mensaje=message, usuario=user)
           

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username': username
        }))

        

    