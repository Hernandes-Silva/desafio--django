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

@api_view(['GET', ])
def generate_quiz(request, pk):

    questions = list(Question.objects.filter(categories = pk))
    questions = random.sample(questions, 2)
    serializer = QuestionSerializer(questions, many=True)
    
    return Response(serializer.data)
    
