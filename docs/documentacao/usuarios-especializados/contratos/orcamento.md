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

Este **Contrato de Dados** descreve o indicador institucional de **orçamento**, a partir do subconjunto mínimo de dados financeiros (Dados Orçamentários). Cada registro é uma linha de execução orçamentária extraída do **Siafi** (via ODI), com a classificação orçamentária completa (órgão, UO, ação, PTRES, fonte, GND) e os valores efetivamente **liquidados** e de **restos a pagar pagos**.

A **PNP** coleta este contrato para relacionar gasto público executado para apoiar as ações de pesquisa e extensão, em especial para os indicadores que analisam quanto do orçamento institucional é aplicado nessas respectivas ações.

## Modelos contidos

- **`dados_orcamentarios`** *(opcional no fluxo)* — dados orçamentários vinculados à execução financeira institucional.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `dados_orcamentarios`.

## Modelo `dados_orcamentarios`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é uma combinação de classificação orçamentária com os valores executados no período. 

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id` | `integer` | sim | `primaryKey` | Identificador do registro |
| `orgao_superior_cod` | `integer` | sim | — | Órgão Superior (Cód)(UO). Origem: (Siafi) |
| `uo_cod` | `string` | sim | — | Unidade Orçamentária (Cód). Origem: (Siafi) |
| `acao_cod` | `string` | sim | — | Ação (Cód). Origem: (Siafi) |
| `ptres` | `string` | sim | — | Programa de Trabalho Resumido. Origem: (Siafi) |
| `origem_despesa` | `string` | sim | `enum` (ver legenda) | Origem da Despesa. Origem: (Siafi) |
| `emenda_impositiva_tipo` | `string` | não | — | Emenda Impositiva (Tipo). Origem: (Siafi) |
| `emenda_impositiva_numero_ano` | `string` | não | — | Emenda Impositiva (Número/Ano). Origem: (Siafi) |
| `programa_interno_cod` | `string` | sim | `enum` (ver legenda) | Programa Interno (Cód). Origem: (Siafi) |
| `programa_interno_desc` | `string` | sim | — | Programa Interno (Desc). Origem: (Siafi) |
| `gnd_cod` | `string` | sim | `enum` (ver legenda) | Grupo de Natureza da Despesa (Cód). Origem: (Siafi) |
| `esfera_cod` | `string` | não | — | Esfera (Cód). Origem: (Siafi) |
| `fonte_cod` | `string` | não | — | Fonte (Cód). Origem: (Siafi) |
| `fonte_grupo_cod` | `string` | não | — | Fonte Grupo (Cód). Origem: (Siafi) |
| `fonte_especificacao_cod` | `string` | não | — | Fonte Especificação (Cód). Origem:  (Siafi) |
| `orgao_gestor_superior_cod` | `string` | não | — | Órgão Gestor Superior (Cód). Origem:  (Siafi) |
| `orgao_gestor_cod` | `string` | não | — | Órgão Gestor (Cód). Origem: (Siafi) |
| `ug_cod` | `string` | não | — | Unidade Gestora (Cód). Origem:  (Siafi) |
| `ugr_cod` | `string` | sim | — | Unidade Gestora Responsável (Cód). Origem: (Siafi) |
| `estrutura_vinculada` | `string` | sim | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se os orçamentos. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `liquidado_valor` | `double` | sim | — | Liquidado (R$). Origem:  (Siafi) |
| `rp_pago_valor` | `double` | sim | — | Restos a Pagar pagos (R$). Origem: (Siafi) |

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

> **Códigos são `string`, não número.** `programa_interno_cod` e `gnd_cod` são declarados como `string`; enviar `20` (inteiro) em vez de `"20"` reprova por tipo, antes mesmo da checagem de enum.

> **`referencia_pnp` é metadado declarativo, não validação.** O campo `estrutura_vinculada` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`.


### Exemplo válido

