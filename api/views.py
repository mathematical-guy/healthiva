from django.shortcuts import render
from account.models import Patient, Caretaker
from account.serializers import PatientSerializer, CaretakerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    
    # def get_renderer_context(self):
    #     context = super().get_renderer_context()
    #     context['name'] = 'mohit'
    #     return context




class CaretakerViewSet(ModelViewSet):
    queryset = Caretaker.objects.all()
    serializer_class = CaretakerSerializer
    permission_classes = [IsAuthenticated]