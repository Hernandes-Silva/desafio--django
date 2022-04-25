from random import randint
from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_post_finish_quiz(client, factory_questions, user):
    responseQ = client.get(reverse('generate-quiz', kwargs={'pk':factory_questions.id}))
    
    answers_questions = []
    answers = ['a', 'b', 'c']
    score = 0
    
    for question in responseQ.data:
        rand = randint(0,2)
        
        answer_user = {'question_id':question['id'], 'user_answer':answers[rand]}

        if answer_user['user_answer'] == question['answer']: score +=1

        answers_questions.append(answer_user)
    
    payload = {'category': factory_questions.id, 'questions':answers_questions}
    response = client.post(reverse('finish-quiz'), payload, format='json')

    assert response.status_code == 200
    assert response.json()['score'] == score


    