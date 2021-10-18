from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync,sync_to_async
from channels.consumer import SyncConsumer
import json
from django.contrib.auth.models import User
from FTC_users.models import Thread,Message
from datetime import datetime

class PersonalChat(WebsocketConsumer):

    def connect(self):
        print("consumer called")
        me=self.scope['url_route']['kwargs']['first_user']
        second_user_username=self.scope['url_route']['kwargs']['second_user']
        print("sender",me)
        print("receiver",second_user_username)
        first_user=User.objects.get(username=me)
        second_user=User.objects.get(username=second_user_username)
        self.thread_obj=Thread.objects.get_or_create_personal_thread(first_user,second_user)

        self.room_group_name=f'personal_thread_{self.thread_obj.id}'
        print("group name:",self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name
        )
        #self.send(
        #    {
        #        'type':'websocket.accept'
        #    }
        #)
        self.accept()

        print("user connected",second_user)
        #self.send(text_data=json.dumps({'status' : 'connected here','room_name':self.room_name}))


    def websocket_receive(self,event):
        print("hello")
        data=event.get('text')
        data = json.loads(data)
        print(data)
        data=data['message']
        self.username=self.scope['url_route']['kwargs']['first_user']
        print(self.username)
        sender=self.username
        print("data:",data)
        now=datetime.now()
        print(now)
        data_dict={
            'text':data,
            'time_stamp':now
        }
        self.store_message(data_dict)
        print(self.room_group_name)
        async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
            {
                'type':'send.order',
                'value':data,
                'sender':sender,
                'time_stamp':now
                
            }
        )
      
    def send_order(self,event):
        print("sending msg to client")
        print (event['value'])
        message=event['value']
        sender=event['sender']
        time_stamp=str(event['time_stamp'])
        self.send(text_data=json.dumps({
                
                'message':message,
                'sender':sender,
                'time_stamp':time_stamp
        }))
    
    def websocket_disconnect(self,*args,**kwargs):
        print("disconnected",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
             self.room_group_name,
             self.channel_name
       
        )
        self.close()

    def store_message(self,text):
        sender=self.scope['url_route']['kwargs']['first_user']
        first_user=User.objects.get(username=sender)
        print(text['text'])
        now=text['time_stamp']
        Message.objects.create(
            thread=self.thread_obj,
            sender=first_user,
            text=text['text'],
            created_at=now

        )
        
class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name='test_consumer_group'
        self.username=self.scope['url_route']['kwargs']['username']
        print(self.username)

        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name
        )
        
        self.accept()
        #self.send(text_data=json.dumps({'status' : 'connected here','room_name':self.room_name}))


    def receive(self,text_data):
        print("hello")
        data = json.loads(text_data)
        print(data)
        self.username=self.scope['url_route']['kwargs']['username']
        print(self.username)
        sender=self.username
        now=datetime.now()
        data_dict={
            'text':data,
            'time_stamp':now
        }
        
        d=self.username + ' : ' + data['message']
        async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
            {
                'type':'send.order',
                'value':data['message'],
                'sender':sender,
                'time_stamp':now
            }
        )
      
    def send_order(self,event):
        print("sending msg to client")
        print (event['value'])
        message=event['value']
        sender=event['sender']
        time_stamp=str(event['time_stamp'])
        self.send(text_data=json.dumps({
            'message':message,
                'sender':sender,
                'time_stamp':time_stamp
        }))
    
    def disconnect(self,*args,**kwargs):
        print("disconnected")
        async_to_sync(self.channel_layer.group_discard)(
             self.room_group_name,
             self.channel_name
       
        )

