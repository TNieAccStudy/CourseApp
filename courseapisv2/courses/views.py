from django.shortcuts import render
from rest_framework import viewsets
from courses.models import Category,Course
from courses.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet,viewsets.generics.ListAPIView):
    queryset = Category.objects.filter(active=True).all()
    serializer_class = CategorySerializer
