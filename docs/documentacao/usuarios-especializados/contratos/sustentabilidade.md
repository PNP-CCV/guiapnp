---
layout: default
title: "Sustentabilidade"
toc: true
---
# Sustentabilidade

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `sustentabilidade` · **Versão:** `1.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Sustentabilidade

## Resumo de negócio

Este **[Contrato de Dados](../../glossario.md#contrato-de-dados)** descreve os **dados e ações de sustentabilidade**, organizados em três subconjuntos temáticos: consumo de água e energia, governança da política de sustentabilidade, e compras e contratações sustentáveis.

A **PNP** coleta este contrato para mensurar a agenda ambiental da Rede Federal — não só o consumo físico (m³, KWh), mas a **maturidade institucional**: existe instância de governança formalmente instituída? Existe normativo de compras sustentáveis? A política é divulgada, e por onde?

É o contrato mais amplo do catálogo em número de campos declarativos, e o que mais usa campos do tipo `array` — os dois de `governanca_gestao_sustentabilidade`. O único outro `array` do catálogo é `municipios_atendidos`, em [Ações de Extensão](acoes_de_extensao).

> **Sustentabilidade também aparece fora deste contrato.** Os contratos de [Projetos de Ensino](projetos_de_ensino), [Projetos de Pesquisa](projetos_de_pesquisa.md), [Ações de Extensão](acoes_de_extensao.md) e [Desenvolvimento Institucional](projetos_desenvolvimento_institucional) carregam, cada um, uma flag `projeto_<domínio>_sustentavel`. Este contrato mede a **estrutura** de sustentabilidade; aqueles medem os **projetos** que a tocam.

## Modelos contidos

- **`agua_energia`** — consumo de água e energia e produção de energia renovável, por estrutura.
- **`governanca_gestao_sustentabilidade`** — instâncias de governança, gestão de resíduos sólidos e canais de divulgação da política.
- **`compras_contratacoes`** — volume de compras e contratações, total e com critério de sustentabilidade.

> **Os três modelos são independentes.**  Todos se organizam pela mesma granularidade — uma linha por `estrutura` (campus) —, mas essa correspondência é convenção, não constraint.

## Modelo `agua_energia`

### Resumo do modelo

Indicadores físicos de consumo e geração por estrutura. Os três valores são **totais do ano de referência**: `agua_consumo` e `energia_consumo` são somas dos consumos mensais; `prod_energia_renovavel` é a produção anual.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id` | `integer` | sim | `primaryKey` | Identificador |
| `estrutura` | `string` | não | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se os consumos e produções de água/energia. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `agua_consumo` | `double` | não | — | Soma dos consumos mensais de água, em m³. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `energia_consumo` | `double` | não | — | Soma dos consumos mensais de energia elétrica, em KWh. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `prod_energia_renovavel` | `double` | não | — | Produção anual de energia elétrica de fonte renovável, em KWh. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |

> **As unidades de medida são usadas só no título do campo.** m³ para água, KWh para energia — nada no schema impede o envio em litros ou MWh. Um campus que reporte energia em MWh passa na validação e entra no indicador mil vezes menor. Confira a unidade na origem.


### Exemplo válido

```json
{
  "id": 1,
  "estrutura": "12",
  "agua_consumo": 18420.5,
  "energia_consumo": 1247800.0,
  "prod_energia_renovavel": 96300.0
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"estrutura": "12", "agua_consumo": 18420.5}` (sem `id`) | `Required field 'id' is missing` |
| `{..., "agua_consumo": "18420,5"}` (decimal com vírgula, `double` espera número) | `Type mismatch on 'agua_consumo': expected double, got string '18420,5'` |
| `{..., "gas_consumo": 120.0}` (coluna não declarada) | `Field 'gas_consumo' not in schema (additionalFields: false)` |

## Modelo `governanca_gestao_sustentabilidade`

### Resumo do modelo

