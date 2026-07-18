---
layout: default
title: "Produção Intectual"
toc: true
---
# Produção Intelectual

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `producao_intelectual` · **Versão:** `1.0.0` · **Owner:** SETEC

**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Pesquisa e Inovação

## Resumo de negócio

Este **Contrato de Dados** descreve a **produção intelectual acadêmica e técnica** dos servidores da instituição: publicações (artigos, livros, capítulos, anais), produções técnico-tecnológicas, artístico-culturais e demais categorias da taxonomia Lattes/CNPq, com classificação Qualis-CAPES quando aplicável.

A **PNP** coleta este contrato para mensurar a **produção acadêmica e técnica** da rede federal e a participação de docentes, TAEs, estudantes e externos em cada produção. Os dois modelos cobrem a produção em si e os participantes vinculados a ela (com PII).

## Modelos contidos

- **`producao_intelectual`** — produções acadêmicas, técnicas, tecnológicas e culturais registradas institucionalmente, com tipo, classificação, ano e área CNPq.
- **`participantes_producao_intelectual`** — pessoas envolvidas em cada produção (docentes, TAEs, estudantes, externos). Contém PII (`cpf`, `nome`).

## Modelo `producao_intelectual`

### Resumo do modelo

Tabela principal do contrato. Cada linha é uma produção intelectual única, identificada por `id_producao`. A tabela `participantes_producao_intelectual` referencia-a por chave estrangeira.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_producao` | `integer` | sim | `primaryKey` | ID produção |
| `tipo_producao` | `string` | sim | `enum: [Acadêmica, Técnica]` | Tipo de produção |
| `classificacao_producao` | `string` | não | — | Categoria de produção conforme taxonomia da base Lattes (técnico-tecnológica, artístico-cultural, etc.) |
| `titulo_producao` | `string` | sim | — | Título da produção |
| `ano_publicacao` | `integer` | não | — | Ano de publicação. Formato: `AAAA` |
| `avaliacao_capes` | `string` | não | `enum: [Qualis, NA]` | Avaliação Capes |
| `area_tematica_cnpq` | `string` | não | — | Área Temática CNPq. Formato: `{id; nome}` |


### Exemplo válido

```json
{
  "id_producao": 7402,
  "tipo_producao": "Acadêmica",
  "classificacao_producao": "Artigo completo publicado em periódico",
  "titulo_producao": "Aprendizado profundo aplicado à classificação de imagens médicas em redes neurais convolucionais",
  "ano_publicacao": 2024,
  "avaliacao_capes": "Qualis",
  "area_tematica_cnpq": "10300007; Ciência da Computação"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"tipo_producao": "Acadêmica", "titulo_producao": "..."}` (sem `id_producao`) | `Required field 'id_producao' is missing` |
| `{"id_producao": 7402, "tipo_producao": "Acadêmica"}` (sem `titulo_producao`) | `Required field 'titulo_producao' is missing` |
| `{"id_producao": 7402, "tipo_producao": "Patente", "titulo_producao": "..."}` (valor fora do `enum`) | `Value 'Patente' for field 'tipo_producao' not in enum [Acadêmica, Técnica]` |
| `{..., "ano_publicacao": "2024"}` (`string` em vez de `integer`) | `Type mismatch on 'ano_publicacao': expected integer, got string` |
| `{..., "doi": "10.1234/exemplo"}` (coluna não declarada) | `Field 'doi' not in schema (additionalFields: false)` |

## Modelo `participantes_producao_intelectual`

### Resumo do modelo

Pessoas envolvidas em cada produção intelectual (autoria, coautoria, orientação, participação técnica), com vínculo, período e situação. Contém PII (`cpf`, `nome`) classificados como `sensitive`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_participante` | `integer` | sim | `primaryKey` | ID participante |
| `cpf` | `string` | não | `pii`, `classification: sensitive` | CPF do participante da produção intelectual |
| `nome` | `string` | não | `pii`, `classification: sensitive` | Nome completo do participante da produção |
| `categoria` | `string` | não | `enum: [docente, TAE, externo, estudante]` | Tipo de vínculo com a produção (ex.: docente, TAE, externo) |
| `id_producao` | `integer` | sim | `references producao_intelectual.id_producao` | Referência à produção intelectual cadastrada |
| `data_ingresso` | `date` | não | — | Data de início da participação na produção |
| `data_saida` | `date` | não | — | Data de encerramento da participação, se aplicável |
| `situacao_participante` | `string` | não | `enum: [Ativo, Inativo]` | Status atual do vínculo do participante com a produção |


