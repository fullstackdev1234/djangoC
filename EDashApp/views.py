from django.shortcuts import render, redirect



# Create your views here.

def Edashboard(request):
    context = {'active_class':'Edashboard'}
    return render(request, 'EDashApp/Edashboard.html', context)


def EApplications(request):
    context = {'active_class':'EApplications'}
    return render(request, 'EDashApp/EApplications.html' , context)

def ECompany_page(request):
    context = {'active_class':'ECompany_page'}
    return render(request, 'EDashApp/ECompany_page.html' ,context)


def EEdit_profile(request):
    context = {'active_class':'EEdit_profile'}
    return render(request, 'EDashApp/EEdit_profile.html' , context)

def EManage_jobs(request):
    context = {'active_class':'EManage_jobs'}
    return render(request, 'EDashApp/EManage_jobs.html' , context)

def EMessage(request):
    context = {'active_class':'EMessage'}
    return render(request, 'EDashApp/EMessage.html' , context)

def EPost_new_job(request):
    context = {'active_class':'EPost_new_job'}
    return render(request, 'EDashApp/EPost_new_job.html' , context)

def EResume(request):
    context = {'active_class':'EResume'}
    return render(request, 'EDashApp/EResume.html' , context)

def EyEdit_profile(request):
    context = {'active_class':'EyEdit_profile'}
    return render(request, 'EDashApp/EyEdit_profile.html' , context)

def EyResetPassword(request):
    context = {'active_class':'EyResetPassword'}
    return render(request, 'EDashApp/EyResetPassword.html' , context)
    