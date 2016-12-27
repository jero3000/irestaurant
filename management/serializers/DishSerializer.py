from rest_framework import serializers
from management.models import Dish
from moneyed import Money
from versatileimagefield.serializers import VersatileImageFieldSerializer

class MoneyField(serializers.Field):
    """
    MoneyField is not officially supported by Django REST framework
    so a new field serializer class should be implemented
    """
    def to_representation(self, obj):
        return {
            'amount': "%f" % (obj.amount),
            'currency': "%s" % (obj.currency),
        }

    def to_internal_value(self, data):
        return Money(data['amount'], data['currency'])


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


class DishSerializer(serializers.ModelSerializer):
    price = MoneyField()
    thumbnail = VersatileImageFiledUniqueVersionSerializer(source='get_main_image', rendition_key='thumbnail__100x100')

    class Meta:
        model = Dish
        fields = ('id', 'restaurant', 'name', 'type', 'description', 'price', 'thumbnail')
