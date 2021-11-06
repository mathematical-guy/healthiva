from django.shortcuts import render
from event.serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
from event.models import Event



class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    