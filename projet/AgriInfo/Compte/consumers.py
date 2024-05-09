import json


from django.utils import timezone
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async #utilisation pour stocker les info dans db sans recharger la page
from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name

        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        user_profile_picture = data['user_profile_picture']
        #date = data['date']
        await self.save_message(username,room,message)
        #enregistrer les données dans db avant de continuer le traitement
        #await self.save_message(username,room,message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
                'user_profile_picture': user_profile_picture,
                'date_added': datetime.now().strftime("%d %b %Y %H:%M")
        
            }
        )
        
        
    async def chat_message(self,event):
        message = event['message']
        username = event['username']
        room = event['room']
        user_profile_picture = event['user_profile_picture']
        date_added = event['date_added']

        await self.send(text_data=json.dumps(
            {
                'message':message,
                'username':username,
                'room':room,
                'user_profile_picture': user_profile_picture,
                'date_added':date_added,
            }
        ))

    #pour enregistrer les donnee dans db
    @sync_to_async
    def save_message(self, username, room, message):
        user = Utilisateur.objects.get(username=username)
        room = Forum.objects.get(id=room)

        new_message = Message_forum.objects.create(user=user, room=room, content=message)
        new_message.save()