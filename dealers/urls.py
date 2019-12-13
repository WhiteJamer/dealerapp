from django.conf.urls import url
from dealers.views import DealerDetail, DealerList, DealerCreate

app_name = 'dealers'

urlpatterns = [
    url(r'^add', DealerCreate.as_view(), name='dealer_add'),
    url(r'^(?P<slug>[\w|\W]+)', DealerDetail.as_view(), name='dealer_detail'),
    url(r'^', DealerList.as_view(), name='dealer_list'),
]
