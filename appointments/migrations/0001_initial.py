# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('categories', '0003_category_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('doctors', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctor', verbose_name=b'M\xc3\xa9dico')),
                ('terapy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name=b'Categoria')),
            ],
            options={
                'ordering': ['doctors'],
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
    ]