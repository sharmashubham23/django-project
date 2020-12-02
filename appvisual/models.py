from django.db import models

# Create your models here.



class Customer(models.Model):
    
	X_axis_Data = models.CharField(max_length=200)
	Y_axis_Data = models.CharField(max_length=200)
    



