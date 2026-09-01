---
layout: default
title: "Ativos de Pesquisa"
toc: true
---
# Ativos de Pesquisa

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `ativos_pesquisa` · **Versão:** `1.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Pesquisa e Inovação

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **ativos de propriedade intelectual** depositados e concedidos à instituição: patentes, marcas, desenhos industriais, cultivares, topografias de circuitos integrados, programas de computador e organismos geneticamente modificados. Cada registro representa um ativo com processo junto ao **INPI**, sua situação de registro e a eventual transferência, licenciamento ou cessão a terceiros.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar a **inovação e a transferência de tecnologia** da Rede Federal — quanto se deposita, quanto se concede e quanto efetivamente chega ao setor produtivo.

Este contrato é composto por um único **[Modelo de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-de-dados)**, e ele é obrigatório — diferente de [Acordos de Parceria]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acordos_de_parceria), cujo modelo único é opcional.

## Modelos contidos

- **`ativos_pesquisa`** *(obrigatório no fluxo)* — ativos de propriedade intelectual com número de processo no INPI, titularidade, datas de depósito e concessão, validade, situação do registro e situação da transferência.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Modelo `ativos_pesquisa`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela única do contrato. Cada linha é um ativo de propriedade intelectual identificado por `id_ativo_pesq`, com o número do processo no INPI como identificador externo. O modelo tem dependência de outros conjuntos de dados da instituição — em especial o de projetos de pesquisa que originou o ativo —, mas essa relação não é declarada como `references` no YAML.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_ativo_pesq` | `integer` | sim | `primaryKey` | Identificador único para cada ativo de propriedade intelectual |
| `num_inpi_ativo_pesq` | `string` | sim | — | Número do processo de registro do ativo junto ao INPI |
| `tipo_ativo_pesq` | `string` | sim | `enum` (8 valores — ver legenda abaixo) | Tipo de propriedade intelectual correspondente ao ativo |
| `titular_inpi_ativo_pesq` | `boolean` | não | — | A instituição que informa o ativo registrou-se como titular junto ao INPI |
| `cotitular_inpi_ativo_pesq` | `boolean` | não | — | A instituição que informa o ativo registrou-se como co-titular junto ao INPI |
| `data_deposito_ativo_pesq` | `date` | não | — | Data em que a instituição depositou o pedido de registro do ativo no INPI |
| `data_concessao_ativo_pesq` | `date` | não | — | Data em que o INPI concedeu o registro do ativo à instituição |
| `validade_ativo_pesq` | `integer` | não | — | Prazo de validade do registro do ativo, em anos |
| `sit_registro_ativo_pesq` | `string` | sim | `enum: [Ativo, Inativo, Pedido em análise]` | Situação atual do registro de propriedade intelectual |
| `sit_transf_ativo_pesq` | `string` | sim | `enum` (4 valores — ver legenda abaixo) | Situação atual do projeto de pesquisa quanto à transferência do ativo |
| `num_transf_ativo_pesq` | `string` | sim | — | Número do contrato de transferência, licenciamento ou cessão do ativo |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os ativos. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |

#### Valores de `tipo_ativo_pesq`

Propriedade industrial: `Patente de Invenção`, `Patente de Modelo de Utilidade`, `Marca`, `Desenho Industrial`, `Topografia de Circuitos Integrados`.

Demais regimes: `Cultivar`, `Programa de Computador`, `Organismo Geneticamente Modificado`.

#### Valores de `sit_transf_ativo_pesq`

| Valor | Quando usar |
|---|---|
| `Transferido: contrato de transferência de tecnologia não patenteada, não patenteável e de know-how` | Houve transferência de tecnologia sem registro de propriedade industrial |
| `Licenciado: contrato de licenciamento de propriedade industrial` | O ativo foi licenciado, e a titularidade continua com a instituição |
| `Cedido: contrato de cessão de propriedade industrial` | A titularidade do ativo foi cedida a terceiro |
| `NA` | Não houve transferência, licenciamento nem cessão |

