from django.urls import path
from . import views


urlpatterns = [    
    path('blog/', views.blog ,name='blog'),
    path('news/', views.blog_news ,name='blog_news'),
    path('reels/', views.blog_reels ,name='blog_reels'),
    path('career/', views.blog_career ,name='blog_career'),
    path('testimonial/', views.blog_testimonial ,name='blog_testimonial'),
    path('blog_demo_page/', views.blog_demo_page ,name='blog_demo_page'),

]