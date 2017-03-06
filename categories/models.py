# coding: utf-8
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    doctors = models.ManyToManyField('doctors.Doctor', blank=True,
                                     related_name='doctor', verbose_name="Médicos")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
