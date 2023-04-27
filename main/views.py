from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, "main/login.html")

def signup(request):
    return render(request, "main/signup.html")

def team(request):
    return render(request, "main/team.html")

def login_user(request):
    pass

def logout_user(request):
    pass