from django.urls import reverse
import pytest
from quiz.models import Category

# Create your tests here.
@pytest.mark.django_db
def test_category(client, db):
    payload = {'name':"Teste"}

    response = client.post(reverse('category-list'), payload)
    category = Category.objects.get(id=response.data.get('id'))

    assert category.name == payload['name']