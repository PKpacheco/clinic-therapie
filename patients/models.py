# coding: utf-8
from datetime import datetime, date
from django.db import models

CITY = (
    ('Mendoza', 'Mendoza'),
    ('General Alvear', 'General Alvear'),
    ('General San Martín', 'General San Martín'),
    ('Godoy Cruz', 'Godoy Cruz'),
    ('Guaymallén', 'Guaymallén'),
    ('Junín', 'Junín'),
    ('La Paz', 'La Paz'),
    ('Las Heras', 'Las Heras'),
    ('Lavalle', 'Lavalle'),
    ('Luján de Cuyo ', 'Luján de Cuyo '),
    ('Maipú ', 'Maipú '),
    ('Malargüe', 'Malargüe'),
    ('Rivadavia', 'Rivadavia'),
    ('San Carlos ', 'San Carlos'),
    ('San Rafael ', 'San Rafael'),
    ('Santa Rosa ', 'Santa Rosa'),
    ('Tunuyán', 'Tunuyán'),
    ('Tupungato ', 'Tupungato'),
    ('outros', 'Outros'),
)


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    dni = models.CharField(verbose_name='DNI', max_length=255, unique=True)

    primary_contact_phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Contato principal')
    telephone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone')
    cellphone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Celular')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='email')
    address = models.CharField(max_length=15, null=True, blank=True, verbose_name='endereço')
    city = models.CharField(max_length=15, choices=CITY, null=True, blank=True, verbose_name='Cidade')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Responsavel'
        verbose_name_plural = 'Responsaveis'
        ordering = ['name']


class Child(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome da criança")
    age = models.CharField(max_length=10, blank=True, null=True)
    date_birth = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    person = models.ForeignKey(Person, blank=True, null=True, related_name='children', verbose_name="Responsável")

    def __unicode__(self):
        return self.name

    def name_parent(self):
        return self.person

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


def get_object(self):
    return self.request.user
