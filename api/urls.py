from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from .views import PatientViewSet, CaretakerViewSet


api_router = SimpleRouter()
api_router.register(r'patient', PatientViewSet)
api_router.register(r'caretaker', CaretakerViewSet)


urlpatterns = api_router.urls