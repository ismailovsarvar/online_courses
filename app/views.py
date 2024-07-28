from django.shortcuts import render

from app.models import Category, Course, PopularCourse, AboutUs

# Create your views here.

"""INDEX VIEWS"""


def index(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    popular_courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'popular_courses': popular_courses
    }
    return render(request, 'index.html', context)


# def about_us(request):
#     a_us = AboutUs.objects.all()
#     context = {
#         'a_us': a_us,
#     }
#     return render(request, 'index.html', context)


"""ABOUT VIEWS"""


def about(request):
    return render(request, 'about.html')


"""COURSES VIEWS"""


def course_list(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    popular_courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'popular_courses': popular_courses
    }

    return render(request, 'course.html', context)


"""TEACHER VIEWS"""


def teacher(request):
    return render(request, 'teacher.html')


"""BLOG VIEWS"""


def blog_list(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'single.html')


"""CONTACT VIEWS"""


def contact(request):
    return render(request, 'contact.html')
