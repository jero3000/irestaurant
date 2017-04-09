from rest_framework import serializers
from management.models import Restaurant, Address
from django.utils import timezone


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'line2', 'city', 'state', 'postal_code', 'country', 'telephone')


class RestaurantSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        dict = super(RestaurantSerializer, self).to_representation(instance)
        current_season = instance.get_current_season(timezone.now())
        season_dict = None
        if current_season is not None:
            season_dict = current_season.to_representation()
        dict['opening_hours'] = season_dict
        return dict

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'email', 'addresses', 'is_open')


class RestaurantSuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'url')


# TODO a restaurant should have images
