from django.urls import path

from blogs.views import (
    BlogListView,
    blog_detail,
)

urlpatterns = [
    path('blog-list/', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/', blog_detail, name='blog_detail')
]
