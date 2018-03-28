# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171201_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, verbose_name='text')),
                ('created_at', models.DateField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('date_visible', models.BooleanField(default=False, verbose_name='Date is Visible')),
                ('classes', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(choices=[('AR', 'Article'), ('BA', 'Banner'), ('QU', 'Quote'), ('IM', 'Image')], default='BA', max_length=2)),
                ('header', models.CharField(max_length=120, verbose_name='Header')),
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
                ('text', models.TextField(null=True, verbose_name='text')),
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
            name='ImageCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, verbose_name='text')),
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
                ('text', models.TextField(null=True, verbose_name='text')),
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
        migrations.RemoveField(
            model_name='card',
            name='article',
        ),
        migrations.RemoveField(
            model_name='card',
            name='author',
        ),
        migrations.RemoveField(
            model_name='card',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
