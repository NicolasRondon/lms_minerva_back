from  django.urls import include, path
from  rest_framework import routers
from learn.views import LessonViewSet, ChapterViewSet, CourseViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]