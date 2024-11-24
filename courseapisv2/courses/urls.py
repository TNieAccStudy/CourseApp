from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from courses.views import CategoryViewSet, CourseViewSet, LessonViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.get_urls()))
]