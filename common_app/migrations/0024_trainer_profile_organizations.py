# Generated by Django 3.1.7 on 2021-06-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0023_auto_20210602_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer_profile',
            name='organizations',
            field=models.ManyToManyField(default=None, to='common_app.organization'),
        ),
    ]
