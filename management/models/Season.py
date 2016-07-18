# -*- coding: utf-8 -*-

from django.db import models
from Restaurant import Restaurant
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Season(models.Model):
    """
    This class represents a season in a restaurant time schedule (opening hours)
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Nombre',
        blank=True,
        null=True
    )

    begin = models.DateField(
        verbose_name='Fecha de inicio',
        help_text='Fecha de inicio de la temporada',
        blank=False,
        null=False
    )

    end = models.DateField(
        verbose_name='Fecha de fin',
        help_text='Fecha de fin de la temporada',
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
        return str(self.restaurant) + str(self.begin) + " - " + str(self.end)

    class Meta:
        verbose_name='Temporada'
        verbose_name_plural='Temporadas'
