from django.shortcuts import render, get_object_or_404
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


class CourseDetailView(View):
    template_name = 'courses/web-design.html'

    def get(self, request, slug, *args, **kwargs):
        course = get_object_or_404(PopularCourse, slug=slug)
        videos = course.videos.all()

        context = {
            'course': course,
            'videos': videos
        }

        return render(request, self.template_name, context)


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
