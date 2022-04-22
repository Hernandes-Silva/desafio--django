from django.urls import path
from quiz.views import ListCreateAPICategory, ListCreateAPIQuestion, generate_quiz
from rest_framework import routers
from django.urls.conf import include

router = routers.DefaultRouter()
router.register(r'category', ListCreateAPICategory)
router.register(r'question', ListCreateAPIQuestion)


urlpatterns = [
    path('', include(router.urls)),
    path('generate-quiz/<int:pk>/', generate_quiz, name='generate-quiz'),
]
