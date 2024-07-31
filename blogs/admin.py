from django.contrib import admin

from blogs.models import BlogList, Comment


# Register your models here.

@admin.register(BlogList)
class BlogListAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    search_fields = ('name',)

