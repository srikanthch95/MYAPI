from rest_framework import serializers
from .models import User,ActivityPeriod

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields =['start_time','end_time']

class UserSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True,read_only=True)

    class Meta:
        model = User
        fields = ['user_id','real_name','time_zone','activities']