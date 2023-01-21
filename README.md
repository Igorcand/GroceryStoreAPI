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

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/database/database.png)


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

# COMO RODAR O PROJETO #
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

# API REST #
Para a utilização da API REST do mercadinho, foi feito um CRUD para as tabelas do banco de dados mais importantes, e outras apenas rotas de GET e POST.

## Categoria ##
Para lançar as categorias dos produtos do seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/categories/


#### ________________________________________________________________________________________________________________________________________________________ ####
#### Visualizar categorias ####
Para visualizar as categorias cadastradas você deve utilizar o método HTTP GET no End-Point abaixo para visualizar todos as categorias cadastradas
- http://localhost/api/categories/ (MÉTODO HTTP GET) 

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/categories/get_all_categories.png)

Caso deseje visualizar apenas uma categoria específica, você poderá adicionar o ID no final do End-Point.

- http://localhost/api/categories/{ID}/ (MÉTODO HTTP GET)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/categories/get-category_by_id.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Adicionar categorias ####
Para adicionar categorias você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/categories/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/categories/post_save_category.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Deletar categorias ####
Para deletar categorias existentes você deve utilizar o End-Point principal, passando na URL o ID da categoria específica ue deseja deletar
- http://localhost/api/categories/{ID}/ (MÉTODO HTTP DELETE)

OBS: Só é possivel deletar categorias existentes, caso o ID passado não exista você será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/categories/delete_category_nonexisting.png)

OBS: Só é possivel deletar categorias existentes, caso a categoria passada não esteja em uso por algum produto, caso tenha, você será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/categories/delete_category_using.png)


#### ________________________________________________________________________________________________________________________________________________________ ####

## Produtos ##
Para lançar os produtos no seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/products/

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Visualizar produtos ####
Para visualizar os produtos cadastrados você deve utilizar o método HTTP GET no End-Point acima para visualizar todos os produtos cadastrados
- http://localhost/api/products/ (MÉTODO HTTP GET)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/get_all_products.png)

Caso deseje visualizar apenas um produto, você poderá adicionar o ID no final do End-Point.

- http://localhost/api/products/{ID}/ (MÉTODO HTTP GET)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/get_product_id.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Adicionar produtos ####
Para adicionar produtos você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/products/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/post_save_product.png)

OBS: O cadastramento de produtos só é possivel tendo um categoria já cadastrado no banco de dados, caso não tenha, voce será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/erro_save_cat_nonexisting.png)

OBS: O cadastramento de produtos só é possivel para um produto novo, caso o produto já exista, voce será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/erro_save_product_already_exist.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Atualizar produtos ####
Para atualizar os produtos existentes você deve utilizar o End-Point principal, passando na URL o ID do produto específico que deseja atualizar, descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/products/{ID}/ (MÉTODO HTTP PUT)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/updating_product.png)

OBS: A atualização de produtos só é possivel tendo um produto já cadastrado no banco de dados, caso não tenha, voce será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/erro_update_noneexiting_product.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Deletar produtos ####
Para deletar os produtos existentes você deve utilizar o End-Point principal, passando na URL o ID do produto específico que deseja deletar
- http://localhost/api/products/{ID}/ (MÉTODO HTTP DELETE)

OBS: Para deletar produtos só é possivel tendo um produto já cadastrado no banco de dados, caso não tenha, voce será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/products/erro_delete_nonexisting_product.png)

#### ________________________________________________________________________________________________________________________________________________________ ####


## Vendas ##
Para lançar as vendas  do seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/sales/

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Visualizar vendas ####
Para visualizar as vendas que aconteceram você deve utilizar o método HTTP GET no End-Point acima para visualizar todas as vendas cadastradas.
- http://localhost/api/sales/ (MÉTODO HTTP GET) 

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/sales/get_sales.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Adicionar vendas ####
Para adicionar as vendas você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o lançamento de vendas
- http://localhost/api/sales/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/sales/save_sales.png)

OBS: O lançamento de vendas só é possivel tendo um produto já cadastrado no banco de dados, caso não tenha, voce será avisado.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/sales/erro_save_sale_nonexisiting_product.png)

OBS: O lançamento de vendas só é possivel caso o produto tenha estoque suficiente para a sua compra

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/sales/error_buy_more_than_stock.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

## Relatórios ##
Para lançar as vendas  do seu mercadinho, voce deve utilizar as rotas com o End-Point:
- /api/sales/

#### ________________________________________________________________________________________________________________________________________________________ ####


#### Visualizar relatórios ####
Para visualizar todos os relatórios que aconteceram você deve utilizar o método HTTP GET no End-Point acima para visualizar todas as vendas cadastradas.
- http://localhost/api/reports/ (MÉTODO HTTP GET) 

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/reports/get_all_reports.png)

#### ________________________________________________________________________________________________________________________________________________________ ####

#### Filtrar relatórios ####
Para filtrar os relatórios você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros que você deseja filtrar, como data, pagamento, produto, etc. 
- http://localhost/api/reports/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/reports/report_filtred.png)

