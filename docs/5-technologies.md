# Tecnologias

## Poetry ##
Criado por Sébastien Eustace em 2018, o Poetry surge para tentar trazer soluções que foram deixadas de lado por gerenciadores antigos. Ele permite que você declare as bibliotecas das quais seu projeto depende e assim tudo será gerenciado para você.

Ao inicialixar um projeto com o poetry é criado dois arquivos que seão responsáveis em administrar seu ambiente virtual, poetry.lock e pyproject.toml

No arquivo pyproject.toml terá informações sobre seu projeto como nome, versão, descrição, dependencias, etc

![Mobile 1](./assets/poetry/pyproject.png)

No arquivo poetry.lock ficará as dependencias do seu projeto que serão utilizadas para a inicialização do ambiente virtual.

![Mobile 1](./assets/poetry/poetry-lock.png)


#### Alguns comandos do Poetry que talvez possa precisar ####

##### Ativação do ambiente virtual #####
```bash
poetry shell
```

##### Adicionar nova biblioteca #####
```bash
# Para adicionar dependencias de produção
poetry add your_lib

# Para adicionar dependencias de desenvolvimento
poetry add --dev your_lib
```

##### Remover nova biblioteca #####
```bash
# Para remover dependencias de produção
poetry remove your_lib

# Para remover dependencias de desenvolvimento
poetry remove --dev your_lib
```

##### Criar um requirements.txt #####
```bash
poetry export -f requirements.txt --output requirements.txt
```

## Formatações de Código ##
Cada programador escreve os códigos de uma maneira, utilizam um tamanho de tela, um softwere, e entre outras diferenças que podem aparecer quando se trata de codas. Com isso, passaram a existir convensões para que as pessoas passasem cada vez mais a utilizarem um padrão, para que fique mais facil o entendimento dos códigos, com isso, para que nós não precisemos lembrar de todas as convenções, existem formatadores de código que fazem isso nós.

Utilizamos nesse projeto, 3 bibliotecas ótimas que fazem essa formatação automaticamente, já corrigindo o erro, que são:
##### blue #####
```bash
poetry shell
blue .
```

##### isort #####
```bash
poetry shell
isort .
```

##### prospector #####
```bash
poetry shell
prospector --with-tool pep257 --docs-warning
```

## Admin ##

<code>
Uma das partes mais poderosas do Django é a interface de administração automática. Ele lê metadados de seus modelos para fornecer uma interface rápida e centrada no modelo, onde usuários confiáveis ​​podem gerenciar o conteúdo em seu site. O uso recomendado do administrador é limitado à ferramenta de gerenciamento interno de uma organização. Não se destina a construir todo o seu front-end.

O administrador tem muitos ganchos para personalização, mas cuidado ao tentar usar esses ganchos exclusivamente. Se você precisar fornecer uma interface mais centrada no processo que abstraia os detalhes de implementação de tabelas e campos do banco de dados, provavelmente é hora de escrever suas próprias exibições.
</code>

Para acessar a página, basta acessar a URL abaixo e fazer o login com o mesmo usuário e senha do seu super usuário.

- https://localhost/admin/

![Mobile 1](./assets/admin/admin_home.png)


![Mobile 1](./assets/admin/category_home.png)


![Mobile 1](./assets/admin/add_category.png)


![Mobile 1](./assets/admin/product_home.png)


![Mobile 1](./assets/admin/add_product.png)


![Mobile 1](./assets/admin/sale_home.png)


![Mobile 1](./assets/admin/add_sale.png)


![Mobile 1](./assets/admin/report_home.png)


## Swagger ##
O Swagger é um framework composto por diversas ferramentas que, independente da linguagem, auxilia a descrição, consumo e visualização de serviços de uma API REST. 

Foi usado a biblioteca drf-yasg na sua versão 1.21.4 para construir a documentação da API, como mostra abaixo.

Para acessar a documentação, acesse a URL abaixo:

- https://localhost/swagger/

![Mobile 1](./assets/swagger/swagger.png)
![Mobile 1](./assets/swagger/routes1.png)
![Mobile 1](./assets/swagger/routes2.png)

Para acessar o redoc, acesse a URL abaixo:

- https://localhost/redoc/

![Mobile 1](./assets/swagger/redoc.png)

## Pytest ##

A framework  pytest facilita a escrita de testes pequenos e legíveis e pode ser dimensionada para oferecer suporte a testes funcionais complexos para aplicativos e bibliotecas.

