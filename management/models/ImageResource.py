# -*- coding: utf-8 -*-

from django.db import models
from Resource import Resource
from versatileimagefield.fields import VersatileImageField


class ImageResource(Resource):
    """
    Represents an image that could be associated to any object in the model
    """

    image = VersatileImageField(
        verbose_name='Imagen',
        upload_to='images/',
        blank=False
    )

    height = models.PositiveIntegerField(
        'Alto',
        blank=True,
        null=True
    )

    width = models.PositiveIntegerField(
        'Ancho',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'