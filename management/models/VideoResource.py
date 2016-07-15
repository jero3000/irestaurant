# -*- coding: utf-8 -*-

from embed_video.fields import EmbedVideoField
from Resource import Resource

class VideoResource(Resource):
    """
    Represents a video that could be associated to any object in the model
    """

    video = EmbedVideoField(
        verbose_name='Video',
        max_length=250,
        blank=False
    )

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'