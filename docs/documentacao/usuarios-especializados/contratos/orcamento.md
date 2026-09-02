---
layout: default
title: "Orçamento"
toc: true
---

* TOC
{:toc}

# Orçamento

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `orcamento` · **Versão:** `1.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Orçamento

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve o indicador institucional de **orçamento**, a partir do subconjunto mínimo de dados financeiros (Dados Orçamentários). Cada registro é uma linha de execução orçamentária extraída do **Siafi** (via ODI), com a classificação orçamentária completa (órgão, UO, ação, PTRES, fonte, GND) e os valores efetivamente **liquidados** e de **restos a pagar pagos**.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para relacionar gasto público executado com a oferta de ensino, pesquisa e extensão — é o insumo dos indicadores de custo por aluno e de aplicação de recursos por finalidade.

## Modelos contidos

- **`dados_orcamentarios`** *(opcional no fluxo)* — dados orçamentários vinculados à execução financeira institucional.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `dados_orcamentarios`.

## Modelo `dados_orcamentarios`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é uma combinação de classificação orçamentária com os valores executados no período. A granularidade é definida pela origem (SIAFI) — o contrato não declara chave composta, apenas o `id` técnico do registro.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_dados_orcamentarios` | `integer` | sim | `primaryKey` | Identificador do registro |
| `orgao_superior_cod` | `string` | sim | — | Órgão Superior (Cód)(UO). Origem: SIAFI |
| `uo_cod` | `string` | sim | — | Unidade Orçamentária (Cód). Origem: SIAFI |
| `acao_cod` | `string` | sim | — | Ação (Cód). Origem: SIAFI |
| `ptres` | `string` | sim | — | Programa de Trabalho Resumido. Origem: SIAFI |
| `origem_despesa` | `string` | sim | `enum` (ver legenda) | Origem da Despesa. Origem: SIAFI |
| `emenda_impositiva_tipo` | `string` | não | — | Emenda Impositiva (Tipo). Origem: SIAFI |
| `emenda_impositiva_numero_ano` | `string` | não | — | Emenda Impositiva (Número/Ano). Origem: SIAFI |
| `programa_interno_cod` | `string` | sim | `enum` (ver legenda) | Programa Interno (Cód). Origem: SIAFI |
| `programa_interno_desc` | `string` | sim | — | Programa Interno (Desc). Origem: SIAFI |
| `gnd_cod` | `string` | sim | `enum` (ver legenda) | Grupo de Natureza da Despesa (Cód). Origem: SIAFI |
| `esfera_cod` | `string` | não | — | Esfera (Cód). Origem: SIAFI |
| `fonte_cod` | `string` | não | — | Fonte (Cód). Origem: SIAFI |
| `fonte_grupo_cod` | `string` | não | — | Fonte Grupo (Cód). Origem: SIAFI |
| `fonte_especificacao_cod` | `string` | não | — | Fonte Especificação (Cód). Origem: SIAFI |
| `orgao_gestor_superior_cod` | `string` | não | — | Órgão Gestor Superior (Cód). Origem: SIAFI |
| `orgao_gestor_cod` | `string` | não | — | Órgão Gestor (Cód). Origem: SIAFI |
| `ug_cod` | `string` | não | — | Unidade Gestora (Cód). Origem: SIAFI |
| `ugr_cod` | `string` | sim | — | Unidade Gestora Responsável (Cód). Origem: SIAFI |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os orçamentos. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `liquidado_valor` | `double` | sim | — | Liquidado (R$). Origem: SIAFI |
| `rp_pago_valor` | `double` | sim | — | Restos a Pagar pagos (R$). Origem: SIAFI |

### Legenda dos enums

Os três campos com `enum` só aceitam os valores abaixo — qualquer outro reprova a validação.

`origem_despesa`

| Valor | Significado |
|---|---|
| `Proposta do executivo` | Dotação originária da proposta orçamentária do Poder Executivo |
| `Emenda` | Dotação originária de emenda parlamentar |
| `-` | Não aplicável / não informado |

`programa_interno_cod`

| Valor | Significado |
|---|---|
| `20` | Pesquisa |
| `21` | Extensão |

`gnd_cod`

