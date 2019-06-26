import pandas as pd

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
        ).order_by('time')

        # create pandas dataframe
        df = pd.DataFrame(list(events.values('value', 'units', 'time', 'id')))
        # add column for date
        df['date'] = df.apply(lambda row: row.time.date(), axis=1)

        resp = {
            'patient_name': patient.name,
            'average_per_day': df['date'].value_counts().mean(),
            'lowest_per_day': df['date'].value_counts().min(),
            'highest_per_day': df['date'].value_counts().max()
        }

        return Response(resp)
