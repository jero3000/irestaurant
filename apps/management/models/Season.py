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
        null=False,
        related_name='seasons'
    )

    def is_open(self, dt):
        """
        Checks if the restaurant is open in the given date&time
        :param dt: date and time to check
        :return: True if the restaurant is open in dt, False in other case
        """

        res=False
        hours=self.opening_hours.all()
        i=0
        while i<len(hours) and not res:
            res= hours[i].is_open(dt)
            i += 1
        return res

    def to_representation(self):
        """
        Returns a valid representation of a Season object (serialization)
        :return: the list which represents the object (compliant with Django REST Framework)
        """
        rep = []
        opening_hours = self.opening_hours.all()
        for oh in opening_hours:
            rep.append(oh.to_representation())

        return rep

    def __str__(self):
        return str(self.restaurant) + " " + str(self.begin) + " - " + str(self.end)

    class Meta:
        verbose_name=_('Season')
        verbose_name_plural=_('Seasons')
