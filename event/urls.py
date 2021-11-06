from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from .views import EventViewSet


event_router = SimpleRouter()
event_router.register(r'', EventViewSet)


urlpatterns = event_router.urls