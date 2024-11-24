from django.shortcuts import render
from rest_framework import viewsets, response
from courses.models import Category, Course, Lesson, User
from rest_framework.decorators import action
from courses.serializers import CategorySerializer, CourseSerializer, LessonSerializer, LessonDetailSerializer, CommentSerializer,UserSerializer
from courses.paginations import CoursePagination


class CategoryViewSet(viewsets.ViewSet, viewsets.generics.ListAPIView):
    queryset = Category.objects.filter(active=True).all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet, viewsets.generics.ListAPIView, viewsets.generics.RetrieveAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def get_queryset(self):
        query = self.queryset
        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            query = Course.objects.filter(category_id=cate_id)

        return query

    @action(methods=['get'], detail=True, url_path='lesson')
    def get_lesson(self, request, pk):
        data = self.get_object().lesson_set.all()
        return response.Response(LessonSerializer(data).data)


class LessonViewSet(viewsets.ViewSet, viewsets.generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonDetailSerializer

    @action(methods=['get'], detail=True, url_path='comments')
    def get_comments(self, request, pk):
        comments = self.get_object().comment_set.select_related('user').filter(active=True)
        return response.Response(data=CommentSerializer(comments, many=True).data)


class UserViewSet(viewsets.ViewSet, viewsets.generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

