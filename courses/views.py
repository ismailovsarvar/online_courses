from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView

from contacts.forms import CourseSignUpForm
from courses.models import Category, PopularCourse

# Create your views here.

"""COURSE VIEWS"""


class CourseView(View):
    template_name = 'courses/course.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        popular_courses = PopularCourse.objects.all()

        context = {
            'categories': categories,
            'popular_courses': popular_courses
        }

        return render(request, 'courses/course.html', context)


# def course_sign_up(request):
#     if request.method == 'POST':
#         form = CourseSignUp(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CourseSignUp()
#
#     return render(request, 'app/login.html', {'form': form})


class CourseSignUpView(FormView):
    template_name = 'app/index.html'
    form_class = CourseSignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WebDesignView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, 'courses/web-design.html', context)


class DevelopmentView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/development.html', context)


class GameDesignView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/game-design.html', context)


class AppsDesignView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/app-design.html', context)


class MarketingView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/marketing.html', context)


class ResearchView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/research.html', context)


class ContentView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/content.html', context)


class SeoView(View):
    def get(self, request, *args, **kwargs):
        courses = PopularCourse.objects.all()

        context = {
            'courses': courses,
        }
        return render(request, 'courses/seo.html', context)
