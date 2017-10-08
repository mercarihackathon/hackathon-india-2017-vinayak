from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .forms import *

def index(request):
    return HttpResponse("YOYO")

def register(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            vehicle = form.save(commit=False)
            vehicle.save()
            return render(request, 'trafficontrol/thanks.html', {})
    else:
        form = VehicleForm()

    return render(request, 'trafficontrol/form.html', {'form': form, 'action_url':'register'})

def missing(request):
    if request.method == 'POST':
        form = MissingForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            missing = form.save(commit=False)
            missing.when = datetime.now()
            missing.save()
            return render(request, 'trafficontrol/thanks.html', {})
    else:
        form = MissingForm()

    return render(request, 'trafficontrol/form.html', {'form': form, 'action_url':'missing'})

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            payment = form.save(commit=False)
            payment.save()
            return render(request, 'trafficontrol/thanks.html', {})
    else:
        form = PaymentForm()

    return render(request, 'trafficontrol/form.html', {'form': form, 'action_url':'payment'})