### Exemplo válido

```json
{
  "id_participante": 33108,
  "cpf": "11122233344",
  "nome": "Ricardo Almeida Costa",
  "categoria": "docente",
  "id_producao": 7402,
  "data_ingresso": "2023-09-01",
  "data_saida": "2024-06-30",
  "situacao_participante": "Inativo"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"cpf": "...", "id_producao": 7402}` (sem `id_participante`) | `Required field 'id_participante' is missing` |
| `{"id_participante": 33108, "categoria": "docente"}` (sem `id_producao`) | `Required field 'id_producao' is missing` |
| `{..., "categoria": "professor"}` (valor fora do `enum`) | `Value 'professor' for field 'categoria' not in enum [docente, TAE, externo, estudante]` |
| `{..., "orcid": "0000-0000-..."}` (coluna não declarada) | `Field 'orcid' not in schema (additionalFields: false)` |


## Contrato de Dados - Formato YAML

```yaml

dataContractSpecification: "1.2.0"
id: "producao_intelectual"
info:
  title: "Produção Intelectual"
  version: "1.0.0"
  status: "active"
  description: >
    Contrato de dados para registrar as produções intelectuais acadêmicas e técnicas realizadas
    pelos servidores da instituição, com classificação, ano de publicação e participação de docentes e TAEs.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/producao-intelectual/{model}/*.parquet"
    format: "parquet"

models:
  producao_intelectual:
    type: table
    title: "Produção Intelectual"
    description: "Modelo de dados para produções acadêmicas, técnicas, tecnológicas e culturais registradas institucionalmente."
    fields:
      id_producao:
        type: integer
        title: "ID produção"
        primaryKey: true
        required: true

      tipo_producao:
        type: string
        title: "Tipo de produção"
        enum: ["Acadêmica", "Técnica"]
        required: true

      classificacao_producao:
        type: string
        title: "Classificação da produção"
        description: "Categoria de produção conforme taxonomia da base Lattes (técnico-tecnológica, artístico-cultural, etc)."

      titulo_producao:
        type: string
        title: "Título da produção"
        required: true

      ano_publicacao:
        type: integer
        title: "Ano de publicação"
        description: "Formato: AAAA"

      avaliacao_capes:
        type: string
        title: "Avaliação Capes"
        enum: ["Qualis", "NA"]

      area_tematica_cnpq:
        type: string
        title: "Área Temática CNPq"
        description: "Formato: {codigo}"
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: aviso
    additionalFields: false

  participantes_producao_intelectual:
    type: table
    title: "Participantes da Produção Intelectual"
    description: "Tabela contendo dados dos indivíduos envolvidos nas produções intelectuais cadastradas institucionalmente."
    fields:
      id_participante:
        type: integer
        title: "ID participante"
        primaryKey: true
        required: true

      cpf:
        type: string
        title: "CPF"
        description: "CPF do participante da produção intelectual."
        pii: true
        classification: "sensitive"
        referencia_pnp:
          recurso: pessoas
          tipo: chave_simples
          chave: cpf
          severidade: erro
          filtro_categoria_campo: categoria
          categorias_validar: ["docente", "TAE", "estudante"]

      nome:
        type: string
        title: "Nome"
        description: "Nome completo do participante da produção."
        pii: true
        classification: "sensitive"

      categoria:
        type: string
        title: "Categoria"
        description: "Tipo de vínculo com a produção (ex.: docente, TAE, externo)."
        enum: ["docente", "TAE", "externo", "estudante"]

      id_producao:
        type: integer
        title: "ID produção"
        description: "Referência à produção intelectual cadastrada."
        references: "producao_intelectual.id_producao"
        required: true

      data_ingresso:
        type: date
        title: "Data de ingresso"
        description: "Data de início da participação na produção."

      data_saida:
        type: date
        title: "Data de saída"
        description: "Data de encerramento da participação, se aplicável."

      situacao_participante:
        type: string
        title: "Situação do participante"
        enum: ["Ativo", "Inativo"]
        description: "Status atual do vínculo do participante com a produção."
    additionalFields: false

```

