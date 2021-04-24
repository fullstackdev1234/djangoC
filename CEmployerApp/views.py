from django.shortcuts import render

# Create your views here.

def employer_category(request):
    context = {'active_class':'employer_category'}
    return render(request, 'CEmployerApp/employer_category.html' ,context)

def employer_list(request):
    context = {'active_class':'employer_list'}
    return render(request, 'CEmployerApp/employer_list.html' ,context)

def employer_detail(request):
    context = {'active_class':'employer_detail'}
    return render(request, 'CEmployerApp/employer_detail.html' ,context)

def Eindex(request):
    context = {'active_class':'Eindex'}
    return render(request, 'CEmployerApp/Eindex.html' ,context)