Maturidade institucional da política de sustentabilidade por estrutura: que instâncias de governança existem, como os resíduos sólidos são geridos, e por onde a política é divulgada. Usa dois campos `array` com `enum` de **códigos abreviados** — as legendas estão nas tabelas abaixo.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id` | `integer` | sim | `primaryKey` | Identificador |
| `estrutura` | `string` | não | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se a governança, implantação e divulgação da sustentabilidade. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `instancia_governanca` | `array` (de `string`) | não | `enum` por item (11 códigos — ver legenda) | Instâncias de governança formalmente instituídas para coordenar e/ou executar a política de sustentabilidade institucional |
| `col_res_solidos` | `boolean` | não | — | Existência de coletores de resíduos sólidos identificados na estrutura. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `sen_com_interna` | `boolean` | não | — | Realização de ações de sensibilização da comunidade interna sobre a gestão dos resíduos sólidos na estrutura. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `par_coop_col_seletiva` | `boolean` | não | — | Formalização de parceria com cooperativa de coleta seletiva ou comprovação de coleta seletiva pela prefeitura na estrutura. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `canais_divulgacao` | `array` (de `string`) | não | `enum` por item (4 códigos — ver legenda) | Canais de divulgação específicos da política/ações de sustentabilidade institucionais na estrutura. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |

#### Legenda de `instancia_governanca`

| Código | Significado |
|---|---|
| `COO` | coordenação |
| `DEP` | departamento |
| `DIR` | diretoria |
| `PRO` | pró-reitoria |
| `COM` | comissão |
| `NUC` | núcleo |
| `GT` | grupo de trabalho |
| `CAM` | câmara |
| `CON` | conselho |
| `CMT` | comitê |
| `OUT` | outra repartição formalmente instituída por ato normativo |

#### Legenda de `canais_divulgacao`

| Código | Significado |
|---|---|
| `PI` | páginas na internet |
| `RS` | redes sociais |
| `ER` | eventos realizados |
| `MD` | materiais didáticos |


### Exemplo válido

```json
{
  "id": 1,
  "estrutura": "12",
  "instancia_governanca": ["COM", "NUC"],
  "col_res_solidos": true,
  "sen_com_interna": true,
  "par_coop_col_seletiva": false,
  "canais_divulgacao": ["PI", "RS", "ER"]
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"estrutura": "12", "instancia_governanca": ["COM"]}` (sem `id`) | `Required field 'id' is missing` |
| `{..., "instancia_governanca": ["COMISSAO"]}` (item fora do `enum`) | `Value 'COMISSAO' for field 'instancia_governanca' not in enum [COO, DEP, DIR, PRO, COM, NUC, GT, CAM, CON, CMT, OUT]` |
| `{..., "instancia_governanca": "COM"}` (`string` em vez de `array`) | `Type mismatch on 'instancia_governanca': expected array, got string` |
| `{..., "canais_divulgacao": ["PI", "PODCAST"]}` (item fora do `enum`) | `Value 'PODCAST' for field 'canais_divulgacao' not in enum [PI, RS, ER, MD]` |
| `{..., "col_res_solidos": "sim"}` (`boolean` espera `true`/`false`) | `Type mismatch on 'col_res_solidos': expected boolean, got string 'sim'` |

## Modelo `compras_contratacoes`

### Resumo do modelo

Volume de compras e contratações por estrutura, com o recorte de quantas aplicaram pelo menos um critério de sustentabilidade. Os quatro contadores são do **ano de referência** do ciclo de coleta.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id` | `integer` | sim | `primaryKey` | Identificador |
| `estrutura` | `string` | não | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se as compras e contratações. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `realiza_compras_contratacoes` | `boolean` | não | — | A estrutura realiza compras e/ou contratações? Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `normativo_compras_sustentaveis` | `boolean` | não | — | Possui normativo que regulamenta compras e contratações com aplicação de critérios de sustentabilidade? Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `compras_sustentaveis` | `integer` | não | — | Número de compras efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `contratacoes_sustentaveis` | `integer` | não | — | Número de contratações efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `compras_geral` | `integer` | não | — | Número de compras efetivadas no ano de referência. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `contratacoes_geral` | `integer` | não | — | Número de contratações efetivadas no ano de referência. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |

> **Os subconjuntos não são checados contra os totais.** `compras_sustentaveis` é, por definição, um subconjunto de `compras_geral` — mas **nenhuma regra declarada garante isso**. `compras_sustentaveis: 90` com `compras_geral: 12` passa na validação e produz um indicador de 750%. O mesmo vale para o par de contratações, e para `realiza_compras_contratacoes: false` acompanhado de contadores positivos. Este modelo é o candidato mais óbvio do catálogo a um bloco `quality` — ver [Validação e qualidade](../validacao-e-qualidade.md).

### Exemplo válido

