from django.db import models
from dealers.models import Dealer
from django.shortcuts import reverse


# Модель услуги которую оказывает агенство
class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель диллерского агенства
class DealerShip(models.Model):
    name = models.CharField(max_length=255, unique=True)
    dealer = models.ForeignKey(Dealer,
                               related_name='dealerships',
                               on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name='dealerships', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dealership:dealership_detail', kwargs={'slug':self.name})
