from random import randint
from django.urls import reverse
import pytest

from django.contrib.auth.models import User
from quiz.utlis import get_position_ranking_global
from tests.quiz.utils import fake_quiz

@pytest.mark.django_db
def test_post_finish_quiz(Authclient, factory_questions, user):
    responseQ = Authclient.get(reverse('generate-quiz', kwargs={'pk':factory_questions.id}))
    
    answers_questions = []
    answers = ['a', 'b', 'c']
    score = 0
    
    for question in responseQ.data:
        rand = randint(0,2)
        
        answer_user = {'question_id':question['id'], 'user_answer':answers[rand]}

        if answer_user['user_answer'] == question['answer']: score +=1

        answers_questions.append(answer_user)
    
    payload = {'category': factory_questions.id, 'questions':answers_questions, 'user':user.id}
    response = Authclient.post(reverse('finish-quiz'), payload, format='json')

    assert response.status_code == 200
    assert response.json()['score'] == score

@pytest.mark.django_db
def test_get_position_ranking_geral(Authclient, factory_questions,factory_questions2, user):
    # generate quiz for test ranking
    fake_quiz(Authclient, factory_questions, user, 5)
    fake_quiz(Authclient, factory_questions2, user, 6)

    user2 = User.objects.create_user(username='herna',
                                 email='test@beatles.com',
                                 password='glass onion')

    fake_quiz(Authclient, factory_questions, user2, 4)
    fake_quiz(Authclient, factory_questions2, user2, 10)
    

    assert  get_position_ranking_global(user) == 2
                            

    
    



    