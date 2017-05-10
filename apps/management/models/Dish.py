# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from djmoney.models.fields import MoneyField
from django.db import models
from Restaurant import Restaurant
from django.utils.translation import ugettext_lazy as _
from MultimediaModel import MultimediaModel


@python_2_unicode_compatible
class Dish(MultimediaModel):
    CH_DISH_TYPE = (
        ('APE', _("Snack")),
        ('ENT', _("Starter")),
        ('PRI', _("Main")),
        ('POS', _("Dessert")),
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name=_('Restaurant')
    )

    name = models.CharField(
        max_length=200,
        verbose_name=_("Name"),
        blank=False
    )

    type = models.CharField(
        max_length=3,
        choices=CH_DISH_TYPE,
        blank=False,
        verbose_name=_("Type")
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True
    )

    price = MoneyField(
        verbose_name=_("Price"),
        max_digits=10,
        decimal_places=2,
        default_currency='EUR',
        blank=True)

    pub_date = models.DateTimeField(
        verbose_name=_("Publish date"),
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Dish")
        verbose_name_plural = _("Dishes")
