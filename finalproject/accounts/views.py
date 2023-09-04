from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from django.views.decorators.cache import cache_control
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import IntegrityError


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
           try:
                user =  User.objects.create_user(form.cleaned_data['username'],
                                                    form.cleaned_data['email'],
                                                    form.cleaned_data['password'],)
                
                user.save()
                return HttpResponseRedirect(reverse('accounts:login'))
           except IntegrityError:
                 form = RegistrationForm()
                 return render(request, "accounts/register.html", {"form": form,
                                                                   "error": "Username already exists"})
               
    form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('new:index'))
        else:
             form = LoginForm()
             return render(request, "accounts/login.html", {"form": form,
                                                            "error": "Incorrect Username or Password"})
    form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def profile(request):
    return render(request, "accounts/profile.html" )
