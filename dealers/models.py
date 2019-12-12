from django.db import models
from uprofile.models import User


class Dealer(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,
                             related_name='dealers',
                             on_delete=models.CASCADE, blank=True, null=True)
