from django.urls import path
from . import views


urlpatterns = [    
    path('employer_category/', views.employer_category ,name='employer_category'),
    path('employer_list/', views.employer_list ,name='employer_list'),
    path('employer_detail/', views.employer_detail ,name='employer_detail'),
    path('Eindex/', views.Eindex ,name='Eindex'),

]