from django import forms
from .models import DealerShip
from dealers.models import Dealer

class DealerShipForm(forms.ModelForm):

    class Meta:
        model = DealerShip
        fields = ['name', 'dealer']

    # Показывает только дилеров текущего пользователя
    def __init__(self, user, *args, **kwargs):
        super(DealerShipForm, self).__init__(*args, **kwargs)
        self.fields['dealer'].queryset = Dealer.objects.filter(user=user)


