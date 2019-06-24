import statistics

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.patient.models import Patient
from apps.event.models import BloodGlucoseEvent


class BloodGlucoseReportView(APIView):

    def get(self, request):
        patient_id = request.query_params.get('patient')
        startDate = request.query_params.get('startDate')
        endDate = request.query_params.get('endDate')
        patient = Patient.objects.get(id=patient_id)
        events = BloodGlucoseEvent.objects.filter(
            patient=patient,
            time__range=(startDate, endDate)
        )

        ordered_events = events.order_by('value')
        values = [e.value for e in ordered_events]

        resp = {
            'average_per_day': statistics.mean(values),
            'lowest_per_day': ordered_events.first().value,
            'highest_per_day': ordered_events.last().value
        }

        return Response(resp)
