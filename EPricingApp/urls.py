from django.urls import path
from . import views


urlpatterns = [    
    path('EPricing/', views.EPricing ,name='EPricing'),

]