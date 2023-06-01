# GroceryStoreAPI #

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Igorcand/GroceryStoreAPI/blob/master/LICENSE) ![version](https://img.shields.io/badge/version-1.2.3-blue) ![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen)

# Sobre o Projeto #
<p> Esse projeto foi desenvolvido com a intenção de praticar as habilidades de Back-End. Como isso, o intuito da aplicação é fazer uma API de gerenciamento de um pequeno mercadinho, utilizando o Django, um framework python, com as seguintes funcionalidades: Cadastro de produtos, Lançamento de vendas e Relatório de caixa. </p>

# Requisitos Obrigatórios #

- Python
- Poetry
- Docker

# Estrutura do projeto #
```bash
|--GroceryStoreAPI/ (APLICAÇÃO PRINCIPAL)
|   |-- src/
|   |	|-- apps/ (PASTA DE APPS)
|   |	|	|-- authorizarion/ (APP DJANGO)
|   |	|	|	|-- apps.py
|   |	|	|	|-- models.py
|   |	|	|	|-- urls.py
|   |	|	|	|-- views.py
|   |	|	|-- products/ (APP DJANGO)
|   |	|	|	|-- tests/ (PASTA PARA TESTES)
|   |	|	|	|	|-- test_categories.py
|   |	|	|	|	|-- test_products.py
|   |	|	|	|-- admin.py
|   |	|	|	|-- apps.py
|   |	|	|	|-- models.py
|   |	|	|	|-- serializers.py
|   |	|	|	|-- urls.py
|   |	|	|	|-- views.py
|   |	|	|-- reports/ (APP DJANGO)
|   |	|	|	|-- tests/ (PASTA PARA TESTES)
|   |	|	|	|	|-- test_reports.py
|   |	|	|	|-- admin.py
|   |	|	|	|-- apps.py
|   |	|	|	|-- models.py
|   |	|	|	|-- serializers.py
|   |	|	|	|-- urls.py
|   |	|	|	|-- views.py
|   |	|	|-- sales/ (APP DJANGO)
|   |	|	|	|-- tests/ (PASTA PARA TESTES)
|   |	|	|	|	|-- test_sales.py
|   |	|	|	|-- admin.py
|   |	|	|	|-- apps.py
|   |	|	|	|-- models.py
|   |	|	|	|-- serializers.py
|   |	|	|	|-- urls.py
|   |	|	|	|-- views.py
|   |	|-- project/ (PROJECT DJANGO)	
|   |	|	|-- asgi.py
|   |	|	|-- settings.py
|   |	|	|-- urls.py
|   |	|	|-- wsgi.py
|   |   |-- manage.py
|	|-- assets/ (PASTA DE IMAGENS)
|	|	|-- admin/ (IMAGENS DO DJANGO-ADMIN)
|	|	|-- api/ (IMAGENS DO FUNCIONAMENTO DAS ROTAS)
|	|	|-- auth/ (IMAGENS DA AUTENTICAÇÃO)
|	|	|-- celery/ (IMAGENS DO CELERY)
|	|	|-- database/ (IMAGENS DO RELECIONAMENTO DAS TABELAS)
|	|	|-- docker/ (IMAGENS DO DOCKER)
|	|	|-- pytest/ (IMAGENS DOS TESTES EXECUTADOS)
|	|	|-- redis/ (IMAGENS DO REDIS)
|	|	|-- swagger/ (IMAGENS DA DOCUMENTAÇÃO SWAGGER)
|   |-- docs/
|   |   | ...
|-- .dockerignore
|-- .env
|-- .gitignore
|-- docker-compose.yaml
|-- Dockerfile
|-- LICENSE
|-- Makefile
|-- mkdocs.yml
|-- poetry.lock
|-- pyproject.toml
|-- pytest.ini
|-- README.md
|-- requirements.txt

```

# Relacionamento de tabelas do Banco de Dados #

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/database/database.png)

Para criar imagens para um melhor entendimento das tabelas do banco de dados, utilize o site <a href="https://dbdiagram.io/" target="_blank">dbdiagram.io</a>

# Instruções #
## Como rodar o projeto ##
```bash
# Fazer o build da imagem
docker build .

# Executar a imagem
docker-compose up -d --build

# Criar as tabelas do Banco de Dados dentro do container
docker-compose exec api python src/manage.py migrate

# Criar um superusuário
docker-compose exec api python src/manage.py createsuperuser

# Finalizar a imagem, caso necessite
docker-compose down

# Após os passos anteriores, para executar a imagem novamente, utilize apenas o comando abaixo
docker-compose up

```

