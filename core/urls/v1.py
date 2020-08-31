from  django.urls import include, path
from  django.conf.urls import  url
from  rest_framework import routers
from learn.views import LessonViewSet, ChapterViewSet, CourseViewSet
from accounts.views import CreateUserView, ActivateUserView
router = routers.DefaultRouter()
router.register(r'cursos', CourseViewSet)
router.register(r'lecciones', LessonViewSet)
router.register(r'capitulos', ChapterViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path(r'register/', CreateUserView.as_view()),
    path(r'activate/<str:uuid>/',ActivateUserView.as_view())
]