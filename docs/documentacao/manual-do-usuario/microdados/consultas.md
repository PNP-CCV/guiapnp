---
layout: default
title: "Consultas"
toc: true
---
# Consultas

As consultas são as tabelas de referência que o operador usa para achar o
código que a [planilha]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/enviar-planilha) ou o
[formulário]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/preencher-pelo-formulario) pedem: o código da estrutura de um
campus, o código de um município, a matrícula de um estudante. Cada consulta
mostra uma tabela, com busca e download.

Estas telas são só do perfil Operador de Área Temática: no menu, em
**Microdados → Consultas**, ou pelos cards de mesmo nome no Painel. São sete:

| Consulta | O que lista | Recorte |
|---|---|---|
| **Ciclos de Coleta** | ano, status e as datas de coleta, envio e correção de cada ciclo | todos os ciclos |
| **Estruturas** | código da estrutura e nome das unidades | unidades da instituição do perfil que têm código de estrutura, ativas ou não |
| **Matrículas** | CPF, nome, matrícula, curso, unidade e código da estrutura | matrículas válidas e atendidas da instituição do perfil |
| **Servidores** | nome, CPF, matrícula, unidade e código da estrutura | servidores não excluídos da instituição do perfil, ativos ou não |
| **Subeixos** | código e nome | todos |
| **Municípios** | código, nome e UF | todos |
| **Áreas CNPq** | código e nome | todas |

As consultas da instituição sempre usam a instituição do perfil ativo; não há
como escolher outra.

![Consulta de Estruturas]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/consultas/estruturas.png)

## Buscar

O campo **Busca**, no bloco **Filtros**, procura o termo em qualquer coluna de
texto da tabela, sem diferenciar maiúsculas de minúsculas. **Filtrar** aplica
a busca e volta à primeira página; **Limpar Filtros** desfaz.

Na consulta de **Ciclos de Coleta**, as datas não entram na busca, e um número
procura o ano exato: "2026" traz o ciclo de 2026.

![Consulta de Ciclos de Coleta]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/consultas/ciclos-coleta.png)

## Baixar

**Baixar XLSX** baixa todas as linhas da consulta numa planilha, com a mesma
busca aplicada na tela, e não só a página que está aberta.

Matrículas e Servidores trazem o CPF completo, na tela e no arquivo.

![Consulta de Matrículas]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/consultas/matriculas.png)
