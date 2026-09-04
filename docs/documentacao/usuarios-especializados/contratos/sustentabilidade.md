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

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **indicadores institucionais de sustentabilidade**, organizados em três subconjuntos temáticos: consumo de água e energia, governança da política de sustentabilidade, e compras e contratações sustentáveis.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar a agenda ambiental da Rede Federal — não só o consumo físico (m³, KWh), mas a **maturidade institucional**: existe instância de governança formalmente instituída? Existe normativo de compras sustentáveis? A política é divulgada, e por onde?

É o contrato mais amplo do catálogo em número de campos declarativos, e o que mais usa campos do tipo `array` — os dois de `governanca_gestao_sustentabilidade`. O único outro `array` do catálogo é `municipios_atendidos`, em [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao).

> ℹ️ **Sustentabilidade também aparece fora deste contrato.** Os contratos de [Projetos de Ensino]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_ensino), [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa), [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) e [Desenvolvimento Institucional]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_desenvolvimento_institucional) carregam, cada um, uma flag `projeto_<domínio>_sustentavel`. Este contrato mede a **estrutura** de sustentabilidade; aqueles medem os **projetos** que a tocam.

## Modelos contidos

- **`agua_energia`** *(obrigatório no fluxo)* — consumo de água e energia e produção de energia renovável, por estrutura.
- **`governanca_gestao_sustentabilidade`** *(obrigatório no fluxo)* — instâncias de governança, gestão de resíduos sólidos e canais de divulgação da política.
- **`compras_contratacoes`** *(obrigatório no fluxo)* — volume de compras e contratações, total e com critério de sustentabilidade.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

> ℹ️ **Os três modelos são independentes.** Nenhum declara `references` para outro. Todos se organizam pela mesma granularidade — uma linha por `estrutura` (campus) —, mas essa correspondência é convenção, não constraint.

## Modelo `agua_energia`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Indicadores físicos de consumo e geração por estrutura. Os três valores são **totais do ano de referência**: `agua_consumo` e `energia_consumo` são somas dos consumos mensais; `prod_energia_renovavel` é a produção anual.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_agua_energia` | `integer` | sim | `primaryKey` | Identificador único do registro |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os consumos e produções de água/energia. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `agua_consumo` | `double` | sim | — | Soma dos consumos mensais de água, em m³ |
| `energia_consumo` | `double` | sim | — | Soma dos consumos mensais de energia elétrica, em KWh |
| `prod_energia_renovavel` | `double` | sim | — | Produção anual de energia elétrica de fonte renovável, em KWh |

> ℹ️ **As unidades vivem só no título do campo.** m³ para água, KWh para energia — nada no schema impede o envio em litros ou MWh. Um campus que reporte energia em MWh passa na validação e entra no indicador mil vezes menor. Confira a unidade na origem.

### Regras de qualidade

Além do schema, o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `agua_consumo`, `energia_consumo` e `prod_energia_renovavel` não podem ser negativos | `mustBe: 0` |
| `estrutura` não pode ser texto vazio | `mustBe: 0` |
| Cada estrutura só pode ter um registro de água e energia | `mustBe: 0` |

### Exemplo válido

```json
{
  "id_agua_energia": 1,
  "estrutura": "12",
  "agua_consumo": 18420.5,
  "energia_consumo": 1247800.0,
  "prod_energia_renovavel": 96300.0
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"estrutura": "12", "agua_consumo": 18420.5}` (sem `id_agua_energia`) | `Required field 'id_agua_energia' is missing` |
| `{..., "agua_consumo": -1.0}` (consumo negativo) | `Consumos e produção de energia não podem ser negativos.: Actual custom_sql(agua_energia) was 1, expected = 0` |
| `{..., "agua_consumo": "18420,5"}` (decimal com vírgula, `double` espera número) | `Type mismatch on 'agua_consumo': expected double, got string '18420,5'` |
| `{..., "gas_consumo": 120.0}` (coluna não declarada) | `Field 'gas_consumo' not in schema (additionalFields: false)` |

