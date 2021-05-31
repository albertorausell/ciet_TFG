from django.db import models

from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from django.dispatch import receiver
import os
import uuid


# Create your models here.


class user (User):

    rol = models.ForeignKey('stakeholders', on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='img/users')


class trainer_profile (models.Model):

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField('user', on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'trainer_profile'

        verbose_name_plural = 'trainer_profiles'


class learner_profile (models.Model):

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField('user', on_delete=models.CASCADE)

    organization = models.ForeignKey('organization', on_delete=models.CASCADE)

    points = models.IntegerField()

    def __str__(self):

        return self.user

    class Meta:

        verbose_name = 'learner_profile'

        verbose_name_plural = 'learner_profiles'


class stakeholders (models.Model):

    name = models.CharField(max_length=50)

    isTrainer = models.BooleanField()

    isLearner = models.BooleanField()

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'stakeholders'

        verbose_name_plural = 'stakeholders'


class organization (models.Model):

    name = models.CharField(max_length=50, default="null")

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


class capability (models.Model):

    name = models.CharField(max_length=50, default=None, blank=True, null=True)

    aproximatedTime = models.FloatField(default=None, blank=True, null=True)

    active = models.BooleanField(default=False, blank=True, null=True)

    description = models.TextField(default=None, blank=True, null=True)

    image = models.ImageField(
        default=None, blank=True, null=True, upload_to='trainer_app/img/capabilities')

    stakeholders = models.ManyToManyField(
        'stakeholders', default=None)

    objectives = models.ManyToManyField(
        'objective', through='capability_objective', default=None)

    trainer = models.ForeignKey(

        'trainer_profile', on_delete=models.CASCADE, default=None, blank=True, null=True)

    organization = models.ForeignKey(

        'organization', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'capability'

        verbose_name_plural = 'capabilities'


class objective (models.Model):

    name = models.CharField(max_length=30)

    activities = models.ManyToManyField('activity')

    def __str__(self):

        return self.name


class dimension (models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name


class phase (models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name


class activity (models.Model):

    name = models.CharField(max_length=50)

    dimension = models.ForeignKey('dimension', on_delete=models.CASCADE)

    phase = models.ForeignKey('phase', on_delete=models.CASCADE)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'activity'

        verbose_name_plural = 'activities'


class content (models.Model):

    name = models.CharField(max_length=20, default=None, blank=True, null=True)

    order = models.IntegerField(default=None, blank=True, null=True)

    capability_objective = models.ForeignKey(

        'capability_objective', on_delete=models.CASCADE, default=None, blank=True, null=True)

    dimension = models.ForeignKey(
        'dimension', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):

        return self.name


class training_technique (models.Model):

    TEXT = 'txt'

    IMAGE = 'img'

    VIDEO = 'vid'

    DOCUMENT = 'doc'

    LINK = 'lnk'

    GAME = 'gme'

    TRAINING_TYPES = (

        (TEXT, 'Text'),

        (IMAGE, 'Image'),

        (VIDEO, 'Video'),

        (DOCUMENT, 'Document'),

        (LINK, 'Link'),

        (GAME, 'Game'),
    )
    type = models.CharField(
        max_length=4, choices=TRAINING_TYPES, default=None, blank=True, null=True)

    order = models.IntegerField(default=None, blank=True, null=True)

    content = models.ForeignKey(
        'content', on_delete=models.CASCADE, default=None, blank=True, null=True)

    objects = InheritanceManager()


class evaluation (models.Model):

    pending = models.BooleanField()

    mark = models.FloatField()

    exercise = models.ForeignKey('exercise', on_delete=models.CASCADE)

    learner_profile = models.ForeignKey(

        'learner_profile', on_delete=models.CASCADE)


class exercise (models.Model):

    CONTENT = 'co'

    OBJECTIVE = 'ob'

    CAPABILITY = 'ca'

    SCOPES = (

        (CONTENT, 'content'),

        (OBJECTIVE, 'objective'),

        (CAPABILITY, 'capability'),
    )

    name = models.CharField(max_length=50, default=None, blank=True, null=True)

    scope = models.CharField(max_length=2, choices=SCOPES,
                             default=None, blank=True, null=True)

    referenceId = models.IntegerField(default=-1, blank=True, null=True)

    leftPending = models.BooleanField(default=False, blank=True, null=True)

    capability = models.ForeignKey(
        'capability', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):

        return self.name


class question (models.Model):

    order = models.IntegerField(default=None, blank=True, null=True)

    question = models.TextField(default=None, blank=True, null=True)

    exercise = models.ForeignKey(
        'exercise', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):

        return self.question


class answer (models.Model):

    answer = models.TextField(default=None, blank=True, null=True)

    isCorrect = models.BooleanField(default=False, blank=True, null=True)

    question = models.ForeignKey(
        'question', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):

        return self.answer


class capability_objective (models.Model):

    order = models.IntegerField(default=0)

    capability = models.ForeignKey('capability', on_delete=models.CASCADE,)

    objective = models.ForeignKey(

        'objective', on_delete=models.CASCADE, default=0)

    class Meta:

        verbose_name = 'capability_objective'

        verbose_name_plural = 'capability_objective'


class capability_learner (models.Model):

    last_content_done = models.OneToOneField(

        'content', on_delete=models.CASCADE)

    capability = models.ForeignKey('capability', on_delete=models.CASCADE)

    learner_profile = models.ForeignKey(

        'learner_profile', on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'capability_learner'

        verbose_name_plural = 'capability_learner'


class text_component (training_technique):

    value = models.TextField(default=None, blank=True, null=True)


class image_component (training_technique):

    value = models.ImageField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)


class video_component (training_technique):

    value = models.FileField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)


class document_component (training_technique):

    value = models.FileField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)


class link_component (training_technique):

    value = models.TextField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)


class game_component (training_technique):

    value = models.TextField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)


@receiver(models.signals.post_delete, sender=image_component)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.value:
        if os.path.isfile(instance.value.path):
            os.remove(instance.value.path)


@receiver(models.signals.post_delete, sender=video_component)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.value:
        if os.path.isfile(instance.value.path):
            os.remove(instance.value.path)


@receiver(models.signals.post_delete, sender=document_component)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.value:
        if os.path.isfile(instance.value.path):
            os.remove(instance.value.path)
