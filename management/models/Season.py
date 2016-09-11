# -*- coding: utf-8 -*-

from django.db import models
from Restaurant import Restaurant
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Season(models.Model):
    """
    This class represents a season in a restaurant time schedule (opening hours)
    """

    name = models.CharField(
        max_length=200,
        verbose_name=_('Name'),
        blank=True,
        null=True
    )

    begin = models.DateField(
        verbose_name=_('Begin'),
        help_text=_('Season begin date'),
        blank=False,
        null=False
    )

    end = models.DateField(
        verbose_name=_('End'),
        help_text=_('Season end date'),
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
        return str(self.restaurant) + " " + str(self.begin) + " - " + str(self.end)

    class Meta:
        verbose_name=_('Season')
        verbose_name_plural=_('Seasons')