## Como rodar os testes ##
```bash
# Entrar no ambiente virtual do Poetry
poetry shell

# Entrar no diretorio src/
cd src/

# Rodar os testes
pytest

```

## Como rodar as verificações de boas práticas ##
```bash
# Entrar no ambiente virtual do Poetry
poetry shell

# Caso tenha o Make instalado em sua máquina, poderá rodar o comando
make format
make lint

# Caso contrário
isort .
blue .
prospector --with-tool pep257

```


# API REST #
API é uma sigla do inglês que significa Application Programming Interface que traduzindo seria uma Interface de Programação de Aplicativos.

APIs são mecanismos que permitem que dois componentes de software se comuniquem usando um conjunto de definições e protocolos. Por exemplo, o sistema de software do instituto meteorológico contém dados meteorológicos diários.

Para a utilização da API REST do mercadinho, foi feito um CRUD para as tabelas do banco de dados mais importantes, e outras apenas rotas de GET e POST.

## Categoria ##
Para ver, adicionar e deletar as categorias dos produtos do seu mercadinho, você deve utilizar as rotas com o End-Point:
- /api/categories/



#### Visualizar categorias ####
Para visualizar as categorias cadastradas você deve utilizar o método HTTP GET no End-Point abaixo para visualizar todas as categorias cadastradas
- http://localhost/api/categories/ (MÉTODO HTTP GET) 

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/develop/assets/api/categories/get_all_categories.png)

Caso deseje visualizar apenas uma categoria específica, você poderá adicionar o ID no final do End-Point.

- http://localhost/api/categories/{ID}/ (MÉTODO HTTP GET)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/categories/get-category_by_id.png)


#### Adicionar categorias ####
Para adicionar categorias você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/categories/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/categories/post_save_category.png)


#### Deletar categorias ####
Para deletar categorias existentes você deve utilizar o End-Point principal, passando na URL o ID da categoria específica que deseja deletar
- http://localhost/api/categories/{ID}/ (MÉTODO HTTP DELETE)

OBS: Só é possivel deletar categorias existentes, caso o ID passado não exista você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/categories/delete_category_nonexisting.png)

OBS: Só é possivel deletar que não estão sendo usadas, caso a categoria passada esteja em uso por algum produto, você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/categories/delete_category_using.png)



## Produtos ##
Para ver, adicionar, deletar e atualizar os produtos no seu mercadinho, você deve utilizar as rotas com o End-Point:
- /api/products/


#### Visualizar produtos ####
Para visualizar os produtos cadastrados você deve utilizar o método HTTP GET no End-Point acima para visualizar todos os produtos cadastrados
- http://localhost/api/products/ (MÉTODO HTTP GET)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/get_all_products.png)

Caso deseje visualizar apenas um produto, você poderá adicionar o ID no final do End-Point.

- http://localhost/api/products/{ID}/ (MÉTODO HTTP GET)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/get_product_id.png)


#### Adicionar produtos ####
Para adicionar produtos você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o cadastramento.
- http://localhost/api/products/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/post_save_product.png)

OBS: O cadastramento de produtos só é possivel tendo um categoria já cadastrada no banco de dados, caso não tenha, você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/erro_save_cat_nonexisting.png)

OBS: O cadastramento de produtos só é possivel para um produto novo, caso o produto já exista, você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/erro_save_product_already_exist.png)


#### Atualizar produtos ####
Para atualizar os produtos existentes você deve utilizar o End-Point principal, passando na URL o ID do produto específico que deseja atualizar e passar um JSON com os parametros necessários para a atualização.
- http://localhost/api/products/{ID}/ (MÉTODO HTTP PUT)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/updating_product.png)

OBS: A atualização de produtos só é possivel tendo o produto já cadastrado no banco de dados, caso não tenha, você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/erro_update_noneexiting_product.png)


#### Deletar produtos ####
Para deletar os produtos existentes você deve utilizar o End-Point principal, passando na URL o ID do produto específico que deseja deletar
- http://localhost/api/products/{ID}/ (MÉTODO HTTP DELETE)

OBS: Para deletar produtos só é possivel tendo o produto já cadastrado no banco de dados, caso não tenha, você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/products/erro_delete_nonexisting_product.png)



