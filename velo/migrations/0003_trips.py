# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0002_about_contacts_navfiles_news_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('trip_name', models.CharField(max_length=255)),
                ('gpsies_id', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['-trip_name'],
            },
        ),
    ]
