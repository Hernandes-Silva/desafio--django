from posixpath import basename
from django.urls import path
from quiz.views import APICategory, APIQuestion, generate_quiz
from rest_framework import routers
from django.urls.conf import include

router = routers.DefaultRouter()
router.register(r'category', APICategory, basename='category')
router.register(r'question', APIQuestion, basename='question')


urlpatterns = [
    path('', include(router.urls)),
    path('generate-quiz/<int:pk>/', generate_quiz, name='generate-quiz'),
]
