# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-24 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_auto_20170224_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayclosed',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days_closed', to='management.Restaurant'),
        ),
    ]