from quiz.models import Quiz
from django.db.models import Sum

def get_ranking_global():
    soma_score = Sum('score')
    ranking_global = Quiz.objects.all().values('user')\
                        .annotate(score_t=soma_score).order_by('-score_t')
    
    return ranking_global

def get_ranking_category(category):
    soma_score = Sum('score')
    ranking_category = Quiz.objects.filter(category = category).values('user')\
                        .annotate(score_t=soma_score).order_by('-score_t')
    
    return ranking_category

def get_position_ranking_global(user):
    soma_score = Sum('score')
    ranking_global = Quiz.objects.all().values('user')\
                        .annotate(score_t=soma_score).order_by('-score_t')

    ranking_user = list(ranking_global.values_list('user', flat=True)).index(user.id)+1
    
    return ranking_user
    