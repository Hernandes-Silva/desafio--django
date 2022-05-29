<h1 align="center">Quiz django</h1>
<h3 align="center">teste de habilidades: Python, Django, Django REST Framework, Pytest e Docker</h3>

<p >Esse quiz foi feito com a intenção de testar as minhas habilidades. Ao navegar pela internet achei um desafio em django
bem interessante que aborda bem as habilidades necessarias para  desenvolver uma API em django.
No final do readme irei deixar a descrição do desafio que encontrei.
</p>

<p align="center">
 <a href="#postman">Postman</a> •
 <a href="#features">Features</a> •
 <a href="#pré-requisitos">Pré Requisitos</a> •
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#autor">Autor</a> •
 <a href="#descrição-do-desafio">Descrição do desafio</a>
</p>

## Postman
#### link de uma collection que está no postman com todas as urls da [API](https://documenter.getpostman.com/view/20832166/UyxdKp8P)

<p align="center">
 <img src="https://github.com/Hernandes-Silva/desafio--django/blob/master/github/postman.png" height='70%' width='70%'>
 
</p>

## Features

- Os Admins:
   - [x] Criar outro admin
   - [x] Criar uma categoria
   - [X] Editar uma categoria
   - [x] Deletar uma categoria
   - [x] Criar uma questão
   - [X] Editar uma questão
   - [x] Deletar uma questão
- Os Users:
   - [x] Gerar um quiz
   - [x] Finalizar um quiz
   - [X] Verificar o ranking global
   - [x] Verificar o ranking por categoria
- Não Users:
  - [x] Criar um usuário
 

### Pré-requisitos

Para executar esse projeto é necessario ter instalado na sua maquina o [git](https://git-scm.com/) e o [docker](https://www.docker.com/get-started/) em conjunto com docker-compose.

### Executando a aplicação

```bash

# clone o projeto
$ git clone https://github.com/Hernandes-Silva/desafio--django

#acesse a pasta do projeto com o terminal/cmd
$ cd desafio--django

# e dê o comando:
$ docker-compose up -d

# agora basta esperar o sistema inicializar.
# e entrar no http://127.0.0.1:8000/admin/
# acessar com o login:admin e senha:admin
# para criar um admin_quiz que pode criar categorias e questões
# va em users depois admin e adicione ele ao grupo admin_quiz.

# Agora você tem um admin_quiz que pode criar categorias, questões
# e outros admin para também administrar o sistema.
# Todas as urls necessarias para fazer essas funções estão na
# na collection que está no postman

```
### Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django rest framework](https://www.django-rest-framework.org/)
- [Pytest-django](https://pytest-django.readthedocs.io/en/latest/)
- [Djangorestframework simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
- [GitHub](https://github.com/) 
- [Docker](https://www.docker.com/get-started/) 


### Autor
* [**Hernandes Matheus**](https://github.com/Hernandes-Silva)

## Descrição do desafio
Nesse desafio iremos avaliar suas habilidades em:

Python<br>
Django<br>
Django REST Framework<br>
Pytest<br>
Docker<br>
Você irá desenvolver a API de uma aplicação para a criação de um quiz de perguntas e respostas!<br>

A aplicação deverá prover o registro e autenticação de dois tipos de usuários:<br>

Admin<br>
Player<br>
Cada quiz é composto por:<br>

10 perguntas com 3 respostas onde apenas 1 é correta.<br>
Cada resposta correta acumula a 1 ponto.<br>
Cada resposta errada perde 1 ponto.<br>
A menor pontuação possível é 0.<br>
Possui uma categoria.<br>
Ao iniciar o jogo:<br>

O player deve escolher uma categoria válida e receber um quiz com perguntas aleatórias referentes a categoria escolhida.<br>

Ao finalizar o jogo:<br>

O player deve receber a contabilização dos seus pontos juntamente com a sua posição atual no ranking global. Não há limitação de quantos quizzes o player pode responder.<br>

O ranking global:<br>

É a contabilização dos pontos acumulados por cada player.<br>

Ranking geral considera todas as categorias.<br>
Ranking por categoria agrupa por categorias.<br>

Permissões:<br>

Todos os endpoints devem estar protegidos por autenticação.<br>

Usuários do tipo Admin tem permissão para criar perguntas e respostas para os quizzes.<br>
Usuários do tipo Player tem permissão para jogar e consultar o ranking.<br>

Requisitos<br>
O projeto precisa estar configurado para rodar em um ambiente macOS ou Ubuntu (preferencialmente como container Docker).<br>

Deve anexar ao seu projeto uma coleção do postman com todos os endpoints criados e exemplos de utilização.<br>
Para executar seu código devemos executar apenas os seguintes comandos:<br>

git clone $seu-fork<br>
cd $seu-fork<br>
comando para instalar dependências<br>
comando para executar a aplicação<br>
Critério de avaliação<br>
Organização do código: Separação de módulos, view e model<br>
Clareza: O README explica de forma resumida qual é o problema e como pode rodar a aplicação?<br>
Assertividade: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?<br>
Legibilidade do código (incluindo comentários)<br>
Segurança: Existe alguma vulnerabilidade clara?<br>
Cobertura de testes (Não esperamos cobertura completa mas é importante garantir o fluxo principal)<br>
Histórico de commits (estrutura e qualidade)<br>
UX: A API é intuitiva?<br>
Escolhas técnicas: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?<br>
## License

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](https://opensource.org/licenses/MIT) para detalhes.
