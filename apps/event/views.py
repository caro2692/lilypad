from rest_framework import viewsets
from .serializers import (
    EventSerializer,
    BloodGlucoseEventSerializer,
    BloodKetoneEventSerializer
)
from .models import (
    Event,
    BloodGlucoseEvent,
    BloodKetoneEvent
)


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class BloodGlucoseEventView(viewsets.ModelViewSet):
    serializer_class = BloodGlucoseEventSerializer
    queryset = BloodGlucoseEvent.objects.all()


class BloodKetoneEventView(viewsets.ModelViewSet):
    serializer_class = BloodKetoneEventSerializer
    queryset = BloodKetoneEvent.objects.all()
