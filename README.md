## Contextos de Trabalho

Foram criados dois contextos de trabalhos com ambiente virtual. O primeiro é para a manutenção do site como um todo gerenciado pelo Pelican, o seguindo é um ambiente de desenvolvimento utilizado como exemplo. Segue abaixo as descriçãoes de cada um deles:

### Ambiente Virtual para atualização dos textos gerenciados pelo Pelican

Para se publicar uma alteração Seguir A seguintes Indicações

No caso se o VsCode não estiver configurado com o ambiente virtual gerado
```bash 
source .vcntEst/bin/activate
```

```bash
pelican content 
git add .
git commit -m "Atualiza Dados"
ghp-import output -b gh-pages
git push origin gh-pages
```

Ativa o ambiente virtual habilitado:
`source .vcntEst/bin/activate`

Gera Conteudo no Pelican
`pelican content`

Aplica comandos no Git para publicação

`git add .`
`git commit -m "Atualiza Dados"`
`ghp-import output -b gh-pages`
`git push origin gh-pages`


### Ambiente Virtual ( Poetry ) para uso dos códigos exemplos

Este item está configurado na seção: "Ambiente de Trabalho Dados" e está na pasta:
`/data-worspace