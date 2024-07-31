from django.urls import path

from app.views import (
    IndexView,
    AboutView,
    LoginView
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('authentication/', LoginView.as_view(), name='login'),
]
