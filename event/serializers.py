from rest_framework.serializers import ModelSerializer
from event.models import Event
from rest_framework import serializers


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


    def validate(self, data):
        if(data['start_time'] > data['end_time']):
            raise serializers.ValidationError("Please enter correct timings")
        return data
