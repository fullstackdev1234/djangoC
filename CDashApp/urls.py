from django.urls import path
from . import views

app_name='dashboard'
urlpatterns = [    
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('edit_profile/', views.edit_profile ,name='edit_profile'),
    path('applied_job/', views.applied_job ,name='applied_job'),
    path('favourite_job/', views.favourite_job ,name='favourite_job'),
    path('message/', views.message ,name='message'),
    path('resume/', views.resume ,name='resume'),
    path('resetPassword/', views.resetPassword ,name='resetPassword'),
    # path('job_single/', views.job_single ,name='job_single'),
]