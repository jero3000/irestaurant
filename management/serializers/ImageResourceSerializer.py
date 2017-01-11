from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import serializers
from management.models import ImageResource


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
