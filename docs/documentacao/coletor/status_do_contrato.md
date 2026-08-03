---
layout: default
title: "Status do contrato"
toc: true
---

# Status do contrato

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página descreve os estados em que um **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** pode estar e como ele transita entre eles. É a página de referência para ler o badge colorido que aparece ao lado de cada contrato no painel. Antes de ler, recomenda-se passar por [Fluxo de negócio]({{ site.baseurl }}/documentacao/coletor/fluxo_de_negocio) e [Operação corrente]({{ site.baseurl }}/documentacao/coletor/operacao_corrente).

## Os estados em uma frase

São **12 códigos de status** e **13 rótulos** — o código `1` cobre dois casos distintos. Os códigos `3` e `4` não existem: eram "Aguardando Testes" e "Testes com Falha", eliminados quando o teste de qualidade passou a rodar dentro da própria extração.

| # | Status | O que significa | O que fazer |
|---|---|---|---|
| 9 | Ciclo de Coleta inativo | O **[Ciclo de Coleta]({{ site.baseurl }}/documentacao/coletor/glossario#ciclo-de-coleta)** do contrato está inativo ou fora do prazo. Tem prioridade sobre todos os outros: bloqueia extração e envio. | Aguardar a janela abrir, ou revisar as datas do ciclo. |
| 1 | Sem Modelos | O contrato existe, mas nenhum **[Modelo de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-de-dados)** foi criado para ele. | Sincronizar com a PNP para trazer os modelos. |
| 14 | Somente Modelos Opcionais | O contrato tem modelos, mas todos são **[opcionais]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-opcional)** e nenhum foi configurado — "não há nada a coletar". Fica **fora** do progresso do wizard. | Nada, se a instituição não vai coletá-los. Para coletar, criar a Configuração de Extração de um deles. |
| 1 | Modelos Não Configurados | Modelo que conta no fluxo existe, mas sem **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)**. | Adicionar uma Configuração ligando o modelo a um **[Provedor de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#provedor-de-dados)**. |
| 2 | Aguardando Extração | Tudo configurado, mas a extração nunca foi executada. | Disparar "Extrair Dados". |
| 7 | Falha na Extração | A última extração registrou erro — inclusive quando o que falhou foi o **teste de qualidade** do contrato, que roda no mesmo run. | Ler o motivo no **[Registro de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-extracao)**, corrigir e re-extrair. |
| 8 | Reextração Necessária | Modelo ou Configuração foram alterados depois da última extração. | Disparar nova extração. |
| 5 | Pronto para Sincronizar | Extração e teste passaram, dados aguardam envio à **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)**. | Disparar "Sincronizar com a PNP". |
| 10 | Aguardando Validação PNP | Enviado; a PNP ainda não validou a estrutura do Parquet. | Nenhuma ação no Coletor — só esperar. |
| 11 | Validação Rejeitada | A PNP rejeitou a validação de um ou mais Parquets. | Ler o motivo, corrigir os dados na origem e re-extrair. |
| 12 | Aguardando Homologação da Área | Validado estruturalmente; aguarda a homologação da área **na PNP**. | Ação humana na PNP — sem botão no Coletor. |
| 13 | Aguardando Aprovação do Reitor | Homologado pela área; aguarda a decisão final do Reitor **na PNP**. | Ação humana na PNP — sem botão no Coletor. |
| 6 | Sincronizado com Sucesso | Aprovado pelo Reitor. Estado terminal do ciclo. | Nenhuma ação. |

> ⚠️ **Metade do fluxo acontece do lado da PNP.** Os estados 10 a 13 espelham o que está acontecendo **na PNP**, não no Coletor. Homologação da Área e Aprovação do Reitor são ações humanas lá — o Coletor apenas consulta o status e reflete o resultado. Não existe botão para avançá-las aqui. Ver [Sincronização com a PNP]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

## Modelos obrigatórios, opcionais e desabilitados {#modelos-obrigatorios-opcionais-e-desabilitados}

O status de um contrato **não olha todos os modelos** — olha os que "contam no fluxo". Quem decide isso é o próprio contrato: para cada modelo, o YAML publicado pela PNP traz dois metadados, `meta.required` e `meta.disabled`. A instituição não edita essa marcação no painel.

| Marcação no contrato | O modelo aparece no painel? | Conta no status e no wizard? |
|---|---|---|
| **[Obrigatório]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-obrigatorio)** (`meta.required: true`, ou sem marcação) | Sim | Sempre |
| **[Opcional]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-opcional)** (`meta.required: false`) | Sim | Só depois que ganhar uma Configuração de Extração |
| **[Desabilitado]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-desabilitado)** (`meta.disabled: true`) | Não — nem chega a ser importado | Nunca |

