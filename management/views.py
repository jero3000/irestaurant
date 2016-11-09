from django.shortcuts import render
from rest_framework import viewsets
from models import Restaurant, Dish
from serializers import RestaurantSerializer, DishSerializer
from django.utils import timezone

class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieves Restaurant objects
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve Dish objects
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_queryset(self):
        """
        Filter the queryset to return only the published Dishes
        :return: queryset filtered
        """

        return self.queryset.filter(pub_date__lte=timezone.now())