# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator
from Restaurant import Restaurant


class Address(models.Model):
    """
    This class represent a restaurant address
    """

    line1 = models.CharField(
        max_length=200,
        verbose_name='Linea 1 de dirección',
        help_text='Calle y número, apartado de correos, nombre empresa',
        blank=False,
        null=False
    )

    line2 = models.CharField(
        max_length=200,
        verbose_name='Linea 2 de dirección',
        help_text='Otra información adicional',
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=200,
        verbose_name='Ciudad',
        blank=False,
        null=False
    )

    state = models.CharField(
        max_length=200,
        verbose_name='Provincia',
        blank=False,
        null=False
    )

    postal_code = models.CharField(
        max_length=200,
        verbose_name='Código postal',
        blank=False,
        null=False
    )

    pais = models.CharField(
        max_length=200,
        verbose_name='Pais',
        blank=False,
        null=False
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

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.line1

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
