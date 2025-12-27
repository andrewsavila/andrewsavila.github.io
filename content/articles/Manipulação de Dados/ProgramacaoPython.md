---
Title:Programação em Dados com Python
Date: 2025-10-26
Category: Programacao
Tags: linguagem 
Slug: programacao-python
Authors: Andre Souza
Summary: Manipulações básicas e mais comuns com dados no Python
---

## Programação em Dados com Python

Mãos a Obra. Vamos passar por alguns conceitos, detalhando os mesmos através de exemplos práticos de manipulação de dados.

Se efetivamente quiser reproduzir o que está listado abaixo será essencial, ter preparado o ambiente, o que foi descrito na seção:
[Configurando e Entendendo o Ambiente de Trabalho em Dados]({filename}ambiente-trabalho.md){:target="_blank"}

Considerando isso alguns pontos são essenciais, recordar do ambiente de trabalho. Estamos usando o poetry, criamos um ambiente limpo, por isso
iremos sempre instalar o pacote e atualizar o ambiente virtual local.

Importante seu Vs Code esta configurado para ao abrir um terminal, ele já abra dentro do contexto do ambiente virtual do poetry, para as dependendencias serem instaladas corretamente.

#### Manipulando arquivos CSV

##### Conceitos Basicos 

###### Incluindo novas dependencias

Nosso ambiente iniciou sem nem um pacote, que usaremos na programação, instalado. Dai antes de começar vamos adicionar o novo pacote que iremos usar nesse exemplo. Como comentado acima, essencial estarmos em nosso ambiente selecionado, o ambiente virtual do Poetry.


```shell
poetry add pandas 
poetry install
```

Vamos ao código:

```python
import pandas as pd

# Defini local onde estão os dados
nomeArquivo01 = 'dados/listapessoas01.csv'
nomeArquivo02 = 'dados/listapessoas02.csv'
nomeArquivoSaida = 'dados/listapessoasUnida.csv'

# Carrega os dados para o DataFrame do Pandas
dfPrimeiroBloco = pd.read_csv(nomeArquivo01, sep=';')
dfSegundoBloco = pd.read_csv(nomeArquivo02, sep=';')

# Garante padronização dos tipos de dados que serão usados para união dos arquivos
dfPrimeiroBloco["codigo"] = dfPrimeiroBloco["codigo"].astype('int64')
dfSegundoBloco["codigo"] = dfSegundoBloco["codigo"].astype('int64')

# Verifica se os tipos de dados estão compatives
display(dfPrimeiroBloco["codigo"].dtypes,'tipo de dado da coluna "codigo" do primeiro arquivo')
display(dfSegundoBloco["codigo"].dtypes,'tipo de dado da coluna "codigo" do segundo arquivo')

# Faz a união de ambos arquivos baseado na chave 
dfUniao = pd.merge(dfPrimeiroBloco,dfSegundoBloco,left_on='codigo',right_on='codigo',how='left',indicator=True)

# Simples manipulação de dados no Pandas
display(dfUniao.query('Nome.str.contains("maria",case=False)', engine='python'))    

# Os dois arquivos estão unidos nesse ponto já, dentro do dataframe. Agora vamos converter o resultado para um novo csv
dfUniao.to_csv(nomeArquivoSaida, sep=";")
```

Vamos descrever sucintamente o que o codigo faz 

* Defini local onde estão os dados
    
    Esse ponto simplesmente define os locais onde os arquivos estarão armazenados

* Carrega os dados para o DataFrame do Pandas

    Comando básico do pandas que carrega um csv para um DataFrame do Pandas, carrega em Memoria

* Garante padronização dos tipos de dados que serão usados para união dos arquivos

    Nesse primeiro exemplo não iremos entrar em muitos detalhes, mas é sempre importante validar os tipos de dados que serão usados como chave de união dos dois arquivos. Esse exemplo simples, não irá gerar problemas nem um. Mas no mundo real, com arquivos maiores onde não temos controle da fonte geradora, poderá ser necessário muitos tratamentos. Mas esse exemplo resolve alguns casos básicos de tipagem.

* Verifica se os tipos de dados estão compatives

    Por garantia é sempre bom validar, e para isso estamos imprimindo na tela, os tipos de dados das chaves de união, para evitar surpresas no caso de volumes altos de dados

