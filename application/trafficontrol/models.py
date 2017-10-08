from django.db import models

class Vehicle(models.Model):
    veh_number = models.CharField("Vehicle Registration Number", max_length = 10,  primary_key = True)
    veh_color = models.CharField("Color of Vehicle", max_length = 10)
    veh_type = models.CharField("Type of Vehicle", max_length = 10)
    veh_make = models.CharField("Make of Vehicle", max_length = 30)
    owner_id = models.IntegerField("Identification of Owner") #Aadhar for India
    road_charge = models.IntegerField("Road Charges Dues", default = 0)
    penalty = models.IntegerField("Penalty Dues", default = 0)
    lastcrossing_lat = models.FloatField("Last seen latitude", default = -1.0)
    lastcrossing_long = models.FloatField("Last seen longitude", default  = -1.0)
    
    def __str__(self):
        return self.veh_number

class Missing(models.Model):
    veh_number = models.ForeignKey(Vehicle, verbose_name = "Vehicle Registration Number")
    when = models.DateTimeField("Date of Missing Report")

'''
class Penalty(models.Model):#Include type of offence in a set
    veh_number = models.ForeignKey(Vehicle)
    offence = models.CharField("Offence", max_length = 100)
    loc_lat = models.FloatField("Latitude")
    loc_long = models.FloatField("Longitude")
    when = models.DateTimeField()
'''

class Charges(models.Model):
    charge_choice = (
		("TC", "Toll Charge"),
		("TV", "Traffic Light Violation"),
		("OS", "Overspeeding"),
    		)	

    veh_number = models.ForeignKey(Vehicle, verbose_name = "Vehicle Registration Number")
    charge_type = models.BooleanField("Offence")
    charge = models.CharField("Charging nature", max_length = 2, choices = charge_choice)
    loc_lat = models.FloatField("Latitude")
    loc_long = models.FloatField("Longitude") 
    when = models.DateTimeField("Date of Charge")
    
    def __str__(self):
        return self.veh_number

class Payment(models.Model): #Implement payment mode in a set
	payment_choice = (
			("CA", "Cash"),
			("NB", "Net Banking"),
			("OW", "Online Wallet"),
			)

	veh_number = models.ForeignKey(Vehicle, verbose_name = "Vehicle Registration Number")
	payment_type = models.BooleanField("Offence")
	payment_mode = models.CharField("Mode of Payment", max_length = 2, choices = payment_choice)
	amount = models.FloatField("Amount Paid", default = 0)
	when = models.DateTimeField("Date of Payment")

class Crossings(models.Model):
	loc_lat = models.FloatField("Latitude")
        loc_long = models.FloatField("Longitude")
