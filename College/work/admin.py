from django.contrib import admin
from .models import CarRent
from .models import Customerdetails,Orders


# Register your models here.

class CarRentAdmin(admin.ModelAdmin):
    list_display=("Carname", "Fueltype", "Price", "img", "phone", "Date", "Details",)

admin.site.register(CarRent, CarRentAdmin)

class CustomerdetailsAdmin(admin.ModelAdmin):
    list_display=("user", "Name", "Email", "phone", "DrivingLicene",  "Address", "Bookingdate", "Returndate", "Bookinglocation", "Destinationlocation", "City", "State", "Pincode", "Country",)

admin.site.register(Customerdetails, CustomerdetailsAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display=("user", "customerdetails", "carid", "price",)
    
admin.site.register(Orders, OrdersAdmin)