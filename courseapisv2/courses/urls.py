from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from courses.views import CategoryViewSet,CourseViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('',include(router.get_urls()))
]