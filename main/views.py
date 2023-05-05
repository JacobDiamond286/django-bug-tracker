from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    #check to see if logging in
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['psw']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, please try again.")
            return redirect('index')
    else:
        return render(request, 'main/index.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

def signup(request):
    return render(request, "main/signup.html")

def team(request):
    return render(request, "main/team.html")
