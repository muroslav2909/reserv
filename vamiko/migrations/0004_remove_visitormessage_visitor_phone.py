# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vamiko', '0003_visitormessage_visitor_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitormessage',
            name='visitor_phone',
        ),
    ]