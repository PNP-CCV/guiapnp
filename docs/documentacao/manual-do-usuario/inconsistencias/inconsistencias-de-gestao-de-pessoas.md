---
layout: default
title: "Inconsistências de Gestão de Pessoas"
toc: true
---
# Inconsistências de Gestão de Pessoas

A plataforma também confere os dados de pessoal da instituição: as
unidades organizacionais (UORGs) e os servidores lotados nelas. O que foge
das regras vira uma **inconsistência**, e esta é a tela onde elas são
corrigidas, justificadas e concluídas. O funcionamento é o mesmo das
[Inconsistências de Ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino), com outras
etapas e outros perfis.

No menu, a tela fica em **Inconsistências → Inconsistências de Gestão de
Pessoas** e aparece para Gestão de Pessoas, Recursos Humanos, Reitor,
Gestor CCV e Suporte CCV. O Gestor CCV e o Suporte CCV só consultam.

## Quando a tela abre

A tela só abre durante o **período de correção** e fora de manutenção do
sistema. Gestão de Pessoas e Recursos Humanos precisam, além disso, ter
concluído a capacitação; o Reitor é dispensado dela. Fora dessas
condições, quem tenta abrir a tela volta ao Painel.

## O caminho de uma inconsistência {#o-caminho-de-uma-inconsistencia}

Aqui a correção tem duas etapas, sem o Pesquisador Institucional:

1. **Gestão de Pessoas** ou **Recursos Humanos** corrige ou justifica. A
   inconsistência vai de *Inconsistente GP* para *Alterado GP*. Só o
   Gestão de Pessoas conclui: a linha vai para *Validado GP* e passa ao
   Reitor.
2. **Reitor** confere e conclui (*Validado RE*). A conclusão do Reitor é
   definitiva.

Nesta tela não há devolução nem exclusão de linhas pela tabela. Gestão
de Pessoas, Recursos Humanos e Reitor veem as UORGs e os servidores da
instituição inteira, sem seletor de unidade; o Gestor CCV e o Suporte CCV
veem os da rede.

![A tela, na aba Unidades Organizacionais, com os filtros]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas/tela.png)

As cores seguem as da tela de Ensino: vermelho para *Inconsistente*,
amarelo para *Alterado*, verde para *Validado*, na coluna **Situação do
Cadastro** e na célula que tem a inconsistência.

## Unidades Organizacionais

A primeira aba lista as UORGs com a inconsistência **UORG não
Vinculada**: a UORG ainda não está ligada a nenhuma unidade da
instituição. Os filtros são tipo de inconsistência, código da UORG,
unidade, situação do cadastro e situação da inconsistência.

![Aba Unidades Organizacionais: uma UORG em cada situação]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas/unidades-organizacionais.png)

Para corrigir, clique na célula vermelha da coluna **Unidade** e escolha a
unidade, obrigatória, entre as da sua instituição. Fora das instituições
ETV, os servidores lotados na UORG passam para a mesma unidade.

![Vínculo de uma UORG a uma unidade]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas/vincular-unidade.png)

Quando o Gestão de Pessoas conclui UORGs, a plataforma gera em segundo
plano as inconsistências de servidor da unidade vinculada. Elas aparecem
na aba **Servidores**.

## Servidores

A segunda aba lista os servidores com inconsistência, com matrícula, dados
pessoais, lotação, escolaridade, titulação, RSC, cargo e jornada. Os
filtros são tipo de inconsistência, código da UORG, servidor (nome,
matrícula ou CPF), unidade, situação do cadastro e situação da
inconsistência.

![Aba Servidores]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas/servidores.png)

Clicar na célula colorida abre a janela do tipo de inconsistência. Todas
as janelas têm o **Histórico** das alterações; o resto depende do tipo:

| Tipo | Na janela |
|---|---|
| Divergência entre Cargo, Escolaridade e Titulação | Corrigir |
| Cargo sem Descrição | Corrigir |
| Docente Lotado em Reitoria | Corrigir ou justificar |
| Duplicidade de Lotação | Justificar ou excluir o servidor |

Um servidor excluído continua na tabela, e o botão de restaurar da coluna
**Ação** desfaz a exclusão, pelas mesmas regras de quem restaura descritas
abaixo.

## Desfazer uma correção

Clicar numa célula que não está em *Inconsistente* na sua etapa abre a
janela da inconsistência com o **Histórico**. Quando a situação está na
sua vez, a janela traz também **Restaurar Inconsistência**, que desfaz as
alterações:

| Situação da inconsistência | Quem restaura | Volta a |
|---|---|---|
| Alterado GP | Gestão de Pessoas | Inconsistente GP |
| Validado GP, Alterado RE | Reitor | Inconsistente RE |

Assim, o Reitor reabre o que o Gestão de Pessoas concluiu para ele mesmo
corrigir.

## Concluir

Marque as linhas prontas e use **Concluir** no topo da tabela. A janela
pede a confirmação e avisa que a conclusão não pode ser desfeita pela
própria etapa.

![Conclusão de uma UORG pelo Gestão de Pessoas]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas/concluir.png)

| Perfil | Conclui linhas em | A linha passa a |
|---|---|---|
| Gestão de Pessoas | Alterado GP | Validado GP |
| Reitor | Validado GP, Alterado RE | Validado RE |

Os botões **Concluir Todas as Unidades Organizacionais** e **Concluir
Todos os Servidores** concluem de uma vez todas as linhas da aba que estão
na sua vez, **sem levar em conta os filtros** aplicados. Em instituição
ETV, a aba Unidades Organizacionais é diferente: o Gestão de Pessoas vê
**Informar Servidores** no lugar de Concluir Todas as Unidades
Organizacionais, e o Reitor não tem botão de concluir todas nessa aba.
