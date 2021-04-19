from django.db import models
from django.contrib.auth.models import User
from learner_app.models import learner, learner_profile
from trainer_app.models import trainer_profile

# Create your models here.


class organization (models.Model):
    name = models.CharField(max_length=50, default="null")
    users = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class capability (models.Model):
    name = models.CharField(max_length=50)
    aproximatedHours = models.FloatField()
    active = models.BooleanField()
    learners = models.ManyToManyField(learner)
    trainer = models.ForeignKey(
        trainer_profile, on_delete=models.CASCADE, default=0)
    organization = models.ForeignKey(
        'organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'capability'
        verbose_name_plural = 'capabilities'


class objective (models.Model):
    name = models.CharField(max_length=30)

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
    objective = models.ForeignKey(
        'objective', on_delete=models.CASCADE, blank=True, null=True)
    dimension = models.ForeignKey('dimension', on_delete=models.CASCADE)
    phase = models.ForeignKey('phase', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'


class content (models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    capability_objective = models.ForeignKey(
        'capability_objective', on_delete=models.CASCADE)
    dimension = models.ForeignKey('dimension', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class training_technique (models.Model):
    TEXT = 'txt'
    IMAGE = 'img'
    VIDEO = 'vid'
    DOCUMENT = 'doc'
    GAME = 'game'
    TRAINING_TYPES = (
        (TEXT, 'text'),
        (IMAGE, 'image'),
        (VIDEO, 'video'),
        (DOCUMENT, 'document'),
        (GAME, 'game'),
    )
    order = models.IntegerField()
    types = models.CharField(max_length=4, choices=TRAINING_TYPES)
    reference = models.TextField()
    content = models.ForeignKey('content', on_delete=models.CASCADE)


class evaluation (models.Model):
    pending = models.BooleanField()
    mark = models.FloatField()
    exercise = models.ForeignKey('exercise', on_delete=models.CASCADE)
    learner_profile = models.ForeignKey(
        learner_profile, on_delete=models.CASCADE)


class exercise (models.Model):
    CONTENT = 'co'
    OBJECTIVE = 'ob'
    GLOBAL = 'gl'
    SCOPES = (
        (CONTENT, 'content'),
        (OBJECTIVE, 'objective'),
        (GLOBAL, 'global'),
    )
    name = models.CharField(max_length=50)
    scope = models.CharField(max_length=2, choices=SCOPES)
    referenceId = models.IntegerField()
    leftPending = models.BooleanField()
    capability = models.ForeignKey('capability', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class question (models.Model):
    order = models.IntegerField()
    question = models.TextField()
    exercise = models.ForeignKey('exercise', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class answer (models.Model):
    answer = models.TextField()
    isCorrect = models.BooleanField()
    question = models.ForeignKey('question', on_delete=models.CASCADE)

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
        learner_profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'capability_learner'
        verbose_name_plural = 'capability_learner'
