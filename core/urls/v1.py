from  django.urls import include, path
from  rest_framework import routers
from learn.views import LessonViewSet, ChapterViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register(r'cursos', ChapterViewSet)
router.register(r'lecciones', LessonViewSet)
router.register(r'capitulos', CourseViewSet)


urlpatterns = [
    path('', include(router.urls))
]