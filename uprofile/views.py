from django.views.generic import ListView, DetailView, View
from .models import User

class UserList(ListView):
    model = User
    queryset = User.objects.all()


class UserDetail(DetailView):
    context_object_name = 'auser' # another user not request.user
    queryset = User.objects.all()




