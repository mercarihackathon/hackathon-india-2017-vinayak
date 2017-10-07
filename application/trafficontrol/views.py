from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("YOYO")

def missing(request):
	if request.POST.get('vehicle') in Vehicle.objects.filter(missing = True):
		return

def add_charge(request):
		 
# Create your views here.
