from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View, DetailView, ListView
from .forms import CarForm
from .models import Car
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CarCreate(View):

    @method_decorator(login_required)
    def get(self, request):
        context = {'form':CarForm(user=request.user)}
        return render(request, 'cars/car_create.html', context)

    @method_decorator(login_required)
    def post(self, request):
        form = CarForm(request.user, request.POST)
        if form.is_valid():
            new_car = Car(
                vin = form.cleaned_data['vin'],
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'],
                color = form.cleaned_data['color'],
                dealer = form.cleaned_data['dealer'],
            )
            new_car.save()
            return redirect(new_car)
        else:
            return redirect(reverse('cars:car_create'))


class CarDetail(DetailView):
    context_object_name = 'car'
    slug_field = 'vin'
    queryset = Car.objects.all()


class CarList(ListView):
    context_object_name = 'cars'
    queryset = Car.objects.all()


class CarUpdate(View):

    def get(self, request, slug):
        car = get_object_or_404(Car, vin__iexact=slug)
        if request.user == car.dealer.user:
            context = {'form':CarForm(request.user, instance=car)}
            return render(request, 'cars/car_update.html', context)
        else:
            HttpResponse('You is not owner')

    def post(self, request, slug):
        car = get_object_or_404(Car, vin__iexact=slug)
        if request.user == car.dealer.user:
            form = CarForm(request.user, request.POST, instance=car)
            if form.is_valid():
                car = form.save()
                return redirect(car)
            else:
                return redirect(reverse('cars:car_edit', kwargs={'slug':car.vin}))
        else:
            HttpResponse('You is not owner')

