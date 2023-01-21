# PoliBrasTest #
# Sobre o Projeto #
Esse projeto foi desenvolvido a partir do processo seletivo para vaga de Back-End da empresa PoliBras Softwere. Como descrito no edital, o intuito da aplicação é fazer uma API de gerenciamento de um pequeno mercadinho, utilizando o Django, um framework python, com as seguintes funcionalidades: Cadastro de produtos, Lançamento de vendas e Relatório de caixa.

# Estrutura do projeto #
```bash
|--PoliBrasTest/ (MAIN PACKAGE)
|	|-- apps/ (PASTA DE APPS)
|	|	|-- authorizarion/ (APP DJANGO)
|	|	|	|-- apps.py
|	|	|	|-- models.py
|	|	|	|-- urls.py
|	|	|	|-- views.py
|	|	|-- products/ (APP DJANGO)
|	|	|	|-- tests/ (PASTA PARA TESTES)
|	|	|	|	|-- test_categories.py
|	|	|	|	|-- test_products.py
|	|	|	|-- admin.py
|	|	|	|-- apps.py
|	|	|	|-- models.py
|	|	|	|-- serializers.py
|	|	|	|-- urls.py
|	|	|	|-- views.py
|	|	|-- reports/ (APP DJANGO)
|	|	|	|-- tests/ (PASTA PARA TESTES)
|	|	|	|	|-- test_reports.py
|	|	|	|-- admin.py
|	|	|	|-- apps.py
|	|	|	|-- models.py
|	|	|	|-- serializers.py
|	|	|	|-- urls.py
|	|	|	|-- views.py
|	|	|-- sales/ (APP DJANGO)
|	|	|	|-- tests/ (PASTA PARA TESTES)
|	|	|	|	|-- test_sales.py
|	|	|	|-- admin.py
|	|	|	|-- apps.py
|	|	|	|-- models.py
|	|	|	|-- serializers.py
|	|	|	|-- urls.py
|	|	|	|-- views.py
|	|-- project/ (PROJECT DJANGO)	
|	|	|-- asgi.py
|	|	|-- settings.py
|	|	|-- urls.py
|	|	|-- wsgi.py
|-- manage.py
|-- requirements-dev.txt
|-- requirements.txt
|-- .gitignore
|-- Dockerfile
|-- docker-compose.yaml
|-- LICENSE
|-- pytest.ini
|-- README.md

```

# Relacionamento de tabelas do Banco de Dados #

imagem do dbdiagram


# Tecnologias usadas #
### Back End ###
- Python
- Django
- Django Rest Framework
- Docker
- Redis
- Pytest
### Banco de Dados ###
- SQLite

## COMO RODAR O PROJETO ##
```bash
# Clonar o repositorio
git clone https://github.com/Igorcand
# Entrar na pasta
PoliBrasTest
# Criar um ambiente virtual
python -m venv venv
# Ativar o ambiente virtual
 /PoliBrasTest/venv/Script/activate.bat
# Voltar para raiz do projeto
/PoliBrasTest/
# Instalar os pacotes necessários
pip install -r requirements.txt
# Criar o banco de dados
python manage.py migrate
# Criar um super usuário
python manage.py createsuperuser
# Rodar o servidor localmente
python manage.py runserver
ou
docker-compose build
docker-compose up

```
	
# FUNCIONALIDADES #

# API REST # outras
Para a utilização da API REST do mercadinho, foi feito um CRUD para as tabelas do banco de dados mais importantes, e outras apenas rotas de GET e POST.

## Categoria ##
Para lançar as categorias dos produtos do seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/categories/

### Como usar ###

#### Visualizar categorias ####
Para visualizar as categorias cadastradas você deve utilizar o método HTTP GET no End-Point abaixo para visualizar todos os produtos cadastrados
- http://localhost/api/categories/ (MÉTODO HTTP GET) 

(IMAGEM)

Caso deseje visualizar apenas uma categoria específica, você poderá adicionar o ID no final do End-Point.

- http://localhost/api/categories/{ID}/ (MÉTODO HTTP GET)

