# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Uri Identifier', max_length=255, unique=True, verbose_name='Slug')),
                ('content', markdownx.models.MarkdownxField()),
                ('created_at', models.DateField(db_index=True, verbose_name='Date Created')),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Published')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('date_visible', models.BooleanField(default=False, verbose_name='Date is Visible')),
                ('classes', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(choices=[('AR', 'Article'), ('BA', 'Banner'), ('QU', 'Quote'), ('IM', 'Image')], default='BA', max_length=2)),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='Article')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BannerCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('date_visible', models.BooleanField(default=False, verbose_name='Date is Visible')),
                ('classes', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(choices=[('AR', 'Article'), ('BA', 'Banner'), ('QU', 'Quote'), ('IM', 'Image')], default='BA', max_length=2)),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ImageCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('date_visible', models.BooleanField(default=False, verbose_name='Date is Visible')),
                ('classes', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(choices=[('AR', 'Article'), ('BA', 'Banner'), ('QU', 'Quote'), ('IM', 'Image')], default='BA', max_length=2)),
                ('image', models.ImageField(upload_to='card-images/%Y/')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('date_visible', models.BooleanField(default=False, verbose_name='Date is Visible')),
                ('classes', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(choices=[('AR', 'Article'), ('BA', 'Banner'), ('QU', 'Quote'), ('IM', 'Image')], default='BA', max_length=2)),
                ('footer', models.CharField(max_length=120, verbose_name='Footer')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
