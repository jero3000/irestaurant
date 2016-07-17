# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Restaurant, Dish, ImageResource, VideoResource
from django.contrib.contenttypes.admin import GenericStackedInline
from embed_video.admin import AdminVideoMixin
from irestaurant.admin import admin_site


class RestaurantAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'telephone']


class ImageResourceInline(GenericStackedInline):
    model = ImageResource
    extra = 1
    readonly_fields = ['height', 'width']
    fields = ['title', 'image', 'height', 'width', 'pub_date']


class VideoResourceInline(AdminVideoMixin, GenericStackedInline):
    model = VideoResource
    extra = 1
    fields = ['title', 'video', 'pub_date']

class DishAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['restaurant', 'name', 'type', 'pub_date']}),
        ('Información adicional', {'fields' : ['description', 'price'], 'classes': ['collapse']})
    ]
    inlines = [ImageResourceInline, VideoResourceInline]

#Use the custom admin_site defined in irestaurant/admin.py
admin_site.register(Restaurant, RestaurantAdmin)
admin_site.register(Dish, DishAdmin)