```json
{
  "id": 1,
  "estrutura": "12",
  "realiza_compras_contratacoes": true,
  "normativo_compras_sustentaveis": true,
  "compras_sustentaveis": 47,
  "contratacoes_sustentaveis": 12,
  "compras_geral": 312,
  "contratacoes_geral": 58
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"estrutura": "12", "compras_geral": 312}` (sem `id`) | `Required field 'id' is missing` |
| `{..., "compras_geral": 312.5}` (`integer` não aceita decimal) | `Type mismatch on 'compras_geral': expected integer, got double` |
| `{..., "normativo_compras_sustentaveis": 1}` (`boolean` espera `true`/`false`) | `Type mismatch on 'normativo_compras_sustentaveis': expected boolean, got integer` |
| `{..., "valor_compras": 480000.0}` (coluna não declarada) | `Field 'valor_compras' not in schema (additionalFields: false)` |

## `referencia_pnp` — metadado declarativo, não validação

Os três modelos declaram, no campo `estrutura`, um bloco `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`. .


## Contrato de Dados - Formato YAML

```yaml
dataContractSpecification: "1.2.0"
id: "sustentabilidade"
info:
  title: "Sustentabilidade"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados dos indicadores institucionais de sustentabilidade,
    organizados por subconjuntos temáticos (água/energia, governança e gestão da sustentabilidade,
    entre outros).

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/sustentabilidade/{model}/*.parquet"
    format: "parquet"

models:
  agua_energia:
    type: table
    title: "Água e Energia"
    description: "Indicadores de consumo de água e energia e de produção de energia renovável."
    fields:
      id:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os consumos e produções de água/energia"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      agua_consumo:
        type: double
        title: "Soma dos consumos mensais de água, em m³"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      energia_consumo:
        type: double
        title: "Soma dos consumos mensais de energia elétrica, em KWh"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      prod_energia_renovavel:
        type: double
        title: "Produção anual de energia elétrica de fonte renovável, em KWh"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."
    additionalFields: false

  governanca_gestao_sustentabilidade:
    type: table
    title: "Governança e Gestão da Sustentabilidade"
    description: "Indicadores de governança, implantação e divulgação da política de sustentabilidade institucional."
    fields:
      id:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se a governança, implantação e divulgação da sustentabilidade"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      instancia_governanca:
        type: array
        items:
          type: string
          enum:
            - "COO"  # coordenação
            - "DEP"  # departamento
            - "DIR"  # diretoria
            - "PRO"  # pró-reitoria
            - "COM"  # comissão
            - "NUC"  # núcleo
            - "GT"   # grupo de trabalho
            - "CAM"  # câmara
            - "CON"  # conselho
            - "CMT"  # comitê
            - "OUT"  # outra repartição formalmente instituída por ato normativo
        title: "Instâncias de governança formalmente instituídas"
        description: >
          Instâncias de governança formalmente instituídas para coordenar e/ou executar a
          política de sustentabilidade institucional.

      col_res_solidos:
        type: boolean
        title: "Existência de coletores de resíduos sólidos identificados na estrutura"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      sen_com_interna:
        type: boolean
        title: "Realização de ações de sensibilização da comunidade interna sobre a gestão dos resíduos sólidos na estrutura"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      par_coop_col_seletiva:
        type: boolean
        title: "Formalização de parceria com cooperativa de coleta seletiva ou comprovação de coleta seletiva pela prefeitura na estrutura"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      canais_divulgacao:
        type: array
        items:
          type: string
          enum:
            - "PI"  # páginas na internet
            - "RS"  # redes sociais
            - "ER"  # eventos realizados
            - "MD"  # materiais didáticos
        title: "Canais de divulgação específicos da política/ações de sustentabilidade institucionais na estrutura"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."
    additionalFields: false

  compras_contratacoes:
    type: table
    title: "Compras e Contratações"
    description: "Indicadores sobre compras e contratações institucionais com aplicação de critérios de sustentabilidade."
    fields:
      id:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se as compras e contratações"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      realiza_compras_contratacoes:
        type: boolean
        title: "A estrutura realiza compras e/ou contratações?"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      normativo_compras_sustentaveis:
        type: boolean
        title: "Possui normativo que regulamenta compras e contratações com aplicação de critérios de sustentabilidade?"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      compras_sustentaveis:
        type: integer
        title: "Número de compras efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      contratacoes_sustentaveis:
        type: integer
        title: "Número de contratações efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      compras_geral:
        type: integer
        title: "Número de compras efetivadas no ano de referência"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      contratacoes_geral:
        type: integer
        title: "Número de contratações efetivadas no ano de referência"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."
    additionalFields: false
```
