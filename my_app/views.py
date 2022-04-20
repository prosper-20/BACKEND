import imp
import re
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Oops, email is already connected to another account")
            elif User.objects.filter(name=name).exists():
                messages.info(request, "Username already exists")
            else:
                User.objects.create(
                    name=name,
                    email=email,
                    password=password,
                )
                User.save()
        else:
            messages.info(request, "Both passowrds do not match")
    return render(request, 'register.html')


def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    context = {
        'amount': amount,
    }
    return render(request, 'counter.html', context)
