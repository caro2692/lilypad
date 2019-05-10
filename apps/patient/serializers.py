from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'name',
            'active',
            'tidepool_userid',
            'tidepool_username'
        )
        read_only_fields = ('id',)
