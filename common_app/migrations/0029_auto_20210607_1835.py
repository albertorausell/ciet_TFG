# Generated by Django 3.1.7 on 2021-06-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0028_auto_20210607_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learner_profile',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='trainer_profile',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='learner_profile',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='trainer_profile',
            name='updated',
        ),
        migrations.AddField(
            model_name='learner_profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stakeholders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-06-02 17:25:47'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stakeholders',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trainer_profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]