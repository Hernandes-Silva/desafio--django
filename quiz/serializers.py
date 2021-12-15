from rest_framework import serializers
from .models import Category, Question, Quiz

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
class QuestionSerializer(serializers.ModelSerializer):
    model = Question
    fields = '__all__'
class QuizSerializer(serializers.ModelSerializer):
    model = Quiz
    exclude = ('user',)