from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from apps.event.models import BloodGlucoseEvent
from apps.event.serializers import BloodGlucoseEventSerializer

from .serializers import PatientSerializer
from .models import Patient


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
        # TODO: pull patient from Tidepool api by pk
        patient, created = Patient.objects.get_or_create(
            name='Todd Test',
            active=True,
            tidepool_userid=pk,
            tidepool_username='blah'
        )
        serializer = PatientSerializer(patient)

        if patient and not created:
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.data)
