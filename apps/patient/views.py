import requests

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from apps.event.models import BloodGlucoseEvent
from apps.event.serializers import BloodGlucoseEventSerializer

from .serializers import PatientSerializer
from .models import Patient


TIDEPOOL_SESSION_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkdXIiOjI1OTIwMDAsImV4cCI6MTU2MjMzNzk4Nywic3ZyIjoibm8iLCJ1c3IiOiIzMTM2NjIyNGMwIn0.d5r4NworAkwztdovDmwdFNuE74qv1vrDTHv5vuoC4i4'
TIDEPOOL_USER_ID = '31366224c0'


class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @detail_route(methods=['get'])
    def events(self, request, pk=None):
        patient = self.get_object()
        events = BloodGlucoseEvent.objects.filter(patient=patient)
        serializer = BloodGlucoseEventSerializer(events, many=True)

        return Response(serializer.data)

    @detail_route(methods=['post'])
    def add_from_tidepool(self, request, pk=None):
        base_url = 'https://int-api.tidepool.org/metadata/users/{}/users?userid={}'.format(
            TIDEPOOL_USER_ID, pk
        )
        headers = {
            'x-tidepool-session-token': TIDEPOOL_SESSION_TOKEN
        }
        tidepool_resp = requests.get(base_url, headers=headers)
        user = tidepool_resp.json()[0]
        patient, created = Patient.objects.get_or_create(
            name=user['profile']['fullName'],
            active=True,
            tidepool_userid=pk,
            tidepool_username=user['username']
        )
        serializer = PatientSerializer(patient)

        if patient and not created:
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.data)
