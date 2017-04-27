from rest_framework import serializers
from management.models import Dish
from moneyed import Money
from ImageResourceSerializer import VersatileImageFiledUniqueVersionSerializer


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


class DishSerializer(serializers.ModelSerializer):
    price = MoneyField()
    thumbnail = VersatileImageFiledUniqueVersionSerializer(source='get_main_image', rendition_key='thumbnail__100x100')

    class Meta:
        model = Dish
        fields = ('id', 'restaurant', 'name', 'type', 'description', 'price', 'thumbnail')
