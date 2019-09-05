
from rest_framework import serializers
from messaging.models import MyDevice
from communicate.models import Message
from fcm.utils import FCMMessage

class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField(many=False,  slug_field='name', queryset=MyDevice.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='name', queryset=MyDevice.objects.all())

    class Meta:
        model = Message
        fields = ('sender','receiver','title', 'body')

    def create(self, validated_data):
        message = Message(**validated_data)
        message.save()
        # debugging....
        FCMMessage().send({'message':'test message'}, to='/topics/my-topic')#create a sample topic to test
        
        #Can change this to match any fetching criteria to be used..
        # receiver = MyDevice.objects.get(id=Message.receiver)

        # receiver.send_message({'title':Message.title, 'message': Message.body})
        
        return message

