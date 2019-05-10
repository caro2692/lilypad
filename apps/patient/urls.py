from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PatientView.as_view()),
]
