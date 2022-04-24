import pytest
from quiz.models import Category
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def category_f(db):
    return Category.objects.create(name="Category")