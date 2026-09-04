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

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **indicadores institucionais que dependem de informações sobre servidores terceirizados**: quem trabalha na instituição sob esse vínculo, em qual estrutura e por quanto tempo.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para calcular os indicadores de força de trabalho da Rede Federal — o dimensionamento de quadro que alimenta o orçamento.

> ℹ️ **O modelo carrega PII.** `servidor_terceirizado` traz `cpf` marcado como `pii: true` e `classification: sensitive`. Vale lembrar o que o [CLAUDE.md](https://github.com/PNP-CCV/coletor-pnp-microdados/blob/master/CLAUDE.md) registra sobre o Coletor: **não há criptografia em nível de aplicação** — a proteção desses dados é responsabilidade da infraestrutura que hospeda o banco e o diretório `storage/extracoes/`.

## Modelos contidos

- **`servidor_terceirizado`** *(obrigatório no fluxo)* — trabalhadores terceirizados vinculados à instituição, nominais. Contém PII (`cpf`).

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

## Modelo `servidor_terceirizado`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`) — o único modelo deste contrato. O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Trabalhadores terceirizados atuando na instituição, um por linha. Contém PII (`cpf`). O modelo rastreia **entrada e saída** (`data_ingresso` / `data_exclusao`) e não tem matrícula — terceirizado não é servidor, não tem SIAPE.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_servidor_terceirizado` | `integer` | sim | `primaryKey` | Identificador único do registro de servidor terceirizado |
| `cpf` | `string` | sim | `pii`, `classification: sensitive` | Cadastro de pessoa física do servidor terceirizado |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os servidores terceirizados. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `situacao` | `string` | sim | `enum: [Ativo, Inativo]` | Permanece atuando ou deixou de atuar na estrutura |
| `data_ingresso` | `date` | sim | — | Data que iniciou atividades na estrutura |
| `data_exclusao` | `date` | não | — | Data que encerrou atividades na estrutura |

### Regras de qualidade

Além do schema (colunas obrigatórias, tipos, `enum` e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `cpf` deve conter 11 dígitos | `mustBe: 0` |
| `data_exclusao` não pode anteceder `data_ingresso`; `situacao: Ativo` não pode ter `data_exclusao` e `situacao: Inativo` precisa ter | `mustBe: 0` |

> A coerência entre `situacao` e `data_exclusao`, que antes ficava por conta da origem, hoje é cobrada pela segunda regra.

### Exemplo válido

```json
{
  "id_servidor_terceirizado": 1,
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
| `{"cpf": "...", "estrutura": "12"}` (sem `id_servidor_terceirizado`) | `Required field 'id_servidor_terceirizado' is missing` |
| `{..., "situacao": "Desligado"}` (valor fora do `enum`) | `Value 'Desligado' for field 'situacao' not in enum [Ativo, Inativo]` |
| `{..., "data_ingresso": "02/05/2024"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_ingresso': expected date, got string '02/05/2024'` |
| `{..., "matricula": "1548923"}` (coluna não declarada neste modelo) | `Field 'matricula' not in schema (additionalFields: false)` |
| `{..., "situacao": "Ativo", "data_exclusao": "2025-01-31"}` (ativo com data de exclusão) | `A situação deve ser coerente com a data de exclusão.: Actual custom_sql(servidor_terceirizado) was 1, expected = 0` |

## `referencia_pnp` — conferido na extração

O modelo declarado traz, no campo `estrutura`, um bloco `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`. O Coletor confere esse código contra o espelho local de estruturas antes de gravar o Parquet, antecipando a checagem que a PNP faz depois do envio. Como a `severidade` declarada é `erro`, um código que não existe no cadastro **reprova o teste do contrato** — a extração conclui, mas o apontamento aparece em **Ver resultados de teste**, com o campo e as linhas envolvidas, e o envio à PNP fica barrado. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-16 | Versão inicial documentada nesta data. | — |
| `1.0.0` | 2026-09-01 | Modelos `servidor_nao_docente` e `prof_equivalente` (desabilitados, nunca coletados) removidos do contrato; `id` renomeado para `id_servidor_terceirizado`; regras `quality` acrescentadas. `info.version` não foi bumpada. | **sim** |

## Contrato de Dados - Formato YAML
```yaml
dataContractSpecification: "1.2.0"
id: "pessoal"
info:
  title: "Pessoal"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados dos indicadores que necessitam de informações sobre servidores terceirizados.

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
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "CPF deve conter 11 dígitos."
        query: >
          SELECT COUNT(*) FROM servidor_terceirizado
          WHERE NOT regexp_full_match(cpf, '[0-9]{11}')
        mustBe: 0
      - type: sql
        description: "A situação deve ser coerente com a data de exclusão."
        query: >
          SELECT COUNT(*) FROM servidor_terceirizado
          WHERE data_exclusao < data_ingresso
             OR (situacao = 'Ativo' AND data_exclusao IS NOT NULL)
             OR (situacao = 'Inativo' AND data_exclusao IS NULL)
        mustBe: 0
    fields:
      id_servidor_terceirizado:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true
        description: "Identificador único do registro de servidor terceirizado."

      cpf:
        type: string
        title: "CPF"
        description: "Cadastro de pessoa física do servidor terceirizado."
        pii: true
        required: true
        classification: "sensitive"

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os servidores terceirizados"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      situacao:
        type: string
        title: "Situação"
        required: true
        enum: ["Ativo", "Inativo"]
        description: "Permanece atuando ou deixou de atuar na estrutura."

      data_ingresso:
        type: date
        required: true
        title: "Data de ingresso"
        description: "Data que iniciou atividades na estrutura."

      data_exclusao:
        type: date
        title: "Data de exclusão"
        description: "Data que encerrou atividades na estrutura."
    additionalFields: false
```

