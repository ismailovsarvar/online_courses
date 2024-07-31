from django.contrib import admin

from courses.models import Category, PopularCourse, CourseSignUp, Video


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)


@admin.register(PopularCourse)
class PopularCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'number_of_students', 'price', 'rating')
    list_filter = ('title', 'number_of_students', 'rating')
    search_fields = ('title', 'price')
    exclude = ('slug',)


@admin.register(CourseSignUp)
class CourseSignUpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)
    search_fields = ('full_name',)


@admin.register(Video)
class VideoAdminModel(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)