| Valor | Significado |
|---|---|
| `1` | Pessoal e encargos sociais |
| `3` | Outras despesas correntes |
| `4` | Investimentos |

> ℹ️ **Códigos são `string`, não número.** `programa_interno_cod` e `gnd_cod` são declarados como `string`; enviar `20` (inteiro) em vez de `"20"` reprova por tipo, antes mesmo da checagem de enum.

> ℹ️ **`referencia_pnp` agora é conferido na extração.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`, e o Coletor confere esse código contra o espelho local de estruturas antes de gravar o Parquet — a mesma checagem que a PNP faz depois do envio, antecipada. O padrão de fábrica é o **modo sombra**: a divergência é registrada no Registro de Extração, mas ainda não reprova. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### Regras de qualidade

Além do schema (campos obrigatórios, tipos, `enum` e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `orgao_superior_cod`, `uo_cod`, `acao_cod`, `ptres`, `ugr_cod` e `estrutura` não podem ser texto vazio | `mustBe: 0` |
| `liquidado_valor` e `rp_pago_valor` não podem ser negativos | `mustBe: 0` |
| Despesa de `origem_despesa: Emenda` exige `emenda_impositiva_tipo` e `emenda_impositiva_numero_ano` no formato `número/ano`; despesa de outra origem não pode trazer nenhum dos dois | `mustBe: 0` |

### Exemplo válido

```json
{
  "id_dados_orcamentarios": 1042,
  "orgao_superior_cod": "26000",
  "uo_cod": "26435",
  "acao_cod": "20RL",
  "ptres": "108963",
  "origem_despesa": "Proposta do executivo",
  "emenda_impositiva_tipo": null,
  "emenda_impositiva_numero_ano": null,
  "programa_interno_cod": "20",
  "programa_interno_desc": "Pesquisa",
  "gnd_cod": "3",
  "esfera_cod": "1",
  "fonte_cod": "1000000000",
  "fonte_grupo_cod": "1000",
  "fonte_especificacao_cod": "000000",
  "orgao_gestor_superior_cod": "26000",
  "orgao_gestor_cod": "26435",
  "ug_cod": "158155",
  "ugr_cod": "158155",
  "estrutura": "12",
  "liquidado_valor": 184320.55,
  "rp_pago_valor": 12040.00
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"uo_cod": "26435", ...}` (sem `id_dados_orcamentarios`) | `Required field 'id_dados_orcamentarios' is missing` |
| `{"id_dados_orcamentarios": 1042, "gnd_cod": "2", ...}` | `Value '2' not in enum for 'gnd_cod'` |
| `{"id_dados_orcamentarios": 1042, "programa_interno_cod": 20, ...}` (inteiro) | `Type mismatch on 'programa_interno_cod': expected string, got integer` |
| `{"id_dados_orcamentarios": 1042, "empenhado_valor": 200000, ...}` (coluna não declarada) | `Field 'empenhado_valor' not in schema (additionalFields: false)` |
| `{..., "origem_despesa": "Emenda", "emenda_impositiva_numero_ano": null}` (emenda sem número/ano) | `Dados de emenda devem ser coerentes com a origem da despesa.: Actual custom_sql(dados_orcamentarios) was 1, expected = 0` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-19 | Versão inicial. | — |

## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "orcamento"
info:
  title: "Orçamento"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados do indicador institucional de orçamento,
    a partir do subconjunto mínimo de dados financeiros (Dados Orçamentários).

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/orcamento/{model}/*.parquet"
    format: "parquet"

models:
  dados_orcamentarios:
    type: table
    title: "Dados Orçamentários"
    description: "Dados orçamentários vinculados à execução financeira institucional."
    meta:
      required: false
      disabled: false
    quality:
      - type: sql
        description: "Códigos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM dados_orcamentarios
          WHERE NULLIF(TRIM(orgao_superior_cod), '') IS NULL
             OR NULLIF(TRIM(uo_cod), '') IS NULL
             OR NULLIF(TRIM(acao_cod), '') IS NULL
             OR NULLIF(TRIM(ptres), '') IS NULL
             OR NULLIF(TRIM(ugr_cod), '') IS NULL
             OR NULLIF(TRIM(estrutura), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Valores financeiros não podem ser negativos."
        query: >
          SELECT COUNT(*) FROM dados_orcamentarios
          WHERE liquidado_valor < 0 OR rp_pago_valor < 0
        mustBe: 0
      - type: sql
        description: "Dados de emenda devem ser coerentes com a origem da despesa."
        query: >
          SELECT COUNT(*) FROM dados_orcamentarios
          WHERE (origem_despesa = 'Emenda'
                 AND (NULLIF(TRIM(emenda_impositiva_tipo), '') IS NULL
                      OR NULLIF(TRIM(emenda_impositiva_numero_ano), '') IS NULL
                      OR NOT regexp_full_match(
                           TRIM(emenda_impositiva_numero_ano),
                           '[0-9]+/[0-9]{4}'
                         )))
             OR (origem_despesa <> 'Emenda'
                 AND (NULLIF(TRIM(emenda_impositiva_tipo), '') IS NOT NULL
                      OR NULLIF(TRIM(emenda_impositiva_numero_ano), '') IS NOT NULL))
        mustBe: 0
    fields:
      id_dados_orcamentarios:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true
        description: >
          Identificador do registro.

      orgao_superior_cod:
        type: string
        required: true
        title: "Órgão Superior (Cód)(UO)"
        description: "Origem: SIAFI"

      uo_cod:
        type: string
        required: true
        title: "UO (Cód)"
        description: "Origem: SIAFI"

      acao_cod:
        type: string
        required: true
        title: "Ação (Cód)"
        description: "Origem: SIAFI"

      ptres:
        type: string
        required: true
        title: "PTRES"
        description: "Origem: SIAFI"

      origem_despesa:
        type: string
        enum:
          - "Proposta do executivo"
          - "Emenda"
          - "-"
        title: "Origem da Despesa"
        required: true
        description: "Origem: SIAFI"

      emenda_impositiva_tipo:
        type: string
        title: "Emenda Impositiva (Tipo)"
        description: "Origem: SIAFI"

      emenda_impositiva_numero_ano:
        type: string
        title: "Emenda Impositiva (Número/Ano)"
        description: "Origem: SIAFI"

      programa_interno_cod:
        type: string
        enum:
          - "20" # pesquisa
          - "21" # extensão
        title: "Programa Interno (Cód) (1)"
        required: true
        description: >
          Origem: SIAFI. Códigos: 20 (Pesquisa) e 21 (Extensão).

      programa_interno_desc:
        type: string
        title: "Programa Interno (Desc)"
        required: true
        description: "Origem: SIAFI"

      gnd_cod:
        type: string
        enum:
          - "1" # Pessoal e encargos sociais
          - "3" # Outras despesas correntes
          - "4" # Investimentos
        title: "GND (Cód)"
        required: true
        description: "Origem: SIAFI. Códigos: 1 (Pessoal e encargos sociais), 3 (Outras despesas correntes) e 4 (Investimentos)."

      esfera_cod:
        type: string
        title: "Esfera (Cód)"
        description: "Origem: SIAFI"

      fonte_cod:
        type: string
        title: "Fonte (Cód)"
        description: "Origem: SIAFI"

      fonte_grupo_cod:
        type: string
        title: "Fonte Grupo (Cód)"
        description: "Origem: SIAFI"

      fonte_especificacao_cod:
        type: string
        title: "Fonte Especificação (Cód)"
        description: "Origem: SIAFI"

      orgao_gestor_superior_cod:
        type: string
        title: "Órgão Gestor Superior (Cód)"
        description: "Origem: SIAFI"

      orgao_gestor_cod:
        type: string
        title: "Órgão Gestor (Cód)"
        description: "Origem: SIAFI"

      ug_cod:
        type: string
        title: "UG (Cód)"
        description: "Origem: SIAFI"

      ugr_cod:
        type: string
        title: "UGR (Cód) (2)"
        required: true
        description: >
          Origem: SIAFI

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os orçamentos"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      liquidado_valor:
        type: double
        required: true
        title: "Liquidado (R$)"
        description: "Origem: SIAFI"

      rp_pago_valor:
        type: double
        title: "RP Pago (R$)"
        required: true
        description: "Origem: SIAFI"

    additionalFields: false
```

