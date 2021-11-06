from rest_framework.serializers import ModelSerializer
from .models import Patient, Caretaker
from event.models import Event




class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'patient',
            'gender',
            'risk',
            'phone',
        ]


    def to_representation(self, instance):
        context = super().to_representation(instance)
        events = Event.objects.filter(patient_associated=instance.id)
        patient_events = []
        
        for val in events:
            patient_events.append([val.event_type, val.start_time, val.start_time])
        context['events'] = patient_events
        
        return context



class CaretakerSerializer(ModelSerializer):
    class Meta:
        model = Caretaker
        fields = [
            'caretaker',
            'patient_associated',
            'phone',
        ]

    
    
    def to_representation(self, instance):
        context = super().to_representation(instance)
        patient = instance.patient_associated
        events = Event.objects.filter(patient_associated=patient)
        patient_events = []
        
        for val in events:
            patient_events.append([val.event_type, val.start_time, val.start_time])
        context['events'] = patient_events
        
        return context