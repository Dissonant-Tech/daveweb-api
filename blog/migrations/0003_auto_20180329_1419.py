# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180328_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecard',
            name='style',
        ),
        migrations.RemoveField(
            model_name='bannercard',
            name='style',
        ),
        migrations.RemoveField(
            model_name='imagecard',
            name='style',
        ),
        migrations.RemoveField(
            model_name='quotecard',
            name='style',
        ),
        migrations.AlterField(
            model_name='articlecard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='articlecard',
            name='date_visible',
            field=models.BooleanField(default=True, verbose_name='Date is Visible'),
        ),
        migrations.AlterField(
            model_name='bannercard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='imagecard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='quotecard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at'),
        ),
    ]
