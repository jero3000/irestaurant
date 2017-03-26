from modeltranslation.translator import register, TranslationOptions
from .models import Dish, Season, ImageResource, VideoResource


@register(Dish)
class DishTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Season)
class SeasonTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ImageResource)
class ImageResourceTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(VideoResource)
class VideoResourceTranslationOptions(TranslationOptions):
    fields = ('title',)
