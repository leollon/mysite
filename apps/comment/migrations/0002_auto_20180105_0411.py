# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 04:11
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment'),
        ),
    ]
