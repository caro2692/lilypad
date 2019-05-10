from rest_framework import viewsets
from .serializers import PatientSerializer
from .models import Patient


class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
