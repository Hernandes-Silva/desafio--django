from django.db.models.query import QuerySet
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from quiz.models import Category, Question, Quiz
from quiz.serializers import CategorySerializer, QuestionSerializer, QuizSerializer
# Create your views here.

class ListCreateAPICategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListCreateAPIQuestion(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class= QuestionSerializer

class CreateAPIQuiz(generics.CreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
