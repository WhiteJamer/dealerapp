from django.db import models
from dealers.models import Dealer


class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=20)
    dealer = models.ForeignKey(Dealer,
                               related_name='cars',
                               on_delete=models.CASCADE)