## Vendas ##
Para adicionar e ver as vendas do seu mercadinho, você deve utilizar as rotas com o End-Point:
- /api/sales/


#### Visualizar vendas ####
Para visualizar as vendas que aconteceram você deve utilizar o método HTTP GET no End-Point acima para visualizar todas as vendas cadastradas.
- http://localhost/api/sales/ (MÉTODO HTTP GET) 

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/sales/get_sales.png)


#### Adicionar vendas ####
Para adicionar as vendas você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros necessários para o lançamento de vendas
- http://localhost/api/sales/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/sales/save_sales.png)

OBS: O lançamento de vendas só é possivel tendo o produto já cadastrado no banco de dados, caso não tenha, você será avisado.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/sales/erro_save_sale_nonexisiting_product.png)

OBS: O lançamento de vendas só é possivel caso o produto tenha estoque suficiente para a sua compra

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/sales/error_buy_more_than_stock.png)


## Relatórios ##
Para ver e filtrar os relatorios do seu mercadinho, você deve utilizar as rotas com o End-Point:
- /api/sales/


#### Visualizar relatórios ####
Para visualizar todos os relatórios que aconteceram você deve utilizar o método HTTP GET no End-Point acima para visualizar todos os relatórios.
- http://localhost/api/reports/ (MÉTODO HTTP GET) 

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/reports/get_all_reports.png)


#### Filtrar relatórios ####
Para filtrar os relatórios você deve utilizar o End-Point principal descrito acima e passar um JSON com os parametros que você deseja filtrar, como data, pagamento, produto, etc. 
- http://localhost/api/reports/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/reports/report_filtred.png)

Na imagem abaixo está um JSON com todos os parâmetros disponíveis.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/api/reports/json_filtring_report.png)



# Admin #

<code>
Uma das partes mais poderosas do Django é a interface de administração automática. Ele lê metadados de seus modelos para fornecer uma interface rápida e centrada no modelo, onde usuários confiáveis ​​podem gerenciar o conteúdo em seu site. O uso recomendado do administrador é limitado à ferramenta de gerenciamento interno de uma organização. Não se destina a construir todo o seu front-end.

O administrador tem muitos ganchos para personalização, mas cuidado ao tentar usar esses ganchos exclusivamente. Se você precisar fornecer uma interface mais centrada no processo que abstraia os detalhes de implementação de tabelas e campos do banco de dados, provavelmente é hora de escrever suas próprias exibições.
</code>

Para acessar a página, basta acessar a URL abaixo e fazer o login com o mesmo usuário e senha do seu super usuário.

- https://localhost/admin/

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/admin_home.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/category_home.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/add_category.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/product_home.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/add_product.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/sale_home.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/add_sale.png)


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/admin/report_home.png)


# Swagger #
O Swagger é um framework composto por diversas ferramentas que, independente da linguagem, auxilia a descrição, consumo e visualização de serviços de uma API REST. 

Foi usado a biblioteca drf-yasg na sua versão 1.21.4 para construir a documentação da API, como mostra abaixo.

Para acessar a documentação, acesse a URL abaixo:

- https://localhost/swagger/

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/swagger/swagger.png)
![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/swagger/routes1.png)
![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/swagger/routes2.png)

Para acessar o redoc, acesse a URL abaixo:

- https://localhost/redoc/

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/swagger/redoc.png)

# Pytest #

A framework  pytest facilita a escrita de testes pequenos e legíveis e pode ser dimensionada para oferecer suporte a testes funcionais complexos para aplicativos e bibliotecas.

No projeto foi constuido testes para todas as rotas descritas na sessão anterior de sobre como utilizar a API do mercadinho. O intuito dos testes são avaliar as responses e os códigos de status, de chamadas que deveriam funcionar e também as que deveriam falhar.


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/pytest/tests.png)

# REDIS #

<p> O Redis é um armazenamento de estrutura de dados de chave-valor de código aberto e na memória. O Redis oferece um conjunto de estruturas versáteis de dados na memória que permite a fácil criação de várias aplicações personalizadas. Os principais casos de uso do Redis incluem cache, gerenciamento de sessões, PUB/SUB e classificações.</p>

<p> No projeto em particular, foi adicionado o mesmo End-Point para a visualização dos produtos utilizando o sistema de cache oferecido pelo Redis. Foi feito a mesma rota pra fins de comparação com o uso do cache e sem, pois com o cache a resposta é mais rápida porém a atualização não é instantânea.</p>

