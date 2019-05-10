from django.views.generic import ListView
# from django.http import HttpResponse

from .models import Patient
# from .utils import get_user_data


class PatientList(ListView):
    model = Patient


# def index(request):
#     response = get_user_data()
#     django_response = HttpResponse(
#         content=response.content,
#         status=response.status_code,
#         content_type=response.headers['Content-Type']
#     )
#     return django_response
