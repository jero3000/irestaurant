# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from ImageResource import ImageResource
from VideoResource import VideoResource
from django.contrib.contenttypes.fields import GenericRelation


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

    images = GenericRelation(
        ImageResource,
        related_query_name='restaurants'
    )

    videos = GenericRelation(
        VideoResource,
        related_query_name='restaurants'
    )

    def get_current_season(self, dt):
        """
        Gets the current season according to dt
        :param dt: date and time to check
        :return: Season object
        """

        current_season = None
        i=0
        seasons = self.seasons.filter(begin__lte=dt.date()).filter(end__gte=dt.date())
        if len(seasons) > 0:
            current_season = seasons[0]

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

    def get_main_image(self):
        """
        Gets the main restaurant image
        :return: VersatileImageField
        """
        main = None
        main_images = self.images.all().filter(main=True)
        if len(main_images) > 0:
            main = main_images[0].image
        return main

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurant")