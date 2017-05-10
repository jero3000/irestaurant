# -*- coding: utf-8 -*-

from django.db import models
from ImageResource import ImageResource
from VideoResource import VideoResource
from django.contrib.contenttypes.fields import GenericRelation


class MultimediaModel(models.Model):
    """
    Represents a multimedia model, this is a model than can have images and/or videos

    This class uses a generic relation in Django. Documentation:
    https://docs.djangoproject.com/en/1.9/ref/contrib/contenttypes/
    """

    images = GenericRelation(
        ImageResource,
    )

    videos = GenericRelation(
        VideoResource,
    )

    def get_main_image(self):
        """
        Gets the main associated image
        :return: VersatileImageField
        """
        main = None
        main_images = self.images.all().filter(main=True)
        if len(main_images) > 0:
            main = main_images[0].image
        return main

    class Meta:
        abstract = True
