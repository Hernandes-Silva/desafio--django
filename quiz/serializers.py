from pyexpat import model
from rest_framework import serializers
from .models import Category, Question, Quiz

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        exclude = ('user',)

class RankingSerializer(serializers.ModelSerializer):
    score_t = serializers.IntegerField()
    user = serializers.IntegerField()
    class Meta:
        model = Quiz
        fields = ('user', 'score_t')
