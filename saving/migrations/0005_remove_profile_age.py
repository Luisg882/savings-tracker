# Generated by Django 4.2.13 on 2024-07-13 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0004_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]
