from django.shortcuts import render
from rest_framework import viewsets
from models import Restaurant
from serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This Viewset manages the HTTP GET method to retrieve Restaurant objects
    in the specified format (json, XML, ...)
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
