from django.shortcuts import render

### Candidate Frontend ####

def index(request):
    context = {'active_class':'index'}
    return render(request ,'JW/index.html' ,context)


def contact_us(request):
    context = {'active_class':'contact_us'}
    return render(request ,'JW/contact_us.html' ,context)

def error(request):
    return render(request ,'JW/error.html' ,context=None)

def about_us(request):
    return render(request ,'JW/about_us.html' ,context=None)

def our_services(request):
    return render(request ,'JW/our_services.html' ,context=None)

def privacy(request):
    return render(request ,'JW/privacy.html' ,context=None)

def terms(request):
    return render(request ,'JW/terms.html' ,context=None)

def sitemap(request):
    return render(request ,'JW/sitemap.html' ,context=None)

def register(request):
    return render(request ,'CRegApp/register.html' ,context=None)

def login(request):
    return render(request ,'CRegApp/login.html' ,context=None)

def otp(request):
    return render(request ,'CRegApp/otp.html' ,context=None)

def cfpwd(request):
    return render(request ,'CRegApp/cfpwd.html' ,context=None)









