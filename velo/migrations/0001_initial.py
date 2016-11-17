# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('announce_text', models.TextField(blank=True, max_length=512, verbose_name='announce')),
                ('text', models.TextField(max_length=4096, verbose_name='text')),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'articles',
            },
        ),
    ]
