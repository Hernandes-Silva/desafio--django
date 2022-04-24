from django.urls import reverse
import pytest
from quiz.models import Category

# Create your tests here.

@pytest.mark.django_db
def test_post_category(client):
    payload = {'name':"Teste"}

    response = client.post(reverse('category-list'), payload)
    category = Category.objects.get(id=response.data.get('id'))

    assert category.name == payload['name']

@pytest.mark.django_db
def test_get_category(client, category_f):
    response = client.get(reverse('category-list'))

    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_category_detail(client, category_f):
    response = client.get(reverse('category-detail',kwargs={'pk':category_f.id}))

    assert response.status_code == 200
    assert response.data.get('name') == category_f.name

@pytest.mark.django_db
def test_get_category_detail_err(client, category_f):
    response = client.get(reverse('category-detail',kwargs={'pk':0}))

    assert response.status_code == 404

@pytest.mark.django_db
def test_put_category_detail(client, category_f):  
    payload = {'name': "Change description"}

    response = client.put(reverse('category-detail',kwargs={'pk':category_f.id}), payload)
    category_f.refresh_from_db()

    assert response.status_code == 200
    assert category_f.name == payload['name']

@pytest.mark.django_db
def test_delete_category_deatil(client, category_f):
    response = client.delete(reverse('category-detail',kwargs={'pk':category_f.id}))
    
    assert response.status_code == 204
    assert len(Category.objects.filter(id=category_f.id)) == 0

    with pytest.raises(Category.DoesNotExist):
        category_f.refresh_from_db()
