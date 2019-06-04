from rest_framework import serializers
from .models import (
    Event,
    BloodGlucoseEvent,
    BloodKetoneEvent
)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'active',
            'device_id',
            'tidepool_id',
            'tidepool_guid',
            'time',
            'timezone_offset',
            'upload_id',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('id',)


class BloodGlucoseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGlucoseEvent
        fields = (
            'id',
            'active',
            'device_id',
            'tidepool_id',
            'tidepool_guid',
            'time',
            'timezone_offset',
            'upload_id',
            'created_at',
            'updated_at',
            'value',
            'units'
        )
        read_only_fields = ('id',)


class BloodKetoneEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodKetoneEvent
        fields = (
            'id',
            'active',
            'device_id',
            'tidepool_id',
            'tidepool_guid',
            'time',
            'timezone_offset',
            'upload_id',
            'created_at',
            'updated_at',
            'value',
            'units',
            'subtype'
        )
        read_only_fields = ('id',)
