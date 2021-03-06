# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('therapies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(max_length=255, verbose_name=b'2')),
                ('tuesday', models.BooleanField(max_length=255, verbose_name=b'3')),
                ('wednesday', models.BooleanField(max_length=255, verbose_name=b'4')),
                ('thursday', models.BooleanField(max_length=255, verbose_name=b'5')),
                ('one', models.BooleanField(max_length=255, verbose_name=b'9:00-10:00')),
                ('two', models.BooleanField(max_length=255, verbose_name=b'10:00-11:00')),
                ('three', models.BooleanField(max_length=255, verbose_name=b'11:00-12:00')),
                ('four', models.BooleanField(max_length=255, verbose_name=b'12:00-13:00')),
                ('five', models.BooleanField(max_length=255, verbose_name=b'13:00-14:00')),
                ('friday', models.BooleanField(max_length=255, verbose_name=b'14:00-15:00')),
            ],
        ),
        migrations.RemoveField(
            model_name='therapie',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='therapie',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='therapie',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='therapie',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='therapie',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='time',
            name='terapy',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='therapies.Therapie', verbose_name=b'Terapia'),
        ),
    ]
