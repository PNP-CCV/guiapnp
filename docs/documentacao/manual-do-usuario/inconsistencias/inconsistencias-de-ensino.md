---
layout: default
title: "Inconsistências de Ensino"
toc: true
---
# Inconsistências de Ensino

Depois de cada carga, a plataforma confere os cursos, ciclos e matrículas
de cada unidade e marca o que foge das regras — um curso sem código
e-MEC, um ciclo com carga horária insuficiente, uma matrícula sem
cor/raça. Cada marca é uma **inconsistência**, e esta é a tela onde elas
são corrigidas, justificadas e concluídas.

No menu, a tela fica em **Inconsistências → Inconsistências de Ensino** e
aparece para Registrador Acadêmico, Executor Acadêmico, Pesquisador
Institucional, Reitor, Gestor CCV e Suporte CCV. O ícone de setas no topo
da página, ao lado das mensagens, também leva a ela: ele lista as
devoluções ainda não lidas, e cada uma abre a tela já na aba do que foi
devolvido, filtrada pelas linhas devolvidas.

O Gestor CCV e o Suporte CCV só consultam: veem as inconsistências, mas
não corrigem, não concluem, não devolvem e não excluem linhas.

## Quando a tela abre

A tela só abre durante o **período de correção** e fora de manutenção do
sistema. Registrador Acadêmico, Executor Acadêmico e Pesquisador
Institucional precisam, além disso, ter concluído a capacitação; o Reitor
é dispensado dela. Fora dessas condições, quem tenta abrir a tela volta
ao Painel.

## O caminho de uma inconsistência {#o-caminho-de-uma-inconsistencia}

A correção passa por três etapas, sempre dentro da instituição:

1. **Registrador Acadêmico** (ou Executor Acadêmico) da unidade corrige
   ou justifica. A inconsistência vai de *Inconsistente RA* para
   *Alterado RA*. Ao concluir, vai para *Validado RA* e passa ao
   Pesquisador Institucional.
2. **Pesquisador Institucional** confere o que o registrador concluiu.
   Pode concluir (*Validado PI*), devolver ao registrador ou reabrir a
   correção para ele mesmo corrigir.
3. **Reitor** confere o que o pesquisador concluiu e conclui
   (*Validado RE*). A conclusão do Reitor é definitiva e encerra o ciclo
   de correções daquela linha.

Só o Registrador Acadêmico conclui na primeira etapa: o Executor
Acadêmico corrige e justifica, mas não conclui.

Cada linha da tabela mostra, na coluna **Situação do Cadastro**, em que
ponto desse caminho ela está. A cor acompanha a situação: vermelho para
*Inconsistente*, amarelo para *Alterado*, verde para *Validado*. A mesma
cor pinta a célula exata que tem a inconsistência.

## Escolher a unidade

O Registrador Acadêmico e o Executor Acadêmico veem direto as
inconsistências da sua unidade. O Pesquisador Institucional e o Reitor
enxergam a instituição inteira e, por isso, escolhem antes a unidade no
seletor ao lado das abas; até escolher, a tela mostra só o aviso.

![Seletor de unidade, para quem vê a instituição inteira]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-ensino/selecionar-unidade.png)

## Abas e filtros

A tela tem três abas — **Cursos**, **Ciclos** e **Matrículas** — e cada
uma mostra, abaixo do título, quantas linhas com inconsistência tem. Os
filtros ficam no topo de cada aba. Todas filtram por tipo de
inconsistência, curso, tipo e modalidade do curso, situação do cadastro,
situação da inconsistência e se a linha foi devolvida; Ciclos e Matrículas
filtram também pelo ciclo e pelo tipo de oferta, e Matrículas, pelo aluno
(matrícula, CPF, código ou nome).

![A tela, na aba Cursos, com os filtros]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-ensino/tela.png)

Os tipos de inconsistência de cada aba:

| Aba | Tipos |
|---|---|
| Cursos | Associação ao Catálogo, Nome do Curso, Código E-MEC, Formação de Professores |
| Ciclos | Evasão 0%, Carga Horária Insuficiente, Programas Associados, Duração do Ciclo, Número de vagas, Ingressantes > Inscritos, Turno de Oferta do Ciclo, Habilitação Ciclo |
| Matrículas | Matrícula Anterior, Matrícula Posterior, Aluno Duplicado, Retenção Crítica, Retenção FIC, Cor/Raça, Renda, Turno do Aluno, Habilitação Matrícula, Forma de Ingresso, Identidade de Gênero, Tipo de Deficiência, Necessidade Educacional Específica |

