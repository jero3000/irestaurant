# -*- coding: utf-8 -*-

from django.db import models
from Season import Season
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class OpeningHours(models.Model):
    """
    This class represent a pattern of opening hours in a Season
    """
    CH_WEEKDAYS = (
        ('lu', _('Monday')),
        ('ma', _('Tuesday')),
        ('mx', _('Wednesday')),
        ('ju', _('Thursday')),
        ('vi', _('Friday')),
        ('sa', _('Saturday')),
        ('do', _('Sunday')),
    )

    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        verbose_name=_('Season'),
        blank=False,
        null=False
    )

    weekdays = models.CharField(
        max_length=100,
        choices=CH_WEEKDAYS,
        verbose_name=_('Weekdays'),
        help_text=_('Weeksdays in which the schedule applies'),
        blank=False,
        null=False
    )

    def __str__(self):
        return self.weekdays

    class Meta:
        verbose_name=_('Opening hours')
        verbose_name_plural=_('Opening hours')
