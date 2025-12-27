## Contextos de Trabalho

Foram criados dois contextos de trabalhos com ambiente virtual. O primeiro é para a manutenção do site como um todo gerenciado pelo Pelican, o seguindo é um ambiente de desenvolvimento utilizado como exemplo. Segue abaixo as descriçãoes de cada um deles:

### Ambiente Virtual para atualização dos textos gerenciados pelo Pelican

Para se publicar uma alteração Seguir A seguintes Indicações

No caso se o VsCode não estiver configurado com o ambiente virtual ativo ative o mesmo
```bash 
source .vcntEst/bin/activate
```


### Código Pelican

Para não confundir o processo de atualização de dados, nosso projeto irá atualizar todos ajustes na master, para manter o histórico de atualizações
Como estou trabalhando sozinho nesse projeto, por algum motivo podem ocorrer conflitos entre a master local e a remota, para isso posso usar o comando descrito abaixo com um `--force`. Ele aplica tudo o que esta localmente na master, descartando o que está la.

```bash
git add .
git commit -m "Atualiza conteúdo Pelican"
git push origin master

# git push origin master --force
```

### Tendo Feito os ajustes iremos gerar o HTML ( Será gerada na pasta output)

```bash
rm -rf output cache __pycache__
```

Agora temos um ponto importante enquanto estiver desenvolvendo e validando localmente. 
Você deverá publicar usando o seguinte commando, estou colocando o pelicanconf.py explicitamente, mas não é obrigatório, o objetivo é a clareza do que esta ocorrendo:

```bash
pelican content -s pelicanconf.py
```

Se for Gerar uma versão para ser publicada em produção, dai terá que usar o comando abaixo, com os adendos registrados em publishconf.py:

```bash
pelican content -s publishconf.py
```

Nosso exemplo de trabalho está seguindo as boas práticas, que configura a branch gh-pages como nossa branch de publicação. Os comandos abaixo estão gerando o conteudo dentro dessa branch e finalmente publicando o conteúdo ajustado em produção

### Publicar site

```bash
ghp-import output -b gh-pages
git push origin gh-pages
```