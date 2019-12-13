from rest_framework import routers
from .views import DealerViewSet

router = routers.DefaultRouter()
router.register(r'dealers', DealerViewSet)