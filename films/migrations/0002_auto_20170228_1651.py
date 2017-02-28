# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='convo_audio',
            field=models.URLField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='convo_author',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='convo_text',
            field=models.TextField(null=True),
        ),
    ]
