from django.db import models

class Vehicle(models.Model):
<<<<<<< HEAD
	veh_number = models.CharField("Number Plate of Vehicle", max_length = 10,  primary_key = True)
	veh_color = models.CharField("Color of Vehicle", max_length = 10)
	veh_type = models.CharField("Type of Vehicle", max_length = 10)
	veh_make = models.CharField("Make of Vehicle", max_length = 30)
	owner_id = models.IntegerField("Identification of Owner") #Aadhar for India
	charges = models.IntegerField("Charges Dues",default = 0)
	penalty = models.IntegerField("Penalty Dues",default = 0)
	lastcrossing_lat = models.FloatField("Last seen latitude", default = -1.0)
	lastcrossing_long = models.FloatField("Last seen longitude", default  = -1.0)
	missing = models.BooleanField("Missing", default = False)
	missing_when = models.DateTimeField("Time of Missing Report", default = None)

=======
    veh_number = models.CharField("Number Plate of Vehicle", max_length = 10,  primary_key = True)
    veh_color = models.CharField("Color of Vehicle", max_length = 10)
    veh_type = models.CharField("Type of Vehicle", max_length = 10)
    veh_make = models.CharField("Make of Vehicle", max_length = 30)
    owner_id = models.IntegerField("Identification of Owner") #Aadhar for India
    charges = models.IntegerField("Charges Dues",default = 0)
    penalty = models.IntegerField("Penalty Dues",default = 0)
    lastcrossing_lat = models.FloatField("Last seen latitude", default = -1.0)
    lastcrossing_long = models.FloatField("Last seen longitude", default  = -1.0)
	
>>>>>>> fd79596c5e7bdd51ca9230cd22440fdbf46f2704
'''
class Penalty(models.Model):#Include type of offence in a set
    veh_number = models.ForeignKey(Vehicle)
    offence = models.CharField("Offence", max_length = 100)
    loc_lat = models.FloatField("Latitude")
    loc_long = models.FloatField("Longitude")
    when = models.DateTimeField()
'''

<<<<<<< HEAD
class Charges(models.Model):
	charge_kind_choice = (
			("TC", "Toll Charge"),
			("TV", "Traffic Light Violation"),
			("OS", "Overspeeding"),
			)	

	veh_number = models.ForeignKey(Vehicle)
	charge_type = models.BooleanField("Offence")
	charge_kind = models.CharField("Charge nature", max_length = 2, choices = charge_kind_choice)
        charge = models.CharField("Charges", max_length = 100)        
	loc_lat = models.FloatField("Latitude")
        loc_long = models.FloatField("Longitude") 
        when = models.DateTimeField("Date of Charge")

class Payment(models.Model): #Implement payment mode in a set
	payment_choice = (
			("CA", "Cash"),
			("NB", "Net Banking"),
			("OW", "Online Wallet"),
			)

	veh_number = models.ForeignKey(Vehicle)
	payment_type = models.BooleanField("Offence")
	payment_mode = models.CharField("Mode of Payment", max_length = 2, choices = payment_choice)
	when = models.DateTimeField("Date of Payment")
=======
class Charges(models.Model):#Implement charge nature in a set
    veh_number = models.ForeignKey(Vehicle)
    charge_type = models.BooleanField("Offence")
    charge_kind = models.CharField("Charge nature", max_length = 30)
    charge = models.CharField("Charges", max_length = 100)        
    loc_lat = models.FloatField("Latitude")
    loc_long = models.FloatField("Longitude") 
    when = models.DateTimeField("Date of Charge")

class Missing(models.Model):
    veh_number = models.ForeignKey(Vehicle)
    when = models.DateTimeField("Date of Filing Report")

class Payment(models.Model): #Implement payment mode in a set
    veh_number = models.ForeignKey(Vehicle)
    payment_type = models.BooleanField("Offence")
    payment_mode = models.CharField("Mode of Payment", max_length = 20)
    when = models.DateTimeField("Date of Payment")
>>>>>>> fd79596c5e7bdd51ca9230cd22440fdbf46f2704

'''
class Crossings(models.Model):
	loc_lat = models.FloatField("Latitude")
        loc_long = models.FloatField("Longitude")
'''	
