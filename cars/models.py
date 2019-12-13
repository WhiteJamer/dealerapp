from django.db import models
from dealers.models import Dealer
from dealership.models import DealerShip
from django.shortcuts import reverse


class Car(models.Model):
    vin = models.CharField(max_length=255, unique=True, blank=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=20)
    dealer = models.ForeignKey(Dealer,
                               related_name='cars',
                               on_delete=models.CASCADE)
    dealership = models.ForeignKey(DealerShip,
                                   related_name='cars',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True)
    def __str__(self):
        return self.brand + ' - ' + self.model + ' | ' + self.color

    def get_absolute_url(self):
        return reverse('cars:car_detail', kwargs={'slug':self.vin})
