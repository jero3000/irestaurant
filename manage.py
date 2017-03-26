#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "irestaurant.settings")

    from django.core.management import execute_from_command_line
    from django.conf import settings

    # Adding the "apps" directory to the sys path to avoid errors imporing apps when they are located in a subdirectory
    sys.path.append(os.path.join(settings.BASE_DIR, "apps"))
    sys.path.append(os.path.join(os.path.join(settings.BASE_DIR, "apps"), "django-location-field"))
    execute_from_command_line(sys.argv)
