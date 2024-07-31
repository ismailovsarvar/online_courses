from django.contrib import admin

from courses.models import Category, PopularCourse, CourseSignUp


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'category')
#     exclude = ('slug',)


@admin.register(PopularCourse)
class PopularCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'number_of_students', 'price', 'rating')
    exclude = ('slug',)


@admin.register(CourseSignUp)
class CourseSignUpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)
