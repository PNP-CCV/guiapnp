---
layout: default
title: "Pessoal Terceirizado"
toc: true
---

* TOC
{:toc}

# Pessoal Terceirizado

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `pessoal` · **Versão:** `1.0.0` · **Owner:** SETEC

**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Sustentabilidade

## Resumo de negócio

Este **[Contrato de Dados]** descreve os **os dados de pessoa terceirizado**: quem trabalha na instituição e em qual estrutura.

A **PNP** coleta este contrato para ter a relação de pessoal terceirazado vinculado as instituições, de forma a apoiar os indicadores de sustentabilidade.

## Modelos contidos

- **`servidor_terceirizado`** — trabalhadores terceirizados vinculados à instituição, nominais.


## Modelo `servidor_terceirizado`

### Resumo do modelo

Trabalhadores terceirizados atuando na instituição, um por linha. Contém PII (`cpf`). Este modelo rastreia **entrada e saída** (`data_ingresso` / `data_exclusao`).

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id` | `integer` | sim | `primaryKey` | Identificador |
| `cpf` | `string` | não | `pii`, `classification: sensitive` | Cadastro de pessoa física do servidor terceirizado |
| `estrutura` | `string` | não | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se os servidores terceirizados. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `situacao` | `string` | não | `enum: [Ativo, Inativo]` | Permanece atuando ou deixou de atuar na estrutura |
| `data_ingresso` | `date` | não | — | Data que iniciou atividades na estrutura |
| `data_exclusao` | `date` | não | — | Data que encerrou atividades na estrutura |

> **`situacao` e `data_exclusao` podem se contradizer.** Nada no schema garante que `situacao: "Inativo"` venha com `data_exclusao` preenchida, nem que `situacao: "Ativo"` venha sem ela. Não há regra de qualidade declarada — a coerência é responsabilidade da origem.



### Exemplo válido

```json
{
  "id": 1,
  "cpf": "98765432100",
  "estrutura": "12",
  "situacao": "Ativo",
  "data_ingresso": "2024-05-02",
  "data_exclusao": null
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"cpf": "...", "estrutura": "12"}` (sem `id`) | `Required field 'id' is missing` |
| `{..., "situacao": "Desligado"}` (valor fora do `enum`) | `Value 'Desligado' for field 'situacao' not in enum [Ativo, Inativo]` |
| `{..., "data_ingresso": "02/05/2024"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_ingresso': expected date, got string '02/05/2024'` |
| `{..., "matricula": "1548923"}` (coluna não declarada neste modelo) | `Field 'matricula' not in schema (additionalFields: false)` |


## Contrato de Dados - Formato YAML
```yaml
dataContractSpecification: "1.2.0"
id: "pessoal"
info:
  title: "Pessoal"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve a relação servidores terceirizados vinculados a instituição e suas respectivas estruturas.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/pessoal/{model}/*.parquet"
    format: "parquet"

models:

  servidor_terceirizado:
    type: table
    title: "Servidor Terceirizado"
    description: "Indicadores relativos aos servidores terceirizados vinculados à instituição."
    fields:
      id:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true

      cpf:
        type: string
        title: "CPF"
        description: "Cadastro de pessoa física do servidor terceirizado."
        pii: true
        classification: "sensitive"

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os servidores terceirizados"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      situacao:
        type: string
        title: "Situação"
        enum: ["Ativo", "Inativo"]
        description: "Permanece atuando ou deixou de atuar na estrutura."

      data_ingresso:
        type: date
        title: "Data de ingresso"
        description: "Data que iniciou atividades na estrutura."

      data_exclusao:
        type: date
        title: "Data de exclusão"
        description: "Data que encerrou atividades na estrutura."
    additionalFields: false
```

