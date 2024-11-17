from django.shortcuts import render
from rest_framework import viewsets, response
from courses.models import Category, Course
from rest_framework.decorators import action
from courses.serializers import CategorySerializer, CourseSerializer, LessonSerializer


class CategoryViewSet(viewsets.ViewSet, viewsets.generics.ListAPIView):
    queryset = Category.objects.filter(active=True).all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet, viewsets.generics.ListAPIView, viewsets.generics.RetrieveAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

    @action(methods=['get'], detail=True, url_path='lesson')
    def get_lesson(self, request, pk):
        data = self.get_object().lesson_set.all()
        return response.Response(LessonSerializer(data).data)

    class Meta:
        paginate_class = 1
