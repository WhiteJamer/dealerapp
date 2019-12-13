from cars.models import Car
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['pk', 'vin', 'brand', 'model', 'color', 'dealer', 'dealership']