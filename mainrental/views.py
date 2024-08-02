from django.shortcuts import render, redirect,HttpResponse
from .models import mainrental_rs,mainrental_register,bookingdetails
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authentication,logout as logout_authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       phone = request.POST['phone']
       user_check =User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() or  mainrental_register.objects.filter(phone=phone).exists()
       if user_check:
           content = {'message': 'User already exists'}
           return render(request,"register.html",content)
           print('User already exists')
       else:
           user = User.objects.create_user(username=username,email=email,password=password)
           user.username = username
           user.email = email
           user.save()
           md=mainrental_register.objects.create()
           md.user= user
           md.phone = phone
           md.save()
           return redirect('login')
           print('success')
    else:
       print('error')

    return render(request, 'register.html')

def Login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            login_authentication(request,user)
            request.session['username'] = user.username  # Set the username in the session
            return redirect('index')
        else:
            content = {'message': 'please check username and password'}
            return render(request,"login.html",content)
    else:
        print('fail')
        return render(request, "login.html")

def index(request):
    return render(request, 'index.html')


def protected_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'), username=request.user.username)
    else:
        return redirect('login')
def logout_view(request):
        logout_authentication(request)
        return redirect('login')
def aboutus(request):
    return render(request,'About Us.html')
def contact(request):
    return render(request,'Contact Us.html')
def rentalservices(request):
    rss=mainrental_rs.objects.all()
    return render(request,'Rental Services.html',{'rss':rss})
def login(request):
    return render(request,'login.html')


def book(request,vid):
    if request.user.is_authenticated:
        veh=mainrental_rs.objects.filter(id=vid).values()
        request.session['vehicle']=vid
        return render(request,'BookVehicle.html',{"vehicle":veh[0]})
    else:
        return redirect('login')

def savebookingdetails(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            try:
                vehicle = mainrental_rs.objects.get(id=request.session.get("vehicle"))

                name=request.POST.get('carname')
                price=request.POST.get('price')
                hours=request.POST.get('duration')
                startdate=request.POST.get('startdate')
                enddate=request.POST.get('enddate')
                phone=request.POST.get('phone')
                # cd=mainrental_register.objects.get(user=request.user)

                md=bookingdetails.objects.create(user=request.user,name=name,price=price,hours=hours,start_date_time=startdate,end_date_time=enddate,phone=phone,car=vehicle)
            except Exception as e:
                return HttpResponse(e)
            return HttpResponse("Added Successfully")


def profile(request):
    user=request.user
    try:
        user_data=mainrental_register.objects.get(user=user)
    except mainrental_register.DoesNotExist:
        user_data=None
    print(user_data)
    return render(request,'MyAccount.html',{"user_data":user_data})


def booking_details(request):
    if request.user.is_authenticated:
        all_booking_details = bookingdetails.objects.filter(user=request.user)
        context = {
            'booking_details': all_booking_details
        }
        print(all_booking_details)
        return render(request, 'MyBookings.html', context)
    else:
        return render(request,'login.html')


from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.hashers import make_password
import random

def generate_otp():
    otp = random.randint(1000, 9999)
    return otp
def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Generate OTP
            otp = generate_otp()
            send_mail('Password Reset OTP', f'Your OTP is: {otp}', 'pavanmnadavilli485@gmail.com', [email])

            # Store OTP in session
            request.session['otp'] = otp
            request.session['email'] = email
            return render(request, 'change_password.html')
        else:
            print('Invalid Email')
    return render(request, 'change_password.html')

def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        print(otp_entered)
        print(request.session.get('otp'))
        if int(otp_entered) == int(request.session.get('otp')):

            email = request.session.get('email')
            user = User.objects.get(email=email)
            new_password = request.POST.get('new_password')
            user.password = make_password(new_password)
            user.save()
            print("password changed")
        else:
            print("invalid password")
    return render(request, 'change_password.html')
