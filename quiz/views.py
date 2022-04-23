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

@api_view(['GET',])
def generate_quiz(request, pk):
    questions = list(Question.objects.filter(categories = pk))
    if len(questions) >=10:
        questions = random.sample(questions, 10)
    serializer = QuestionSerializer(questions, many=True)
    
    return Response(serializer.data)

""" @api_view(['POST',])
def finish_quiz(request):
    questions = request.data.getlist('questions')
    category = request.data.get('category')
    score = 0
    if len(questions) <=10:
        for question in questions:
            correct = Question.objects.get(question['question_id']).answer == question['answer']
            if correct """




    
