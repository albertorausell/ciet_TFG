# Generated by Django 3.1.7 on 2021-06-17 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0035_auto_20210614_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document', models.FileField(blank=True, default=None, null=True, upload_to='excel')),
                ('organization', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.organization')),
                ('trainer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.trainer_profile')),
            ],
        ),
    ]
