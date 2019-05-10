from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(
    r'patient',
    views.PatientView,
    base_name='patient'
)
