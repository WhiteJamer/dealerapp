from django.db import models
from uprofile.models import User
from django.shortcuts import reverse


class Dealer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User,
                             related_name='dealers',
                             on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dealers:dealer_detail', kwargs={'slug':self.name})
