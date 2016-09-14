# -*- coding: utf-8 -*-

from django.db import models
from Restaurant import Restaurant
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class DayClosed(models.Model):
    """
    This class represents a day in which the restaurant is closed
    """


    day = models.DateField(
        verbose_name=_('Day closed'),
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
        return str(self.restaurant) + " " + str(self.day)

    class Meta:
        verbose_name=_('Day closed')
        verbose_name_plural=_('Days closed')
