# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre",
        blank=False
    )

    address = models.CharField(
        max_length=200,
        verbose_name="Dirección"
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número de telefono debe tener el siguiente formato: '+999999999'. No más de 15 dígitos"
    )

    telephone = models.CharField(
        max_length=20,
        validators=[phone_regex],
        verbose_name="Telefono"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"