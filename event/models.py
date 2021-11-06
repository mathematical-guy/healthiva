from django.db import models
from account.models import Patient


event_choices = [
    ("TALK", "TALK"),
    ("SHOPPING", "SHOPPING"),
    ("WALK", "WALK"),
    ("INTERACTION", "INTERACTION")
]



class Event(models.Model):
    event_type = models.CharField(max_length=20, choices=event_choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    patient_associated = models.ForeignKey(Patient, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.event_type