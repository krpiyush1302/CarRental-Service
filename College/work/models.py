from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarRent(models.Model):
    Carname = models.CharField(max_length=150)
    Fueltype = models.CharField(max_length=50)
    Price = models.CharField(max_length=500)
    img = models.ImageField(default='')
    phone = models.CharField(max_length=15)
    Date = models.DateField(null=True)
    Details = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.Carname} {self.Fueltype} {self.Price} {self.img} {self.phone} {self.Date} {self.Details}"
    
class Customerdetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    DrivingLicene = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    img = models.ImageField(default='')
    Bookingdate = models.DateTimeField(null=True)
    Returndate = models.DateTimeField(null=True)
    Bookinglocation = models.CharField(max_length=255)
    Destinationlocation = models.CharField(max_length=255)
    City=models.CharField(max_length=35)
    State=models.CharField(max_length=50)
    Pincode=models.IntegerField(null=True)
    Country=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Name}"

class Orders(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     customerdetails = models.ForeignKey(Customerdetails,on_delete=models.CASCADE)
     carid = models.CharField(max_length=100)
     price = models.CharField(max_length=100)

     def __str__(self):
        return f"{self.user} {self.customerdetails} {self.carid} {self.price}"