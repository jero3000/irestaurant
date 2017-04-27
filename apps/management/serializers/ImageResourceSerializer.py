from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import serializers
from management.models import ImageResource


class VersatileImageFiledUniqueVersionSerializer(VersatileImageFieldSerializer):
    """
    VersatileImageFiledSerializer specialization for a unique image representation.
    This serializer avoid a JSON object serializing a VersatileImageField
    """

    def __init__(self, rendition_key, *args, **kwargs):
        super(VersatileImageFiledUniqueVersionSerializer, self).__init__(
            [('unique_version', rendition_key), ], *args, **kwargs
        )

    def to_representation(self, value):
        data = super(VersatileImageFiledUniqueVersionSerializer, self).to_representation(value)
        return data["unique_version"]


class ImageResourceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='object_id')
    image = VersatileImageFieldSerializer(sizes=
    [
        ('large', 'url'),
        ('medium', 'crop__400x400'),
        ('small', 'thumbnail__100x100')
    ])

    class Meta:
        model = ImageResource
        fields = ('id', 'title', 'pub_date', 'image', 'height', 'width', 'main')
