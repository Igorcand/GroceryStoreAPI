# PoliBrasTest #
## Sobre o Projeto ## 
Esse projeto foi desenvolvido a partir do processo seletivo para vaga de Back-End da empresa PoliBras Softwere. Como descrito no edital, o intuito da 
aplicação é fazer uma API de gerenciamento de um pequeno mercadinho, utilizando o Django, um framework python, com as seguintes funcionalidades: Cadastro de produtos, 
Lançamento de vendas e Relatório de caixa.

## Tecnologias usadas ##
##### Back End #####
- Python
- Django
- Django Rest Framework
- Docker
- Redis
- Pytest
##### Banco de Dados #####
- SQLite

## Como este projeto foi desenvolvido ##
Esse projeto apresenta todas as funcionalidades descritas no edital e mais algumas tecnologias sugeridas, como o Docker, Django Rest Framework, Django Admin, 
Redis, Swagger, Postman.
Inicialmente foi feito a API inteiramente com o DRF, validando os Models, Serializers e Views, buscando usar o método de CBV (Class Based View). 
Depois disso, foi feito o cadastro dos Models no Django-Admin e customizando de forma simples as tabelas.
Após a API estar toda 
funcionalmente rodando foi feito os testes utilizando a bibliteca Pytest, sempre validando as Responses, Status code e os erros esperados de cada rota.
Foi adicionado o Redis para serviços de cache. Segurança na rota utilizando o token JWT. Documentação da API utilizando o Swagger 
OBS: Por causa da autenticação JWT nas rotas, ao rodar os testes para simular requisições estava obtendo um erro de não autorizado mesmo tentando passar o token 
no Header da requisição. Então foi optado em retirar a autenticação das rotas principais e criar uma rota chamada '/api/authorization/' que não está sendo utilizada 
nos testes, então a rota autenticada poderá ser testada utilizando o Postman, Insoimina, ou outra plataforma. 
-----------
Probelmas ao usar o Docker:
DOCKER: Adicionado o Docker e o arquivo de docker-compose para a facilitação ao rodar o container.
OBS: Não consegui fazer o docker rodar o banco de dados Postgres, segui tutoriais no youtube e documentação oficial mas sempre obtinha erro de permissão ao conectar no banco.
OBS2: Não consegui fazer o docker conectar ao servidor do Regis, apenas rodando localmente sem utilizar containers
-----

## REQUISITOS ##
### REQUISITOS OBRIGATÓRIO ###
- python 3 instalado na máquina, para a instalação do python segue o link (.....)
### REQUISITOS FACULTATIVOS ###
 - Docker, para a instalação do docker segue o link (.....)
 - Redis, para a instalação do redis segue o link (.....), caso voce utilize Windows, poderá seguir o video (......)

## FUNCIONALIDADES ##
[[[[[[[


FOTOS E DESCRIÇÃO DAS ROTAS, E MOSTRAR AS TECNOLIGIAS FUNCIONANDO


REDIS:

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
sudo service redis-server restart
redis-cli 

RODAR LOCALMENTE 

python -m venv venv
venv/Script/activate.bat
pip install -r requirements

PYTEST:
set DJANGO_SETTINGS_MODULE=project.settings
pytest


]]]]]]]

## COMO RODAR O PROJETO ##

1 Clonar o repositorio (.....)
	- git clone https://github.com/Igorcand
2 Entrar na pasta
	- PoliBrasTest
3 Criar um ambiente virtual
	- python -m venv venv
4 Ativar o ambiente virtual
	- /PoliBrasTest/venv/Script/activate.bat
5 Voltar para raiz do projeto
	- /PoliBrasTest/
6 Instalar os pacotes necessários
	- pip install -r requirements.txt
7 Criar o banco de dados
	- python manage.py migrate
8 Criar um super usuário
	- python manage.py createsuperuser
9 Rodar o servidor localmente
	- python manage.py runserver
	ou
	- docker-compose build
	- docker-compose up
	






