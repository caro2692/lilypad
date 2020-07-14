from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(
    r'event',
    views.EventView,
    base_name='event'
)

router.register(
    r'blood_glucose_event',
    views.BloodGlucoseEventView,
    base_name='blood_glucose_event'
)

router.register(
    r'blood_ketone_event',
    views.BloodKetoneEventView,
    base_name='blood_ketone_event'
)
