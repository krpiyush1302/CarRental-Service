from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import *
from . models import CarRent
from . models import Customerdetails,Orders

# Create your views here.
def home(request):
    rent = CarRent.objects.all()
    return render(request,'index.html',{'rent':rent})


def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('login_page')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('login_page')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('home')
     
    # Render the login page template (GET request)
    return render(request, 'login.html')


def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('register_page')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('register_page')
     
    # Render the registration page template (GET request)
    return render(request, 'Register.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def cardetails(request):
    carid = request.GET.get('carid','')
    cardata = CarRent.objects.filter(id=carid)
    return render(request,'cardetails.html',{'car':cardata})

def checkout1(request):
    carprice = request.GET.get('carprice','')
    carid = request.GET.get('carbook','')
    #print(carprice)
    if request.method == 'POST':
        name = request.POST.get('name','')
        cprice = request.POST.get('price','')
        carid = request.POST.get('carid','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        licence = request.POST.get('licence','')
        images = request.POST.get('images','')
        address = request.POST.get('Address','')
        bookingdate = request.POST.get('bookingdate','')
        bookinglocation = request.POST.get('bookinglocation','')
        returndate = request.POST.get('returndate','')
        destinationlocation = request.POST.get('destinationlocation','')
        city = request.POST.get('city','')
        state = request.POST.get('State','')
        pincode = request.POST.get('pincode','')
        country = request.POST.get('country','')
        Customerdetails.objects.filter()
        if request.user.is_authenticated:
            Customerdetails.objects.create(
                user = request.user,
                Name = name ,
                Email = email ,
                phone = phone ,
                DrivingLicene = licence , 
                img = images , 
                Address = address , 
                Bookingdate = bookingdate , 
                Returndate = returndate , 
                Bookinglocation = bookinglocation , 
                Destinationlocation = destinationlocation , 
                City = city , 
                State = state , 
                Pincode = pincode , 
                Country = country

            )
            
        bookingdate = datetime.strptime(bookingdate, '%Y-%m-%d')
        returndate = datetime.strptime(returndate, '%Y-%m-%d') 
        difference = relativedelta(returndate, bookingdate)
        number_of_days = difference.days 
        print(number_of_days)
        print("hi")
        print(cprice)
        #print(number_of_days*carprice)
        amount=int(number_of_days)* int(cprice)
        print(amount)
        return render(request,'payment.html',{'days':number_of_days,'price':cprice, 'amount':amount,'carid':carid,'licence':licence})
        
    return render(request,'checkout.html',{"price":carprice,'carid':carid})

def ridepayment(request):

    return render(request,'payment.html')

def about_us(request):
    return render(request, 'AboutUs.html')

def order1(request):
    carid = request.GET.get('carid', '')
    days = request.GET.get('days', '')
    price = request.GET.get('price', '')
    amount = request.GET.get('amount', '')
    licence = request.GET.get('licence', '')
    cardata = CarRent.objects.filter(id= carid)

    
    customerdata=Customerdetails.objects.get(DrivingLicene=licence)
    #id = 0
    #for i in customerdata:
     #   id +=i.id

    if request.user.is_authenticated:
        Orders.objects.create(
            user=request.user,
            customerdetails = customerdata,
            carid=carid,
            price=amount
        )
        
    return render(request, 'order.html', {'cardata': cardata, 'days': days, 'price': price, 'amount': amount})
    
    