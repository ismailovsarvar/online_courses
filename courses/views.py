from django.shortcuts import render, redirect

from courses.models import Category, PopularCourse, CourseSignUp

# Create your views here.

"""COURSE VIEWS"""


def course(request):
    categories = Category.objects.all()
    popular_courses = PopularCourse.objects.all()

    context = {
        'categories': categories,
        'popular_courses': popular_courses
    }

    return render(request, 'courses/course.html', context)


def course_sign_up(request):
    if request.method == 'POST':
        form = CourseSignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseSignUp()

    return render(request, 'app/index.html', {'form': form})


def web_design(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/web-design.html', context)


def development(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/development.html', context)


def game_design(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/game-design.html', context)


def apps_design(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/app-design.html', context)


def marketing(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/marketing.html', context)


def research(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/research.html', context)


def content(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/content.html', context)


def seo(request):
    courses = PopularCourse.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses/seo.html', context)
