# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

class MyAdminSite(AdminSite):
    """
    Custom AdminSite class to specify the correct site header
    """
    site_header = _('iRestaurant Administration')

admin_site = MyAdminSite(name='myadmin')
admin_site.register(User)
admin_site.register(Group)