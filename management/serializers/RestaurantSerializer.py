from rest_framework import serializers
from management.models import Restaurant, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'line2', 'city', 'state', 'postal_code', 'country', 'telephone')


class RestaurantSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'email', 'addresses', 'is_open')

# TODO Google Maps localization (Address class)
# TODO Timetable for the restaurant and open? (boolean)
# TODO sugggest API for searching restaurnts
# TODO a restaurant should have images
