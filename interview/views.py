from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QASerializer, QASerializerOne


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QASerializer
    filter_backends = [OrderingFilter, ]
    ordering_fields = ['importance', ]
    ordering = ['-importance']


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QASerializerOne


class QuestionAnswerList(generics.ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QASerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['category','question']

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('category_id'))


