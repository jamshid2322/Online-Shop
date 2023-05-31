from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def user_login(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        if not phone_number or not password:
            messages.info(request, "Phone Number or password not given.")
            return redirect("user_login")
        
        user = User.objects.filter(phone_number=phone_number)
        if not user:
            messages.error(request, "Phone number not found")
            return redirect("user_login")
        
        user = authenticate(phone_number=phone_number,password=password)
        if not user:
            messages.info(request, "Password incorrect!!")
            return redirect('user_login')
        
        login(request, user)
        return redirect("home")
    
    return render(request, 'user_login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')



        if not phone_number or not password :
            messages.info(request, 'Fill in gaps!!!')
            return redirect('register')  
        user = User.objects.filter(phone_number=phone_number).first()
        if user:
            messages.info(request, "Phone number has already registered. Go to login.")
            return redirect('register')
        if password != password1:
            messages.info(request, "Password must match!")
            return redirect('register')  
        User.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, password=password)
        return redirect("home")
    

    return render(request, 'login-register.html')


def user_logout(request):
    logout(request)
    return redirect("home")
