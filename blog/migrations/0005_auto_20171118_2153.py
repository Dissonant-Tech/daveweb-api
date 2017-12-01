# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171115_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='classes',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='date',
            field=models.DateField(db_index=True, null=True, verbose_name='Publish Date'),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(null=True, upload_to='card-images/%Y/'),
        ),
        migrations.AlterField(
            model_name='card',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.TextField(null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=120, null=True, verbose_name='Title'),
        ),
    ]