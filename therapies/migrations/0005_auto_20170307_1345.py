# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapies', '0004_auto_20170307_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='weekday',
            field=models.CharField(choices=[(b'monday', b'2\xc2\xaa'), (b'tuesday', b'3\xc2\xaa'), (b'wednesday', b'4\xc2\xaa'), (b'thursday', b'5\xc2\xaa'), (b'friday', b'6\xc2\xaa')], max_length=255, verbose_name=b'WD'),
        ),
    ]
