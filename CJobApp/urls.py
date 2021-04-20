from django.urls import path
from . import views


urlpatterns = [    
    path('jobs_list/', views.jobs_list ,name='jobs_list'),
    path('job_detail/', views.job_detail ,name='job_detail'),
    path('job_listing/', views.job_listing ,name='job_listing'),
    path('job_category/', views.job_category ,name='job_category'), 
]