from django.shortcuts import render

# Create your views here.

"""BLOG VIEWS"""


def blog_list(request):
    return render(request, 'blog/blog.html')


def blog_detail(request):
    return render(request, 'blog/single.html')