<p> Para utilizar a rota com cache do Redis no projeto, você precisa necessáriamente de ter o servidor do Redis rodando localmente, na porta 6379. </p>

<p> Para a instalação, siga o passo a passo descrito na documentação oficial. </p>

- <a href="https://redis.io/docs/getting-started/installation/install-redis-on-linux/" target="_blank">Linux</a>
- <a href="https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/" target="_blank">MacOS</a>
- <a href="https://redis.io/docs/getting-started/installation/install-redis-on-windows/" target="_blank">Windows</a>

<p> Após a instalação, você deve iniciar o servidor. Você pode seguir os passos abaixo ou na própria documentação: </p>

- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install redis-server
- sudo service redis-server restart
- redis-cli 

- <a href="https://redis.io/docs/getting-started/" target="_blank">Getting started</a>


![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/redis/redis_running.png)


O End-Point contruido na aplicação é: 
- https://localhost/api/products_cache/ (MÉTODO HTTP GET)

<p> Você poderá testar a rota adicionando um produto como descrito na sessão acima, e utilizar a rota acima, você verá que o produto recém adicionado não irá aparecer, e se você rodar a rota de visualizar todos os produtos, ele estará lá. Só após 60 segundos que seu produto irá aparecer na rota em que o cache do Redis está funcionando. </p>


# Celery #
O Celery é um sistema distribuído simples, flexível e confiável para processar grandes quantidades de mensagens, ao mesmo tempo em que fornece às operações as ferramentas necessárias para manter esse sistema.

É uma fila de tarefas com foco no processamento em tempo real, além de oferecer suporte ao agendamento de tarefas.As filas de tarefas são usadas como um mecanismo para distribuir o trabalho entre threads ou máquinas.A entrada de uma fila de tarefas é uma unidade de trabalho denominada tarefa. Processos de trabalho dedicados monitoram constantemente as filas de tarefas para novos trabalhos a serem executados.

O Celery requer um transporte de mensagens para enviar e receber mensagens. Os transportes do broker RabbitMQ e Redis são completos, mas também há suporte para Amazon SQS, Apachhe Zookeeper, entre outros.

No projeto em si, será utilizado o Redis para o sistema de mensageria pois já está feito a instalação como descrito na sessão anterior. Foi adicionado uma simples rota para exemplificar como o sistema de filas e tarefas funcionam em uma aplicação, e para ter uma noção de como escalar para caso a aplicação cresca.

#### Passos ####
1 - Ter o Redis rodando no endereço redis://127.0.0.1:6379 como na sessão anterior.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/redis/redis_running.png)

2 - Ter a API rodando normalmente utilizando o comando "python manage.py runserver"

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/celery/api_running.png)

3 - Abrir outro terminal, acessar a pasta do projeto, ativar o ambiente virtual e executar o comando abaixo:

- celery -A project.celery worker --pool=solo -l info

4 - Abrir o Postman, ou qualquer outra plataforma de API, e fazer a simples chamada no End-Point abaixo:

 - https://localhost/celery/ (MÉTODO HTTP GET)

Esta rota irá apenas retornar uma mensagem "Done" e um código 200. 

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/celery/route.png)

Porém, se você observar no terminal que você rodou o comando do celery, poderá observar que foi executada uma ação que foi justamente mostrar na tela os números de 0 a 9. Isso mostra como o celery funciona, em que ele passa a responsabilidade da execução da operação para outra máquina, desocupando a principal para que ela possa executar  outra coisa, e quando a tarefa executada pelo Celery terminar, ele irá devolver a resposta.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/celery/celery_working.png)

Utilizando a biblioteca django-celery-results nos podemos ver o resultado das tarefas executadas de uma maneira mais clara e legível. Pois com ela, nos podemos acessar o admin do django pela URL abaixo e ver que temos mais duas tabelas acrescentadas.

- https://localhost/admin/ 

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/celery/celery_admin.png)

A se clicarmos em "Task results" podemos ver mais informações sobre a tarefa executada que antes eram omitidas.

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/celery/tasks.png)

Para a implementação do Celery na aplicação foi utilizado o link abaixo como referência para a integração do Django, Celery e o Redis.
- <a href="https://www.youtube.com/watch?v=EfWa6KH8nVI" target="_blank">link para o vídeo</a>

