---
Title: Pacotes do Python
Date: 2025-10-28
Category: Programacao
Tags: linguagem 
Slug: pacotes-codigo-python
Authors: Andre Souza
Summary: Introdução breve para iniciar com os pacotes do Python que iremos usar em nosso trabalho
---


#### Ambiente Virtual

É muito comum na programação em python, trabalhar com um ambiente isolado, o que chamamos de ambiente virtual. Para não se misturar as configurações desse ambiente de trabalho com os demais itens do computador de trabalho pessoal.

E alem disso, podemos trabalhar em equipe sendo necessário compartilhar nosso ambiente com outros da equipe, as dependência para conexão de dados e até bibliotecas especificas para o trabalho padronizado, irá exigir um ambiente controlado em termos de versionamento do que estamos usando no momento.

O Poetry nos ajudará nisso

#### Inclusão de Pacotes 

Durante o trabalho de manipulação de dados, vamos utilizar uma grande quantidade de pacotes construidos por terceiros. E tais pacotes podem ser instalados de várias formas, nesse exemplo vamos nos ater a forma de instalação usando o poetry.

#### Gerenciador de Pacotes python Poetry
---

##### **1. Instalar o Poetry (caso ainda não tenha)**

Se você ainda não instalou o Poetry, execute no terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Depois, adicione o caminho à sua shell (caso necessário). Ou reinicie o terminal.

---

##### **2. Ir para o diretório do seu projeto**

```bash
cd /caminho/do/seu/projeto
```

Esse é o diretório onde está o seu notebook Jupyter e onde você quer usar o Poetry.

---

##### **3. Inicializar o projeto com o Poetry**

Rode:

```bash
poetry init
```

O `poetry init` vai interagir com você, perguntando:

* Nome do pacote
* Versão
* Descrição
* Autor
* Versão do Python (ex: `^3.10`)
* Dependências

Você pode simplesmente apertar `Enter` para aceitar os padrões e editar depois no `pyproject.toml`.
Ou apenas usar o `poetry add <pacote>` explicado abaixo

---

##### **4. Criar o ambiente virtual e instalar dependências**

Após gerar o `pyproject.toml`, você pode instalar dependências com:

```bash
poetry install
```

Ou adicionar uma específica, por exemplo:

```bash
poetry add pandas jupyter matplotlib
```

Isso criará um ambiente virtual isolado com tudo que você precisa.

---

##### **5. Ativar o ambiente virtual do Poetry no Jupyter**

Para que o Jupyter reconheça o ambiente virtual do Poetry como um *kernel*, você deve:

```bash
poetry run python -m ipykernel install --user --name=nome_do_projeto --display-name "Python (projeto)"
```

Depois disso, ao abrir seu Jupyter Notebook, você poderá selecionar o kernel **"Python (projeto)"**.

---

##### **6. Rodar o Jupyter a partir do Poetry (opcional)**

Se quiser rodar o Jupyter dentro do ambiente do Poetry:

```bash
poetry run jupyter notebook
```

Ou:

```bash
poetry run jupyter lab
```

---

##### Resultado

Seu projeto agora está com:

* Um ambiente isolado via Poetry
* Dependências gerenciadas com `pyproject.toml`
* Um kernel próprio visível no Jupyter

---

