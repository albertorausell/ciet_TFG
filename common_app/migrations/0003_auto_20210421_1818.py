# Generated by Django 3.1.7 on 2021-04-21 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0002_auto_20210420_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objective',
            old_name='activity',
            new_name='activities',
        ),
    ]
