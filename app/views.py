from django.shortcuts import render
from django.views import View

from courses.models import Category, PopularCourse
from teachers.models import Teacher

# Create your views here.

"""INDEX VIEWS"""


class IndexView(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        popular_courses = PopularCourse.objects.all()
        teachers = Teacher.objects.all()

        context = {
            'categories': categories,
            'popular_courses': popular_courses,
            'teachers': teachers,
        }
        return render(request, self.template_name, context)


"""ABOUT VIEWS"""


class AboutView(View):
    template_name = 'app/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


"""LOGIN VIEWS"""


class LoginView(View):
    template_name = 'auth/auth.html'

    def get(self, request):
        return render(request, self.template_name)
