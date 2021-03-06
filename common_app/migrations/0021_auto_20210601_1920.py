# Generated by Django 3.1.7 on 2021-06-01 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common_app', '0020_auto_20210531_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner_profile',
            name='imagen',
            field=models.ImageField(default='static/unknown_profile.png', upload_to='img/users'),
        ),
        migrations.AddField(
            model_name='learner_profile',
            name='rol',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.stakeholders'),
        ),
        migrations.AddField(
            model_name='trainer_profile',
            name='imagen',
            field=models.ImageField(default='static/unknown_profile.png', upload_to='img/users'),
        ),
        migrations.AddField(
            model_name='trainer_profile',
            name='rol',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.stakeholders'),
        ),
        migrations.AlterField(
            model_name='learner_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
