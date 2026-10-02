---
layout: default
title: "Monitoramento de Tarefas"
toc: true
---
# Monitoramento de Tarefas

A plataforma faz boa parte do trabalho pesado em segundo plano: a carga
dos arquivos do SISTEC, a correção em lote de inconsistências, a
validação dos datasets de microdados. Cada execução dessas é uma
**tarefa**. Esta tela mostra todas as tarefas da plataforma, de todos os
usuários, e permite intervir numa tarefa presa ou que falhou.

No menu, a tela fica em **Central de Atividades → Monitoramento de
Tarefas**, e o card de mesmo nome no Painel também leva a ela. É só do
Administrador.

![Faixa de saúde e lista de tarefas]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/monitoramento-de-tarefas/lista.png)

A tela se atualiza sozinha a cada 5 segundos, e mostra a hora da última
atualização. O botão **Pausar atualização** congela a lista e a faixa de
saúde, para ler sem as linhas mudarem de lugar; **Retomar atualização**
volta ao normal. Os filtros e a página ficam no endereço da tela, então
abrir uma tarefa e voltar mantém a lista como estava.

## A situação

A faixa **Situação** resume a saúde das tarefas em *Saudável*, *Atenção*
ou *Crítico*, com a contagem de recursos com falha e de tarefas presas.
Fica em *Atenção* com mais de 5 recursos com falha, mais de 5 tarefas
presas ou taxa
de sucesso abaixo de 90%, e em *Crítico* com mais de 10, mais de 10 ou
abaixo de 80%. A taxa só pesa quando a amostra tem pelo menos 20
recursos.

Se a plataforma não conseguir atualizar a situação, a faixa diz "Não foi
possível atualizar" e mostra a hora dos dados que está exibindo, em vez de
continuar com o último veredito como se fosse atual.

Os indicadores abaixo dela:

- **Taxa de sucesso (por recurso)** — entre os recursos cuja última
  tarefa das últimas 72 horas terminou, quantos terminaram com sucesso. Uma
  falha seguida de um sucesso conta como recuperada.
- **Recursos com falha** — os recursos cuja última tarefa terminou em
  erro.
- **Tarefas ativas** — as que estão na fila ou rodando agora.
- **Presos** — as tarefas rodando que pararam de dar sinal de vida (ver
  abaixo).
- **Taxa de falhas (24h)** e **Taxa de falhas (7 dias)** — a proporção
  das execuções terminadas no período que terminaram em erro; a de 7
  dias traz a curva dia a dia.

## A lista

Cada linha é uma tarefa, da atualizada mais recentemente para a mais
antiga:

- **Recurso** — o que a tarefa processa, pelo tipo e pelo número, como
  *Arquivo de importação em lote #43*.
- **Estágio** — a etapa em que a tarefa está, pelo nome, como
  *Processamento dos dados*, com o identificador (`processar_dados`) logo
  abaixo, em cinza. É o identificador que o filtro **Estágio** aceita.
- **Status** — *Pendente*, *Recebida*, *Iniciada*, *Em progresso*,
  *Repetindo*, *Concluída*, *Falhou*, *Rejeitada*, *Cancelada*,
  *Ignorada* ou *Pausada* (interrompida pela
  [manutenção do sistema]({{site.baseurl}}/documentacao/manual-do-usuario/central-de-atividades/manutencao-do-sistema)).
- **Progresso**, **Mensagem** e **Atualizado em**.

Uma tarefa *Iniciada*, *Em progresso* ou *Repetindo* que passa mais de
30 minutos sem se atualizar ganha a marca **Preso** junto do status, e
a coluna **Atualizado em** passa a mostrar há quanto tempo ela está
parada.

Os **Filtros** buscam pelo **Tipo de recurso** e pelo **Status**,
escolhidos numa lista, e pelo **ID do recurso** e pelo **Estágio**, que
precisam ser escritos por inteiro.

## O detalhe de uma tarefa

O ícone de olho abre a tarefa, com o recurso no título: **Andamento**
(status, estágio e mensagem), **Tarefa** (o recurso, a fila, as
tentativas, as datas e o nome técnico, que identifica o código que a
tarefa roda), a **Linha do tempo** com cada mudança de status e de etapa
e, quando a tarefa terminou em erro, a seção **Erro**, com o tipo, a
mensagem e o rastreamento técnico. No detalhe, o estágio também aparece pelo nome,
como *Importação de Forma de Ingresso*, com o identificador entre parênteses.

![Seção Erro de uma tarefa que falhou]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/monitoramento-de-tarefas/erro.png)

## Intervir numa tarefa

Os botões aparecem no alto do detalhe, conforme o status da tarefa, e todos
pedem confirmação.

**Resetar tarefa** aparece nas tarefas ativas — *Pendente*, *Recebida*,
*Iniciada*, *Em progresso* e *Repetindo*. O reset revoga a tarefa e
devolve o recurso a um estado em que pode ser processado de novo. Se a
tarefa ainda dá sinal de vida, o reset não faz nada, a menos que você
marque **Forçar**; marque só quando souber que o processo que rodava a
tarefa parou.

![Confirmação do reset, com a opção de forçar]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/monitoramento-de-tarefas/resetar.png)

**Cancelar tarefa** aparece nas tarefas *Pendente*, *Iniciada* e *Em
progresso*. O processamento para no próximo ponto de verificação, e o
recurso volta a um estado em que pode ser processado de novo. O
cancelamento não pode ser desfeito.

**Reprocessar** aparece nas tarefas *Falhou* e *Cancelada*. A confirmação
explica que o reprocessamento põe na fila, de novo, a mesma tarefa com
os argumentos originais.
