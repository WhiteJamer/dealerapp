from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View, DetailView, ListView
from dealers.models import Dealer
from .forms import DealerForm
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class DealerCreate(View):

    @method_decorator(login_required)
    def get(self, request):
        context = {'form':DealerForm}
        return render(request, 'dealers/dealer_create.html', context)

    @method_decorator(login_required)
    def post(self, request):
        form = DealerForm(request.POST)
        if form.is_valid():
            new_dealer = Dealer(
                name = form.cleaned_data['name'],
                user = request.user
            )
            new_dealer.save()
            return redirect(new_dealer)
        else:
            return redirect(reverse('dealers:dealer_create'))


class DealerDetail(DetailView):
    context_object_name = 'dealer'
    slug_field = 'name'
    queryset = Dealer.objects.all()


class DealerList(ListView):
    context_object_name = 'dealers'
    queryset = Dealer.objects.all()


class DealerUpdate(View):

    def get(self, request, slug):
        dealer = get_object_or_404(Dealer, name__iexact=slug)
        if request.user == dealer.user:
            context = {'form':DealerForm(initial=dealer)}
            return render(request, 'dealers/dealer_update.html', context)
        else:
            HttpResponse('You is not owner')

    def post(self, request, slug):
        dealer = get_object_or_404(Dealer, name__iexact=slug)
        if request.user == dealer.user:
            form = DealerForm(request.user, request.POST)
            if form.is_valid():
                new_dealer = Dealer(
                    name = form.cleaned_data['name'],
                    dealer = form.cleaned_data['dealer']
                )
                new_dealer.save()
                return redirect(new_dealer)
            else:
                return redirect(reverse('dealership:dealership_update'))
        else:
            HttpResponse('You is not owner')

