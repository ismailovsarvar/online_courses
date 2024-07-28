from django.db import models
from django.utils.text import slugify

# Create your models here.

"""ABOUT MODEL"""


class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


"""COURSES MODEL"""


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
    url_name = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('web_design', 'Web Design'),
        ('development', 'Development'),
        ('seo', 'SEO'),
        ('game_design', 'Game Design'),
    ])
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers', null=True, blank=True)

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


"""CONTACT MODEL"""


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
