from django.db import models
from django.utils.text import slugify

from courses.models import Category

# Create your models here.

"""TEACHER MODEL"""


class Teacher(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'Junior',
        MIDDLE = 'Middle',
        SENIOR = 'Senior'

    full_name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    level = models.CharField(choices=LevelChoices.choices, default=LevelChoices.MIDDLE.value)
    image = models.ImageField(upload_to='teachers/')
    slug = models.SlugField(unique=True, blank=True)
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
