# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-24 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_imageresource_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='management.Restaurant'),
        ),
    ]
