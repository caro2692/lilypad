from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from apps.patient import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientView, 'patient')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
