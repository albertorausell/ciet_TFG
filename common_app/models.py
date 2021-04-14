from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organization (models.Model):
    users = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'onrganizations'

  #  def __str__(self):
  #      return user.get_full_name(self)
