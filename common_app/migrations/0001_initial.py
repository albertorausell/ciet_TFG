# Generated by Django 3.1.7 on 2021-04-20 15:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='capability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('aproximatedHours', models.FloatField()),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'capability',
                'verbose_name_plural': 'capabilities',
            },
        ),
        migrations.CreateModel(
            name='capability_objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('capability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.capability')),
            ],
            options={
                'verbose_name': 'capability_objective',
                'verbose_name_plural': 'capability_objective',
            },
        ),
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
                ('capability_objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.capability_objective')),
            ],
        ),
        migrations.CreateModel(
            name='dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('scope', models.CharField(choices=[('co', 'content'), ('ob', 'objective'), ('gl', 'global')], max_length=2)),
                ('referenceId', models.IntegerField()),
                ('leftPending', models.BooleanField()),
                ('capability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.capability')),
            ],
        ),
        migrations.CreateModel(
            name='learner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='trainer_profile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('rol', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='img/users')),
            ],
            options={
                'verbose_name': 'trainer_profile',
                'verbose_name_plural': 'trainer_profiles',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='training_technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('types', models.CharField(choices=[('txt', 'text'), ('img', 'image'), ('vid', 'video'), ('doc', 'document'), ('game', 'game')], max_length=4)),
                ('reference', models.TextField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.content')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('question', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activity', models.ManyToManyField(to='common_app.activity')),
            ],
        ),
        migrations.CreateModel(
            name='learner_profile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('rol', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='img/users')),
                ('points', models.IntegerField()),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.learner')),
            ],
            options={
                'verbose_name': 'learner_profile',
                'verbose_name_plural': 'learner_profiles',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending', models.BooleanField()),
                ('mark', models.FloatField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.exercise')),
                ('learner_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.learner_profile')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='dimension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.dimension'),
        ),
        migrations.AddField(
            model_name='capability_objective',
            name='objective',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='common_app.objective'),
        ),
        migrations.CreateModel(
            name='capability_learner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.capability')),
                ('last_content_done', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='common_app.content')),
                ('learner_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.learner_profile')),
            ],
            options={
                'verbose_name': 'capability_learner',
                'verbose_name_plural': 'capability_learner',
            },
        ),
        migrations.AddField(
            model_name='capability',
            name='learners',
            field=models.ManyToManyField(to='common_app.learner'),
        ),
        migrations.AddField(
            model_name='capability',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.organization'),
        ),
        migrations.AddField(
            model_name='capability',
            name='trainer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='common_app.trainer_profile'),
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('isCorrect', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.question')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='dimension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.dimension'),
        ),
        migrations.AddField(
            model_name='activity',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.phase'),
        ),
    ]