# Generated by Django 3.1.7 on 2021-05-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0012_auto_20210513_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='training_technique',
            name='type',
            field=models.CharField(blank=True, choices=[('txt', 'Text'), ('img', 'Image'), ('vid', 'Video'), ('doc', 'Document'), ('lnk', 'Link'), ('gme', 'Game')], default=None, max_length=4, null=True),
        ),
    ]
