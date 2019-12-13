from dealership.models import DealerShip, Service
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import DealerShipSerializer, ServiceSerializer


class DealerShipViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = DealerShip.objects.all()
    serializer_class = DealerShipSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