```json
{
  "id": 1042,
  "orgao_superior_cod": 26000,
  "uo_cod": "26435",
  "acao_cod": "20RL",
  "ptres": "108963",
  "origem_despesa": "Proposta do executivo",
  "emenda_impositiva_tipo": "-",
  "emenda_impositiva_numero_ano": "-",
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
  "estrutura_vinculada": "12",
  "liquidado_valor": 184320.55,
  "rp_pago_valor": 12040.00
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"uo_cod": "26435", ...}` (sem `id`) | `Required field 'id' is missing` |
| `{"id": 1042, "gnd_cod": "2", ...}` | `Value '2' not in enum for 'gnd_cod'` |
| `{"id": 1042, "programa_interno_cod": 20, ...}` (inteiro) | `Type mismatch on 'programa_interno_cod': expected string, got integer` |
| `{"id": 1042, "empenhado_valor": 200000, ...}` (coluna não declarada) | `Field 'empenhado_valor' not in schema (additionalFields: false)` |



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
    fields:
      id:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true
        description: >
          Identificador do registro.

      orgao_superior_cod:
        type: integer
        title: "Órgão Superior (Cód)(UO)"
        description: "Origem: (Siafi)"

      uo_cod:
        type: string
        title: "UO (Cód)"
        description: "Origem: (Siafi)"

      acao_cod:
        type: string
        title: "Ação (Cód)"
        description: "Origem: (Siafi)"

      ptres:
        type: string
        title: "PTRES"
        description: "Origem: (Siafi)"

      origem_despesa:
        type: string
        enum:
          - "Proposta do executivo"
          - "Emenda"
          - "-"
        title: "Origem da Despesa"
        description: "Origem:  (Siafi)"

      emenda_impositiva_tipo:
        type: string
        title: "Emenda Impositiva (Tipo)"
        description: "Origem:  (Siafi)"

      emenda_impositiva_numero_ano:
        type: string
        title: "Emenda Impositiva (Número/Ano)"
        description: "Origem:  (Siafi)"

      programa_interno_cod:
        type: string
        enum:
          - "20"  # pesquisa
          - "21"  # extensão
        title: "Programa Interno (Cód) (1)"
        description: >
          Origem: (Siafi)

      programa_interno_desc:
        type: string
        title: "Programa Interno (Desc)"
        description: "Origem: (Siafi)"

      gnd_cod:
        type: string
        enum:
          - "1"  # Pessoal e encargos sociais
          - "3"  # Outras despesas correntes
          - "4"  # Investimentos
        title: "GND (Cód)"
        description: "Origem:  (Siafi)"

      esfera_cod:
        type: string
        title: "Esfera (Cód)"
        description: "Origem:  (Siafi)"

      fonte_cod:
        type: string
        title: "Fonte (Cód)"
        description: "Origem:  (Siafi)"

      fonte_grupo_cod:
        type: string
        title: "Fonte Grupo (Cód)"
        description: "Origem:  (Siafi)"

      fonte_especificacao_cod:
        type: string
        title: "Fonte Especificação (Cód)"
        description: "Origem:  (Siafi)"

      orgao_gestor_superior_cod:
        type: string
        title: "Órgão Gestor Superior (Cód)"
        description: "Origem:  (Siafi)"

      orgao_gestor_cod:
        type: string
        title: "Órgão Gestor (Cód)"
        description: "Origem:  (Siafi)"

      ug_cod:
        type: string
        title: "UG (Cód)"
        description: "Origem:  (Siafi)"

      ugr_cod:
        type: string
        title: "UGR (Cód) (2)"
        description: >
          Origem: (Siafi)

      estrutura_vinculada:
        type: string
        title: "Estrutura à qual vinculam-se os orçamentos"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      liquidado_valor:
        type: double
        title: "Liquidado (R$)"
        description: "Origem:  (Siafi)"

      rp_pago_valor:
        type: double
        title: "RP Pago (R$)"
        description: "Origem: (Siafi)"

    additionalFields: false

```

