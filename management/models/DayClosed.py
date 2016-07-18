# -*- coding: utf-8 -*-

from django.db import models
from Restaurant import Restaurant
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class DayClosed(models.Model):
    """
    This class represents a day in which the restaurant is closed
    """


    day = models.DateField(
        verbose_name='Fecha de inicio',
        help_text='Fecha de inicio de la temporada',
        blank=False,
        null=False
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return str(self.restaurant) + str(self.day)

    class Meta:
        verbose_name='Día cerrado'
        verbose_name_plural='Días cerrado'
