---
layout: default
title: "Orçamento"
toc: true
---

* TOC
{:toc}

# Orçamento

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `orcamento` · **Versão:** `1.0.3` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Orçamento

## Resumo de negócio

Este **[Contrato de Dados]({{site.baseurl}}/documentacao/coletor/glossario#contrato-de-dados)** descreve o indicador institucional de **orçamento**, a partir do subconjunto mínimo de dados financeiros (Dados Orçamentários). Cada registro é uma linha de execução orçamentária extraída do **Siafi** (via ODI), com a classificação orçamentária completa (órgão, UO, ação, PTRES, fonte, GND) e os valores efetivamente **liquidados** e de **restos a pagar pagos**.

A **[PNP]({{site.baseurl}}/documentacao/coletor/glossario#pnp)** coleta este contrato para conhecer o gasto público executado por estrutura e por classificação orçamentária.


### Uso do Tesouro Gerencial

Para o contrato, sugere-se que os dados sejam obtidos por meio do Tesouro Gerencial, realizando consulta com os seguintes parâmetros: 

Filtro do relatório: ({Item Informação} = 31:DESPESAS LIQUIDADAS (CONTROLE EMPENHO), 44:RESTOS A PAGAR NAO PROCESSADOS LIQUIDADOS) E ({Órgão UGE} = 26XXX:NOME INSTITUIÇÃO) E ({Ano Lançamento} = 2025) E ({Unidade Orçamentária} = 26XXX:NOME INSTITUIÇÃO)

Template:
- Órgão UGE - Órgão Superior 
- Unidade Orçamentária 
- Ação Governo 
- PTRES 
- Resultado Primário Lei
- Autor Emendas Orçamento
- PI 
- Grupo Despesa 
- Esfera Orçamentária 
- Fonte Recursos Detalhada 
- Fonte Recursos Reduzida 
- Grupo Fonte 
- Fonte Recursos 
- UG Executora 
- UG Responsável 
- Item Informação 

**Métrica**:
- Movim. Líquido - R$ (Item Informação) 
- Valor do Movimento Líquido, em Real. Para uso concomitante com o atributo "Item Informação". 
- {Movim. Líquido no mês - R$ (Item Informação)} + {Var.Cambial Saldo ant. - R$ (Item Informação)}

## Modelos contidos

- **`dados_orcamentarios`** *(opcional no fluxo)* — dados orçamentários vinculados à execução financeira institucional.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{site.baseurl}}/documentacao/coletor/glossario#configuracao-de-extracao)** para `dados_orcamentarios`.

## Modelo `dados_orcamentarios`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é uma combinação de classificação orçamentária com os valores executados no período. A granularidade é definida pela origem (SIAFI) — o contrato não declara chave composta, apenas o `id` técnico do registro.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_dados_orcamentarios` | `integer` | sim | `primaryKey` | Identificador do registro |
| `ano` | `integer` | sim | — | Ano da execução orçamentária. Formato: `AAAA` |
| `orgao_superior_cod` | `string` | sim | `enum` (ver legenda) | Órgão Superior (Cód)(UO). Origem: SIAFI |
| `uo_cod` | `string` | sim | — | Unidade Orçamentária (Cód). Origem: SIAFI |
| `acao_cod` | `string` | sim | — | Ação (Cód). Origem: SIAFI |
| `ptres` | `string` | sim | — | Programa de Trabalho Resumido. Origem: SIAFI |
| `origem_despesa` | `string` | sim | `enum` (ver legenda) | Origem da Despesa. Origem: SIAFI |
| `emenda_impositiva_tipo` | `string` | não | — | Emenda Impositiva (Tipo). Origem: SIAFI |
| `emenda_impositiva_numero_ano` | `string` | não | — | Emenda Impositiva (Número/Ano). Origem: SIAFI |
| `programa_interno_cod` | `string` | sim | `minLength: 11`, `maxLength: 11` | Programa Interno (Cód). Exatamente 11 caracteres. Origem: SIAFI |
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

`orgao_superior_cod`

| Valor | Significado |
|---|---|
| `26000` | Ministério da Educação |

`gnd_cod`

| Valor | Significado |
|---|---|
| `1` | Pessoal e encargos sociais |
| `3` | Outras despesas correntes |
| `4` | Investimentos |
| `5` | Inversões financeiras |

> ℹ️ **Códigos são `string`, não número.** `orgao_superior_cod` e `gnd_cod` são declarados como `string`; enviar `26000` (inteiro) em vez de `"26000"` reprova por tipo, antes mesmo da checagem de enum.

> ℹ️ **`referencia_pnp` agora é conferido na extração.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`, e o Coletor confere esse código contra o espelho local de estruturas antes de gravar o Parquet — a mesma checagem que a PNP faz depois do envio, antecipada. Como a `severidade` declarada é `erro`, um código que não existe no cadastro **reprova o teste do contrato** — a extração conclui, mas o apontamento aparece em **Ver resultados de teste**, com o campo e as linhas envolvidas, e o envio à PNP fica barrado. Ver [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### Regras de qualidade

Além do schema (campos obrigatórios, tipos, `enum` e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `orgao_superior_cod`, `uo_cod`, `acao_cod`, `ptres`, `ugr_cod` e `estrutura` não podem ser texto vazio | `mustBe: 0` |
| `liquidado_valor` e `rp_pago_valor` não podem ser negativos | `mustBe: 0` |
| `ano` tem de ser o **ano de referência** da coleta | `mustBe: 0` |
| `uo_cod` tem de ser o **código da instituição** na PNP | `mustBe: 0` |
| Despesa de `origem_despesa: Emenda` exige `emenda_impositiva_tipo` e `emenda_impositiva_numero_ano` no formato `número/ano`; despesa de outra origem não pode trazer nenhum dos dois | `mustBe: 0` |

> ℹ️ **Ano de referência.** A regra do `ano` usa o token `#ANO_REFERENCIA#`, substituído pelo Coletor antes de o contrato chegar ao motor: é o **ano-base** da coleta, `ciclo.ano - 1` (o ciclo de 2026 coleta a execução de 2025). Contrato que usa o token sem ciclo de coleta associado falha com erro explícito, em vez de mandar SQL quebrado ao motor.

> ℹ️ **Código da instituição.** A regra de `uo_cod` usa o token `#CODIGO_INSTITUICAO#`, substituído pelo Coletor antes de o contrato chegar ao motor: é o código que a PNP devolve para a instituição da instância (IFRN é `26435`). Se a instância ainda não obteve o código, o teste do contrato reprova com erro explícito; salvar as **Configurações** da instância resolve.

### Exemplo válido

```json
{
  "id_dados_orcamentarios": 1042,
  "ano": 2025,
  "orgao_superior_cod": "26000",
  "uo_cod": "26435",
  "acao_cod": "20RL",
  "ptres": "108963",
  "origem_despesa": "Proposta do executivo",
  "emenda_impositiva_tipo": null,
  "emenda_impositiva_numero_ano": null,
  "programa_interno_cod": "M20RLP0100N",
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
| `{"id_dados_orcamentarios": 1042, "programa_interno_cod": "20", ...}` (menos de 11 caracteres) | `Check that field programa_interno_cod has a min length of 11` |
| `{"id_dados_orcamentarios": 1042, "ano": 2024, ...}` (ciclo 2026, ano de referência 2025) | `O ano deve ser o ano de referência.: Actual custom_sql(dados_orcamentarios) was 1, expected = 0` |
| `{"id_dados_orcamentarios": 1042, "ano": "2025", ...}` (`string` em vez de `integer`) | `Type mismatch on 'ano': expected integer, got string` |
| `{"id_dados_orcamentarios": 1042, "empenhado_valor": 200000, ...}` (coluna não declarada) | `Field 'empenhado_valor' not in schema (additionalFields: false)` |
| `{..., "origem_despesa": "Emenda", "emenda_impositiva_numero_ano": null}` (emenda sem número/ano) | `Dados de emenda devem ser coerentes com a origem da despesa.: Actual custom_sql(dados_orcamentarios) was 1, expected = 0` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-19 | Versão inicial. | — |
| `1.0.1` | 2026-10-27 | `programa_interno_cod` passa a exigir exatamente 11 caracteres (`minLength`/`maxLength`). | Sim — códigos com outro tamanho são reprovados no teste de qualidade. |
| `1.0.2` | 2026-10-27 | Novo campo obrigatório `ano` (`integer`), que tem de ser o ano de referência da coleta (`#ANO_REFERENCIA#`). | Sim — extrações sem a coluna `ano` são rejeitadas no schema, e anos diferentes do de referência reprovam o teste de qualidade. |
| `1.0.3` | 2026-10-27 | Regra `quality` nova: `uo_cod` tem de ser o código da instituição (`#CODIGO_INSTITUICAO#`). | Sim — linhas com UO de outra instituição reprovam o teste de qualidade. |

## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "orcamento"
info:
  title: "Orçamento"
  version: "1.0.3"
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
        description: "O ano deve ser o ano de referência."
        query: >
          SELECT COUNT(*) FROM dados_orcamentarios
          WHERE ano <> #ANO_REFERENCIA#
        mustBe: 0
      - type: sql
        description: "Todos os códigos UO devem ser da mesma instituição."
        query: >
          SELECT COUNT(*) FROM dados_orcamentarios
          WHERE uo_cod <> '#CODIGO_INSTITUICAO#'
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

      ano:
        type: integer
        required: true
        title: "Ano"
        description: "Ano da execução orçamentária. Formato: AAAA"

      orgao_superior_cod:
        type: string
        enum:
          - "26000" # Ministério da Educação
        required: true
        title: "Órgão Superior (Cód)(UO)"
        description: "Origem: SIAFI."

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
        title: "Programa Interno (Cód) (1)"
        required: true
        minLength: 11
        maxLength: 11
        description: >
          Origem: SIAFI. Deve ter exatamente 11 caracteres.

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
          - "5" # Inversões financeiras
        title: "GND (Cód)"
        required: true
        description: "Origem: SIAFI. Códigos: 1 (Pessoal e encargos sociais), 3 (Outras despesas correntes), 4 (Investimentos) e 5 (Inversões financeiras)."

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

