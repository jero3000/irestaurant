# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Restaurant, Dish, ImageResource, VideoResource, DayClosed, Season, OpeningHours, TimeSlot, Address
from django.contrib.contenttypes.admin import GenericStackedInline
from embed_video.admin import AdminVideoMixin
from irestaurant.admin import admin_site
from django import forms

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1


class DayClosedInline(admin.TabularInline):
    model = DayClosed
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    fields = ['name', 'email']
    inlines = [AddressInline, SeasonInline, DayClosedInline]


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


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 1


class SeasonAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline]


class TimeSlotInline(admin.TabularInline):
    model = TimeSlot
    extra = 1

class MultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = ('temporada', 'weekdays',)
        widgets = {
            'weekdays' : forms.SelectMultiple
        }


class OpeningHoursAdmin(admin.ModelAdmin):
    inlines = [TimeSlotInline]
    form = MultipleChoiceForm

#Use the custom admin_site defined in irestaurant/admin.py
admin_site.register(Restaurant, RestaurantAdmin)
admin_site.register(Dish, DishAdmin)
admin_site.register(Season, SeasonAdmin)
admin_site.register(OpeningHours, OpeningHoursAdmin)