from django.urls import reverse
import pytest
from quiz.models import Category

# Create your tests here.

@pytest.mark.django_db
def test_post_category(AuthAdmin):
    payload = {'name':"Teste"}

    response = AuthAdmin.post(reverse('category-list'), payload)
    category = Category.objects.get(id=response.data.get('id'))

    assert category.name == payload['name']

@pytest.mark.django_db
def test_get_category(Authclient, category_f):
    response = Authclient.get(reverse('category-list'))

    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_category_detail(Authclient, category_f):
    response = Authclient.get(reverse('category-detail',kwargs={'pk':category_f.id}))

    assert response.status_code == 200
    assert response.data.get('name') == category_f.name

@pytest.mark.django_db
def test_get_category_detail_err(Authclient, category_f):
    response = Authclient.get(reverse('category-detail',kwargs={'pk':0}))

    assert response.status_code == 404

@pytest.mark.django_db
def test_put_category_detail(Authclient, category_f):  
    payload = {'name': "Change description"}

    response = Authclient.put(reverse('category-detail',kwargs={'pk':category_f.id}), payload)
    category_f.refresh_from_db()

    assert response.status_code == 200
    assert category_f.name == payload['name']

@pytest.mark.django_db
def test_delete_category_detail(Authclient, category_f):
    response = Authclient.delete(reverse('category-detail',kwargs={'pk':category_f.id}))
    
    assert response.status_code == 204
    assert len(Category.objects.filter(id=category_f.id)) == 0

    with pytest.raises(Category.DoesNotExist):
        category_f.refresh_from_db()
