from django.urls import path

from courses.views import (
    course,
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
    path('course/', course, name='courses'),
    # Courses link:
    path('web-design/', web_design, name='web_design'),
    path('development/', development, name='development'),
    path('game-design/', game_design, name='game_design'),
    path('app-design/', apps_design, name='apps_design'),
    path('marketing/', marketing, name='marketing'),
    path('research/', research, name='research'),
    path('content/', content, name='content'),
    path('seo/', seo, name='seo'),
]
