from dealers.models import Dealer
from rest_framework import viewsets, permissions
from .serializers import DealerSerializer
from .permissions import IsOwnerOrReadOnly

class DealerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer