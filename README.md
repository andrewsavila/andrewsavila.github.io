## Contextos de Trabalho

Foram criados dois contextos de trabalhos com ambiente virtual. O primeiro é para a manutenção do site como um todo gerenciado pelo Pelican, o seguindo é um ambiente de desenvolvimento utilizado como exemplo. Segue abaixo as descriçãoes de cada um deles:

### Ambiente Virtual para atualização dos textos gerenciados pelo Pelican

Para se publicar uma alteração Seguir A seguintes Indicações

No caso se o VsCode não estiver configurado com o ambiente virtual ativo ative o mesmo
```bash 
source .vcntEst/bin/activate
```

```bash
pelican content 
git add .
git commit -m "Atualiza Dados"

# Estamos usando o **User site** andrewsavila.github.io
ghp-import output -b master
git push origin master
```
