# Generated by Django 3.1.7 on 2021-05-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0013_training_technique_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document_component',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='game_component',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='image_component',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='link_component',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='video_component',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
