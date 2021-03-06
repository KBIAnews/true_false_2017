# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=1024)),
                ('image', models.ImageField(upload_to='images/film_images')),
                ('trailer_embed', models.URLField(max_length=1024)),
            ],
        ),
    ]
