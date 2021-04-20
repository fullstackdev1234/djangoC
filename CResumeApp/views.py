from django.shortcuts import render



def resume_category(request):
    context = {'active_class':'resume'}
    return render(request ,'CResumeApp/resume_category.html' ,context)

def resume_listing(request):
    context = {'active_class':'resume'}
    return render(request ,'CResumeApp/resume_listing.html' ,context)

def resume_detail(request):
    context = {'active_class':'Resume'}
    return render(request ,'CResumeApp/resume_detail.html' ,context)


def resume_list(request):
    context = {'active_class':'Resume'}
    return render(request ,'CResumeApp/resume_list.html' ,context)



