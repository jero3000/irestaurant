import django_filters
from rest_framework import viewsets
from models import Restaurant, Dish, ImageResource, VideoResource
from serializers import RestaurantSerializer, DishSerializer, ImageResourceSerializer, VideoResourceSerializer
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


class ImageFilter(django_filters.rest_framework.FilterSet):
    """
    This class enables ImageResource filtering by a Dish id
    """
    dish_id = django_filters.NumberFilter(name="dishes__id")

    class Meta:
        model = ImageResource
        fields = ['dish_id']


class ImageResourceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve ImageResource objects
    """
    queryset = ImageResource.objects.all()
    serializer_class = ImageResourceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ImageFilter

    def get_queryset(self):
        """
        Filter the queryset to return only the published images
        :return: queryset filtered
        """

        return self.queryset.filter(pub_date__lte=timezone.now())


class VideoFilter(django_filters.rest_framework.FilterSet):
    """
    This class enables ImageResource filtering by a Dish id
    """
    dish_id = django_filters.NumberFilter(name="dishes__id")

    class Meta:
        model = VideoResource
        fields = ['dish_id']


class VideoResourceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve VideoResource objects
    """

    queryset = VideoResource.objects.all()
    serializer_class = VideoResourceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = VideoFilter

    def get_queryset(self):
        """
        Filter the queryset to return only the published videos
        :return: queryset filtered
        """

        return self.queryset.filter(pub_date__lte=timezone.now())