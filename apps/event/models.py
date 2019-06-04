from django.db import models
from django.utils import timezone

from apps.patient.models import Patient


class Event(models.Model):
    patient = models.ForeignKey(Patient)
    active = models.BooleanField(default=True)
    device_id = models.CharField(max_length=36)
    tidepool_id = models.CharField(max_length=36)
    tidepool_guid = models.CharField(max_length=36)
    time = models.DateTimeField(default=timezone.now)
    timezone_offset = models.IntegerField(default=0)
    upload_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class BloodGlucoseEvent(Event):
    value = models.FloatField(default=0.0)
    units = models.CharField(max_length=24, default='mmol/L')


class BloodKetoneEvent(Event):
    value = models.FloatField(default=0.0)
    units = models.CharField(max_length=24, default='mmol/L')
    subtype = models.CharField(max_length=36, blank=True)
