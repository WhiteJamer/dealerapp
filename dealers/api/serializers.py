from dealers.models import Dealer
from rest_framework import serializers

class DealerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dealer
        fields = ['pk', 'name']