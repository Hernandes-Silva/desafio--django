from django.urls import reverse

def fake_quiz(client, factory_questions, user, correct):
    # Takes 10 questions and generates a quiz with 'correct' right questions
    
    response2 = client.post('/api/token/', {'username':user.username, 'password': 'glass onion'})
    token  = response2.json()['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    responseQ = client.get(reverse('generate-quiz', kwargs={'pk':factory_questions.id}))
    
    answers_questions = []
    count = 0
    
    for question in responseQ.data:
        answer = 'a'

        if count < correct: answer = question['answer']
        else:
            if question['answer'] == 'a':
                answer = 'b'

        answer_user = {'question_id':question['id'], 'user_answer':answer}
        answers_questions.append(answer_user)

        count += 1

    payload = {'category': factory_questions.id, 'questions':answers_questions, 'user':user.id}
    response = client.post(reverse('finish-quiz'), payload, format='json')

