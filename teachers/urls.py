from django.urls import path

from teachers.views import teacher

urlpatterns = [
    path('teacher/', teacher, name='teachers'),
]
