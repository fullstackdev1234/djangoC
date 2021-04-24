from django.shortcuts import render

# Create your views here.

def pricing(request):
    context = {'active_class':'pricing'}
    return render(request, 'CPricingApp/pricingplan.html' ,context)