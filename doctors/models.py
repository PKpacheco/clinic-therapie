# coding: utf-8
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


class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    dni = models.CharField(verbose_name='DNI', max_length=255, unique=True)

    primary_contact_phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Contato principal')
    telephone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone')
    cellphone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Celular')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='email')
    address = models.CharField(max_length=15, null=True, blank=True, verbose_name='endereço')
    city = models.CharField(max_length=15, choices=CITY, null=True, blank=True, verbose_name='Cidade')
    category = models.ManyToManyField('categories.Category', blank=True,
                                      related_name='doctor', verbose_name="Categoria")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['name']
