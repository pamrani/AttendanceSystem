# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20171117_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='student_name_no',
            new_name='student_roll_no',
        ),
    ]
