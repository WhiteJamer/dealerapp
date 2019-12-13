from django.conf.urls import url
from dealership.views import DealerShipDetail, DealerShipList, DealerShipCreate, DealerShipUpdate

app_name = 'dealership'

urlpatterns = [
    url(r'^add', DealerShipCreate.as_view(), name='dealership_add'),
    url(r'^(?P<slug>[\w|\W]+)/edit', DealerShipUpdate.as_view(), name='dealership_edit'),
    url(r'^(?P<slug>[\w|\W]+)', DealerShipDetail.as_view(), name='dealership_detail'),

    url(r'^', DealerShipList.as_view(), name='dealership_list'),
]
