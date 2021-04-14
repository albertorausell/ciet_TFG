from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LearnerProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='img/users')
    points = models.IntegerField()

    class Meta:
        verbose_name = 'learner'
        verbose_name_plural = 'learners'

  #  def __str__(self):
  #      return user.get_full_name(self)
