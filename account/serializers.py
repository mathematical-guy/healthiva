from rest_framework.serializers import ModelSerializer
from .models import Patient, Caretaker



class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class CaretakerSerializer(ModelSerializer):
    class Meta:
        model = Caretaker
        fields = '__all__'