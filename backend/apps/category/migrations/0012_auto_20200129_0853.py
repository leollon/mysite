# Generated by Django 2.2.8 on 2020-01-29 08:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_auto_20200112_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]