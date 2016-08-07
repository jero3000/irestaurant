# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from OpeningHours import OpeningHours
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class TimeSlot(models.Model):
    """
    This class represent a time slot in which the restaurant is opened
    """

    begin = models.TimeField(
        verbose_name=_('Begin'),
        blank=False,
        null=False
    )

    end = models.TimeField(
        verbose_name=_('End'),
        blank=False,
        null=False
    )

    hours = models.ForeignKey(
        OpeningHours,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return str(self.begin) + " - " + str(self.end)

    class Meta:
        verbose_name = _('Time slot')
        verbose_name_plural = _('Time slots')
