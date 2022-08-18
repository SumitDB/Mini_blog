from multiprocessing import AuthenticationError
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm , LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from reg.models import Post
# Create your views here.
#Home
def Home(request):
    posts = Post.objects.all()
    return render(request, 'reg/home.html', {'posts':posts})

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
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations.. !!! You have become an Author')
            form.save()
    else:
        form = SignUpForm() 
    return render(request, 'reg/signup.html',{'form':form})

#Login
def User_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Logout
def User_Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, " Logged in Successfully !!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'reg/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

#Login
def Login(request):
    return render(request, 'reg/login.html')