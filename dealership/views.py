from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View, DetailView, ListView
from .models import DealerShip
from dealers.models import Dealer
from .forms import DealerShipForm
from django.shortcuts import redirect, reverse

class DealerShipCreate(View):

    def get(self, request):
        context = {'form':DealerShipForm(user=request.user)}
        return render(request, 'dealership/dealership_create.html', context)

    def post(self, request):
        form = DealerShipForm(request.user, request.POST)
        if form.is_valid():
            new_dealership = DealerShip(
                name = form.cleaned_data['name'],
                dealer = form.cleaned_data['dealer']
            )
            new_dealership.save()
            return redirect(new_dealership)
        else:
            return redirect(reverse('dealership:dealership_add'))


class DealerShipDetail(DetailView):
    context_object_name = 'dealership'
    slug_field = 'name'
    queryset = DealerShip.objects.all()


class DealerShipList(ListView):
    context_object_name = 'dealerships'
    queryset = DealerShip.objects.all()


class DealerShipUpdate(View):

    def get(self, request, slug):
        dealership = get_object_or_404(DealerShip, name__iexact=slug)
        if request.user == dealership.dealer.user:
            context = {'form':DealerShipForm(user=request.user, instance=dealership)}
            return render(request, 'dealership/dealership_update.html', context)
        else:
            HttpResponse('You is not owner')

    def post(self, request, slug):
        dealership = get_object_or_404(DealerShip, name__iexact=slug)
        if request.user == dealership.dealer.user:
            form = DealerShipForm(user=request.user, data=request.POST)
            if form.is_valid():
                new_dealership = DealerShip(
                    name = form.cleaned_data['name'],
                    dealer = form.cleaned_data['dealer']
                )
                new_dealership.save()
                return redirect(new_dealership)
            else:
                return redirect(reverse('dealership:dealership_edit'))
        else:
            HttpResponse('You is not owner')
