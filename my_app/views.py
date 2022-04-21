from email import message
import imp
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Oops, email is already connected to another account")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                messages.info(request, "Your account has been created successfully")
                return redirect("index")
        else:
            messages.info(request, "Both passowrds do not match")
            # You just it from register.html to form-regsiter
    return render(request, 'form-regiser.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, "You are logged in")
            return redirect('/')
        else:
            messages.error(request, "Credentials not valid")
            return redirect("login")
    #You changed from login.htnl to form-register
    return render(request, 'form-regiser.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
        


def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    context = {
        'amount': amount,
    }
    return render(request, 'counter.html', context)
