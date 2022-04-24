from turtle import title
import pytest
from django.urls import reverse

from quiz.models import Category, Question


@pytest.fixture
def question_f(category_f):
    question = Question.objects.create(title="question",
                                       text="question",
                                       a="opção a",
                                       b="opção b",
                                       c="opção C",
                                       answer="a"
                                       )

    question.categories.add(category_f)
    question.save()
   
    return question

@pytest.mark.django_db
def test_post_question(client, category_f):
    payload = {'title': "question c", 'text': "question", 'a': "opção a",
               'b': "opção b", 'c': "opção C", 'answer': "a", 'categories':category_f.id}

    response = client.post(reverse('question-list'), payload)

    question = Question.objects.all().first()

    assert response.status_code == 201
    assert question.title == payload['title']

@pytest.mark.django_db
def test_get_question(client, question_f):
    response = client.get(reverse('question-list'))

    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_question_detail(client, question_f):
    response = client.get(reverse('question-detail', kwargs={'pk': question_f.id}))
    
    assert response.status_code == 200
    assert response.data.get('title') == question_f.title
    assert response.data.get('id') == question_f.id

@pytest.mark.django_db
def test_get_question_detail_err(client, question_f):
    response = client.get(reverse('question-detail', kwargs={'pk':0}))
    
    assert response.status_code == 404

@pytest.mark.django_db
def test_put_question_detail(client, question_f):
    payload = {'title': "change title", 'text': question_f.text, 'a': question_f.a,
               'b': question_f.b, 'c': question_f.b, 'answer': question_f.answer, 
               'categories': question_f.categories.all().values_list('id', flat=True)}
    
    response = client.put(reverse('question-detail', kwargs={'pk':question_f.id}), payload)
    question_f.refresh_from_db()

    assert response.status_code == 200
    assert question_f.title == payload['title']

@pytest.mark.django_db
def test_delete_question_detail(client, question_f):
    response = client.delete(reverse('question-detail', kwargs={'pk':question_f.id}))
    
    assert response.status_code == 204
    assert len(Question.objects.all()) == 0

    with pytest.raises(Question.DoesNotExist):
        question_f.refresh_from_db()



   
