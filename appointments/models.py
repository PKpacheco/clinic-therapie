# coding: utf-8
from django.db import models


class Appointment(models.Model):
    therapie = models.ForeignKey('therapies.Therapie', blank=True, verbose_name="Terapia")
    child = models.ForeignKey('patients.Child', blank=True, verbose_name="Paciente")

    def __unicode__(self):
        return str(self.child)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['therapie']
