# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0014_auto_20171121_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_date_time',
            field=models.DateTimeField(auto_now_add=True, help_text='Date of the Lecture'),
        ),
    ]
