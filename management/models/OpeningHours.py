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
        verbose_name=_('Weekdays'),
        help_text=_('Weeksdays in which the schedule applies'),
        blank=False,
        null=False
    )

    @classmethod
    def serialize_weekdays(cls, weekdays):
        """
        Serializes weekdays field removid unuseful characters generated by CheckBoxSelectMultiple widget
        :param weekdays: weekdays filed filled by CheckBoxSelectMultiple widget
        :return: weekdays keys (CH_WEEKDAYS) separated by commas
        """
        return weekdays.replace(" ", '').replace("[u'", '').replace(",u'", ',').replace("'", '') \
            .replace("]", '')

    @classmethod
    def deserialize_weekdays(cls, weekdays):
        """
        :param weekdays: weekdays field
        :return: Array containing the translated weekdays separated by commas
        """
        days=[]
        for day in weekdays.split(","):
            for t in cls.CH_WEEKDAYS:
                if t[0] == day:
                    days.append(unicode(t[1]))
                    break
        return days

    def save(self, *args, **kwargs):
        """
        Overwrite django "save" method to serialize weekdays field correctly
        """
        self.weekdays = self.serialize_weekdays(self.weekdays)
        super(OpeningHours, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        days = self.deserialize_weekdays(self.weekdays)

        return ', '.join(days)

    class Meta:
        verbose_name=_('Opening hours')
        verbose_name_plural=_('Opening hours')
