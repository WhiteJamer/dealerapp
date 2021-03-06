from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def get_absolute_url(self):
        return reverse('uprofile:user_detail', kwargs={'username': self.username})