No projeto foi constuido testes para todas as rotas descritas na sessão anterior de sobre como utilizar a API do mercadinho. O intuito dos testes são avaliar as responses e os códigos de status, de chamadas que deveriam funcionar e também as que deveriam falhar.


![Mobile 1](./assets/pytest/tests.png)

```bash
## Como rodar os testes ##

# Entrar no ambiente virtual do Poetry
poetry shell

# Entrar no diretorio src/
cd src/

# Rodar os testes
pytest
```


## REDIS ##

<p> O Redis é um armazenamento de estrutura de dados de chave-valor de código aberto e na memória. O Redis oferece um conjunto de estruturas versáteis de dados na memória que permite a fácil criação de várias aplicações personalizadas. Os principais casos de uso do Redis incluem cache, gerenciamento de sessões, PUB/SUB e classificações.</p>

<p> No projeto em particular, foi adicionado o mesmo End-Point para a visualização dos produtos utilizando o sistema de cache oferecido pelo Redis. Foi feito a mesma rota pra fins de comparação com o uso do cache e sem, pois com o cache a resposta é mais rápida porém a atualização não é instantânea.</p>

O End-Point contruido na aplicação é: 
- https://localhost/api/products_cache/ (MÉTODO HTTP GET)

<p> Você poderá testar a rota adicionando um produto como descrito na sessão acima, e utilizar a rota acima, você verá que o produto recém adicionado não irá aparecer, e se você rodar a rota de visualizar todos os produtos, ele estará lá. Só após 60 segundos que seu produto irá aparecer na rota em que o cache do Redis está funcionando. </p>


## Celery ##
O Celery é um sistema distribuído simples, flexível e confiável para processar grandes quantidades de mensagens, ao mesmo tempo em que fornece às operações as ferramentas necessárias para manter esse sistema.

É uma fila de tarefas com foco no processamento em tempo real, além de oferecer suporte ao agendamento de tarefas.As filas de tarefas são usadas como um mecanismo para distribuir o trabalho entre threads ou máquinas.A entrada de uma fila de tarefas é uma unidade de trabalho denominada tarefa. Processos de trabalho dedicados monitoram constantemente as filas de tarefas para novos trabalhos a serem executados.

O Celery requer um transporte de mensagens para enviar e receber mensagens. Os transportes do broker RabbitMQ e Redis são completos, mas também há suporte para Amazon SQS, Apachhe Zookeeper, entre outros.

No projeto em si, será utilizado o Redis para o sistema de mensageria pois já está feito a instalação como descrito na sessão anterior. Foi adicionado uma simples rota para exemplificar como o sistema de filas e tarefas funcionam em uma aplicação, e para ter uma noção de como escalar para caso a aplicação cresca.


Para utilizar o end-point wue foi criado para o celery basta abrir o Postman, ou qualquer outra plataforma de API, e fazer a simples chamada no End-Point abaixo:

 - https://localhost/celery/ (MÉTODO HTTP GET)

Esta rota irá apenas retornar uma mensagem "Done" e um código 200. 

![Mobile 1](./assets/celery/route.png)

Porém, se você observar no terminal que você rodou o comando do celery, poderá observar que foi executada uma ação que foi justamente mostrar na tela os números de 0 a 9. Isso mostra como o celery funciona, em que ele passa a responsabilidade da execução da operação para outra máquina, desocupando a principal para que ela possa executar  outra coisa, e quando a tarefa executada pelo Celery terminar, ele irá devolver a resposta.

![Mobile 1](./assets/celery/celery_working.png)

Utilizando a biblioteca django-celery-results nos podemos ver o resultado das tarefas executadas de uma maneira mais clara e legível. Pois com ela, nos podemos acessar o admin do django pela URL abaixo e ver que temos mais duas tabelas acrescentadas.

- https://localhost/admin/ 

![Mobile 1](./assets/celery/celery_admin.png)

A se clicarmos em "Task results" podemos ver mais informações sobre a tarefa executada que antes eram omitidas.

![Mobile 1](./assets/celery/tasks.png)

Para a implementação do Celery na aplicação foi utilizado o link abaixo como referência para a integração do Django, Celery e o Redis.
- <a href="https://www.youtube.com/watch?v=EfWa6KH8nVI" target="_blank">link para o vídeo</a>

