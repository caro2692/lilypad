# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
                ('tidepool_user_id', models.CharField(max_length=36, null=True, blank=True)),
                ('tidepool_username', models.CharField(max_length=56, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
