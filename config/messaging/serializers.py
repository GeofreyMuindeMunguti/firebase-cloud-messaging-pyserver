from rest_framework import serializers
from fcm.models import Device
from fcm.utils import FCMMessage


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('dev_id','reg_id','name','is_active')

 