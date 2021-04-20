from django.shortcuts import render

# Create your views here.

def job_detail(request):
    context = {'active_class':'jobs_detail'}
    return render(request, 'CJobApp/job_detail.html' ,context)

def jobs_list(request):
    context = {'active_class':'jobs_list'}
    return render(request, 'CJobApp/job_listing_list_left_filter.html' , context)

def job_listing(request):
    context = {'active_class':'jobs_list'}
    return render(request, 'CJobApp/job_listing_based_on_location.html' , context)

def job_category(request):
    context = {'active_class':'job_category'}
    return render(request, 'CJobApp/job_category.html' , context)
