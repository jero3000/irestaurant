import django_filters
from rest_framework import viewsets
from models import Restaurant, Dish, ImageResource, VideoResource, Address
from serializers import RestaurantSerializer, DishSerializer, ImageResourceSerializer, VideoResourceSerializer, \
    RestaurantSuggestSerializer
from django.utils import timezone
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.utils.http import urlquote


class RestaurantByCityFilter(django_filters.rest_framework.FilterSet):
    """
    This class enables Restaurant filtering by the restaurant city
    """
    city = django_filters.CharFilter(name="addresses__city", label='Restaurant city')

    class Meta:
        model = Restaurant
        fields = ['city']


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieves Restaurant objects
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = RestaurantByCityFilter
    suggest_limit = 5 # Number of results for suggestions

    @list_route(methods=['get'])
    def suggestions(self, request):
        """
        Implements the suggest API for Restaurants objects. Assumes a "search" parameter
        indicating the search term. The search is performed over restaurant names and restaurant cities
        :param request: request object with query params (search parameter required)
        :return: json indicating the matching results (restaurants and locations). The information is reduced for
        performance reason but hyperlinks are provided in order to retrieve more info.
        """
        search = request.query_params.get('search', None)
        res_data = []
        loc_data = []
        if search is not None:
            restaurant_queryset = Restaurant.objects.filter(name__icontains=search)[:self.suggest_limit]
            cities = Address.objects.filter(city__icontains=search).values('city').distinct()[:self.suggest_limit]
            for city in cities:
                city_data = {
                    'name' : city,
                    'url' : reverse('restaurant-list', request=request) + "?city=" + urlquote(city['city'])
                }
                loc_data.append(city_data)
            restaurant_serializer = RestaurantSuggestSerializer(restaurant_queryset, many=True, context={'request': request})
            res_data = restaurant_serializer.data
        data = {
            'res:' : res_data,
            'loc' : loc_data,
        }
        return Response(data)


class DishFilter(django_filters.rest_framework.FilterSet):
    """
    This class enables Dish filtering by restaurant id and
    dish type
    """
    restaurant_id = django_filters.NumberFilter(name="restaurant__id")
    type = django_filters.CharFilter(name="type")

    class Meta:
        model = Dish
        fields = ['restaurant_id', 'type']


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve Dish objects
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = DishFilter

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
    This class enables VideoResource filtering by a Dish id
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