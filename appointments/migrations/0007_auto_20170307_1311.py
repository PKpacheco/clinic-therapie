# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_auto_20170307_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekdays',
            name='segunda',
            field=models.BooleanField(max_length=255, verbose_name=b'Segunda de atendimento'),
        ),
    ]
