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
        fields = ('id', 'name', 'email', 'addresses')
