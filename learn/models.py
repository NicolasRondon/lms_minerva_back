from django.db import models

# Create your models here.
class Chapter(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True)
    video = models.FileField()

    def __str__(self):
        return self.title



class Lesson(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True)
    chapters = models.ForeignKey(Chapter, related_name='chapters', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True)
    lessons = models.ForeignKey(Lesson, related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return self.title