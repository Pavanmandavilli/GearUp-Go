from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contact',views.contact,name='contact'),
    path('rentalservices',views.rentalservices,name='rentalservices'),
    path('book/<int:vid>',views.book,name='book'),
    path('login',views.Login_view,name='login'),
    path('myaccount',views.profile,name='myaccount'),
    path('booking',views.savebookingdetails,name='booking'),
    path('bookingdetails',views.booking_details,name='bookingdetails'),
    path('register',views.register,name='register'),
    path('protected',views.protected_view,name='home_page'),
    path('logout',views.logout_view,name='logout'),
    path('verifyotp',views.verify_otp,name='verifyotp'),
    path('password_reset',views.password_reset,name='password_reset'),
]