from django.db import models

class Vehicle(models.Model):
	veh_number = models.CharField("Number Plate of Vehicle", max_length = 10,  primary_key = True)
	veh_color = models.CharField("Color of Vehicle", max_length = 10)
	veh_type = models.CharField("Type of Vehicle", max_length = 10)
	veh_make = models.CharField("Make of Vehicle", max_length = 30)
	owner_id = models.IntegerField("Identification of Owner") #Aadhar for India
	road_charges = models.IntegerField("Charges due", default = 0)
	penalty = models.IntegerField("Fines due", default = 0)
	lastcrossing_lat = models.FloatField("Last seen latitude", default = -1.0)
	lastcrossing_long = models.FloatField("Last seen longitude", default  = -1.0)
	

class Penalty(models.Model):#Include type of offence in a set
	veh_number = models.ForeignKey(Vehicle)
	offence = models.CharField("Offence", max_length = 100)
	loc_lat = models.FloatField("Latitude")
        loc_long = models.FloatField("Longitude")
	when = models.DateTimeField()

class Charges(models.Model):#Include location of tolls
	veh_number = models.ForeignKey(Vehicle)
        charge = models.CharField("Charges", max_length = 100)        
	loc_lat = models.FloatField("Latitude")
        loc_long = models.FloatField("Longitude") 
        when = models.DateTimeField()

class Crossings(models.Model):
	loc_lat = models.FloatField("Latitude")
        loc_long = models.FloatField("Longitude")
	
