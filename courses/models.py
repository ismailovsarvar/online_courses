from django.db import models
from django.utils.text import slugify
# Create your models here.

"""COURSE MODEL"""


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='categories/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PopularCourse(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    title = models.CharField(max_length=100)
    time_of_teaching = models.TextField()
    number_of_students = models.IntegerField(default=0)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='courses/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
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


class CourseSignUp(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    select_a_course = models.ForeignKey('PopularCourse', related_name='select_a_course', on_delete=models.CASCADE, null=True,
                                        blank=True)

    def __str__(self):
        return f"{self.full_name} {self.select_a_course}"

    def is_valid(self):
        pass
