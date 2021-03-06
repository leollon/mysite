# Generated by Django 2.2.6 on 2020-01-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('mail_message', models.TextField()),
                ('ip', models.GenericIPAddressField()),
                ('mail_state', models.CharField(max_length=16)),
                ('reason', models.TextField(blank=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'email_records',
                'ordering': ('username', 'created_time'),
                'verbose_name': 'email_record',
                'verbose_name_plural': 'email_records',
            },
        ),
    ]
