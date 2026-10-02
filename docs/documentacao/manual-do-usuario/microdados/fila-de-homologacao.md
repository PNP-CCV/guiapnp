---
layout: default
title: "Fila de Homologação"
toc: true
---
# Fila de Homologação

A homologação é o primeiro dos dois passos de aprovação de um dataset: o
Gestor de Área Temática confere o que chegou da sua área e homologa ou
rejeita. O que ele homologa segue para a
[Aprovação de Microdados]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/aprovacao-de-microdados), do Reitor.

No menu, esta tela aparece só para o perfil Gestor de Área Temática, em
**Microdados → Fila de Homologação**.

## Ver a fila

A fila mostra os datasets com status Disponível — aprovados na validação
automática — da instituição e da área temática do seu perfil. Datasets de
outras áreas ou de outras instituições não aparecem. Para cada um, a
tabela traz a instituição, o contrato, o modelo, o status, o número de
linhas e quando foi recebido. Na coluna **Ação**, da esquerda para a
direita: pré-visualizar, homologar e rejeitar.

![Fila de homologação]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/fila-de-homologacao/fila.png)

## Pré-visualizar o conteúdo

O ícone de olho abre a pré-visualização do dataset: as linhas do arquivo
recebido numa tabela, 50 por página, para conferir antes de decidir.

![Pré-visualização de um dataset da fila]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/fila-de-homologacao/pre-visualizacao.png)

## Homologar

O ícone de confirmação pede uma confirmação e, ao homologar, o dataset
passa a **Homologado pela área** e sai desta fila para a do Reitor.

![Confirmação da homologação]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/fila-de-homologacao/homologar.png)

## Rejeitar

O ícone de rejeição abre um campo de **Justificativa**, obrigatório, com
até 500 caracteres. Ao rejeitar, o dataset passa a **Rejeitado pela
área** e sai da fila. A justificativa fica registrada no dataset — o
Gestor CCV a vê no detalhe, em
[Datasets de Microdados]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/datasets-de-microdados) — e é devolvida ao
extrator da instituição.

![Rejeição de um dataset, com a justificativa]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/fila-de-homologacao/rejeitar.png)

## Depois da decisão

Não há como desfazer uma homologação ou uma rejeição pela tela. O que
muda o quadro é a instituição enviar uma extração mais nova do mesmo
recorte: quando ela passa na validação, substitui a anterior — inclusive
uma já homologada — e volta para esta fila (ver
[o caminho de um dataset]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/datasets-de-microdados#o-caminho-de-um-dataset)).
Pelo mesmo motivo, se um dataset for substituído enquanto está na fila, a
plataforma recusa a decisão sobre ele com uma mensagem que diz o status
atual do dataset — por exemplo, "Dataset não está disponível para
homologação (status atual: Substituído)." — e recarrega a fila, já sem ele.
