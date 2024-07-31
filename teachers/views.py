from django.shortcuts import render

from teachers.models import Teacher

# Create your views here.

"""TEACHER VIEWS"""


def teacher(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
    }
    return render(request, 'teacher/teacher.html', context)
