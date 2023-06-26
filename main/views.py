from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def index(request):
    #check to see if logging in
    if request.method == "POST":
        username = 'uname' in request.POST
        password = 'psw' in request.POST
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

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have succesfully registered, Welcome!")
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'main/register.html', {'form':form})
    
    return render(request, 'main/register.html', {'form':form})

def team(request):
    return render(request, "main/team.html")
