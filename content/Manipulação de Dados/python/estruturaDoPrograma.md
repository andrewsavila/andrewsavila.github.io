---
Title: Ferramento para Codificar em Python
Date: 2025-10-29
Category: Programacao
Tags: linguagem 
Slug: ide-estrutura-codigo-python
Authors: Andre Souza
Summary: Apresentação e Estrutura simplificada para trabalhar nas ferramentas de codificação em Python
---


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

