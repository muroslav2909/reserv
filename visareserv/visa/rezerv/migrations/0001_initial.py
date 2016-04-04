# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateChecker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('name', models.CharField(blank=True, help_text='Name of company.', max_length=200, null=True)),
                ('nationality', models.CharField(choices=[(b'Ukraine', b'Ukraine')], default=b'Ukraine', max_length=20, null=True)),
                ('status', models.CharField(choices=[(b'Stop', b'Stop'), (b'Run', b'Run')], default='UKRAINE', max_length=20, null=True)),
                ('period', models.IntegerField(default=10, help_text='Max count parsed object per day.')),
            ],
        ),
        migrations.CreateModel(
            name='DateCheckerBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, help_text='Example of field for saving some information.', max_length=500, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('free_date', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, default=None, help_text='The company that is owner of this element.', null=True, on_delete=django.db.models.deletion.CASCADE, to='rezerv.DateChecker')),
            ],
        ),
    ]
