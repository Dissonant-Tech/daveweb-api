# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180329_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecard',
            name='title',
            field=models.CharField(max_length=120, null=True, verbose_name='Title'),
        ),
    ]
