# coding: utf-8

from django.db import models
from datetime import datetime, date


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    dni = models.EmailField(verbose_name='DNI', max_length=255, unique=True)

    primary_contact_phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Contato principal')
    cellphone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Celular')
    email = models.CharField(max_length=20, blank=True, null=True, verbose_name='email')
    address = models.CharField(max_length=15, null=True, blank=True, verbose_name='Celular')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Responsavel'
        verbose_name_plural = 'Responsaveis'
        ordering = ['name']


class Child(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da Criança")
    age = models.CharField(max_length=10, blank=True, null=True)
    date_birth = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    person = models.ForeignKey(Person, blank=True, null=True, related_name='children', verbose_name="Responsável")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Crianca'
        verbose_name_plural = 'Criancas'
        ordering = ['name']

    def age(bday, d=None):
        if d is None:
            d = date.today()
        return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))

    def update_age():
        for child in Child.objects.all():
            _age = age(child.date_birth)
            child.age = str(_age)
            child.save()
