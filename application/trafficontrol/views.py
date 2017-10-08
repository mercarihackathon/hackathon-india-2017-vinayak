from django.shortcuts import render
from django.http import HttpResponse

Toll = 0
LV_charge = 2000
OS_charge = 5000

def index(request):
    return HttpResponse("YOYO")
    
def alert_police(request):
    cont = 1
    missing_obj = Vehicle.objects.filter(missing = True)
    missing_veh = [x.veh_number for x in missing_obj]
    if request.POST.get('vehicle') in missing_veh:
        cont = 0 #Alert police for a theft
    elif len(Vehicle.objects.filter(veh_number = 'vehicle', veh_color = 'color', veh_type = 'type', veh_make = 'make')) == 0:
        cont = 0 #Alert police for some discrepancy
    return cont

def add_charge(request):
    cont = alert_police(request)
    if cont:
        #veh_number, charge, loc_lat, loc_long, when
        
        
# Create your views here.
