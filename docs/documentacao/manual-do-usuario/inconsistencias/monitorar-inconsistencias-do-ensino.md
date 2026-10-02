---
layout: default
title: "Monitorar Inconsistências do Ensino"
toc: true
---
# Monitorar Inconsistências do Ensino

Esta tela acompanha o andamento da correção das
[inconsistências de ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino): quantas estão em
cada etapa, por instituição, por unidade e por tipo de inconsistência. Ela só
mostra números. A correção, a conclusão e a devolução são feitas na tela
Inconsistências de Ensino.

No menu, a tela fica em **Inconsistências → Monitorar Inconsistências do
Ensino**, e o card de mesmo nome no Painel também leva a ela. Aparece para
Registrador Acadêmico, Executor Acadêmico, Pesquisador Institucional,
Reitor, Administrador, Gestor CCV e Suporte CCV.

## Quando a tela abre

O Administrador, o Gestor CCV e o Suporte CCV acompanham a rede a qualquer
momento. Para os demais perfis, a tela segue a mesma regra da correção:
só abre durante o **período de correção** e fora de manutenção do sistema.
Registrador Acadêmico, Executor Acadêmico e Pesquisador Institucional
precisam, além disso, ter concluído a capacitação. O Reitor é dispensado
dela. Fora dessas condições, o card do Painel fica desabilitado, e quem
tenta abrir a tela volta ao Painel.

## Os três níveis

A tela tem três níveis, um dentro do outro:

- **a rede**, com uma linha por instituição;
- **a instituição**, com uma linha por unidade;
- **a unidade**, com uma linha por tipo de inconsistência.

Cada perfil começa no nível do seu alcance. O Administrador, o Gestor CCV e
o Suporte CCV começam na rede. O Pesquisador Institucional e o Reitor
começam na própria instituição. O Registrador Acadêmico e o Executor
Acadêmico, na própria unidade.

Para descer um nível, use o ícone de olho (**Visualizar**) na coluna
**Ação** da linha. O caminho no topo da página volta aos níveis de cima,
para quem tem alcance sobre eles.

![A tela na visão da rede, com os totais por etapa e o filtro]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/monitorar-inconsistencias-do-ensino/tela.png)

## Os totais por etapa

Os três quadros no alto da página somam as inconsistências do nível
aberto, uma para cada etapa da correção:

- **Total Inconsistências RA** — a etapa do Registrador Acadêmico;
- **Total Inconsistências PI** — a etapa do Pesquisador Institucional;
- **Total Inconsistências RE** — a etapa do Reitor.

Cada quadro mostra quantas estão *Inconsistente*, *Alterado* e *Validado*
naquela etapa. As situações são as da tela de correção, explicadas em
[O caminho de uma inconsistência]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino#o-caminho-de-uma-inconsistencia).
O número é a situação de agora: quando o Pesquisador Institucional
conclui uma linha, ela sai de *Validado RA* e passa a contar em
*Validado PI*. Inconsistências de linhas excluídas não entram na conta.

## Abas e filtro

As abas **Tudo**, **Cursos**, **Ciclos** e **Matrículas** separam as
inconsistências pelo que elas marcam. O número abaixo de cada aba é a
quantidade de linhas da tabela, isto é, de instituições, unidades ou tipos
que têm inconsistência naquela aba. Não é a quantidade de inconsistências.

Na rede, o filtro é por **Instituição**. Na instituição, é por **Unidade**.
A unidade não tem filtro.

## A tabela

A tabela tem uma coluna para cada situação, de *Inconsistente RA* a
*Validado RE*, e o **Total de Inconsistências** da linha. A coluna com o
nome da instituição, da unidade ou do tipo de inconsistência fica no fim,
ao lado de **Ação**. Só aparecem as linhas que têm pelo menos uma
inconsistência.

Na rede, uma linha por instituição:

![Inconsistências por instituição, na visão da rede]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/monitorar-inconsistencias-do-ensino/rede.png)

Na instituição, uma linha por unidade:

![Inconsistências por unidade de uma instituição]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/monitorar-inconsistencias-do-ensino/instituicao.png)

Na unidade, uma linha por tipo de inconsistência. Aqui não há coluna
**Ação**, porque este é o último nível.

![Inconsistências por tipo, dentro de uma unidade]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/monitorar-inconsistencias-do-ensino/unidade.png)
