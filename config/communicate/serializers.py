
from rest_framework import serializers

from communicate.models import Message
from fcm.utils import FCMMessage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('title', 'body')

    def create(self, validated_data):
        message = Message(**validated_data)
        message.save()
        FCMMessage().send({'message':'my test message'}, to='/topics/my-topic')
        
        return message