Na imagem abaixo está um JSON com todos os parâmetros disponíveis.

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/api/reports/json_filtring_report.png)

#### ________________________________________________________________________________________________________________________________________________________ ####


# Pytest #

A framework  pytest facilita a escrita de testes pequenos e legíveis e pode ser dimensionada para oferecer suporte a testes funcionais complexos para aplicativos e bibliotecas.

No projeto foi constuido testes para todas as rotas descritas na sessão anterior de sobre como utilizar a API do mercadinho. O intuito dos testes são avaliar as responses e os códigos de status, de chamadas que deveriam funcionar e também as que deveriam falhar.

### COMO RODAR OS TESTES ###
```bash
# Estar na raiz do projeto
/PoliBrasTest/
# Setar as configurações do django
set DJANGO_SETTINGS_MODULE=project.settings
# Rodar os testes
pytest
```

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/pytest/tests.png)

# REDIS #

O Redis é um armazenamento de estrutura de dados de chave-valor de código aberto e na memória. O Redis oferece um conjunto de estruturas versáteis de dados na memória que permite a fácil criação de várias aplicações personalizadas. Os principais casos de uso do Redis incluem cache, gerenciamento de sessões, PUB/SUB e classificações.

No projeto em particular, foi adicionado o mesmo End-Point para a visualização dos produtos utilizando o sistema de cache oferecido pelo Redis. Foi feito a mesma rota pra fins de comparação com o uso do cache e sem, pois com o cache a resposta é mais rápida porém a atualização não é instantânea.

Para utilizar a rota com cache do Redis no projeto, você precisa necessáriamente de ter o servidor do Redis rodando localmente, na porta 6379.

Para a instalação, siga o passo a passo descrito na documentação oficial.

- <a href="https://redis.io/docs/getting-started/installation/install-redis-on-linux/" target="_blank">Linux</a>
- <a href="https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/" target="_blank">MacOS</a>
- <a href="https://redis.io/docs/getting-started/installation/install-redis-on-windows/" target="_blank">Windows</a>

Após a instalação, você deve iniciar o servidor. Você pode seguir os passos abaixo ou na própria documentação:
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install redis-server
- sudo service redis-server restart
- redis-cli 
- <a href="https://redis.io/docs/getting-started/" target="_blank">Getting started</a>


![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/redis/redis_running.png)


O End-Point contruido na aplicação é: 
- https://localhost/api/products_cache/ (MÉTODO HTTP GET)

Para título de curiosidade, você poderá testar a rota adicionando um produto como descrito na sessão acima, e utilizar a rota acima, você verá que o produto recém adicionado não irá aparecer, e se você rodar a rota de visualizar todos os produtos, ele estará lá. Só após 60 segundos que seu produto irá aparecer na rota em que o cache do Redis está funcionando.

# Autenticação JWT #

JWT (JSON Web Token) é um método RCT 7519 padrão da indústria para realizar autenticação entre duas partes por meio de um token assinado que autentica uma requisição web. Esse token é um código em Base64 que armazena objetos JSON com os dados que permitem a autenticação da requisição.

Para fazer essa autenticação por token foi usado a biblioteca djangorestframework-simplejwt na sua versão 5.2.2 e com sua implementação vem duas rotas para isso, a de geração do token e o refresh do token.

Para gerar o token, você precisa necessariamente de ser super usuário, e então você passa o nome de usuário e a senha na rota abaixo:
- https://localhost/token/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/auth/create_token.png)

Para gerar um novo token utilizando o refresh, basta passar o refresh token como parâmetro de entrada na rota abaixo: 
- https://localhost/refresh/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/auth/refresh.png)

Durante o processo de desenvolvimento da aplicação, ocorreu um erro de integração de tecnologias ao usar a autenticação JWT e os testes, pois sempre que a autenticação das rotas estava ativa, os testes não conseguiam testar as rotas por causa de justamente não terem o token para enviar. Com isso, foi criado uma rota simples para mostrar o funcionamento da autenticação.

- https://localhost/api/authorization/ (MÉTODO HTTP GET)

Caso você tente executar essa rota sem enviar o token no Header da requisição, irá apresentar erro:

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/auth/without_auth.png)

Caso você tente executar essa rota sem enviar o token válido, irá apresentar erro:

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/auth/token_not_valid.png)

Caso envie o token dessa maneira:

Header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MzEyMTQwLCJpYXQiOjE2NzQzMTE4NDAsImp0aSI6ImI4NmYyMTVmZGYzNTQzOTRhNmUzMDM1NWZkNTY2ZjhiIiwidXNlcl9pZCI6MX0.T-1bg-5sVZ_4B8VHjdG5MIOYc6WsDxEnLovyPbAXj8g"}

Irá apresentar essa mensagem simples:

![Mobile 1](https://github.com/Igorcand/PoliBrasTest/blob/master/assets/auth/have_authorization.png)

# Author

Igor Cândido Rodrigues

https://www.linkedin.com/in/igorc%C3%A2ndido/