# Autenticação JWT #

<p> JWT (JSON Web Token) é um método RCT 7519 padrão da indústria para realizar autenticação entre duas partes por meio de um token assinado que autentica uma requisição web. Esse token é um código em Base64 que armazena objetos JSON com os dados que permitem a autenticação da requisição.</p>

<p> Para fazer essa autenticação por token foi usado a biblioteca djangorestframework-simplejwt na sua versão 5.2.2 e com sua implementação vem duas rotas para isso, a de geração do token e o refresh do token. </p>

<p> Para gerar o token, você precisa necessariamente de ser super usuário, e então você passa o nome de usuário e a senha na rota abaixo: </p>
- https://localhost/token/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/auth/create_token.png)

Para gerar um novo token utilizando o refresh, basta passar o refresh token como parâmetro de entrada na rota abaixo: 
- https://localhost/refresh/ (MÉTODO HTTP POST)

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/auth/refresh.png)

<p> Durante o processo de desenvolvimento da aplicação, ocorreu um erro de integração de tecnologias ao usar a autenticação JWT e os testes, pois sempre que a autenticação das rotas estava ativa, os testes não conseguiam testar as rotas por causa de justamente não terem o token para enviar. Com isso, foi criado uma rota simples para mostrar o funcionamento da autenticação. </p>

- https://localhost/api/authorization/ (MÉTODO HTTP GET)

Caso você tente executar essa rota sem enviar o token no Header da requisição, irá apresentar erro:

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/auth/without_auth.png)

Caso você tente executar essa rota sem enviar o token válido, irá apresentar erro:

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/auth/token_not_valid.png)

Caso envie o token dessa maneira:

Header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MzEyMTQwLCJpYXQiOjE2NzQzMTE4NDAsImp0aSI6ImI4NmYyMTVmZGYzNTQzOTRhNmUzMDM1NWZkNTY2ZjhiIiwidXNlcl9pZCI6MX0.T-1bg-5sVZ_4B8VHjdG5MIOYc6WsDxEnLovyPbAXj8g"}

Irá apresentar essa mensagem simples:

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/auth/have_authorization.png)


# Docker #

Docker é uma forma de virtualizar aplicações no conceito de “containers”, trazendo da web ou de seu repositório interno uma imagem completa, incluindo todas as dependências necessárias para executar sua aplicação.

A aplicação uma segunda forma de funcionar que é a partir de imagem e containers do Docker, e para isso, você precisa ter o Docker instalado na sua máquina.

<a href="https://docs.docker.com/desktop/install/windows-install/" target="_blank">link para instalar</a>

Para a criação de container e a imagem capaz de rodar a aplicação django, foi feita uma pesquisa na internet para achar o melhor modelo de imagem.

### COMO RODAR PELO DOCKER ###
```bash
# Fazer o build da imagem
docker build .

# Executar a imagem
docker-compose up -d --build

# Criar as tabelas do Banco de Dados dentro do container
docker-compose exec api python src/manage.py migrate

# Criar um superusuário
docker-compose exec api python src/manage.py createsuperuser


# Finalizar a imagem, caso necessite
docker-compose down

# Após os passos anteriores, para executar a imagem novamente, utilize apenas o comando abaixo
docker-compose up

```

#### Imagem criada ####

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/docker/build.png)

#### Rodando a partir do Docker #####

![Mobile 1](https://github.com/Igorcand/GroceryStoreAPI/blob/master/assets/docker/running.png)


#### Observações ####
Durante o desenvolvimento a partir da criação de containers, tive dificuldades em fazer as imagens comunicarem entre si. Apesar de ter conseguido buildar a imagem do Redis pelo docker com sucesso, o container não conseguia conectar na porta que o Redis estava funcionando localmente, então ao acessar a rota "/api/products_cache/" apresentará um erro, que é justamente a rejeição da tentativa de conexão.

Outro ponto em que tive dificuldades foi a conexão da aplicação em Django em se conectar com o banco de dados Postgres, da mesma forma que o Redis, consegui buildar a imagem com sucesso a partir do Docker, porém, a aplicação django não reconhecia as informações de username, password e host do própio banco de dados. Por esse motivo, foi optado em deixar a aplicação rodando com o banco de dados padrão, o SQLite.


# Autor

Igor Cândido Rodrigues

https://www.linkedin.com/in/igorc%C3%A2ndido/

