# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20170301_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='convo_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
