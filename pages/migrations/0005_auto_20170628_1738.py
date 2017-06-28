# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170628_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedflatpage',
            name='keywords',
            field=models.CharField(db_index=True, max_length=255, verbose_name='keywords'),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='keywords_en',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='keywords'),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='keywords_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='keywords'),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='meta_description',
            field=models.CharField(db_index=True, max_length=255, verbose_name='meta_description'),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='meta_description_en',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='meta_description'),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='meta_description_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='meta_description'),
        ),
    ]
