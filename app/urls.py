from django.urls import path

from app.views import (
    index,
    about,
)

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about')
]
