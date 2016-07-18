# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Restaurant(models.Model):
    """
    This class represents a Restaurant
    """
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre",
        blank=False
    )

    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"