## Modelo `governanca_gestao_sustentabilidade`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Maturidade institucional da política de sustentabilidade por estrutura: que instâncias de governança existem, como os resíduos sólidos são geridos, e por onde a política é divulgada. Usa dois campos `array` com `enum` de **códigos abreviados** — as legendas estão nas tabelas abaixo.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_governanca_gestao_sustentabilidade` | `integer` | sim | `primaryKey` | Identificador único do registro |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se a governança, implantação e divulgação da sustentabilidade. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `instancia_governanca` | `array` (de `string`) | sim | `enum` por item (11 códigos — ver legenda) | Instâncias de governança formalmente instituídas para coordenar e/ou executar a política de sustentabilidade institucional |
| `col_res_solidos` | `boolean` | sim | — | Existência de coletores de resíduos sólidos identificados na estrutura |
| `sen_com_interna` | `boolean` | sim | — | Realização de ações de sensibilização da comunidade interna sobre a gestão dos resíduos sólidos na estrutura |
| `par_coop_col_seletiva` | `boolean` | sim | — | Formalização de parceria com cooperativa de coleta seletiva ou comprovação de coleta seletiva pela prefeitura na estrutura |
| `canais_divulgacao` | `array` (de `string`) | sim | `enum` por item (4 códigos — ver legenda) | Canais de divulgação específicos da política/ações de sustentabilidade institucionais na estrutura |

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

> ℹ️ **As legendas só existem como comentário no YAML.** Os significados acima estão em comentários `#` ao lado de cada valor do `enum` no arquivo de fixture — comentário YAML é invisível para qualquer parser, inclusive o `datacontract-cli`. Do ponto de vista da validação, `COO` e `CMT` são apenas duas strings permitidas. Esta página é o único lugar do projeto onde a legenda é legível por máquina de busca ou por gente.

> ℹ️ **O `enum` vale por item, não pelo array.** `instancia_governanca` é uma lista: cada elemento precisa estar no `enum`. Array vazio ou com valores repetidos, que o schema sozinho aceitaria, é barrado pela primeira regra de qualidade abaixo.

### Regras de qualidade

Além do schema, o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `instancia_governanca` e `canais_divulgacao` precisam de ao menos um item, e sem valores repetidos | `mustBe: 0` |
| `estrutura` não pode ser texto vazio | `mustBe: 0` |
| Cada estrutura só pode ter um registro de governança e gestão da sustentabilidade | `mustBe: 0` |

### Exemplo válido

```json
{
  "id_governanca_gestao_sustentabilidade": 1,
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
| `{"estrutura": "12", "instancia_governanca": ["COM"]}` (sem `id_governanca_gestao_sustentabilidade`) | `Required field 'id_governanca_gestao_sustentabilidade' is missing` |
| `{..., "canais_divulgacao": []}` (array vazio) | `Arrays de governança e divulgação devem possuir ao menos um item e não podem conter valores duplicados.: Actual custom_sql(governanca_gestao_sustentabilidade) was 1, expected = 0` |
| `{..., "instancia_governanca": ["COMISSAO"]}` (item fora do `enum`) | `Value 'COMISSAO' for field 'instancia_governanca' not in enum [COO, DEP, DIR, PRO, COM, NUC, GT, CAM, CON, CMT, OUT]` |
| `{..., "instancia_governanca": "COM"}` (`string` em vez de `array`) | `Type mismatch on 'instancia_governanca': expected array, got string` |
| `{..., "canais_divulgacao": ["PI", "PODCAST"]}` (item fora do `enum`) | `Value 'PODCAST' for field 'canais_divulgacao' not in enum [PI, RS, ER, MD]` |
| `{..., "col_res_solidos": "sim"}` (`boolean` espera `true`/`false`) | `Type mismatch on 'col_res_solidos': expected boolean, got string 'sim'` |

## Modelo `compras_contratacoes`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Volume de compras e contratações por estrutura, com o recorte de quantas aplicaram pelo menos um critério de sustentabilidade. Os quatro contadores são do **ano de referência** do ciclo de coleta.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_compras_contratacoes` | `integer` | sim | `primaryKey` | Identificador único do registro |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se as compras e contratações. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `normativo_compras_sustentaveis` | `boolean` | sim | — | Possui normativo que regulamenta compras e contratações com aplicação de critérios de sustentabilidade? |
| `compras_sustentaveis` | `integer` | sim | — | Número de compras efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência |
| `contratacoes_sustentaveis` | `integer` | sim | — | Número de contratações efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência |
| `compras_geral` | `integer` | sim | — | Número de compras efetivadas no ano de referência |
| `contratacoes_geral` | `integer` | sim | — | Número de contratações efetivadas no ano de referência |

