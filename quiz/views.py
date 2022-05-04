
from django.shortcuts import render
from desafio.permissions import IsAdminOrReadOnly, IsAdminOrReadOnlyViewSet
from quiz.utlis import get_position_ranking_global, get_ranking_category, get_ranking_global
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import random
from django.http import JsonResponse
from quiz.models import Category, Question, Quiz, QuizQuestion
from quiz.serializers import CategorySerializer, QuestionSerializer, QuizSerializer, RankingSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class APICategory(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyViewSet]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class APIQuestion(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyViewSet]
    queryset = Question.objects.all()
    serializer_class= QuestionSerializer
    
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def generate_quiz(request, pk):
    questions = list(Question.objects.filter(categories = pk))
    if len(questions) >=10:
        questions = random.sample(questions, 10)
    serializer = QuestionSerializer(questions, many=True)
    
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['POST',])
def finish_quiz(request):
    questions = request.data.get('questions')
    category = request.data.get('category')
    score = 0
    
    quiz_questions = []

    if len(questions) <= 10:
        for question in questions:
            query_question =  Question.objects.get(id=question['question_id'], categories = category)
            
            quiz_question = QuizQuestion.objects\
                                        .create(
                                            question=query_question,
                                            user_answer=question['user_answer']
                                        )
            quiz_questions.append(quiz_question)

            correct = query_question.answer == question['user_answer']

            if correct: score += 1
        user = request.user
        quiz = Quiz.objects.create(
                                    user = user,
                                    score= score,
                                    category= Category.objects.get(id=category)
                                )

        quiz.questions.set(quiz_questions)
        quiz.save()

        ranking = get_position_ranking_global(user)
        resp = {'score': score,'ranking': ranking }

        return JsonResponse(resp)

@permission_classes([IsAuthenticated])
@api_view(['get'])
def ranking_global(request):
    ranking = get_ranking_global()
    serializer = RankingSerializer(ranking, many=True)

    return Response(serializer.data)
    
@permission_classes([IsAuthenticated])
@api_view(['get'])
def ranking_category(request, pk):
    ranking = get_ranking_category(pk)
    serializer = RankingSerializer(ranking, many=True)

    return Response(serializer.data)

    





    
