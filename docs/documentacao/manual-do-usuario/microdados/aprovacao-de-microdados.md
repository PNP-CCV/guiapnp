---
layout: default
title: "Aprovação de Microdados"
toc: true
---
# Aprovação de Microdados

A aprovação do Reitor é o segundo e último passo de um dataset: depois que
o Gestor de Área Temática o homologa (ver
[Fila de Homologação]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/fila-de-homologacao)), o Reitor da instituição
dá a aprovação final.

No menu, esta tela aparece só para o perfil Reitor, em **Microdados →
Aprovação de Microdados**.

## Ver a fila

A fila mostra os datasets com status Homologado pela área da instituição
do seu perfil, de todas as áreas temáticas. Para cada um, a tabela traz a
instituição, o contrato, o modelo, o status, o número de linhas e quando
foi recebido.

![Fila de aprovação de microdados]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/aprovacao-de-microdados/fila.png)

## Aprovar

A única ação é aprovar: não há rejeição neste passo. O ícone de
confirmação, na coluna **Ação**, pede uma confirmação e, ao aprovar, o
dataset passa a **Aprovado pelo Reitor** e sai da fila.

![Confirmação da aprovação]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/aprovacao-de-microdados/aprovar.png)

Não há como desfazer a aprovação pela tela. Se a instituição enviar uma
extração mais nova do mesmo recorte e ela passar na validação, a versão
nova substitui a aprovada e recomeça o caminho pela homologação da área
(ver [o caminho de um dataset]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/datasets-de-microdados#o-caminho-de-um-dataset)).
Um dataset substituído enquanto está na fila não pode mais ser aprovado: a
plataforma recusa com uma mensagem que diz o status atual do dataset — por
exemplo, "Dataset não está homologado pela área para aprovação (status:
Substituído)." — e recarrega a fila, já sem ele.
