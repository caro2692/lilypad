from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    tidepool_userid = models.CharField(max_length=36, null=True, blank=True)
    tidepool_username = models.CharField(max_length=56, null=True, blank=True)

    def __str__(self):
        return self.name
