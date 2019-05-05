# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGlucoseEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=0.0)),
                ('units', models.CharField(default=b'mmol/L', max_length=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BloodKetoneEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=0.0)),
                ('units', models.CharField(default=b'mmol/L', max_length=24)),
                ('subtype', models.CharField(max_length=36, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('device_id', models.CharField(max_length=36)),
                ('tidepool_id', models.CharField(max_length=36)),
                ('tidepool_guid', models.CharField(max_length=36)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('timezone_offset', models.IntegerField(default=0)),
                ('upload_id', models.CharField(max_length=36)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('event_type', models.CharField(max_length=36)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(to='event.EventType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='patient',
            field=models.ForeignKey(to='patient.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bloodketoneevent',
            name='event',
            field=models.ForeignKey(to='event.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bloodglucoseevent',
            name='event',
            field=models.ForeignKey(to='event.Event'),
            preserve_default=True,
        ),
    ]
