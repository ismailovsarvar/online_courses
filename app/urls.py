from django.urls import path

from app.views import (
    IndexView,
    AboutView
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about')
]
