from django.conf.urls import url, include
from management import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
