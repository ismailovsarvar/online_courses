from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from blogs.forms import CommentModelForm
from blogs.models import BlogList

# Create your views here.

"""BLOG VIEWS"""


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        blog = BlogList.objects.all()
        comments = blog.comments.filter(is_possible=True)
        context = {
            'blog': blog,
            'comments': comments
        }
        return render(request, 'blog/blog.html', context)


def blog_detail(request):
    return render(request, 'blog/single.html')


def add_comment(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('index')

    else:
        form = CommentModelForm

    return render(request, 'blog/single.html', {'form': form})



