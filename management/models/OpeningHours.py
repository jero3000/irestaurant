# -*- coding: utf-8 -*-

from django.db import models
from Season import Season
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class OpeningHours(models.Model):
    """
    This class represent a pattern of opening hours in a Season
    """
    CH_WEEKDAYS = (
        ('lu', 'Lunes'),
        ('ma', 'Martes'),
        ('mx', 'Miércoles'),
        ('ju', 'Jueves'),
        ('vi', 'Viernes'),
        ('sa', 'Sábado'),
        ('do', 'Domingo'),
    )

    temporada = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        verbose_name='Temporada',
        blank=False,
        null=False
    )

    weekdays = models.CharField(
        max_length=100,
        choices=CH_WEEKDAYS,
        verbose_name='Días de la semana',
        help_text='Días de la semana en los que aplica este horario',
        blank=False,
        null=False
    )

    def __str__(self):
        return self.weekdays

    class Meta:
        verbose_name='Horas de apertura'
        verbose_name_plural='Horas de apertura'
