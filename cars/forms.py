from django import forms
from .models import Car
from dealers.models import Dealer

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['vin', 'brand', 'model', 'color', 'dealer', 'dealership']

    # Показывает только дилеров текущего пользователя
    def __init__(self, user, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['dealer'].queryset = Dealer.objects.filter(user=user)


