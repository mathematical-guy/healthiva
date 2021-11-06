from django.contrib import admin
from .models import Patient, Caretaker


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'gender',
        'risk',
        'phone',
    ]

@admin.register(Caretaker)
class CaretakerAdmin(admin.ModelAdmin):
    list_display = [
        'caretaker',
        'patient_associated',
        'phone',
    ]