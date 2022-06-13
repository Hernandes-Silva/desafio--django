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
    user__first_name = serializers.CharField(max_length=250)
    class Meta:
        model = Quiz
        fields = ('user','user__first_name', 'score_t')
