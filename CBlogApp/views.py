from django.shortcuts import render

# Create your views here.

### Blog ####

def blog(request):
    context = {'active_class':'blog'}
    return render(request ,'CBlogApp/blog_homepage.html' ,context)

def blog_news(request):
    context = {'active_class':'blog'}
    return render(request ,'CBlogApp/blog_listing.html' ,context)
    
def blog_reels(request):
    context = {'active_class':'blog'}
    return render(request ,'CBlogApp/blog_page.html' ,context)

def blog_career(request):
    context = {'active_class':'blog'}
    return render(request ,'CJobApp/job_listing_list_left_filter.html' ,context)

def blog_test(request):
    context = {'active_class':'blog'}
    return render(request ,'CJobApp/job_listing_list_left_filter.html' ,context)

def blog_testimonial(request):
    context = {'active_class':'blog'}
    return render(request ,'CJobApp/job_listing_list_left_filter.html' ,context)

def blog_demo_page(request):
    context = {'active_class':'blog'}
    return render(request, 'CBlogApp/demo_blog_page.html' , context)

