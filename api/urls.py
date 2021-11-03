from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PatientAPI, CaretakerAPI


router = SimpleRouter()
router.register(r'patient', PatientAPI)
router.register(r'caretaker', CaretakerAPI)