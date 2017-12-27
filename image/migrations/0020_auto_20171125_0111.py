# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0019_auto_20171123_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student_roll_no',
            field=models.ManyToManyField(blank=True, to='image.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='course_id',
            field=models.ManyToManyField(blank=True, to='image.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='lecture_id',
            field=models.ManyToManyField(blank=True, to='image.Lecture'),
        ),
    ]
