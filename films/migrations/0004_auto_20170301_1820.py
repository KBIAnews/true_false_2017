# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20170301_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screening_time', models.DateTimeField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=1024)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='screening',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Venue'),
        ),
    ]