## Logs e Sentry ##
Logging é uma maneira de rastrear eventos que acontecem quando algum software executa. O desenvolvedor de software adiciona chamadas de logging no código para indicar que determinado evento ocorreu. Um evento é descrito por uma mensagem descritiva que pode opcionalmente conter o dado de uma variável (ex.: dado que é potencialmente diferente pra cada ocorrência do evento). Eventos também tem um peso que o desenvolvedor atribui para o evento; o peso pode também ser chamada de níveis ou severidade.

Logging provê um conjunto de funções convenientes para o uso simples de logging. Estas funções são debug(), info(), warning(), error() e critical().

Para uma melhor visualização dos logs, nos integramos a aplicação com Sentry, é um serviço de monitoramento que você pode configurar para se hospedar ou usado como um serviço para capturar e relatar erros em seus aplicativos da web Python .

Caso queira integrar com o Sentry, você precisa criar uma variável de ambiente no arquivo .env com o link do seu projeto
##### Exemplo ##### 

```bash
SENTRY_URL = "https://sua_hash@sua_hash.ingest.sentry.io/sua_hash"
```

##### Interface do Sentry #####
![Mobile 1](./assets/log/sentry.png)

Caso você não queira integrar com o sentry, também é criado um arquivo logfile.log com as informações dos logs.

![Mobile 1](./assets/log/logfile.png)

## Autenticação JWT ##

<p> JWT (JSON Web Token) é um método RCT 7519 padrão da indústria para realizar autenticação entre duas partes por meio de um token assinado que autentica uma requisição web. Esse token é um código em Base64 que armazena objetos JSON com os dados que permitem a autenticação da requisição.</p>

<p> Para fazer essa autenticação por token foi usado a biblioteca djangorestframework-simplejwt na sua versão 5.2.2 e com sua implementação vem duas rotas para isso, a de geração do token e o refresh do token. </p>

<p> Para gerar o token, você precisa necessariamente de ser super usuário, e então você passa o nome de usuário e a senha na rota abaixo: </p>
- https://localhost/token/ (MÉTODO HTTP POST)

![Mobile 1](./assets/auth/create_token.png)

Para gerar um novo token utilizando o refresh, basta passar o refresh token como parâmetro de entrada na rota abaixo: 
- https://localhost/refresh/ (MÉTODO HTTP POST)

![Mobile 1](./assets/auth/refresh.png)

<p> Durante o processo de desenvolvimento da aplicação, ocorreu um erro de integração de tecnologias ao usar a autenticação JWT e os testes, pois sempre que a autenticação das rotas estava ativa, os testes não conseguiam testar as rotas por causa de justamente não terem o token para enviar. Com isso, foi criado uma rota simples para mostrar o funcionamento da autenticação. </p>

- https://localhost/api/authorization/ (MÉTODO HTTP GET)

Caso você tente executar essa rota sem enviar o token no Header da requisição, irá apresentar erro:

![Mobile 1](./assets/auth/without_auth.png)

Caso você tente executar essa rota sem enviar o token válido, irá apresentar erro:

![Mobile 1](./assets/auth/token_not_valid.png)

Caso envie o token dessa maneira:

Header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MzEyMTQwLCJpYXQiOjE2NzQzMTE4NDAsImp0aSI6ImI4NmYyMTVmZGYzNTQzOTRhNmUzMDM1NWZkNTY2ZjhiIiwidXNlcl9pZCI6MX0.T-1bg-5sVZ_4B8VHjdG5MIOYc6WsDxEnLovyPbAXj8g"}

Irá apresentar essa mensagem simples:

![Mobile 1](./assets/auth/have_authorization.png)


## Docker ##

Docker é uma forma de virtualizar aplicações no conceito de “containers”, trazendo da web ou de seu repositório interno uma imagem completa, incluindo todas as dependências necessárias para executar sua aplicação.

A aplicação uma segunda forma de funcionar que é a partir de imagem e containers do Docker, e para isso, você precisa ter o Docker instalado na sua máquina.

<a href="https://docs.docker.com/desktop/install/windows-install/" target="_blank">link para instalar</a>


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

![Mobile 1](./assets/docker/build.png)

#### Rodando a partir do Docker #####
##### Django API #####
![Mobile 1](./assets/docker/docker-api-running.png)

##### Postgres DataBase #####

![Mobile 1](./assets/docker/docker-postgres-running.png)

##### Redis #####

![Mobile 1](./assets/docker/docker-redis-running.png)

##### Celery #####

![Mobile 1](./assets/docker/docker-celery-running.png)


