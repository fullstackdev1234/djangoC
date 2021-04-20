from django.shortcuts import render, redirect



# Create your views here.

def Eregister(request):
    context = {'active_class':'Eregister'}
    return render(request, 'ERegApp/Eregister.html', context)


def Elogin(request):
    context = {'active_class':'Elogin'}
    return render(request, 'ERegApp/Elogin.html' , context)

def Eotp(request):
    context = {'active_class':'Eotp'}
    return render(request, 'ERegApp/Eotp.html' ,context)


def Efpwd(request):
    context = {'active_class':'Efpwd'}
    return render(request, 'ERegApp/Efpwd.html' , context)