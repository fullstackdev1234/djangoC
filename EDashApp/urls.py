from django.urls import path
from . import views


urlpatterns = [    
    path('Edashboard/', views.Edashboard ,name='Edashboard'),
    path('EApplications/', views.EApplications ,name='EApplications'),
    path('ECompany_page/', views.ECompany_page ,name='ECompany_page'),
    path('EEdit_profile/', views.EEdit_profile ,name='EEdit_profile'),
    path('EManage_jobs/', views.EManage_jobs ,name='EManage_jobs'),
    path('EMessage/', views.EMessage ,name='EMessage'),
    path('EPost_new_job/', views.EPost_new_job ,name='EPost_new_job'),
    path('EResume/', views.EResume ,name='EResume'),
    path('EyEdit_profile/', views.EyEdit_profile ,name='EyEdit_profile'),
    path('EyResetPassword/', views.EyResetPassword ,name='EyResetPassword'),

]