# coding: utf-8
from django.db import models


class Appointment(models.Model):
    doctors = models.Primarykey('doctors.Doctor', blank=True, verbose_name="Médico")
    terapy = models.Primarykey('categories.Category', blank=True, verbose_name="Categoria")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