Na tabela, a coluna **Ação** tem dois botões por linha: restaurar uma
linha excluída (apagado enquanto a linha não foi excluída) e o histórico
de devoluções. Quando a linha foi devolvida, o botão do histórico pisca,
e clicar nele mostra a justificativa de quem devolveu.

![Tabela da aba Cursos: uma linha em cada situação]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-ensino/cursos.png)

## Corrigir uma inconsistência {#corrigir-uma-inconsistencia}

Clique na célula colorida. Se a inconsistência está na sua etapa —
*Inconsistente RA* para o registrador, *Inconsistente PI* para o
pesquisador, *Inconsistente RE* para o Reitor —, abre a janela daquele
tipo de inconsistência. O conteúdo varia com o tipo; as partes possíveis
são:

- **Corrigir Inconsistência** — informar o valor certo daquela linha;
- **Corrigir Inconsistência em Lote** — baixar um arquivo modelo em XLSX,
  preencher e enviar de volta, para corrigir várias linhas de uma vez;
- **Justificar Inconsistência** — escolher uma justificativa da lista,
  quando o dado está certo apesar da regra;
- **Excluir** o curso, ciclo ou matrícula, quando a linha não deveria
  existir;
- **Histórico** — as alterações já feitas naquela inconsistência.

Nem todo tipo tem todas as partes: Nome do Curso, por exemplo, só se
justifica ou exclui. Corrigida ou justificada, a inconsistência passa a
*Alterado* na sua etapa.

![Correção de uma inconsistência de Código e-MEC]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-ensino/corrigir.png)

No Código e-MEC, o campo é obrigatório e aceita só números, de 4 a 9
dígitos.

## Desfazer uma correção

Clicar numa célula que não está em *Inconsistente* na sua etapa abre a
janela da inconsistência com o **Histórico** das alterações. Quando a
situação está na sua vez, a janela traz também **Restaurar
Inconsistência**, que desfaz as alterações e devolve a inconsistência à
situação *Inconsistente*. A plataforma só aceita a restauração de quem
está na vez daquela situação:

| Situação da inconsistência | Quem restaura | Volta a |
|---|---|---|
| Alterado RA | Registrador Acadêmico, Executor Acadêmico | Inconsistente RA |
| Validado RA, Alterado PI | Pesquisador Institucional | Inconsistente PI |
| Validado PI, Alterado RE | Reitor | Inconsistente RE |

Assim, o Pesquisador Institucional reabre o que o registrador concluiu
para ele mesmo corrigir, e o Reitor, o que o pesquisador concluiu.

## Concluir

Marque as linhas prontas e use **Concluir** no topo da tabela. A janela
pede a confirmação e diz para onde a linha vai depois. A conclusão vale
para a linha inteira: todas as inconsistências dela passam a *Validado*
na sua etapa.

![Conclusão de um curso pelo Registrador Acadêmico]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-ensino/concluir.png)

Cada perfil conclui as linhas que estão na sua vez:

| Perfil | Conclui linhas em | A linha passa a |
|---|---|---|
| Registrador Acadêmico | Alterado RA | Validado RA |
| Pesquisador Institucional | Validado RA, Alterado PI | Validado PI |
| Reitor | Validado PI, Alterado RE | Validado RE |

O botão **Concluir Todos** conclui de uma vez todas as linhas da unidade
que estão na sua vez, **sem levar em conta os filtros** aplicados na aba.

## Devolver

O Pesquisador Institucional pode devolver ao registrador as linhas que
estão na vez dele — *Validado RA* ou *Alterado PI*. Marque as linhas, use
**Devolver** e escreva a justificativa, obrigatória e com até 500
caracteres. A linha volta a
*Alterado RA*, marcada como devolvida, e o Registrador Acadêmico da
unidade recebe a devolução pelo ícone de setas no topo da página.

![Devolução de um curso pelo Pesquisador Institucional]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/inconsistencias-de-ensino/devolver.png)

## Excluir linhas

O Registrador Acadêmico e o Pesquisador Institucional também excluem
linhas inteiras pela tabela: marque as linhas e use **Excluir**. O
registrador exclui o que ainda está na etapa dele (*Inconsistente RA* ou
*Alterado RA*); o pesquisador, o que está na dele (*Inconsistente PI* ou
*Alterado PI*). A linha excluída continua na tabela, e o botão de
restaurar, na coluna **Ação**, desfaz a exclusão.
