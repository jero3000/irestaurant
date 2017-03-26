# -*- coding: utf-8 -*-

from django.db import models
from Resource import Resource
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.utils.translation import ugettext_lazy as _


class ImageResource(Resource):
    """
    Represents an image that could be associated to any object in the model
    """

    image = VersatileImageField(
        verbose_name=_('Image'),
        upload_to='images/',
        height_field='height',
        width_field='width',
        blank=False,
        ppoi_field='ppoi'
    )

    height = models.PositiveIntegerField(
        verbose_name=_('Height'),
        blank=True,
        null=True
    )

    width = models.PositiveIntegerField(
        verbose_name=_('Width'),
        blank=True,
        null=True
    )

    #Point of interest filed
    ppoi = PPOIField(
        verbose_name=_('Point of interest')
    )

    main = models.BooleanField(
        verbose_name=_('Main picture'),
        help_text=_('This a main representative picture that can be used for thumbnails'),
        blank=False,
        null=False,
        default=False
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')