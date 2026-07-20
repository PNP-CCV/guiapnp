---
layout: default
title: "Visão geral do Coletor"
---

# Visão geral do Coletor

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página apresenta o que é o **Coletor de Microdados** (Coletor:PNP), qual o seu papel na cadeia de coleta de microdados da Rede Federal e quem são os atores envolvidos. É a porta de entrada para as demais páginas da seção.

## O que é o Coletor

O Coletor é um sistema operado por cada instituição da Rede Federal de Educação Profissional para extrair microdados dos seus sistemas internos via **[Provedores de Dados](/documentacao/coletor/glossario#provedor-de-dados)** cadastrados, validá-los contra um **[Contrato de Dados](/documentacao/coletor/glossario#contrato-de-dados)** padronizado e enviá-los à **[PNP](/documentacao/coletor/glossario#pnp)**. O IFRN desenvolve e mantém a ferramenta em parceria com a SETEC/**[MEC](/documentacao/coletor/glossario#mec)**, que define os contratos esperados e recebe os dados consolidados. O objetivo é reduzir trabalho manual de coleta, padronizar entregas e tornar todo o processo auditável.

## Contexto na Plataforma Nilo Peçanha

A Plataforma Nilo Peçanha é o sistema oficial do MEC, mantido pela SETEC, que consolida e publica anualmente os microdados da Rede Federal de Educação Profissional, Científica e Tecnológica. Cada instituição da rede precisa entregar à PNP uma série de tabelas seguindo schemas obrigatórios. Historicamente, esse trabalho era manual, sujeito a divergências de interpretação e difícil de auditar.

O Coletor atua como ponte entre os sistemas legados de cada instituição (SUAP, SIPAC, planilhas de gestão, bancos próprios) e a PNP. Ele lê os dados de onde estiverem, normaliza para o schema do contrato vigente, valida a qualidade automaticamente e sincroniza o resultado com a PNP. Cada instituição roda a sua própria instância — os dados nunca saem da rede da instituição até passarem pela validação do contrato.

## Atores

| Ator | Papel |
|---|---|
| Instituição (IFs, CEFETs, Colégio Pedro II, ETVs) | Mantém os sistemas-fonte e roda uma instância do Coletor. |
| Operador / gestor da instituição | Configura **[Provedores de Dados](/documentacao/coletor/glossario#provedor-de-dados)** e contratos, dispara extrações e acompanha a **[Sincronização](/documentacao/coletor/glossario#sincronizacao)**. |
| MEC / equipe da PNP | Define os contratos esperados e recebe os arquivos sincronizados. |
| Sistema fonte (SUAP, SIPAC, planilhas) | Origem dos microdados consultada pelo Coletor. |
| Integrador externo | Outras instituições que precisam entender os contratos publicados pela PNP. |

## Capacidades em uma página

- Quatro tipos de Provedor de Dados selecionáveis: API HTTP, banco relacional, planilha online (Google Docs, Dropbox, SharePoint) e upload de planilha (XLS / XLSX / ODS).
- Cada provedor alimenta um ou mais **[Modelos de Dados](/documentacao/coletor/glossario#modelo-de-dados)** — tabelas lógicas (ações de extensão, projetos de pesquisa, etc.) que compõem um contrato.
- Validação automática contra um Contrato de Dados em YAML, com checagem de schema (colunas, tipos, restrições) e regras de qualidade declarativas.
- **[Sincronização](/documentacao/coletor/glossario#sincronizacao)** programática com a PNP, com controle de janela do **[Ciclo de Coleta](/documentacao/coletor/glossario#ciclo-de-coleta)** e do **[Período de Correção](/documentacao/coletor/glossario#periodo-de-correcao)**.
- Trilha de auditoria completa via **[Registros de Extração](/documentacao/coletor/glossario#registro-de-extracao)** e Registros de Sincronização, com motivos de erro, métricas de duração e detalhes técnicos.
- Execução em background, permitindo disparo em lote e re-execução manual sob demanda sem travar o navegador.
- Interface única no **painel** (`/painel/`), em português, sem necessidade de console ou linha de comando para operação rotineira.

## O que esta seção cobre

Esta seção do guia descreve o fluxo de negócio, o ciclo de coleta, a operação corrente, a máquina de status do contrato e o [Manual de Operação](/documentacao/coletor/manual_de_operacao) completo (requisitos, instalação e uso passo a passo). A especificação de cada contrato está em [Usuários Especializados › Contratos de Dados](/documentacao/usuarios-especializados/contratos/conceito); a documentação técnica interna (arquitetura, código, extensão) permanece no [site de documentação do Coletor](https://pnp-ccv.github.io/coletor-pnp-microdados/).

## Veja também

- [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio)
- [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta)
- [Manual de Operação](/documentacao/coletor/manual_de_operacao)
