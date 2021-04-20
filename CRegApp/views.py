from django.shortcuts import render, redirect



# Create your views here.

def register(request):
    context = {'active_class':'register'}
    return render(request, 'CRegApp/register.html', context)


def login(request):
    context = {'active_class':'login'}
    return render(request, 'CRegApp/login.html' , context)

def otp(request):
    context = {'active_class':'otp'}
    return render(request, 'CRegApp/otp.html' ,context)


def cfpwd(request):
    context = {'active_class':'cfpwd'}
    return render(request, 'CRegApp/cfpwd.html' , context)