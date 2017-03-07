# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20170306_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekdays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[(b'seg', b'segunda'), (b'ter', b'terca')], max_length=255, verbose_name=b'Dias de atendimento')),
                ('segunda', models.CharField(max_length=255, verbose_name=b'Segunda de atendimento')),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='weekday',
        ),
        migrations.AddField(
            model_name='appointment',
            name='weekday',
            field=models.ManyToManyField(to='appointments.Weekdays', verbose_name=b'Dias de atendimento'),
        ),
    ]
