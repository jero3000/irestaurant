# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20160808_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='weekdays',
            field=models.CharField(help_text='Weeksdays in which the schedule applies', max_length=100, verbose_name='Weekdays'),
        ),
    ]
