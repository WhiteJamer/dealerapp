from django.views.generic import ListView, DetailView, View
from .models import User

class UserDetail(DetailView):
    slug_field = 'username'
    context_object_name = 'auser' # another user not request.user
    queryset = User.objects.all()




