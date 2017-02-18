This project was designed to run on:

- Django 1.9.7
- Python 2.7.11
- GNU gettext tools 0.15
- Graphviz (for model diagrams)

Python dependencies:

- py-moneyed 0.6

Django dependencies:

- django-money 0.8 - https://github.com/django-money/django-money
- django-versatileimagefield 1.5 - http://django-versatileimagefield.readthedocs.io/en/latest/
- django-embed-video 1.1.0 - http://django-embed-video.readthedocs.io/en/v1.1.0/
- django-extensions 1.6.7 - http://django-extensions.readthedocs.io/en/latest/
- django-modeltranslation 0.11 http://django-modeltranslation.readthedocs.io/en/stable/installation.html
- djangorestframework 3.4.3 - http://www.django-rest-framework.org
- django-filter - To enable filtering in REST API

To update the model diagram:

python manage.py graph_models management -g -o doc/diagrams/actual/model.png

Admin login:

user: jmunoz
pass: irestaurant123

URLS:

http://127.0.0.1:8000/ (main page)
http://127.0.0.1:8000/admin (admin interface)
http://127.0.0.1:8000/management/dishes/ (dishes REST API)
http://127.0.0.1:8000/management/restaurants/ (restaurants REST API)

Django REST Framework example:

from management.models import Dish
from management.serializers import DishSerializer
from rest_framework.renderers import JSONRenderer
d=Dish.objects.all()[0]
ds=DishSerializer(d)
JSONRenderer().render(ds.data)

