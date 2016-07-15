# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import moneyed
from djmoney.models.fields import MoneyField
from django.db import models

@python_2_unicode_compatible
class Dish(models.Model):
    CH_DISH_TYPE = (
        ('APE', "Aperitivo"),
        ('ENT', "Entrante"),
        ('PRI', "Princiapal"),
        ('POS', "Postre"),
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Nombre",
        blank=False
    )

    type = models.CharField(
        max_length=3,
        choices=CH_DISH_TYPE,
        blank=False,
        verbose_name="Tipo"
    )

    description = models.TextField(
        verbose_name="Descripción",
        blank=True
    )

    price = MoneyField(
        verbose_name="Precio",
        max_digits=10,
        decimal_places=2,
        default_currency='EUR',
        blank=True)

    pub_date = models.DateTimeField(
        verbose_name="Fecha de publicación",
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"
