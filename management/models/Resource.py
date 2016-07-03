from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Resource(models.Model):
    """
    Represents a multimedia resource, it can be an image, a video...
    """

    content_type =  models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_type = GenericForeignKey(
        'content_type',
        'object_id'
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Título"
    )

    pub_date = models.DateTimeField(
        verbose_name="Fecha de publicación",
        blank = False
    )

    @python_2_unicode_compatible
    def __str__(self):
        return self.title;

    class Meta:
        abstract = True