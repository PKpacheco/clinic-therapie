# coding: utf-8
from django.db import models

WEEKDAYS = (
    ('monday', '2ª'),
    ('tuesday', '3ª'),
    ('wednesday', '4ª'),
    ('thursday', '5ª'),
    ('friday', '6ª')

)


class Therapie(models.Model):
    doctors = models.ForeignKey('doctors.Doctor', blank=True, verbose_name="Médico")
    terapy = models.ForeignKey('categories.Category', blank=True, verbose_name="Categoria")

    def __unicode__(self):
        return str(self.doctors)

    class Meta:
        verbose_name = 'Atendimento'
        ordering = ['doctors']


class Time(models.Model):
    terapy = models.ForeignKey('Therapie', blank=True, verbose_name="Terapia")

    weekday = models.CharField(choices=WEEKDAYS, max_length=255, verbose_name="Dias")
    one = models.BooleanField(max_length=255, verbose_name="9:00-10:00")
    two = models.BooleanField(max_length=255, verbose_name="10:00-11:00")
    three = models.BooleanField(max_length=255, verbose_name="11:00-12:00")
    four = models.BooleanField(max_length=255, verbose_name="12:00-13:00")
    five = models.BooleanField(max_length=255, verbose_name="13:00-14:00")
    six = models.BooleanField(max_length=255, verbose_name="14:00-15:00")
    seven = models.BooleanField(max_length=255, verbose_name="15:00-16:00")

    def __unicode__(self):
        return str(self.terapy)

    class Meta:
        verbose_name = 'Horário'
        ordering = ['terapy']
