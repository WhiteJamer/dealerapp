from rest_framework import routers
from .views import DealerShipViewSet
from .views import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'dealerships', DealerShipViewSet)
router.register(r'services', ServiceViewSet)