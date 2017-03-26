from django.conf.urls import url, include
from management import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'dishes', views.DishViewSet)
router.register(r'images', views.ImageResourceViewSet)
router.register(r'videos', views.VideoResourceViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
