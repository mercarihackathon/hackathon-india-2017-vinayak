from django import forms

from trafficontrol.models import Missing, Vehicle, Payment

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['veh_number', 'veh_color', 'veh_type', 'veh_make', 'owner_id']


class MissingForm(forms.ModelForm):
    when = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Missing
        fields = ['veh_number']


class PaymentForm(forms.ModelForm):
    when = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Payment
        fields = ['veh_number', 'payment_type', 'payment_mode']
