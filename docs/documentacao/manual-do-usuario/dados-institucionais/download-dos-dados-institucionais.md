---
layout: default
title: "Download dos Dados Institucionais"
toc: true
---
# Download dos Dados Institucionais

A tela reúne os arquivos que a plataforma gera para cada instituição —
dados de ensino, dados de servidores e relatórios, como o de
inconsistências e os de matrículas atendidas e ingressantes —, em pastas
por instituição e por ano-base. É daqui que se baixam esses arquivos.

No menu, a tela fica em **Dados Institucionais → Download dos Dados
Institucionais** e aparece para Reitor, Pesquisador Institucional,
Gestor CCV, Suporte CCV e Administrador. No Painel, o card que leva a ela
se chama **Download de Arquivos Institucionais**, para os mesmos perfis;
a página abre com o título **Arquivos Institucionais**. A tela é de
consulta e download: nenhum perfil cadastra, edita ou exclui arquivos por
ela.

## O que cada perfil vê

- **Administrador** e **Gestor CCV** veem as pastas de todas as
  instituições e os arquivos em qualquer situação;
- **Reitor** e **Pesquisador Institucional** vão direto para a pasta da
  sua instituição e veem só os arquivos publicados;
- **Suporte CCV** não tem instituição no papel, e a tela mostra o aviso
  "Sem instituição ativa.": para ver os arquivos de uma instituição, é
  preciso trocar para um papel vinculado a ela.

## Ver as pastas

Para o Administrador e o Gestor CCV, a tela abre com as **Pastas
Institucionais**, uma por instituição. Cada pasta mostra a sigla, até
quatro anos-base com arquivos (os mais recentes; os demais aparecem como
"+N"), o nome da instituição e o número de itens. O botão de visualizar
abre a pasta.

A **Busca** procura pela sigla, pelo nome da instituição ou pelo ano. Os
dois botões no alto da lista alternam entre a visualização em lista e em
grade.

![Pastas institucionais, uma por instituição]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/download-dos-dados-institucionais/pastas.png)

## Ver os arquivos de uma pasta

Dentro da pasta, os botões de ano escolhem o ano-base; a pasta abre no
mais recente. Cada arquivo mostra o formato, o tipo, o ano, o tamanho, a
situação, o nome e a data de envio. O botão **i** mostra a descrição do
arquivo.

O bloco **Filtros** filtra por **Tipo** e por **Formato** (CSV, XLSX,
PDF, PARQUET ou ZIP). A **Busca** procura pelo código do tipo, do
formato ou da situação — `csv` ou `publicado`, por exemplo —, não pelo
nome do arquivo.

![Arquivos de uma instituição no ano-base 2025, vistos pelo Administrador]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/download-dos-dados-institucionais/arquivos.png)

## A situação de um arquivo

A legenda acima da lista mostra as quatro situações:

- **Gerando**: a plataforma ainda está produzindo o arquivo;
- **Publicado**: o arquivo está disponível para download;
- **Erro**: a geração falhou;
- **Substituído**: uma versão mais nova foi publicada no lugar dele.

Para cada instituição, ano-base, tipo e formato, só um arquivo fica
publicado: ao publicar uma versão nova, a anterior passa a
*Substituído*.

## Baixar um arquivo

O botão de download aparece só nos arquivos **publicados**; os de outra
situação não podem ser baixados.

O Reitor e o Pesquisador Institucional abrem a tela já na pasta da sua
instituição, só com os arquivos publicados.

![Pasta da própria instituição, vista pelo Reitor: só os arquivos publicados]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/download-dos-dados-institucionais/reitor.png)