Consequências práticas:

- Um contrato cujos modelos são **todos opcionais e nenhum configurado** fica no status **14 · Somente Modelos Opcionais** e sai da conta do wizard. É o esperado, não um erro — o painel pode mostrar 8/8 com contratos nesse estado na tela, e o card desse contrato exibe `0/0` modelos configurados.
- O contador do card (`configurados/total`) usa o mesmo critério: o denominador são os **modelos que contam**, e por isso pode ser menor que o número de modelos listados dentro do contrato.
- Um contrato que perde **todos** os modelos por `disabled` deixa de existir no painel. Nada é apagado de fato: a remoção é lógica e o histórico continua guardado.
- Como o cálculo é feito na hora, o caminho é reversível: configurar a extração de um modelo opcional traz o contrato de volta ao fluxo; remover todas as configurações o devolve ao 14.

O status **9 tem prioridade sobre o 14**: um contrato com o ciclo bloqueado mostra "Ciclo de Coleta inativo", mesmo que só tenha modelos opcionais não configurados.

> ℹ️ **Contrato antigo continua igual.** Quando o YAML não traz `meta`, o Coletor assume a opção conservadora: modelo **obrigatório e habilitado**. Valores que não sejam `true`/`false` puros também caem nesse padrão. Depois de atualizar o Coletor, rode **"Sincronizar com a PNP"** uma vez para que as marcações do contrato entrem em vigor.

> ⚠️ **Não confunda com a coluna "Obrigatório" do catálogo.** Nas tabelas de campos de cada contrato, "obrigatório" fala de **coluna** (o campo precisa vir preenchido). Aqui fala de **modelo** (a tabela inteira precisa ser coletada). São dois conceitos diferentes com a mesma palavra.

## Transições entre estados

| De | Para | O que dispara |
|---|---|---|
| — | Sem Modelos | Contrato importado, ainda sem modelos |
| Sem Modelos | Modelos Não Configurados | Chegam modelos da PNP, e ao menos um é obrigatório |
| Sem Modelos | Somente Modelos Opcionais | Chegam modelos da PNP, mas todos são opcionais |
| Somente Modelos Opcionais | Aguardando Extração | Operador configura a extração de um modelo opcional — que passa a ser cobrado |
| Aguardando Extração | Somente Modelos Opcionais | Todas as configurações dos modelos opcionais são removidas |
| Modelos Não Configurados | Aguardando Extração | Operador adiciona a Configuração de Extração |
| Aguardando Extração | Pronto para Sincronizar | Extração + teste concluídos com sucesso |
| Aguardando Extração | Falha na Extração | Extração ou teste falhou |
| Falha na Extração | Pronto para Sincronizar | Nova extração bem-sucedida |
| Pronto para Sincronizar | Aguardando Validação PNP | Operador enviou à PNP |
| Aguardando Validação PNP | Aguardando Homologação da Área | Validação estrutural passou |
| Aguardando Validação PNP | Validação Rejeitada | PNP rejeitou o parquet |
| Validação Rejeitada | Aguardando Extração | Operador corrige o dado e re-extrai |
| Aguardando Homologação da Área | Aguardando Aprovação do Reitor | Área homologou |
| Aguardando Homologação da Área | Validação Rejeitada | Área rejeitou com justificativa |
| Aguardando Aprovação do Reitor | Sincronizado com Sucesso | Reitor aprovou (terminal) |
| Sincronizado com Sucesso | Reextração Necessária | Modelo ou configuração alterados |
| Reextração Necessária | Pronto para Sincronizar | Nova extração bem-sucedida |
| qualquer um | Ciclo de Coleta inativo | Ciclo fecha ou fica fora do prazo (bloqueia tudo) |

> ℹ️ **O status é calculado em tempo real** a cada renderização — não fica persistido no banco. A tela não precisa de refresh manual: o badge do contrato se atualiza sozinho a cada 10 segundos, e o wizard do dashboard a cada 120 segundos. Se o badge parecer "preso" por mais que isso, aí sim vale investigar.

## Veja também

- [Operação corrente]({{ site.baseurl }}/documentacao/coletor/operacao_corrente)
- [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)
- [Fluxo de negócio]({{ site.baseurl }}/documentacao/coletor/fluxo_de_negocio)
