from rest_framework.views import APIView
from rest_framework.response import Response

from apps.event.models import BloodGlucoseEvent
# from .serializers import BloodGlucoseReportSerializer


class BloodGlucoseReportView(APIView):

    def get(self, request):
        users = ['blah', 'test']
        return Response(users)
