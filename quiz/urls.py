from posixpath import basename
from django.urls import path
from quiz.views import APICategory, APIQuestion, finish_quiz, generate_quiz, ranking_category, ranking_global
from rest_framework import routers
from django.urls.conf import include

router = routers.DefaultRouter()
router.register(r'category', APICategory, basename='category')
router.register(r'question', APIQuestion, basename='question')


urlpatterns = [
    path('', include(router.urls)),
    path('generate-quiz/<int:pk>/', generate_quiz, name='generate-quiz'),
    path('finish-quiz/', finish_quiz, name='finish-quiz'),
    path('ranking-global/', ranking_global, name='ranking-global'),
    path('ranking-category/<int:pk>/', ranking_category, name='ranking-category'),
]
