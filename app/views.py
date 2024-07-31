from django.shortcuts import render

from courses.models import Category, PopularCourse
from teachers.models import Teacher

# Create your views here.

"""INDEX VIEWS"""


def index(request):
    categories = Category.objects.all()
    popular_courses = PopularCourse.objects.all()
    teachers = Teacher.objects.all()

    context = {
        'categories': categories,
        'popular_courses': popular_courses,
        'teachers': teachers,
    }
    return render(request, 'app/index.html', context)


"""ABOUT VIEWS"""


def about(request):
    return render(request, 'app/about.html')









