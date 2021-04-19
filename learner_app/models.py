from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class learner_profile (User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='img/users')
    points = models.IntegerField()
    learner = models.ForeignKey('learner', on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'learner_profile'
        verbose_name_plural = 'learner_profiles'


class learner (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
