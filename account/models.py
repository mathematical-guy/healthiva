from django.db import models
from django.contrib.auth.models import User





gender_choices = [
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHERS", "OTHERS"),
]


risk_choices = [
    ("LOW", "LOW"),
    ("MEDIUM", "MEDIUM"),
    ("HIGH", "HIGH"),
]


class Patient(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choices)
    risk = models.CharField(max_length=10, choices=risk_choices)
    phone = models.CharField(max_length=13)


    def __str__(self):
        return self.patient.username


class Caretaker(models.Model):
    caretaker = models.OneToOneField(User, on_delete=models.CharField)
    patient_associated = models.ForeignKey(Patient, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)


    def __str__(self):
        return self.caretaker.username