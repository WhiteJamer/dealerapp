from django.conf.urls import url
from .views import CarDetail, CarList, CarCreate, CarUpdate

app_name = 'cars'

urlpatterns = [
    url(r'^add', CarCreate.as_view(), name='car_add'),
    url(r'^(?P<slug>[\w|\W]+)/edit', CarUpdate.as_view(), name='car_edit'),
    url(r'^(?P<slug>[\w|\W]+)', CarDetail.as_view(), name='car_detail'),
    url(r'^', CarList.as_view(), name='car_list'),
]
