# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator
from Restaurant import Restaurant
from django.utils.translation import ugettext_lazy as _
from location_field.models.plain import PlainLocationField

class Address(models.Model):
    """
    This class represent a restaurant address
    """

    line1 = models.CharField(
        max_length=200,
        verbose_name=_('Line 1'),
        help_text=_('Street and number, post office box, company name'),
        blank=False,
        null=False
    )

    line2 = models.CharField(
        max_length=200,
        verbose_name=_('Line 2'),
        help_text=_('Other additional info'),
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=200,
        verbose_name=_('City'),
        blank=False,
        null=False
    )

    state = models.CharField(
        max_length=200,
        verbose_name=_('State'),
        blank=False,
        null=False
    )

    postal_code = models.CharField(
        max_length=200,
        verbose_name=_('Postal code'),
        blank=False,
        null=False
    )

    country = models.CharField(
        max_length=200,
        verbose_name=_('Country'),
        blank=False,
        null=False
    )

    location = PlainLocationField(
        based_fields=['city', 'line1'],
        verbose_name=_('Location'),
        zoom=7,
        blank=False,
        null=False)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("The phone number should have the following format: '+999999999'. 15 digits max")
    )

    telephone = models.CharField(
        max_length=20,
        validators=[phone_regex],
        verbose_name=_('Telephone')
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="addresses"
    )

    def __str__(self):
        return self.line1

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
