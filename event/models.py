from django.db import models
from django.utils import timezone


class EventType(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=36)


class Event(models.Model):
    active = models.BooleanField(default=True)
    device_id = models.CharField(max_length=36)
    tidepool_id = models.CharField(max_length=36)
    tidepool_guid = models.CharField(max_length=36)
    time = models.DateTimeField(default=timezone.now)
    timezone_offset = models.IntegerField(default=0)
    upload_id = models.CharField(max_length=36)
    type_id = models.ForeignKey(EventType)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class BloodGlucoseEvent(models.Model):
    event_id = models.ForeignKey(Event)
    value = models.FloatField(default=0.0)
    units = models.CharField(max_length=24, default='mmol/L')


class BloodKetoneEvent(models.Model):
    event_id = models.ForeignKey(Event)
    value = models.FloatField(default=0.0)
    units = models.CharField(max_length=24, default='mmol/L')
    subtype = models.CharField(max_length=36, blank=True)
