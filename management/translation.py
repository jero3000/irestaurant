from modeltranslation.translator import register, TranslationOptions
from .models import Dish


@register(Dish)
class DishTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

