from django.shortcuts import render, redirect



# Create your views here.

def EPricing(request):
    context = {'active_class':'EPricing'}
    return render(request, 'EPricingApp/Epricingplan.html', context)

