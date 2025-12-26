---
Title: Configurando e Entendendo o Ambiente de Trabalho em Dados
Date: 2025-10-29
Category: Programacao
Tags: linguagem 
Slug: ambiente-trabalho
Authors: Andre Souza
Summary: Apresentação e Estrutura simplificada para trabalhar nas ferramentas de codificação em Python
---

## Criando um Ambiente de Trabalho em Dados
Para trabalhar com dados, individualmente, porem considerando que podemos tambem compartilhar o que fazemos com uma equipe exige a organização dos scripts de dados de forma que possamos reutiliza-lo futuramente ou até mesmo voltar a ele no futuro, de forma simples e rápida.

Sendo assim vamos a construção de um “ambiente de trabalho padrão de dados”, não um projeto de software tradicional.
Vamos evitar padrões de “produto Python” e focar em organização operacional, rastreabilidade e longevidade.

### Como será nosso ambiente de trabalho
Linux/Ubuntu + Poetry + VS Code + Notebooks + Scripts de dados compartilhados em equipe


### Objetivo do Setup

* *Um único ambiente Poetry*

* *Usado por toda a equipe*

* *Para vários scripts e notebooks*

* *Executados de forma esporádica e sob demanda

* *Com código reutilizável*

* *Sem acoplamento a um “projeto fechado”*


### Visão Geral da Arquitetura

* *Poetry = gestão de dependências*

* *.venv local = isolamento*

* *VS Code = ambiente de execução*

* *Notebooks = exploração / análise*

* *Scripts Python = processamento reutilizável*


---

# *1.* Instalar o Poetry (1 vez por máquina)

No Linux / Ubuntu:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verifique:

```bash
poetry --version
```

📌 Cada membro da equipe instala localmente.
📌 O projeto é quem define as dependências, não o sistema.

---

# *2.* Criar a pasta base do ambiente de dados

Essa pasta **é o que será versionado e compartilhado**.

```text
data-workspace/
```

Entre nela:

```bash
cd data-workspace
```

---

# *3.* Inicializar o Poetry (modo controlado)

```bash
poetry init
```

Respostas **recomendadas**:

* Package name [meu-projeto] → **notebook**
* Define dependencies interactively? → **No**
* Define dev dependencies interactively? → **No**

📌 O objetivo é **um `pyproject.toml` limpo e estável**.

---

# *4.* Fixar o virtualenv dentro do projeto

Esse passo é **fundamental para consistência no VS Code**.

```bash
poetry config virtualenvs.in-project true
```

# *5.* Como iremos trabalhar com o notebook é essencial a instalação do ipykernel em nosso ambiente local

```bash
poetry add --group dev ipykernel
```

Depois:

```bash
poetry install
```

Resultado:

```text
data-workspace/
├── .venv/
├── pyproject.toml
├── poetry.lock
```

📌 Cada pessoa da equipe terá a mesma estrutura.
📌 Nenhum kernel global necessário.

---


### *6.* Selecione explicitamente o interpretador Python para deixar o Ambiente Python com o Env local

No VS Code:

* `Ctrl + Shift + P`
* Digite: **Python: Select Interpreter**
* Escolha:

```text
./.venv/bin/python
```

📌 Esse passo é **obrigatório**
📌 Sem isso, o kernel nunca aparece

Você pode validar abrindo um terminal integrado:

```bash
which python
```
### 6.1 Ao selecionar o “Python: Select Interpreter”

Esse comando **não resolve notebooks** depois desse ponto.
Agora você precisa atuar **no contexto do Jupyter**.

---

### 6.2 Clique em **Select Kernel** (no topo do notebook)

Fluxo correto:

```
Select Kernel
  → Select Another Kernel
      → Python Environments
```

- 📌 **Esse caminho é essencial**
- 📌 Não escolha “Existing Jupyter Server”

---

### 6.3 Agora escolha o Python da `.venv`

Você deve ver algo parecido com:

```
Python 3.11.x (.venv)
```

ou

```
./.venv/bin/python
```

Selecione esse.

- ✔️ A partir desse momento, o notebook fica vinculado
- ✔️ Essa escolha fica salva no próprio `.ipynb`
- ✔️ Isso foi possivel pois logo acima foi adicionado o ipykernel pelo commando :`poetry add --group dev ipykernel`



### 6.3 Agora que está tudo pronto. Vamos configurar um WorkSpace.

Isso irá facilitar muito a facilidade para reproduzir esse ambiente em outras maquinas e evitar qualquer problema na configuração

Abaixo consta um exemplo, onde fazemos referencia a pastas criadas acima na inicialição do ambiente via Poetry, onde criamos um ambiente localmente dentro do contexto da página corrente de trabalho.

```python
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {

		// Python / Poetry
		"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
		"python.terminal.activateEnvironment": true,

		// Terminal
		"terminal.integrated.env.linux": {
		"PYTHONPATH": "${workspaceFolder}"
		}

	}
} 
```






# *7.* Estrutura de pastas (padrão da equipe)

