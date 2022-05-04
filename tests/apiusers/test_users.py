import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def payload():
    return  {'username': 'test', 'first_name':"testando", 'last_name':'fff',
                'email': 'test@gmail.com', 'password':'segura12'}

@pytest.mark.django_db
def test_post_create_admin_forbidden(Authclient, client, payload):
    response = Authclient.post(reverse('admin-create'), payload)

    assert response.status_code == 403

    # without auth
    response_without = client.post(reverse('admin-create'), payload)

    assert response_without.status_code == 403



@pytest.mark.django_db
def test_post_create_admin(AuthAdmin, payload):
    response = AuthAdmin.post(reverse('admin-create'), payload)
    
    assert response.status_code == 201

    assert response.json()['first_name'] == payload['first_name']

@pytest.mark.django_db
def test_post_create_user(client, payload):
    response = client.post(reverse('user-create'), payload)

    assert response.status_code == 201

    assert response.json()['first_name'] == payload['first_name']


