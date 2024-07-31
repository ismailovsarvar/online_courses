from django.db import models
from social_core.utils import slugify

import courses.models


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    education = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return self.full_name


class BlogList(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs/')
    course = models.ForeignKey(courses.models.Category, on_delete=models.CASCADE, blank=True, related_name='blogs')
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(BlogList, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    comment_body = models.TextField()
    is_possible = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comments/')
    blog_list = models.ForeignKey(BlogList, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name
