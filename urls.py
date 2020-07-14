from django.conf.urls import include, url
from django.contrib import admin
from apps.patient.urls import router as patient_router
from apps.event.urls import router as event_router
from apps.report.views import BloodGlucoseReportView

api_urls = (patient_router.urls + event_router.urls)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^api/blood_glucose_report/', BloodGlucoseReportView.as_view(), name='blood_glucose_report'),
]
