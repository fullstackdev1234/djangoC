from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [    
    path('resume_category/', views.resume_category ,name='resume_category'),
    path('resume_listing/', views.resume_listing ,name='resume_listing'),
    path('resume_list/', views.resume_list ,name='resume_list'),
    path('resume_detail/', views.resume_detail ,name='resume_detail'),
]