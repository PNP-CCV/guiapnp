---
layout: default
title: "Conteúdos"
toc: true
---
# Conteúdos

O conteúdo é uma página HTML que o PNP Gestor publica no portal da PNP —
um painel, um relatório. Cada conteúdo tem um histórico de versões: cada
arquivo enviado vira uma versão, e uma delas é a que está no ar.

Esta tela está disponível para os perfis Administrador, Operador SETEC e
Gestor Setec, que também cadastram, editam, publicam e excluem conteúdos.

## Ver os conteúdos cadastrados

Em **PNP Gestor → Conteúdos**, a plataforma lista os conteúdos em cartões,
com o nome, a data da última atualização e etiquetas coloridas, explicadas
na **Legenda**: a visibilidade (azul), a categoria (verde) e os grupos de
permissão (cinza). Os botões acima dos cartões alternam entre a visualização
em lista e em grade.

O bloco **Filtros** permite buscar por palavra-chave e restringir por
categoria, grupo de permissão, visibilidade e se o conteúdo está ativo — o
conteúdo deixa de estar ativo quando a sua categoria é desativada, ou
quando todos os seus grupos estão desativados.

Em cada cartão, os ícones abrem o detalhe, a edição, a exclusão e o envio
de uma nova versão. Arrastar um cartão pela alça à esquerda muda a ordem em
que os conteúdos aparecem no portal; esta lista continua em ordem
alfabética.

![Listagem de conteúdos]({{site.baseurl}}/assets/img/docs/manual-do-usuario/pnp-gestor/conteudos/lista.png)

## Quem vê um conteúdo

A visibilidade decide quem vê o conteúdo no portal:

- **Público** — qualquer pessoa, mesmo sem entrar na plataforma;
- **Privado** — as pessoas dos [grupos de permissão]({{site.baseurl}}/documentacao/manual-do-usuario/pnp-gestor/grupos-de-permissao)
  ativos associados ao conteúdo, e quem o criou;
- **Restrito** — o conteúdo que não é público e não tem grupo ativo: só
  quem o criou e o Administrador.

Um conteúdo público não aceita grupo de permissão. E o conteúdo de uma
[categoria]({{site.baseurl}}/documentacao/manual-do-usuario/pnp-gestor/categorias-de-conteudo) desativada sai do portal para todos.

## Cadastrar um conteúdo

O botão **Criar Conteúdo** abre o formulário. São obrigatórios:

- **Nome**;
- **Slug** — o identificador do conteúdo no endereço; é preenchido sozinho
  a partir do nome e não pode repetir o de outro conteúdo;
- **Arquivo** — o arquivo `.html`, de até 2 MB.

A descrição, a categoria, os grupos de permissão, a imagem de destaque
(**Thumbnail**: PNG, JPEG ou JPG, até 2 MB) e a descrição da versão são
opcionais. A caixa **Tornar conteúdo público** e a escolha de grupos se
excluem: marcar a caixa limpa os grupos, e com grupos escolhidos a caixa
fica desabilitada. Sem grupos e sem a caixa marcada, o conteúdo fica
restrito.

![Formulário de cadastro de conteúdo]({{site.baseurl}}/assets/img/docs/manual-do-usuario/pnp-gestor/conteudos/cadastrar.png)

## O arquivo enviado

O arquivo precisa ser autocontido: tudo o que a página usa — estilos,
scripts, imagens — vai dentro dele. A plataforma confere o arquivo no envio
e recusa, entre outros:

- arquivo vazio ou que não é HTML em UTF-8;
- os elementos `iframe`, `object`, `embed`, `form`, `base`, `link`, `frame`
  e `frameset`;
- vídeo e áudio;
- script vindo de fora do arquivo e redirecionamento por `meta refresh`;
- imagem, estilo ou outro recurso apontando para fora do arquivo — use
  `data:` ou embuta o recurso;
- arquivo idêntico a uma versão que o conteúdo já tem.

Links comuns para fora (`<a href>`) não impedem o envio, mas a plataforma
avisa que eles não vão funcionar. Aprovado na conferência, o arquivo vira
uma versão nova e é publicado na hora; a versão anterior continua guardada.

## Ver o detalhe e as versões

O ícone de detalhe abre a página do conteúdo: os dados gerais, a imagem de
destaque e o **Histórico de Versões**, com a versão atual em destaque e a
tabela de todas as versões — número, nome do arquivo, autor, data,
descrição e o hash do arquivo. O botão **Editar**, no alto, altera o
conteúdo, e **Adicionar Versão** envia um arquivo novo.

Na tabela de versões, o ícone de download baixa o arquivo como foi
enviado, e o ícone de reativar, nas versões que não são a atual, pede
confirmação e coloca aquela versão no ar de novo.

![Detalhe de um conteúdo]({{site.baseurl}}/assets/img/docs/manual-do-usuario/pnp-gestor/conteudos/detalhe.png)

## Excluir um conteúdo

A exclusão, pelo ícone no cartão, pede confirmação e apaga o conteúdo com
todas as versões. Não há como desfazer.
