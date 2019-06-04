from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

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
