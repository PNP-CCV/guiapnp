---
layout: default
title: "Monitoramento de Importações em Lote"
toc: true
---
# Monitoramento de Importações em Lote

Esta tela acompanha os arquivos que você enviou para correção em lote de
inconsistências — a planilha de **Corrigir Inconsistência em Lote**, das
[inconsistências de ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino#corrigir-uma-inconsistencia),
por exemplo. A plataforma processa esses arquivos em segundo plano, e é
aqui que se vê em que pé cada um está. Cada pessoa vê só os arquivos que
ela mesma enviou.

No menu, a tela fica em **Central de Atividades → Monitoramento de
Importações em Lote**, para Administrador, Gestor CCV, Suporte CCV,
Reitor, Pesquisador Institucional, Registrador Acadêmico e Executor
Acadêmico. Gestão de Pessoas e Recursos Humanos não a têm no menu: chegam
a ela pelo card **Monitoramento de Importações em Lote** do Painel, que
aparece também para os perfis acima.

![Arquivos em cada estado do processamento]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/monitoramento-de-importacoes-em-lote/lista.png)

## A tabela

Cada linha é um arquivo enviado, do mais recente para o mais antigo:

- **Estado da tarefa** — *Em progresso*, *Concluída com sucesso*,
  *Concluída com pendências*, *Concluída com erro* ou *Pausada para
  manutenção*.
- **Progresso** — o percentual já processado.
- **Nome da tarefa** — o tipo de correção, como *Importação de Forma
  Ingresso*.
- **Mensagem** — o andamento contado pela plataforma. Quando o arquivo
  falha, aparece *Erro no processamento do arquivo*.
- **Nome do Arquivo** — o nome do arquivo enviado.

O filtro **Status** mostra só os arquivos *Em progresso*, *Concluída com
sucesso*, *Concluída com erro* ou *Pausada para manutenção*. Use
**Filtrar** para aplicar.

## O arquivo de retorno

Quando o processamento deixa linhas sem corrigir, a plataforma gera um
arquivo de retorno: uma planilha com essas linhas e uma coluna
**Motivo** para cada uma. O ícone de download, na coluna **Ação**, baixa
esse arquivo; ele só aparece nas linhas que têm retorno.

## Durante uma manutenção

Um arquivo *Pausada para manutenção* teve o processamento interrompido
pela manutenção do sistema num ponto seguro, sem perder o que já foi
feito. A **Mensagem** diz se ele será retomado quando o sistema voltar
ao normal.

## A ampulheta no cabeçalho

A ampulheta no alto da página, ao lado do envelope das
[mensagens]({{site.baseurl}}/documentacao/manual-do-usuario/central-de-atividades/mensagens), lista em **Tarefas Submetidas** os avisos de
processamento de arquivo que você ainda não viu. **Ver Todas** leva a
esta tela.
