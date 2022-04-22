from unicodedata import category
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Question(models.Model):
    categories = models.ManyToManyField(Category, related_name='questions')
    choice_answer = (('a','A'), ('b', 'B'), ('c', 'C'))
    title = models.CharField(max_length=250)
    text = models.TextField()
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    answer = models.CharField(max_length=1, choices=choice_answer)

class Quiz(models.Model):
    user = models.ForeignKey(User, related_name='quizzes', on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name='quizzes')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

