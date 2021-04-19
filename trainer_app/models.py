from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class trainer_profile (User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='img/users')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'trainer_profile'
        verbose_name_plural = 'trainer_profiles'
