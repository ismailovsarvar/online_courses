from django.urls import path
from app.views import (index, about, course_list, teacher, blog_list, blog_detail, contact)


urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('course/', course_list, name='courses'),
    path('teacher/', teacher, name='teachers'),
    path('blog-list/', blog_list, name='blog_list'),
    path('blog-detail/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
]