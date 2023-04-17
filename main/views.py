from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, "main/login.html")

def signup(request):
    return render(request, "main/signup.html")

def team(request):
    return render(request, "main/team.html")