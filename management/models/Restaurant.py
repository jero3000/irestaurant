# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurant")