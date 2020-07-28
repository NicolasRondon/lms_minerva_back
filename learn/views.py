from django.shortcuts import render
from rest_framework import  viewsets
from .serializers import ChapterSerializer, CourseSerializer, LessonSerializer
from  .models import Course, Chapter, Lesson

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer



