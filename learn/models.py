from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True)
    course = models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True)
    video = models.FileField()
    lesson= models.ForeignKey(Lesson, related_name='lesson', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



