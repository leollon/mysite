# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 14:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0007_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('email', models.EmailField(blank=True, max_length=32, unique=True)),
                ('link', models.CharField(blank=True, max_length=32)),
                ('comment_text', models.TextField(max_length=256)),
                ('comment_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
        ),
    ]