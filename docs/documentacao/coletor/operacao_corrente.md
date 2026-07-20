---
layout: default
title: "Operação corrente"
toc: true
---

# Operação corrente

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página descreve a rotina diária do operador do Coletor — o que acompanhar, quando re-extrair, quando re-sincronizar e quais antipadrões evitar. Para o pano de fundo do calendário e do fluxo, leia antes [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta) e [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio).

## Rotina diária do operador

- Abrir o painel do Coletor e olhar a lista de **Contratos de Dados** do **[Ciclo de Coleta](/documentacao/coletor/glossario#ciclo-de-coleta)** ativo.
- Conferir os contratos que não estão em "Sincronizado com Sucesso" e ler o badge de status de cada um.
- Re-disparar extrações dos **Modelos** que estão com falha, depois de checar o motivo do erro. Lembre que o teste de qualidade roda **dentro** da extração — não há passo separado para executá-lo.
- Enviar à **[PNP](/documentacao/coletor/glossario#pnp)** os contratos em "Pronto para Sincronizar".
- Nos contratos já enviados, acompanhar o estado da validação **do lado da PNP** — o Coletor só espelha, não avança.

## Extração manual vs agendada

Na prática, **hoje toda extração é manual** — disparada pelo operador, no botão "Extrair Dados" do contrato ou do modelo, ou em "Extrair todos". As tarefas agendadas que o sistema mantém (visíveis em **Tarefas Agendadas**) cuidam de rotinas internas — como a verificação periódica da validação na PNP — e **nenhuma delas extrai dados**.

| Critério | Extração manual |
|---|---|
| Quando usar | Sempre — é o único caminho disponível |
| Como disparar | Botão "Extrair Dados" no contrato ou no modelo, ou "Extrair todos" |
| Tipo registrado | `Manual` |

## Como acompanhar uma extração

A execução de cada extração ocorre em background, então o navegador não trava. Para acompanhar o andamento, o operador tem dois pontos de observação principais: a lista de **Extrações** (`/painel/extracoes/`), que registra cada execução com início, fim, status, motivo do erro e detalhes técnicos; e o badge de status do contrato, que se reposiciona conforme novas extrações e testes são processados. Para extrações grandes, espere até alguns minutos antes de concluir que algo travou.

## Quando re-extrair

- O **[Provedor de Dados](/documentacao/coletor/glossario#provedor-de-dados)** mudou (novo endpoint, nova credencial, mudança de host do banco).
- A **[Configuração de Extração](/documentacao/coletor/glossario#configuracao-de-extracao)** foi alterada (query SQL diferente, nova aba de planilha).
- O **[Modelo de Dados](/documentacao/coletor/glossario#modelo-de-dados)** foi atualizado e o sistema marcou o contrato como "Reextração Necessária".
- O teste do contrato falhou e o problema foi corrigido na origem.
- O contrato evoluiu para uma nova versão com schema ajustado.

A máquina de status, com todas as transições possíveis, está descrita em [Status do contrato](/documentacao/coletor/status_do_contrato).

## Quando re-sincronizar

- A última **[Sincronização](/documentacao/coletor/glossario#sincronizacao)** falhou por instabilidade da PNP ou da rede.
- Dados foram corrigidos durante o **[Período de Correção](/documentacao/coletor/glossario#periodo-de-correcao)** e precisam reentrar na consolidação.
- O contrato foi sincronizado em ciclo anterior e precisa ser reenviado por solicitação do **[MEC](/documentacao/coletor/glossario#mec)** dentro da janela atual.

## O que NÃO fazer

- Não disparar dezenas de extrações simultâneas no mesmo minuto. O número de tarefas em paralelo é limitado, e a fila atrasa as demais operações da instituição.
- Não editar um Contrato enquanto há extração em curso para ele. A extração pode terminar contra um schema antigo e produzir um Parquet que o teste rejeita.
- Não concluir que algo travou só porque o badge não mudou no primeiro minuto. O status é calculado em tempo real a cada renderização e a tela se atualiza sozinha (10 s no contrato, 120 s no wizard do dashboard) — não é preciso dar refresh manual.

> 💡 **Dica.** Mantenha um print da lista de contratos do dia anterior. Comparar a foto de ontem com a de hoje é a forma mais rápida de detectar regressões silenciosas (um contrato que voltou para "Reextração Necessária" sem aviso).

## Veja também

- [Status do contrato](/documentacao/coletor/status_do_contrato)
- [Quando algo falha](/documentacao/coletor/quando_algo_falha)
- [Perguntas frequentes](/documentacao/coletor/faq)
