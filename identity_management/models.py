from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'custom users'

    def __str__(self):
        return self.username



