from django.db import models


class Patient(models.Model):
    patient_id = models.CharField(max_length=200)
