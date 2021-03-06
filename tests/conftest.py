import pytest
from quiz.models import Category, Question
from rest_framework.test import APIClient
from random import randint
from django.contrib.auth.models import User, Group
from django.core.management import call_command

# loaddata initial.json
@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'initial.json')

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def Authclient(client, user):
    response2 = client.post('/api/token/', {'username':'john', 'password': 'glass onion'})
    token  = response2.json()['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
  
@pytest.fixture  
def AuthAdmin(client, admin):
    response2 = client.post('/api/token/', {'username':'john', 'password': 'glass onion'})
    
    token  = response2.json()['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    return client

@pytest.fixture
def user():
    user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')

    my_group = Group.objects.get(name='user_quiz') 
    my_group.user_set.add(user)

    return user


@pytest.fixture
def admin():
    user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')

    my_group = Group.objects.get(name='admin_quiz') 
    my_group.user_set.add(user)           

    return user

@pytest.fixture
def category_f(db):
    return Category.objects.create(name="Category")



@pytest.fixture
def factory_questions():
    category = Category.objects.create(name="Category")
    answers = ['a', 'b', 'c']
    for x in range(20):
        rand = randint(0,2)
        question = Question.objects.create(title=f"Title {x}",
                                       text=f"question {x}",
                                       a=f"op????o a {x}",
                                       b=f"op????o b {x}",
                                       c=f"op????o C {x}",
                                       answer=answers[rand]
                                       )

        question.categories.add(category)
        question.save()
    
    return category

@pytest.fixture
def factory_questions2():
    category = Category.objects.create(name="Category")
    answers = ['a', 'b', 'c']
    for x in range(20):
        rand = randint(0,2)
        question = Question.objects.create(title=f"Title {x}",
                                       text=f"question {x}",
                                       a=f"op????o a {x}",
                                       b=f"op????o b {x}",
                                       c=f"op????o C {x}",
                                       answer=answers[rand]
                                       )

        question.categories.add(category)
        question.save()
    
    return category