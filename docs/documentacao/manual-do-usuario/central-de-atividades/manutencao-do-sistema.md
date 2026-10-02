---
layout: default
title: "Manutenção do Sistema"
toc: true
---
# Manutenção do Sistema

Esta é a tela de onde se tira a plataforma do ar para uma manutenção — um
deploy, uma migração do banco — e se devolve a plataforma aos usuários
depois. Ela mostra em que **modo** o sistema está, agenda a janela de
manutenção com o aviso aos usuários e faz as mudanças de modo.

No menu, a tela fica em **Central de Atividades → Manutenção do
Sistema**, e o card de mesmo nome no Painel também leva a ela. É só do
Administrador.

## O estado do sistema

O topo da tela mostra o modo atual, a sequência dos modos de uma
manutenção com o atual marcado, o indicador de deploy, desde quando o
sistema está no modo e o motivo da última mudança. **Histórico de
transições** abre a lista das mudanças de modo já feitas. Abaixo vêm os
indicadores (tarefas ativas, aguardando, pausados, descartes a revisar e
workers ativos), a retomada do trabalho pausado e a lista das **Tarefas em
execução**. A tela se atualiza sozinha a cada 5 segundos.

![Topo da tela com o sistema em NORMAL]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/manutencao-do-sistema/estado.png)

## Os modos

| Modo | Escrita dos usuários | Tarefas novas | Sai para |
|---|---|---|---|
| NORMAL | aceita | começam | DRAINING, KILL_NOW |
| DRAINING | recusada | não começam; ficam guardadas | MAINTENANCE, NORMAL, KILL_NOW |
| MAINTENANCE | recusada | não começam; ficam guardadas | NORMAL, CONTROLLED_RESUME, KILL_NOW |
| CONTROLLED_RESUME | recusada | começam, e o trabalho pausado volta a rodar | NORMAL, DRAINING, KILL_NOW |
| KILL_NOW | recusada | não começam | só MAINTENANCE |

Em **DRAINING** o sistema espera as tarefas em execução terminarem. Os que
passam do prazo e sabem parar param num ponto seguro e ficam guardados
para voltar depois — é o que aparece como *Pausada* no
[Monitoramento de Tarefas]({{site.baseurl}}/documentacao/manual-do-usuario/central-de-atividades/monitoramento-de-tarefas) e no
[Monitoramento de Importações em Lote]({{site.baseurl}}/documentacao/manual-do-usuario/central-de-atividades/monitoramento-de-importacoes-em-lote).
**CONTROLLED_RESUME** põe esse trabalho para rodar de novo com a escrita
ainda fechada, para ele terminar antes de a plataforma voltar aos
usuários. De **KILL_NOW** não se volta direto para NORMAL: passa-se por
MAINTENANCE.

A tabela completa, com o que acontece com o trabalho que já estava
rodando em cada modo, está no fim da tela, em **Como funcionam os
modos**.

## Mudar de modo

O cartão **Ações de controle** mostra só as mudanças possíveis a partir
do modo atual, cada uma com o que ela faz. O **Motivo** é obrigatório
para entrar em DRAINING, CONTROLLED_RESUME e KILL_NOW, e fica registrado
no histórico.

![Ações de controle a partir de NORMAL, com o motivo preenchido]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/manutencao-do-sistema/acoes.png)

- **Iniciar draining** fecha a escrita e a entrada de trabalho novo.
- **Entrar em manutenção** fica disponível quando não há mais tarefas em
  execução. Antes disso, **Forçar entrada em manutenção** pede que você
  confirme, numa caixa de marcação, que as tarefas listadas continuarão
  rodando até terminarem ou pararem.
- **Voltar ao modo NORMAL** reabre a escrita. Com trabalho pausado que
  ainda não voltou a rodar, o botão fica desabilitado e aparece
  **Forçar reabertura**, que pede a confirmação e o motivo.
- **Iniciar retomada controlada** entra em CONTROLLED_RESUME.
- **Pronto para deploy** não é uma ação: diz se o ambiente já pode
  receber o deploy e, se não, por quê.
- **Kill now** manda as tarefas em execução abortarem no próximo ponto
  seguro e leva o sistema a KILL_NOW. A parada depende de cada tarefa
  cooperar; o que não coopera termina o que começou. A confirmação
  exige digitar `KILL NOW`.

## O que os usuários veem

Fora de NORMAL, toda tela da plataforma mostra uma faixa vermelha no
topo, com o texto do modo:

- DRAINING — *Manutenção em andamento. O sistema está em modo
  somente-leitura: nada pode ser salvo agora.*
- MAINTENANCE e KILL_NOW — *Sistema em manutenção. Algumas ações estão
  temporariamente indisponíveis.*
- CONTROLLED_RESUME — *Estamos concluindo o processamento que ficou
  pendente da manutenção. Em instantes o sistema volta a aceitar
  alterações.*

![A faixa que os usuários veem em MAINTENANCE]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/manutencao-do-sistema/banner.png)

Os usuários continuam consultando. O que eles tentarem salvar é
recusado, com uma mensagem que explica a manutenção em andamento.

## Agendar uma janela de manutenção

Sem janela agendada, a tela mostra o formulário **Agendar janela**. No
**Início**, o sistema entra em DRAINING sozinho e espera as tarefas
terminarem. Sair da manutenção continua sendo com você: o **Fim
previsto** é só previsão.

![Formulário de agendamento da janela]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/manutencao-do-sistema/janela.png)

- **Início** e **Motivo** são obrigatórios. O início precisa estar pelo
  menos a antecedência do aviso à frente de agora.
- **Fim previsto**, se informado, precisa ser depois do início.
- **Prazo de drenagem (minutos)** — quanto tempo as tarefas em execução têm
  para terminar depois do início. Vem com 10.
- **Antecedência do aviso (minutos)** — quanto tempo antes do início o
  aviso aparece para os usuários. Vem com 30. O aviso não fecha nada por
  si.
- **Mensagem do aviso** — o texto que os usuários leem no topo da
  plataforma. Sem ela, o aviso diz *Sistema em manutenção.*
- **Motivo** — fica registrado junto da mudança de modo e não aparece
  para os usuários.

Agendada, a janela vira um cartão com a situação dela (*Agendada*,
*Drenando*, *Em manutenção*...). Enquanto está *Agendada*, ela pode ser
editada. **Encerrar** tira a janela de cena: antes do início, cancela o
agendamento; durante a drenagem, deixa escolher entre voltar ao NORMAL e
manter o sistema fechado; em manutenção, marca a janela como concluída
ou cancelada, sem reabrir a escrita.

## Aviso sem janela

**Publicar aviso sem janela** abre **Aviso aos usuários**, para avisar
os usuários sem agendar uma manutenção — uma instabilidade conhecida,
por exemplo. Informe a **Mensagem** e, se quiser, **Início** e **Fim**, e
use **Agendar aviso**. **Desativar aviso** tira o aviso do ar, e
**Recolher** fecha o formulário. O selo ao lado do título diz se o aviso
está *Ativo*, *Agendado* ou se não há aviso agendado.

Enquanto este aviso está no ar, a correção de inconsistências fica
bloqueada. Quando há janela anunciando, o aviso da janela aparece no
lugar deste; e, fora de NORMAL, a faixa do modo aparece no lugar de
qualquer aviso.
