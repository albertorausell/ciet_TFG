# Generated by Django 3.1.7 on 2021-05-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0010_auto_20210512_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training_technique',
            name='content',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.content'),
        ),
        migrations.AlterField(
            model_name='training_technique',
            name='order',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='training_technique',
            name='reference',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='training_technique',
            name='types',
            field=models.CharField(blank=True, choices=[('txt', 'Text'), ('img', 'Image'), ('vid', 'Video'), ('doc', 'Document'), ('lnk', 'Link'), ('gme', 'Game')], default=None, max_length=4, null=True),
        ),
    ]
