from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from models import *

toll_charge = 100
lv_charge = 2000
os_charge = 5000

def index(request):
    return HttpResponse("YOYO")
    
def alert_police(request):
    cont = 1
    missing_obj = Vehicle.objects.filter(missing = True)
    missing_veh = [x.veh_number for x in missing_obj]
    vehicle = request.POST.get('vehicle')
    vcolor = request.POST.get('color')
    vtype = request.POST.get('type')
    vmake = request.POST.get('make')
    if len(Vehicle.objects.filter(veh_number = vehicle, veh_color = vcolor, veh_type = vtype, veh_make = vmake)) == 0:
        cont = 0 #Alert police for some discrepancy
    elif vehicle in missing_veh:
        cont = 0 #Alert police for finding a stolen vehicle
        Vehicle.objects.filter(veh_number = vehicle).loc_lat = request.POST.get('loc_lat')
        Vehicle.objects.filter(veh_number = vehicle).loc_long = request.POST.get('loc_long')
    return cont

def update(request):
    if request.method == "POST":
        cont = alert_police(request)
        if cont:
            Vehicle.objects.filter(veh_number = vehicle).loc_lat = request.POST.get('loc_lat')
            Vehicle.objects.filter(veh_number = vehicle).loc_long = request.POST.get('loc_long')
            if request.POST.get('charge'):
                add_charge(request)
    

def add_charge(request): #Receveing: veh_number, veh_color, veh_type, veh_make, loc_lat, loc_long
    charge = Charges()
    charge.veh_number = request.POST.get('vehicle')
    charge.charge = request.POST.get('charge_nature')
    if charge.charge == "TC":
        charge.charge_type = 0
        Vehicle.objects.filter(veh_number = charge.veh_number).road_charge += toll_charge
    else:
        charge.charge_type = 1
        if charge.charge == "OS":
            am = os_charge
            #Alert adjancent crossigs of a potential accident 
        elif charge.charge == "LV":
            am = lv_charge
        Vehicle.objects.filter(veh_number = charge.veh_number).penalty += am
    charge.loc_lat = request.POST.get('loc_lat')
    charge.loc_long = request.POST.get('loc_long')
    charge.when = datetime.now()
    return 1

 

from .forms import *

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
            payment.when = datetime.now()
            payment.save()
            return render(request, 'trafficontrol/thanks.html', {})
    else:
        form = PaymentForm()

    return render(request, 'trafficontrol/form.html', {'form': form, 'action_url':'payment'})

def demo(request):
    vform = VehicleForm()
    cform = ChargeForm()
    return render(request, 'trafficontrol/demo.html', {'vform': vform, 'cform': cform})
