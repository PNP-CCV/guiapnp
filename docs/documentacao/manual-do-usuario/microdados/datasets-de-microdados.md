---
layout: default
title: "Datasets de Microdados"
toc: true
---
# Datasets de Microdados

O dataset é o arquivo de microdados (no formato Parquet) que o extrator de
uma instituição envia para um modelo de um contrato de dados. Ninguém
cadastra datasets por esta tela: eles chegam pelo extrator e, ao chegar,
são validados automaticamente contra o schema do contrato. Esta tela
acompanha o que chegou, de todas as instituições.

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV — os três consultam, pré-visualizam e baixam os arquivos.
Excluir um dataset é só do Administrador e do Gestor CCV.

## O caminho de um dataset {#o-caminho-de-um-dataset}

| Status | O que significa |
|---|---|
| Recebido | chegou e aguarda a validação |
| Validando | a validação está em andamento |
| Erro | a validação não passou — por exemplo, faltam colunas obrigatórias do schema, ou algum valor não confere com o cadastro da PNP; o motivo aparece no detalhe, em **Detalhe do Erro** |
| Disponível | aprovado na validação; aguarda a [homologação da área]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/fila-de-homologacao) |
| Rejeitado pela área | o Gestor de Área Temática rejeitou; a justificativa aparece no detalhe, em **Justificativa da Rejeição**, e também é devolvida ao extrator da instituição |
| Homologado pela área | o Gestor de Área Temática homologou; aguarda a [aprovação do Reitor]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/aprovacao-de-microdados) |
| Aprovado pelo Reitor | aprovação final |
| Substituído | uma extração mais nova do mesmo recorte passou na validação e tomou o lugar desta |

O **recorte** é a combinação de contrato, modelo, instituição e ciclo.
Cada recorte tem no máximo uma versão Disponível, Homologada pela área ou
Aprovada pelo Reitor. Quando uma extração mais nova do mesmo recorte passa
na validação, ela substitui a anterior — mesmo que a anterior já tenha sido
homologada ou aprovada — e o caminho recomeça: a versão nova volta para a
fila de homologação.

## Ver os datasets recebidos

Em **Microdados → Datasets de Microdados**, a plataforma lista os datasets
recebidos, com a instituição, o contrato (cujo nome já traz o ano do
ciclo), o modelo, o status, o número de linhas e quando cada um foi
recebido. O bloco **Filtros** permite buscar por modelo ou contrato e
filtrar por instituição, contrato, modelo, status e ciclo.

A coluna **Ação**, no fim de cada linha, traz o detalhe e a exclusão.

![Listagem de datasets de microdados]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/datasets-de-microdados/lista.png)

## Ver um dataset

O detalhe mostra os dados do envio — instituição, contrato, modelo,
status, linhas, tamanho, versão do contrato, data da extração, data de
recebimento e o checksum do arquivo — e tem três partes:

- **Baixar Parquet**, no alto, baixa o arquivo recebido.
- **Conteúdo**: o botão **Carregar pré-visualização** mostra as linhas do
  arquivo numa tabela, 50 por página, com **Anterior** e **Próxima**
  quando há mais de uma página.
- **Validação (tarefa assíncrona)**: o andamento da validação automática —
  o status da tarefa, o estágio, pelo nome da etapa, e a mensagem final.

![Detalhe de um dataset, com o conteúdo carregado]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/datasets-de-microdados/detalhe.png)

## Excluir um dataset

A exclusão apaga o registro e o arquivo, e não pode ser desfeita. O
recorte fica sem versão disponível: a versão Substituída anterior **não**
volta a valer, e a única forma de recuperar é a instituição enviar de novo
pelo extrator. Um dataset em validação (status Validando) não pode ser
excluído: a plataforma recusa com a mensagem "Dataset em validação não pode
ser apagado (aguarde o fim da validação)." — aguarde o fim da validação.
