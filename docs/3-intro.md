# Instruções

## Como clonar o projeto ##
```bash
# Clonar o repositório
git clone https://github.com/Igorcand/GroceryStoreAPI.git

#Entrar na pasta
cd GroceryStoreAPI

```

## Variáveis de ambiente ##
As variáveis de ambiente são cadeias de caracteres que contêm informações sobre o ambiente do sistema e sobre o usuário que está no momento conectado. Alguns programas de software usam as informações para determinar onde colocar arquivos (como por exemplo, os arquivos temporários).

Para o projeto ficar mais seguro, não é recomendado que coloque informações sensíveis direto no código, por isso usamos as variáveis de ambiente. Com isso, as variáveis SECRET_KEY e DEBUG precisam ser adicionadas ao código para funcionar.
##### Passo 1 #####
 Criar um arquivo chamado '.env' na raiz do projeto
##### Passo 2 #####
 Adicionar no arquivo criado os valores correspondente das variáveis 
##### Exemplo #####
```bash
SECRET_KEY = "sua_secret_key"
DEBUG = True
```

## Como rodar o projeto ##
```bash
# Clonar o repositório
git clone https://github.com/Igorcand/GroceryStoreAPI.git

#Entrar na pasta
cd GroceryStoreAPI

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

