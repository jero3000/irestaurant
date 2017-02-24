# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

@python_2_unicode_compatible
class Restaurant(models.Model):
    """
    This class represents a Restaurant
    """
    name = models.CharField(
        max_length=200,
        verbose_name=_('Name'),
        blank=False
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
        null=True
    )

    def get_current_season(self, dt):
        """
        Gets the current season according to dt
        :param dt: date and time to check
        :return: Season object
        """
        current_season = None
        i=0
        seasons = self.seasons.all()
        while (i<len(seasons)) and (current_season is None):
            season = seasons[i]
            if (dt.date() >= season.begin) and (dt.date() <= season.end):
                current_season = season
            i+=1
        return current_season

    def is_open(self, dt=timezone.now()):
        """
        Checks if the restaurant is open in the given date&time
        :type dt: datetime object
        :param dt: date and time to check
        :return: True if the restaurant is open in dt, False in other case
        """
        res=False
        season=self.get_current_season(dt)
        if season is not None:
            closed = False
            days = self.days_closed.all()
            i = 0
            while i < len(days) and not closed:
                closed = (days[i].day == dt.date())
                i += 1
            if not closed:
                res = season.is_open(dt)
        return res

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurant")