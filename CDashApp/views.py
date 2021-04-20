from django.shortcuts import render


def dashboard(request):
    context = {'link_active':'dashboard' , 'active_class':'dashboard'} 
    return render(request ,'CDashApp/dashboard.html' ,context)


def edit_profile(request):
    context = {'link_active':'edit_profile', 'active_class':'dashboard'}
    return render(request ,'CDashApp/edit_profile.html' ,context)



def applied_job(request):
    context = {'link_active':'applied_job', 'active_class':'dashboard'}
    return render(request ,'CDashApp/applied_job.html' ,context)



def favourite_job(request):
    context = {'link_active':'favourite_job', 'active_class':'dashboard'}
    return render(request ,'CDashApp/favourite_job.html' ,context)


def message(request):
    context = {'link_active':'message', 'active_class':'dashboard'}
    return render(request ,'CDashApp/message.html' ,context)


def resume(request):
    context = {'link_active':'resume', 'active_class':'dashboard'}
    return render(request ,'CDashApp/resume.html' ,context)

def resetPassword(request):
    context = {'link_active':'reset_password', 'active_class':'dashboard'}
    return render(request ,'CDashApp/resetPassword.html' ,context=None)
