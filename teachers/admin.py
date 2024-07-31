from django.contrib import admin

from teachers.models import Teacher


# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'category', 'image')
