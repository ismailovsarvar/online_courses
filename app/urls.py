from django.urls import path

from app.views import (
    index,
    about,
    course,
    teacher,
    blog_list,
    blog_detail,
    contact,
    web_design,
    development,
    game_design,
    apps_design,
    marketing,
    research,
    content,
    seo,
)

urlpatterns = [
    # Template link:
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('course/', course, name='courses'),
    path('teacher/', teacher, name='teachers'),
    path('blog-list/', blog_list, name='blog_list'),
    path('blog-detail/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
    # Courses link:
    path('course/web-design/', web_design, name='web_design'),
    path('course/development/', development, name='development'),
    path('course/game-design/', game_design, name='game_design'),
    path('course/app-design/', apps_design, name='apps_design'),
    path('course/marketing/', marketing, name='marketing'),
    path('course/research/', research, name='research'),
    path('course/content/', content, name='content'),
    path('course/seo/', seo, name='seo'),
]
