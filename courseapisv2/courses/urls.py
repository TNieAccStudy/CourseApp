from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from courses.views import CategoryViewSet

router = routers.DefaultRouter()
router.register('categories',CategoryViewSet)

urlpatterns = [
    path('',include(router.get_urls()))
]