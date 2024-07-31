from django.urls import path
from .views import login_view, register, logout_page

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_page, name='logout'),
]
