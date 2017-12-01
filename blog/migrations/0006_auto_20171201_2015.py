# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 20:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171118_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='article',
            name='date_publish',
        ),
        migrations.RemoveField(
            model_name='card',
            name='date',
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateField(db_index=True, default=datetime.datetime(2017, 12, 1, 20, 15, 0, 569197), verbose_name='Date Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='Article'),
        ),
        migrations.AddField(
            model_name='card',
            name='created_at',
            field=models.DateField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='date_visible',
            field=models.BooleanField(default=False, verbose_name='Date is Visible'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
    ]