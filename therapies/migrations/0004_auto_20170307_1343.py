# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapies', '0003_auto_20170307_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='time',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='time',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='time',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='time',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='time',
            name='weekday',
            field=models.CharField(choices=[(b'seg', b'segunda'), (b'ter', b'terca')], default='', max_length=255, verbose_name=b'WD'),
            preserve_default=False,
        ),
    ]
