# -*- coding: utf-8 -*-

from embed_video.fields import EmbedVideoField
from Resource import Resource
from django.utils.translation import ugettext_lazy as _

class VideoResource(Resource):
    """
    Represents a video that could be associated to any object in the model
    """

    video = EmbedVideoField(
        verbose_name=_('Video'),
        max_length=250,
        blank=False
    )

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')