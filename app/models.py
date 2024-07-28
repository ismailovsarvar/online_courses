from django.db import models
from django.utils.text import slugify


# Create your models here.

class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='courses')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PopularCourse(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    title = models.CharField(max_length=100)
    description = models.TextField()
    number_of_students = models.IntegerField(default=0)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='courses/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while PopularCourse.objects.filter(slug=slug).exists():
                slug = base_slug + str(counter)
                counter += 1
            self.slug = slug
        super(PopularCourse, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
