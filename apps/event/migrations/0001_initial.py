# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        ),
        migrations.CreateModel(
            name='BloodGlucoseEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.Event')),
                ('value', models.FloatField(default=0.0)),
                ('units', models.CharField(default='mmol/L', max_length=24)),
            ],
            bases=('event.event',),
        ),
        migrations.CreateModel(
            name='BloodKetoneEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.Event')),
                ('value', models.FloatField(default=0.0)),
                ('units', models.CharField(default='mmol/L', max_length=24)),
                ('subtype', models.CharField(blank=True, max_length=36)),
            ],
            bases=('event.event',),
        ),
        migrations.AddField(
            model_name='event',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]