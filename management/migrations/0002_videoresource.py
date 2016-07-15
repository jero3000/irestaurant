# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(blank=True, max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('pub_date', models.DateTimeField(verbose_name=b'Fecha de publicaci\xc3\xb3n')),
                ('video', embed_video.fields.EmbedVideoField(max_length=250, verbose_name=b'Video')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
