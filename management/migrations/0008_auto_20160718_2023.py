# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20160718_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Direcci\xf3n', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AddField(
            model_name='address',
            name='line2',
            field=models.CharField(blank=True, help_text=b'Otra informaci\xc3\xb3n adicional', max_length=200, null=True, verbose_name=b'Linea 2 de direcci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line1',
            field=models.CharField(default='', help_text=b'Calle y n\xc3\xbamero, apartado de correos, nombre empresa', max_length=200, verbose_name=b'Linea 1 de direcci\xc3\xb3n'),
            preserve_default=False,
        ),
    ]
