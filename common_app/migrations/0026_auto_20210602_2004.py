# Generated by Django 3.1.7 on 2021-06-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0025_trainer_profile_actual_organization_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer_profile',
            name='actual_organization_id',
        ),
        migrations.AddField(
            model_name='trainer_profile',
            name='actual_organization_pos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