```text
data-workspace/
│
├── pyproject.toml
├── poetry.lock
├── .venv/
│
├── notebooks/
│   ├── exploracao/
│   │   └── 01_exemplo.ipynb
│   │
│   └── processamento/
│       └── 01_transformacao.ipynb
│
├── scripts/
│   ├── comuns/
│   │   ├── limpeza.py
│   │   ├── datas.py
│   │   └── io.py
│   │
│   └── especificos/
│       └── segmento_x.py
│
├── data/
│   ├── raw/
│   └── processed/
│
└── README.md
```

- 📌 **Notebooks não contêm lógica pesada**
- 📌 Lógica reutilizável fica em `scripts/comuns`

---

# *8.* Tornar os scripts reutilizáveis

Crie arquivos `__init__.py`:

```bash
touch scripts/__init__.py
touch scripts/comuns/__init__.py
```

Agora, em notebooks ou scripts:

```python
from scripts.comuns.limpeza import normalizar_colunas
```

📌 Isso evita duplicação e caos futuro.

---

# 9 Adicionar dependências com Poetry

Sempre via Poetry:

```bash
poetry add pandas numpy sqlalchemy
poetry add --group dev ipykernel
```

📌 Toda a equipe compartilha o mesmo `poetry.lock`.

---

# *10.* Configurar o VS Code (ponto-chave)

1. Abra a pasta `data-workspace` no VS Code
2. Abra um notebook `.ipynb`
3. Clique em **Select Kernel**
4. Escolha:

   ```
   Python (.venv)
   ```

- 📌 **Nada mais é necessário**
- 📌 O VS Code usa diretamente o Poetry

---

# *11.* Padrão de uso diário (time inteiro)

* Novo notebook? → use `.venv`
* Nova lib? → `poetry add`
* Código reutilizável? → `scripts/comuns`
* Código pontual? → `scripts/especificos`
* Dados processados? → `data/processed`

---

# *12.* Por que isso funciona no longo prazo

✔️ Um único ambiente
✔️ Dependências versionadas
✔️ Scripts antigos continuam rodando (até onde possível)
✔️ Evolução controlada de bibliotecas
✔️ Facilidade de onboarding
✔️ Histórico claro do que foi feito

📌 Quando uma lib precisa ser atualizada, **toda a equipe evolui junto**.

---

# Conclusão objetiva

Você **não está montando um projeto Python**.
Você está montando um **ambiente de trabalho de dados profissional**.

O setup acima:

* Evita improviso
* Evita kernel global
* Evita perda de contexto
* Evita “scripts esquecidos”

E, principalmente, **escala com o tempo**.

---


## Conteúdo Antigo-Necessario Revisar


#### O que é feito em uma IDE

É um termo muito usado na programação, e significa "Ambiente de Desenvolvimento Integrado", que é o local onde será usado a linguagem python para codificar o tratamento em dados. Materializarei aqui uma estrutura simples e básica, para organizar o código. Que se trata onde devo escrever o que, na codificação.

O tratamento de dados será feito via programação com Python, por isso preciso ter um código de fácil manutenção.

#### Notebook & Código padrão

Um notebook é uma forma de programar, interativa, onde programo e vejo e resultado de forma imediata. E tambem posso ir documentando os trechos de código, para facilitar o entendimento quando precisar voltar no assunto. Esse arquivos possuem a extensão ".ipynb"

Podemos criar rotinas em Python que irão executar em algum local como um serviço, dentro de um container. Nesse caso os arquivos possuem a extensão ".py"

#### Nesse documento vamos descrever duas estruturas/organização do código para já iniciar o processo de forma organizada

``` python 
├── Area de Trabalho/
|   ArquivoNoteBook.ipynb
|   ├── dataControl/
|   ├── __init__.py
|   ├── data_mySql.py
|   ├── data_s3.py
|   ├── data_file.py
|   ├── data_athena.py
|   └── data_msSql.py
└──
```

##### NoteBook

Arquivos com extensão ".ipynb"

Esse código abaixo não precisa de nem um pacote python para rodar, a instalação nativa do python já tras esse pacote que se chama ipykernel.
E se trata de um simples código que trabalha com uma estrutura simples de dados em lista e um loop nessa lista escrevendo no console os resultados

``` python
lista_dados = [
    {"membro": "pai", "nome": "André Wanderley de Souza", "idade": 51, "peso": 68},
    {"membro": "mae", "nome": "Cleuza Samai Alves Souza", "idade": 54, "peso": 52},
    {"membro": "filho", "nome": "Augusto Samai de Souza", "idade": 22, "peso": 55},
    {"membro": "filho", "nome": "Álvaro Samai de Souza", "idade": 15, "peso": 45}
]

print("Essa família tem quatro membros")
for item in lista_dados:
    print(f"O {item['membro']} se chama {item['nome']}, tem {item['idade']} anos e pesa {item['peso']} kg")

```

##### Codificação Tracicional


Arquivos com extensão ".py"

O código acima é exatamente o mesmo com a diferença que não irá precisar do pacote ipykernel, porem a forma de execução e estrutura da documentação é diferente de um notebook