> ℹ️ **Os subconjuntos agora são checados contra os totais.** `compras_sustentaveis` é, por definição, um subconjunto de `compras_geral`, e a segunda regra de qualidade abaixo faz valer isso — `compras_sustentaveis: 90` com `compras_geral: 12`, que antes passava e produzia um indicador de 750%, hoje reprova o teste do contrato. Ver [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade).

### Regras de qualidade

Além do schema, o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| Os quatro contadores não podem ser negativos | `mustBe: 0` |
| `compras_sustentaveis` não pode superar `compras_geral`, nem `contratacoes_sustentaveis` superar `contratacoes_geral` | `mustBe: 0` |
| `estrutura` não pode ser texto vazio | `mustBe: 0` |
| Cada estrutura só pode ter um registro de compras e contratações | `mustBe: 0` |

### Exemplo válido

```json
{
  "id_compras_contratacoes": 1,
  "estrutura": "12",
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
| `{"estrutura": "12", "compras_geral": 312}` (sem `id_compras_contratacoes`) | `Required field 'id_compras_contratacoes' is missing` |
| `{..., "compras_sustentaveis": 90, "compras_geral": 12}` (subconjunto maior que o total) | `Quantidades sustentáveis não podem superar os respectivos totais.: Actual custom_sql(compras_contratacoes) was 1, expected = 0` |
| `{..., "compras_geral": 312.5}` (`integer` não aceita decimal) | `Type mismatch on 'compras_geral': expected integer, got double` |
| `{..., "normativo_compras_sustentaveis": 1}` (`boolean` espera `true`/`false`) | `Type mismatch on 'normativo_compras_sustentaveis': expected boolean, got integer` |
| `{..., "valor_compras": 480000.0}` (coluna não declarada) | `Field 'valor_compras' not in schema (additionalFields: false)` |

## `referencia_pnp` — conferido na extração

Os três modelos declaram, no campo `estrutura`, um bloco `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`. O Coletor confere esse código contra o espelho local de estruturas antes de gravar o Parquet, antecipando a checagem que a PNP faz depois do envio. Como a `severidade` declarada é `erro`, um código que não existe no cadastro **reprova o teste do contrato** — a extração conclui, mas o apontamento aparece em **Ver resultados de teste**, com o campo e as linhas envolvidas, e o envio à PNP fica barrado. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-16 | Versão inicial documentada nesta data. | — |

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
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Consumos e produção de energia não podem ser negativos."
        query: >
          SELECT COUNT(*) FROM agua_energia
          WHERE agua_consumo < 0 OR energia_consumo < 0 OR prod_energia_renovavel < 0
        mustBe: 0
      - type: sql
        description: "A estrutura deve ser preenchida com um valor não vazio."
        query: >
          SELECT COUNT(*) FROM agua_energia
          WHERE NULLIF(TRIM(estrutura), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Cada estrutura deve possuir apenas um registro de água e energia."
        query: >
          SELECT COUNT(*) FROM (
            SELECT TRIM(estrutura)
            FROM agua_energia
            WHERE NULLIF(TRIM(estrutura), '') IS NOT NULL
            GROUP BY TRIM(estrutura) HAVING COUNT(*) > 1
          ) estruturas_duplicadas
        mustBe: 0
    fields:
      id_agua_energia:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true
        description: "Identificador único do registro de consumo de água e energia e produção de energia renovável."

      estrutura:
        type: string
        required: true
        title: "Estrutura à qual vinculam-se os consumos e produções de água/energia"
        description: >
          Formato: {codigo}. Fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      agua_consumo:
        type: double
        required: true
        title: "Consumo anual de água, em m³"
        description: "Soma dos consumos mensais de água, em m³"

      energia_consumo:
        type: double
        required: true
        title: "Consumo anual de energia elétrica, em KWh"
        description: "Soma dos consumos mensais de energia elétrica, em KWh"

      prod_energia_renovavel:
        type: double
        required: true
        title: "Produção anual de energia elétrica de fonte renovável, em KWh"
        description: "Soma da produção mensal de energia elétrica de fonte renovável, em KWh"
    additionalFields: false

  governanca_gestao_sustentabilidade:
    type: table
    title: "Governança e Gestão da Sustentabilidade"
    description: "Indicadores de governança, implantação e divulgação da política de sustentabilidade institucional."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Arrays de governança e divulgação devem possuir ao menos um item e não podem conter valores duplicados."
        query: >
          SELECT COUNT(*) FROM governanca_gestao_sustentabilidade
          WHERE len(coalesce(instancia_governanca, [])) = 0
             OR len(coalesce(canais_divulgacao, [])) = 0
             OR array_length(instancia_governanca) <> array_length(array_distinct(instancia_governanca))
             OR array_length(canais_divulgacao) <> array_length(array_distinct(canais_divulgacao))
        mustBe: 0
      - type: sql
        description: "A estrutura deve ser preenchida com um valor não vazio."
        query: >
          SELECT COUNT(*) FROM governanca_gestao_sustentabilidade
          WHERE NULLIF(TRIM(estrutura), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Cada estrutura deve possuir apenas um registro de governança e gestão da sustentabilidade."
        query: >
          SELECT COUNT(*) FROM (
            SELECT TRIM(estrutura)
            FROM governanca_gestao_sustentabilidade
            WHERE NULLIF(TRIM(estrutura), '') IS NOT NULL
            GROUP BY TRIM(estrutura) HAVING COUNT(*) > 1
          ) estruturas_duplicadas
        mustBe: 0
    fields:
      id_governanca_gestao_sustentabilidade:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true
        description: "Identificador único do registro de governança, implantação e divulgação da política de sustentabilidade institucional."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se a governança, implantação e divulgação da sustentabilidade"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      instancia_governanca:
        type: array
        required: true
        items:
          type: string
          enum:
            - "COO" # coordenação
            - "DEP" # departamento
            - "DIR" # diretoria
            - "PRO" # pró-reitoria
            - "COM" # comissão
            - "NUC" # núcleo
            - "GT" # grupo de trabalho
            - "CAM" # câmara
            - "CON" # conselho
            - "CMT" # comitê
            - "OUT" # outra repartição formalmente instituída por ato normativo
        title: "Instâncias de governança formalmente instituídas"
        description: >
          Instâncias de governança formalmente instituídas para coordenar e/ou executar a
          política de sustentabilidade institucional vinculadas a estrutura. COO = coordenação; DEP = departamento; DIR = diretoria; PRO = pró-reitoria; COM = comissão; NUC = núcleo; GT = grupo de trabalho; CAM = câmara; CON = conselho; CMT = comitê; OUT = outra repartição formalmente instituída por ato normativo.

      col_res_solidos:
        type: boolean
        required: true
        title: "Existência de coletores de resíduos sólidos identificados na estrutura"
        description: "Existem coletores de resíduos sólidos identificados na estrutura, para coleta seletiva e/ou resíduos perigosos?"

      sen_com_interna:
        type: boolean
        required: true
        title: "Realização de ações de sensibilização da comunidade interna sobre a gestão dos resíduos sólidos na estrutura"
        description: "A estrutura realiza ações de sensibilização da comunidade interna sobre a gestão dos resíduos sólidos?"

      par_coop_col_seletiva:
        type: boolean
        required: true
        title: "Formalização de parceria com cooperativa de coleta seletiva ou comprovação de coleta seletiva pela prefeitura na estrutura"
        description: "A estrutura formalizou parceria com cooperativa de coleta seletiva ou comprovou que a coleta seletiva é realizada pela prefeitura?"

      canais_divulgacao:
        type: array
        items:
          type: string
          enum:
            - "PI" # páginas na internet
            - "RS" # redes sociais
            - "ER" # eventos realizados
            - "MD" # materiais didáticos
        title: "Canais de divulgação específicos da política/ações de sustentabilidade institucionais na estrutura"
        required: true
        description: >
          Canais de divulgação específicos da política/ações de sustentabilidade institucionais
          na estrutura. PI = páginas na internet; RS = redes sociais; ER = eventos realizados; MD = materiais didáticos.
    additionalFields: false

  compras_contratacoes:
    type: table
    title: "Compras e Contratações"
    description: "Indicadores sobre compras e contratações institucionais com aplicação de critérios de sustentabilidade no ano de referência."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Quantidades de compras e contratações não podem ser negativas."
        query: >
          SELECT COUNT(*) FROM compras_contratacoes
          WHERE compras_sustentaveis < 0 OR contratacoes_sustentaveis < 0
             OR compras_geral < 0 OR contratacoes_geral < 0
        mustBe: 0
      - type: sql
        description: "Quantidades sustentáveis não podem superar os respectivos totais."
        query: >
          SELECT COUNT(*) FROM compras_contratacoes
          WHERE compras_sustentaveis > compras_geral
             OR contratacoes_sustentaveis > contratacoes_geral
        mustBe: 0
      - type: sql
        description: "A estrutura deve ser preenchida com um valor não vazio."
        query: >
          SELECT COUNT(*) FROM compras_contratacoes
          WHERE NULLIF(TRIM(estrutura), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Cada estrutura deve possuir apenas um registro de compras e contratações."
        query: >
          SELECT COUNT(*) FROM (
            SELECT TRIM(estrutura)
            FROM compras_contratacoes
            WHERE NULLIF(TRIM(estrutura), '') IS NOT NULL
            GROUP BY TRIM(estrutura) HAVING COUNT(*) > 1
          ) estruturas_duplicadas
        mustBe: 0

    fields:
      id_compras_contratacoes:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true
        description: "Identificador único do registro de compras e contratações institucionais com aplicação de critérios de sustentabilidade no ano de referência."

      estrutura:
        type: string
        required: true
        title: "Estrutura à qual vinculam-se as compras e contratações"
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      normativo_compras_sustentaveis:
        type: boolean
        required: true
        title: "Possui normativo que regulamenta compras e contratações com aplicação de critérios de sustentabilidade?"
        description: "Indica se a estrutura possui normativo que regulamenta compras e contratações com aplicação de critérios de sustentabilidade."

      compras_sustentaveis:
        type: integer
        required: true
        title: "Número de compras efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência"
        description: "Total de compras efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência."
      contratacoes_sustentaveis:
        type: integer
        required: true
        title: "Número de contratações efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência"
        description: "Total de contratações efetivadas utilizando pelo menos um critério de sustentabilidade, no ano de referência."

      compras_geral:
        type: integer
        required: true
        title: "Número de compras efetivadas no ano de referência"
        description: "Total de compras efetivadas no ano de referência, independentemente da aplicação de critérios de sustentabilidade."

      contratacoes_geral:
        type: integer
        required: true
        title: "Número de contratações efetivadas no ano de referência"
        description: "Total de contratações efetivadas no ano de referência, independentemente da aplicação de critérios de sustentabilidade."
    additionalFields: false
```
