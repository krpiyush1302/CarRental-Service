from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('login/',views.login_page, name='login_page'),
    path('logout/',views.logout_page, name='logout_page'),
    path('cardetails/',views.cardetails,name='cardetails'),
    path('checkout1/',views.checkout1,name='checkout1'),
    path('ridepayment/',views.ridepayment,name='ridepayment'),
    path('about_us/',views.about_us,name='about_us'),
    path('order1/', views.order1, name='order1'),
    path('register/',views.register_page,name='register_page'),
]