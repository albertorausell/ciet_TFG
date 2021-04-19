# Generated by Django 3.1.7 on 2021-04-19 18:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer_profile',
            options={'verbose_name': 'trainer_profile', 'verbose_name_plural': 'trainer_profiles'},
        ),
        migrations.AlterModelManagers(
            name='trainer_profile',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='trainer_profile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trainer_profile',
            name='user',
        ),
        migrations.AddField(
            model_name='trainer_profile',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
    ]
