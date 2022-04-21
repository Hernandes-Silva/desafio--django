from django.urls import path
from quiz.views import ListCreateAPICategory, ListCreateAPIQuestion

urlpatterns = [
    path('category', ListCreateAPICategory.as_view(), name='category'),
    path('question', ListCreateAPIQuestion.as_view(), name='question'),
]
