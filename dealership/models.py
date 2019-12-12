from django.db import models
from dealers.models import Dealer


# Модель услуги которую оказывает агенство
class Service(models.Model):
    name = models.CharField(max_length=255)


# Модель диллерского агенства
class DealerShip(models.Model):
    name = models.CharField(max_length=255)
    dealer = models.ForeignKey(Dealer,
                               related_name='dealerships',
                               on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name='dealerships')
