from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=255)
