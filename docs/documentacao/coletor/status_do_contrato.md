---
layout: default
title: "Status do contrato"
toc: true
---

# Status do contrato

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página descreve os estados em que um **[Contrato de Dados](/documentacao/coletor/glossario#contrato-de-dados)** pode estar e como ele transita entre eles. É a página de referência para ler o badge colorido que aparece ao lado de cada contrato no painel. Antes de ler, recomenda-se passar por [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio) e [Operação corrente](/documentacao/coletor/operacao_corrente).

## Os estados em uma frase

São **11 códigos de status** e **12 rótulos** — o código `1` cobre dois casos distintos. Os códigos `3` e `4` não existem: eram "Aguardando Testes" e "Testes com Falha", eliminados quando o teste de qualidade passou a rodar dentro da própria extração.

| # | Status | O que significa | O que fazer |
|---|---|---|---|
| 9 | Ciclo de Coleta inativo | O **[Ciclo de Coleta](/documentacao/coletor/glossario#ciclo-de-coleta)** do contrato está inativo ou fora do prazo. Tem prioridade sobre todos os outros: bloqueia extração e envio. | Aguardar a janela abrir, ou revisar as datas do ciclo. |
| 1 | Sem Modelos | O contrato existe, mas nenhum **[Modelo de Dados](/documentacao/coletor/glossario#modelo-de-dados)** foi criado para ele. | Sincronizar com a PNP para trazer os modelos. |
| 1 | Modelos Não Configurados | Modelo existe, mas sem **[Configuração de Extração](/documentacao/coletor/glossario#configuracao-de-extracao)**. | Adicionar uma Configuração ligando o modelo a um **[Provedor de Dados](/documentacao/coletor/glossario#provedor-de-dados)**. |
| 2 | Aguardando Extração | Tudo configurado, mas a extração nunca foi executada. | Disparar "Extrair Dados". |
| 7 | Falha na Extração | A última extração registrou erro — inclusive quando o que falhou foi o **teste de qualidade** do contrato, que roda no mesmo run. | Ler o motivo no **[Registro de Extração](/documentacao/coletor/glossario#registro-de-extracao)**, corrigir e re-extrair. |
| 8 | Reextração Necessária | Modelo ou Configuração foram alterados depois da última extração. | Disparar nova extração. |
| 5 | Pronto para Sincronizar | Extração e teste passaram, dados aguardam envio à **[PNP](/documentacao/coletor/glossario#pnp)**. | Disparar "Sincronizar com a PNP". |
| 10 | Aguardando Validação PNP | Enviado; a PNP ainda não validou a estrutura do Parquet. | Nenhuma ação no Coletor — só esperar. |
| 11 | Validação Rejeitada | A PNP rejeitou a validação de um ou mais Parquets. | Ler o motivo, corrigir os dados na origem e re-extrair. |
| 12 | Aguardando Homologação da Área | Validado estruturalmente; aguarda a homologação da área **na PNP**. | Ação humana na PNP — sem botão no Coletor. |
| 13 | Aguardando Aprovação do Reitor | Homologado pela área; aguarda a decisão final do Reitor **na PNP**. | Ação humana na PNP — sem botão no Coletor. |
| 6 | Sincronizado com Sucesso | Aprovado pelo Reitor. Estado terminal do ciclo. | Nenhuma ação. |

> ⚠️ **Metade do fluxo acontece do lado da PNP.** Os estados 10 a 13 espelham o que está acontecendo **na PNP**, não no Coletor. Homologação da Área e Aprovação do Reitor são ações humanas lá — o Coletor apenas consulta o status e reflete o resultado. Não existe botão para avançá-las aqui. Ver [Sincronização com a PNP](/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

## Transições entre estados

| De | Para | O que dispara |
|---|---|---|
| — | Sem Modelos | Contrato importado, ainda sem modelos |
| Sem Modelos | Modelos Não Configurados | Chegam modelos da PNP |
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

- [Operação corrente](/documentacao/coletor/operacao_corrente)
- [Validação e qualidade](/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)
- [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio)