(IMAGEM)

#### Adicionar categorias ####
Para adicionar categorias você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/categories/ (MÉTODO HTTP POST)

(IMAGEM DO JSON)


#### Deletar categorias ####
Para deletar categorias existentes você deve utilizar o End-Point principal, passando na URL o ID da categoria específica ue deseja deletar
- http://localhost/api/categories/{ID}/ (MÉTODO HTTP DELETE)

OBS: Só é possivel deletar categorias existentes, caso o ID passado não exista você será avisado.

(IMAGEM)

OBS: Só é possivel deletar categorias existentes, caso a categoria passada não esteja em uso por algum produto, caso tenha, você será avisado.

(IMAGEM)

# -------- #

## Produtos ##
Para lançar os produtos no seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/products/

### Como usar ###

#### Visualizar produtos ####
Para visualizar os produtos cadastrados você deve utilizar o método HTTP GET no End-Point acima para visualizar todos os produtos cadastrados
- http://localhost/api/products/ (MÉTODO HTTP GET)

(IMAGEM)

Caso deseje visualizar apenas um produto, você poderá adicionar o ID no final do End-Point.

- http://localhost/api/products/{ID}/ (MÉTODO HTTP GET)

(IMAGEM)

#### Adicionar produtos ####
Para adicionar produtos você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/products/ (MÉTODO HTTP POST)

(IMAGEM DO JSON)

OBS: O cadastramento de produtos só é possivel tendo um categoria já cadastrado no banco de dados, caso não tenha, voce será avisado.

(IMAGEM)

#### Atualizar produtos ####
Para atualizar os produtos existentes você deve utilizar o End-Point principal, passando na URL o ID do produto específico que deseja atualizar, descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/products/{ID}/ (MÉTODO HTTP PUT)

(IMAGEM DO JSON)

OBS: A atualização de produtos só é possivel tendo um produto já cadastrado no banco de dados, caso não tenha, voce será avisado.
(IMAGEM)

#### Deletar produtos ####
Para deletar os produtos existentes você deve utilizar o End-Point principal, passando na URL o ID do produto específico que deseja deletar
- http://localhost/api/products/{ID}/ (MÉTODO HTTP DELETE)

OBS: Para deletar produtos só é possivel tendo um produto já cadastrado no banco de dados, caso não tenha, voce será avisado.
(IMAGEM)

# -------- #

## Vendas ##
Para lançar as vendas  do seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/sales/

### Como usar ###

#### Visualizar vendas ####
Para visualizar as vendas que aconteceram você deve utilizar o método HTTP GET no End-Point acima para visualizar todas as vendas cadastradas.
- http://localhost/api/sales/ (MÉTODO HTTP GET) 

(IMAGEM)

#### Adicionar vendas ####
Para adicionar as vendas você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o lançamento de vendas
- http://localhost/api/sales/ (MÉTODO HTTP POST)

(IMAGEM DO JSON)

OBS: O lançamento de vendas só é possivel tendo um produto já cadastrado no banco de dados, caso não tenha, voce será avisado.

(IMAGEM)

OBS: O lançamento de vendas só é possivel caso o produto tenha estoque suficiente para a sua compra

(IMAGEM)

# -------- #

## Relatórios ##
Para lançar as vendas  do seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/sales/

### Como usar ###

#### Visualizar relatórios ####
Para visualizar todos os relatórios que aconteceram você deve utilizar o método HTTP GET no End-Point acima para visualizar todas as vendas cadastradas.
- http://localhost/api/reports/ (MÉTODO HTTP GET) 

(IMAGEM)

#### Filtrar relatórios ####
Para filtrar os relatórios você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros que você deseja filtrar, como data, pagamento, produto, etc. Na imagem abaixo está um JSON com todos os parâmetros disponíveis.
- http://localhost/api/reports/ (MÉTODO HTTP POST)

(IMAGEM)


# -------- #



# Author

Igor Cândido Rodrigues

https://www.linkedin.com/in/igorc%C3%A2ndido/