* Faz a união de ambos arquivos baseado na chave 

    Esse é uma união simples entre os dois arquivos( DataFrames ) usando algumas regrinhas basicas:

        - Estou explicitamente definindo o "left_on" e "right_one" para tomar consciência que existe essa opção e os nomes das colunas poderiam ser um pouco diferentes.

        - Estou usando um operação de junção "row='left'" para tratar alguns casos especiais, onde no arquivo ( DataFrame ) da esquerda podem ter mais linhas que o da direita, e mesmo assim traria sempre o resultado, nesse nosso exemplo garantindo que do lado esquerdo('left'), traga todas as linhas independente se ela existir no que esta no arquivo ( DataFrame ) da direita

        - Acrescentamos o operador "indicator=True" para incluir uma nova coluna chamada "_merge", no resultado final. No resultado poderá aparecer ["both","only_left"]. Onde o "both" indica que existem dados em ambos arquivos, e o "only_left" que o dado somente existe no arquivo1

* Simples manipulação de dados no Pandas

    Estamos usando um operador muito comum no NoteBook, de mostrar na tela o resultado que esta dentro do DataFrame, nesse caso estamos fazendo uma operação bem simples. Listando todos as linhas que tem no nome "maria" contido na coluna "Nome", o "case=False" garante que a pesquisa não fará diferença entre minúscula ou maiúscula

* Os dois arquivos estão unidos nesse ponto já, dentro do dataframe. Agora vamos converter o resultado para um novo csv

    Finalmente pegamos o resultado da união de ambos arquivos e salvamos ele em um novo arquivo apontado pelo caminho.


É muito comum trabalhar com volumes grandes de dados, e tais dados estão muitas vezes em csv ou excel.
Nesse exemplo iremos fazer algumas manipulações básicas e comuns.

#### Lendo dados em Diversos Formatos 

* *Lendo dados no formato Json*
* *Lendo dados no formato CSV*
* *Lendo dados no format excel*
* *Transformando todos eles em um mesmo padrão, tratamento de tipo*
* *Unindo-os em um mesmo formato - Pandas*
* *Salvando o resultado de nosso trabalho em um novo csv*

#### Trabalhando com dados no Formato Json

* *Lendo dados no formato Json*
* *Manipulando dados no formato Json*
* *Serializando e Deserializando os dados Json*
* *Convertendo o Json para Pandas*
* *Retornando o Pandas para Json e Persistindo em um arquivo o resultado


#### Substituindo o Sql pela manipulação no Pandas 

Com um bom conhecimento da linguagem Sql podemos fazer muitos tratamentos e processamentos, na manipulação de dados. Porem em python, ganhamos a liberdade de conectar em fontes diferentes e trabalhar com esses dados em um local centralizado, logo o formato e localização da fonte de dados deixa de ser um problema. Porem esse conhecimento não descarta as vantagens de dominar a linguagem Sql, que existem processos e recursos que essa linguagem nos oferece que é simplesmente imbatível em vantagens.
E não depender de fornecedor nem um apenas de sua criatividade e capacidade, é algo que inicialmente pode assustar mas destrava a liberdade para avançar muito.
No início tudo é mais desafiador, mas com o tempo, a familiarização e o conhecimento torna fácil aquilo que era aparentemente difícil no inicio. 
Dai a sugestão de investir na manipulação de dados via Python, nos tornamos independente de ferramentas de terceiro e o limite é estabelecido por uma linguagem de uso amplo no mercado, e que esta em constante avanço e atualizações.

##### Manipulando dados com pandas*

* *Lendo um exemplo de dados em csv para manipulação*
* *Iterando em blocos de dados do Pandas*
* *Realizando pesquisas dentro de um bloco de dados dentro do Pandas*
* *Salvando o resultado das manipulações de dados*


##### Manipulando dados cuja origem é um banco relacional ( read_sql )

* *Conectando no banco de dados*
* *Lendo dados no banco de dados*
* *Tratamento de tipo na leitura de dados Sql para Pandas*
* *Salvando os dados do banco de dados localmente, para evitar repetidas idas ao banco*


##### Manipulando dados com iteração com um banco relacional ( to_sql )

* *Conectando no banco de dados*
* *Lendo dados no banco de dados*
* *Salvando os dados do banco de dados localmente, para evitar repetidas idas ao banco*
* *Inserindo dados no banco de dados a partir do pandas*
* *Atualizando dados no banco de dados a partir do pandas*