> ℹ️ **`referencia_pnp` é conferido na extração.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`, e o Coletor confere esse código contra o cadastro local de estruturas antes de gravar o Parquet — a mesma checagem que a PNP faz depois do envio, antecipada. O padrão de fábrica é o **modo sombra**: a divergência é registrada no Registro de Extração, mas ainda não reprova a extração. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### Regras de qualidade

Atualmente não declaradas neste contrato (bloco `quality` ausente). A validação ativa hoje é apenas o schema (colunas obrigatórias, tipos, e rejeição de colunas extras via `additionalFields: false`).

> ⚠️ **`num_transf_ativo_pesq` é obrigatório mesmo sem transferência.** O contrato não declara condicionalidade entre campos, então um ativo com `sit_transf_ativo_pesq: "NA"` precisa preencher a coluna assim mesmo — na prática, com um marcador como `NA`. Deixá-la vazia reprova a extração.

### Exemplo válido

```json
{
  "id_ativo_pesq": 811,
  "num_inpi_ativo_pesq": "BR 10 2023 012345 6",
  "tipo_ativo_pesq": "Patente de Invenção",
  "titular_inpi_ativo_pesq": true,
  "cotitular_inpi_ativo_pesq": false,
  "data_deposito_ativo_pesq": "2023-06-19",
  "data_concessao_ativo_pesq": "2025-11-04",
  "validade_ativo_pesq": 20,
  "sit_registro_ativo_pesq": "Ativo",
  "sit_transf_ativo_pesq": "Licenciado: contrato de licenciamento de propriedade industrial",
  "num_transf_ativo_pesq": "LIC 007/2026-IFRN",
  "estrutura": "12"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"num_inpi_ativo_pesq": "BR 10 ...", "tipo_ativo_pesq": "Marca"}` (sem `id_ativo_pesq`) | `Required field 'id_ativo_pesq' is missing` |
| `{"id_ativo_pesq": 811, "tipo_ativo_pesq": "Marca"}` (sem `sit_transf_ativo_pesq`) | `Required field 'sit_transf_ativo_pesq' is missing` |
| `{..., "tipo_ativo_pesq": "Patente"}` (valor fora do `enum`) | `Value 'Patente' for field 'tipo_ativo_pesq' not in enum` |
| `{..., "data_deposito_ativo_pesq": "19/06/2023"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_deposito_ativo_pesq': expected date, got string '19/06/2023'` |
| `{..., "validade_ativo_pesq": "20 anos"}` (`string` em vez de `integer`) | `Type mismatch on 'validade_ativo_pesq': expected integer, got string` |
| `{..., "inventor": "Ana Souza"}` (coluna não declarada) | `Field 'inventor' not in schema (additionalFields: false)` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-08-13 | Versão inicial documentada nesta data. | — |

## YAML completo

```yaml
dataContractSpecification: "1.2.0"
id: "ativos_pesquisa"
info:
  title: "Ativos de Pesquisa"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve o modelo de dados dos ativos de propriedade intelectual

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/ativos-de-pesquisa/{model}/*.parquet"
    format: "parquet"

models:
  ativos_pesquisa:
    type: table
    title: "Ativos de propriedade intelectual depositados e concedidos"
    description: >
      ativos_pesquisa é um dos conjuntos de dados necessários para cálculo dos
      indicadores de pesquisa e inovação da Rede Federal. Neste modelo há dados
      com dependências de outros conjuntos.
    meta:
      required: true
      disabled: false
    fields:
      id_ativo_pesq:
        type: integer
        title: "ID do ativo"
        primaryKey: true
        required: true
        description: "Identificador único para cada ativo de propriedade intelectual."

      num_inpi_ativo_pesq:
        type: string
        title: "Número do processo no INPI"
        required: true
        description: "Número do processo de registro do ativo junto ao INPI."

      tipo_ativo_pesq:
        type: string
        title: "Tipo de propriedade intelectual"
        required: true
        enum:
          - "Patente de Invenção"
          - "Patente de Modelo de Utilidade"
          - "Marca"
          - "Desenho Industrial"
          - "Cultivar"
          - "Topografia de Circuitos Integrados"
          - "Programa de Computador"
          - "Organismo Geneticamente Modificado"
        description: "Tipo de propriedade intelectual correspondente ao ativo."

      titular_inpi_ativo_pesq:
        type: boolean
        title: "É instituição titular no INPI?"
        required: false
        description: >
          A instituição que está informando o ativo neste BD registrou-se
          como titular do ativo junto ao INPI.

      cotitular_inpi_ativo_pesq:
        type: boolean
        title: "É instituição co-titular no INPI?"
        required: false
        description: >
          A instituição que está informando o ativo neste BD registrou-se
          como co-titular do ativo junto ao INPI.

      data_deposito_ativo_pesq:
        type: date
        title: "Data do depósito"
        required: false
        description: "Data em que a instituição depositou pedido de registro do ativo intelectual junto ao INPI."

      data_concessao_ativo_pesq:
        type: date
        title: "Data da concessão"
        required: false
        description: "Data em que o INPI concedeu o registro do ativo intelectual à instituição."

      validade_ativo_pesq:
        type: integer
        title: "Prazo de validade em anos"
        required: false
        description: "Prazo de validade do registro do ativo intelectual, em anos."

      sit_registro_ativo_pesq:
        type: string
        title: "Situação do registro de propriedade intelectual"
        required: true
        enum: ["Ativo", "Inativo", "Pedido em análise"]
        description: "Situação atual do registro de propriedade intelectual."

      sit_transf_ativo_pesq:
        type: string
        title: "Situação da transferência do ativo"
        required: true
        enum:
          - "Transferido: contrato de transferência de tecnologia não patenteada, não patenteável e de know-how"
          - "Licenciado: contrato de licenciamento de propriedade industrial"
          - "Cedido: contrato de cessão de propriedade industrial"
          - "NA"
        description: "Situação atual do projeto de pesquisa quanto à transferência do ativo."

      num_transf_ativo_pesq:
        type: string
        title: "Número do contrato de transferência"
        required: true
        description: "Número do contrato de transferência, licenciamento ou cessão do ativo."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os ativos"
        required: true
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro
    additionalFields: false
```

## Veja também

- [Conceito de Contrato de Dados]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/conceito)
- [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Produção Intelectual]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/producao_intelectual) — contrato vizinho, cobre a produção acadêmica e técnica (incluindo `PATENTE`, `MARCA` e `DESENHO-INDUSTRIAL` como classificação de produção)
