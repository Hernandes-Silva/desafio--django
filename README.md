<h1 align="center">Quiz django</h1>
<h3 align="center">teste de habildiades: Python, Django, Django REST Framework, Pytest e Docker</h3>

<p >Esse quiz foi feito com a intenção de testar as minhas habilidades. Ao navegar pela internet achei um desafio em django
bem interessante que aborda bem as habilidades necessarias para  desenvolver uma API em django.
No final do readme irei deixar a descrição do desafio que encontrei.
</p>

<p align="center">
 <a href="#pré-requisitos">Pré Requisitos</a> •
 <a href="#-features">Features</a> •
 <a href="#rodando-o-mobile">Rodando a aplicação</a> •
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#autor">Autor</a>
</p>

## 📩 Postman
#### link de uma collection que está no postman com todas as urls da [API](https://documenter.getpostman.com/view/20832166/UyxdKp8P)

<p align="center">
 <img src="https://github.com/Hernandes-Silva/desafio--django/blob/master/github/postman.png" height='70%' width='70%'>
 
</p>

## ⚙️ Features

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
# va em users depois admin e adicione ele ao grupo admin_quiz
# agora você tem um admin_quiz que pode criar outros admin
# através da url http://127.0.0.1:8000/api/admin-create/

```

