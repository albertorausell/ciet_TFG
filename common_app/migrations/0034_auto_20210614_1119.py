# Generated by Django 3.1.7 on 2021-06-14 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0033_auto_20210614_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='created',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='updated',
        ),
    ]
