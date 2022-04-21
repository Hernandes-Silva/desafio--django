from django.urls import path
from quiz.views import ListCreateAPICategory

urlpatterns = [
    path('category', ListCreateAPICategory.as_view(), 'category')
]
