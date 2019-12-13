from cars.models import Car
from rest_framework import viewsets, permissions
from .serializers import CarSerializer
from .permissions import IsOwnerOrReadOnly

class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Car.objects.all()
    serializer_class = CarSerializer