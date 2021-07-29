# Generated by Django 3.1.7 on 2021-06-24 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0037_objective_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='dimension',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.dimension'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='phase',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_app.phase'),
        ),
    ]
