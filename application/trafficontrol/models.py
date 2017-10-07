from django.db import models

class Car(models.Model):
	car_id = models.IntegerField("Identification of Car", default = None, primary_key = True)
	owner_id = models.IntegerField("Identification of Owner", default = None) #Aadhar for India
	
	
