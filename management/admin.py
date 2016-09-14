# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Restaurant, Dish, ImageResource, VideoResource, DayClosed, Season, OpeningHours, TimeSlot, Address
from django.contrib.contenttypes.admin import GenericStackedInline
from embed_video.admin import AdminVideoMixin
from irestaurant.admin import admin_site
from django import forms
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationGenericStackedInline, TranslationTabularInline

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class SeasonInline(TranslationTabularInline):
    model = Season
    extra = 1


class DayClosedInline(admin.TabularInline):
    model = DayClosed
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    fields = ['name', 'email']
    inlines = [AddressInline, SeasonInline, DayClosedInline]


class ImageResourceInline(TranslationGenericStackedInline):
    model = ImageResource
    extra = 1
    readonly_fields = ['height', 'width']
    fields = ['title', 'image', 'height', 'width', 'pub_date']


class VideoResourceInline(AdminVideoMixin, TranslationGenericStackedInline):
    model = VideoResource
    extra = 1
    fields = ['title', 'video', 'pub_date']


class DishAdmin(TabbedTranslationAdmin):
    fieldsets = [
        (None, {'fields': ['restaurant', 'name', 'type', 'pub_date']}),
        (_('Additional info'), {'fields' : ['description', 'price'], 'classes': ['collapse']})
    ]
    inlines = [ImageResourceInline, VideoResourceInline]


class SeasonAdmin(TabbedTranslationAdmin):
    None


class TimeSlotInline(admin.TabularInline):
    model = TimeSlot
    extra = 1

class CheckboxSelectMultipleWrapper(forms.CheckboxSelectMultiple):
    """
    Overwrites CheckboxSelectMultiple because the renderer should take a
    list as argument (weekdays)
    """
    def render(self, name, value, attrs=None, choices=()):
        return super(CheckboxSelectMultipleWrapper, self).render(name, value.split(","), attrs, choices)

class MultipleChoiceForm(forms.ModelForm):
    weekdays = forms.MultipleChoiceField(widget=CheckboxSelectMultipleWrapper(),
                                         choices=OpeningHours.CH_WEEKDAYS)


class OpeningHoursAdmin(admin.ModelAdmin):
    inlines = [TimeSlotInline]
    form = MultipleChoiceForm

#Use the custom admin_site defined in irestaurant/admin.py
admin_site.register(Restaurant, RestaurantAdmin)
admin_site.register(Dish, DishAdmin)
admin_site.register(Season, SeasonAdmin)
admin_site.register(OpeningHours, OpeningHoursAdmin)