---
Title: Onde Salvar as Senhas
Date: 2025-10-27
Category: Programacao
Tags: linguagem 
Slug: .env-python
Authors: Andre Souza
Summary: Organização básica de onde armazenar as senhas utilizadas na manipulação de dados ( .env )
---

#### Variáveis de Ambiente .env

Ao trabalhar com dados, muitas vezes esses são de acesso restrito, sendo necessário utilizar alguma credencial específica para acessar determinada fonte de dados. É muito importante armazenar essas senhas em um arquivo especial, quando estamos trabalhando localmente, para aumentar a segurança a medida que esses arquivos em nossa máquina começam a ter que ir para outro ambiente, seja no ambiente de produção, na máquina de um colega ou até mesmo em alguma ferramente de gerencialmente de versão de código como o GitHub.

Para isso vamos usar o .env, dentro do python.

##### Na raiz do programa, vamos criar um arquivo .env

```shell
echo "" > .env
```

##### Dentro desse arquivo iremos inserir as diversas credenciais que iremos utilizar no código segue um exemplo

```python
DATABASE='insira aqui o nome do banco de dados'
USER='insira aqui o usuario utilizado para conectar on banco de dados'
PASSWORD='insira aqui a senha utilizada para, o usuario informado, conectar no banco de dados'
HOST='insira aqui o nome do servidor onde esta a base de dados'

TOPIC_PATH_SUB_GOOGLE="caminho do topico para acesso acessar o google via codigo"
SERVICE_ACCOUNT_BRAZIL = ' local onde está armazenado localmente o arquivo json com as credenciais para acessar o google '

```

##### Agora de dentro do programa em python, vamos carregar os dados do arquivo .env para utilizar as credenciais para conexao a fonte de dados

```python
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text

# Vamos carregar o arquivo local .env para memoria, porem desconsiderando container ou qualquer complexidade de ambiente

load_dotenv()

def Conecta_sqlalchemy_mysql():

    
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    port = 3306

    engine = create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

    return engine.connect()

con =  Conecta_sqlalchemy_mysql()

sql = text("select id, Membro, Nome, Idade, Peso from NomeTabela;")

objResult = con.execute(sql)   
```

Neste exemplo implementamos codigos a mais, que serão explicados em outro momento. Mas por hora será utlil entender o funcionamento do arquivo .env