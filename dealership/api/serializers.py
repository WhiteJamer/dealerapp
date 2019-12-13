from dealership.models import DealerShip, Service
from rest_framework import serializers


class DealerShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DealerShip
        fields = ['pk', 'name', 'dealer']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['pk', 'name']