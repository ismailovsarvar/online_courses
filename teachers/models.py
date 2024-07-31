from django.db import models
from django.utils.text import slugify

from courses.models import Category

# Create your models here.

"""TEACHER MODEL"""


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField()
    phone = models.CharField()
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='teachers/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            t_slug = slugify(self.full_name)
            slug = t_slug
            counter = 1
            while Teacher.objects.filter(slug=slug).exists():
                slug = t_slug + str(counter)
                counter += 1
            self.slug = slug
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
