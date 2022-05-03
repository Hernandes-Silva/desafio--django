import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_create_admin_forbidden(Authclient):
    payload = {'username': 'test', 'first_name':"testando", 'last_name':'fff',
                'email': 'test@gmail.com', 'password':'segura12'}

    response = Authclient.post(reverse('admin-create'), payload)
    
    assert response.status_code == 403