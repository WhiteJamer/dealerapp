from django.conf.urls import url
from .views import UserDetail

app_name = 'uprofile'

urlpatterns = [
    url(r'^(?P<slug>[\w|\W]+)/$', UserDetail.as_view(), name='user_detail')
]
