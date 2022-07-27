from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
#Home
def Home(request):
    return render(request, 'reg/home.html')

#About
def About(request):
    return render(request, 'reg/about.html')

#Contact
def Contact(request):
    return render(request, 'reg/contact.html')

#Dashboard
def Dashboard(request):
    return render(request, 'reg/dashboard.html')

#Signup
def User_Signup(request):
    form = SignUpForm()
    return render(request, 'reg/signup.html',{'form':form})

#Login
def User_Logout(request):
    return HttpResponseRedirect('/')

#Logout
def User_Login(request):
    return render(request, 'reg/login.html')

#Login
def Login(request):
    return render(request, 'reg/login.html')