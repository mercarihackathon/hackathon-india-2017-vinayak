from django import forms

from trafficontrol.models import *

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['veh_number', 'veh_color', 'veh_type', 'veh_make', 'owner_id']


class MissingForm(forms.ModelForm):
    class Meta:
        model = Missing
        fields = ['veh_number']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['veh_number', 'payment_type', 'payment_mode', 'amount']

class ChargesForm(forms.ModelForm):
    class Meta:
        model = Charges
        fields = ['veh_number', 'charge', 'loc_lat', 'loc_long']

class CrossingsForm(forms.ModelForm):
    class Meta:
        model = Crossings
        fields = ['loc_lat', 'loc_long']
