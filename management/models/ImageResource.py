# -*- coding: utf-8 -*-

from django.db import models
from Resource import Resource
from versatileimagefield.fields import VersatileImageField, PPOIField


class ImageResource(Resource):
    """
    Represents an image that could be associated to any object in the model
    """

    image = VersatileImageField(
        verbose_name='Imagen',
        upload_to='images/',
        height_field='height',
        width_field='width',
        blank=False,
        ppoi_field='ppoi'
    )

    height = models.PositiveIntegerField(
        verbose_name='Alto',
        blank=True,
        null=True
    )

    width = models.PositiveIntegerField(
        verbose_name='Ancho',
        blank=True,
        null=True
    )

    ppoi = PPOIField(
        verbose_name='Punto de interés'
    )

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'