---
layout: default
title: "Projetos de Desenvolvimento Institucional"
toc: true
---
# Projetos de Desenvolvimento Institucional

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `projeto_desenvolvimento_institucional` · **Versão:** `1.0.0` · **Owner:** SETEC

**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Desenvolvimento Institucional

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **projetos de gestão e desenvolvimento institucional** conduzidos pela instituição — projetos voltados à própria máquina institucional (gestão, processos, infraestrutura, governança), e não ao ensino, à pesquisa ou à extensão.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar o esforço de desenvolvimento interno da Rede Federal e, em especial, **quanto desse esforço é dirigido à sustentabilidade** — recorte que o schema captura no par `projeto_gestao_sustentabilidade` (a marcação) e `natureza_projeto_gestao_sustentabilidade` (as naturezas envolvidas).

Este contrato é o gêmeo estrutural de [Projetos de Ensino]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_ensino): mesmos campos de vigência, fomento, situação e produto, mudando o domínio e a lista de naturezas.

## Modelos contidos

- **`projetos_gestao_di`** *(opcional no fluxo)* — projetos de gestão e desenvolvimento institucional, com recorte de sustentabilidade, vigência, fomento, contrapartidas financeiras e produto final.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `projetos_gestao_di`.

## Modelo `projetos_gestao_di`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é um projeto de gestão/desenvolvimento institucional identificado por `id_projeto_gestao_di`.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_projeto_gestao_di` | `integer` | sim | `primaryKey` | ID projeto de gestão institucional |
| `projeto_gestao_sustentabilidade` | `boolean` | sim | — | O projeto é de gestão institucional da sustentabilidade? |
| `natureza_projeto_gestao_sustentabilidade` | `array` (de `string`) | não | `enum` (10 valores — ver abaixo) | Naturezas de sustentabilidade cobertas pelo projeto — lista, obrigatória quando `projeto_gestao_sustentabilidade` é `true` e vazia quando é `false` (ver *Regras de qualidade*) |
| `titulo_projeto` | `string` | sim | — | Título do Projeto |
| `resumo_projeto` | `string` | não | — | Resumo do Projeto |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os projetos. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `nome_coordenador` | `string` | sim | — | Nome do Coordenador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | não | — | Data de término. Pode ficar em branco enquanto o projeto estiver em andamento |
| `situacao_projeto` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação do projeto |
| `entidade_financiadora` | `string` | não | `enum` (7 valores — ver abaixo) | Qual a principal entidade financiadora? |
| `contrapartida_financeira_institucional` | `double` | não | — | Valor da contrapartida fornecida pela instituição, em reais. Usar `0` quando não houver |
| `contrapartida_financeira_externa` | `double` | não | — | Valor da contrapartida fornecida pela entidade financiadora, em reais. Usar `0` quando não houver |
| `produto` | `string` | não | — | Produto final |

#### Valores de `natureza_projeto_gestao_sustentabilidade`

- `Construções sustentáveis`
- `Transformação digital e redução do uso de papel`
- `Acessibilidade e inclusão sustentável`
- `Mobilidade sustentável`
- `Relação com a Agenda Ambiental na Administração Pública (A3P)`
- `Relação com o Plano de Logística Sustentável (PLS)`
- `Mitigação e adaptação às mudanças climáticas`
- `Relação com os Objetivos de Desenvolvimento Sustentável (ODS)`
- `Respostas institucionais a situações de calamidade pública`
- `Outro projeto de gestão institucional da sustentabilidade`

#### Valores de `entidade_financiadora`

- `sem fomento externo (própria instituição)`
- `MEC`
- `outro órgão do poder executivo federal`
- `órgão do poder executivo municipal ou estadual`
- `instituição de fomento nacional`
- `organização ou instituição internacional`
- `outro`

> ℹ️ **`referencia_pnp` agora é conferido na extração.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`, e o Coletor confere esse código contra o espelho local de estruturas antes de gravar o Parquet — a mesma checagem que a PNP faz depois do envio, antecipada. O padrão de fábrica é o **modo sombra**: a divergência é registrada no Registro de Extração, mas ainda não reprova. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### Regras de qualidade

Além do schema (colunas obrigatórias, tipos, `enum` e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `titulo_projeto`, `estrutura` e `nome_coordenador` não podem ser texto vazio | `mustBe: 0` |
| `data_termino` não pode anteceder `data_inicio`, e projeto `Finalizado`/`Cancelado` precisa de `data_termino` | `mustBe: 0` |
| `natureza_projeto_gestao_sustentabilidade` tem de vir preenchida quando `projeto_gestao_sustentabilidade` é `true`, vazia quando é `false`, e sem valores repetidos | `mustBe: 0` |
| As contrapartidas não podem ser negativas; contrapartida externa maior que zero exige entidade financiadora externa, e entidade financiadora externa exige contrapartida externa maior que zero | `mustBe: 0` |

> ℹ️ **A sustentabilidade agora se concilia sozinha.** A marcação (`projeto_gestao_sustentabilidade`) e a lista de naturezas passaram a ser cobradas uma pela outra na terceira regra — a combinação incoerente que antes passava batido hoje reprova o teste do contrato.

### Exemplo válido

```json
{
  "id_projeto_gestao_di": 318,
  "projeto_gestao_sustentabilidade": true,
  "natureza_projeto_gestao_sustentabilidade": ["Transformação digital e redução do uso de papel"],
  "titulo_projeto": "Digitalização do acervo de processos administrativos",
  "resumo_projeto": "Eliminação do fluxo de papel nos processos da Diretoria de Administração, com trilha de auditoria eletrônica.",
  "estrutura": "12",
  "nome_coordenador": "Roberto Álvares Pinto",
  "data_inicio": "2026-02-02",
  "data_termino": "2026-12-18",
  "situacao_projeto": "Em andamento",
  "entidade_financiadora": "sem fomento externo (própria instituição)",
  "contrapartida_financeira_institucional": 74500.0,
  "contrapartida_financeira_externa": 0.0,
  "produto": "Acervo digitalizado e norma de processo eletrônico publicada"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"titulo_projeto": "...", "projeto_gestao_sustentabilidade": true}` (sem `id_projeto_gestao_di`) | `Required field 'id_projeto_gestao_di' is missing` |
| `{"id_projeto_gestao_di": 318, "projeto_gestao_sustentabilidade": true}` (sem `titulo_projeto`) | `Required field 'titulo_projeto' is missing` |
| `{..., "natureza_projeto_gestao_sustentabilidade": ["Projeto de sustentabilidade"]}` (valor fora do `enum`) | `Value 'Projeto de sustentabilidade' for field 'natureza_projeto_gestao_sustentabilidade' not in enum` |
| `{..., "projeto_gestao_sustentabilidade": true, "natureza_projeto_gestao_sustentabilidade": []}` (marcação sem natureza) | `As naturezas de sustentabilidade devem ser coerentes com a classificação do projeto e não podem se repetir.: Actual custom_sql(projetos_gestao_di) was 1, expected = 0` |
| `{..., "contrapartida_financeira_institucional": "R$ 74.500,00"}` (`double` espera número, não string formatada) | `Type mismatch on 'contrapartida_financeira_institucional': expected double, got string 'R$ 74.500,00'` |
| `{..., "data_inicio": "02/02/2026"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_inicio': expected date, got string '02/02/2026'` |
| `{..., "area_tematica": "Gestão"}` (coluna não declarada) | `Field 'area_tematica' not in schema (additionalFields: false)` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-16 | Versão inicial documentada nesta data. | — |
| `2.0.0` | 2026-09-01 | `natureza_projeto` + `projeto_gestao_di_sustentavel` viraram `projeto_gestao_sustentabilidade` + `natureza_projeto_gestao_sustentabilidade` (array); `fomento_tipo` removido; `orcamento_projeto` virou o par `contrapartida_financeira_institucional`/`contrapartida_financeira_externa`; `data_termino` deixou de ser obrigatória. | **sim** |

## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "desenvolvimento_institucional"
info:
  title: "Desenvolvimento Institucional"
  version: "2.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados dos projetos de gestão e desenvolvimento
    institucional conduzidos na instituição, incluindo aqueles voltados à temática da
    sustentabilidade.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/desenvolvimento-institucional/{model}/*.parquet"
    format: "parquet"

models:
  projetos_gestao_di:
    type: table
    title: "Projetos de Gestão e Desenvolvimento Institucional"
    description: "Informações estruturadas sobre projetos de gestão e desenvolvimento institucional."
    meta:
      required: false
      disabled: false
    quality:
      - type: sql
        description: "Textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM projetos_gestao_di
          WHERE NULLIF(TRIM(titulo_projeto), '') IS NULL
             OR NULLIF(TRIM(estrutura), '') IS NULL
             OR NULLIF(TRIM(nome_coordenador), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Datas e situação do projeto devem ser coerentes."
        query: >
          SELECT COUNT(*) FROM projetos_gestao_di
          WHERE data_termino < data_inicio
             OR (situacao_projeto IN ('Finalizado', 'Cancelado') AND data_termino IS NULL)
        mustBe: 0
      - type: sql
        description: "As naturezas de sustentabilidade devem ser coerentes com a classificação do projeto e não podem se repetir."
        query: >
          SELECT COUNT(*) FROM projetos_gestao_di
          WHERE (
            projeto_gestao_sustentabilidade = TRUE
            AND len(coalesce(natureza_projeto_gestao_sustentabilidade, [])) = 0
          ) OR (
            projeto_gestao_sustentabilidade = FALSE
            AND len(coalesce(natureza_projeto_gestao_sustentabilidade, [])) > 0
          ) OR (
            array_length(natureza_projeto_gestao_sustentabilidade)
            <> array_length(array_distinct(natureza_projeto_gestao_sustentabilidade))
          )
        mustBe: 0
      - type: sql
        description: "As contrapartidas financeiras não podem ser negativas e o financiamento externo deve ser coerente com a entidade financiadora."
        query: >
          SELECT COUNT(*) FROM projetos_gestao_di
          WHERE contrapartida_financeira_institucional < 0
             OR contrapartida_financeira_externa < 0
             OR (
               contrapartida_financeira_externa > 0
               AND (
                 NULLIF(TRIM(entidade_financiadora), '') IS NULL
                 OR entidade_financiadora = 'sem fomento externo (própria instituição)'
               )
             )
             OR (
               NULLIF(TRIM(entidade_financiadora), '') IS NOT NULL
               AND entidade_financiadora <> 'sem fomento externo (própria instituição)'
               AND coalesce(contrapartida_financeira_externa, 0) <= 0
             )
        mustBe: 0
    fields:
      id_projeto_gestao_di:
        type: integer
        title: "ID projeto de gestão institucional"
        primaryKey: true
        required: true

      projeto_gestao_sustentabilidade:
        type: boolean
        title: "O projeto é de gestão institucional da sustentabilidade?"
        required: true
        description: "Indica se o projeto de gestão e desenvolvimento institucional está relacionado à temática da sustentabilidade."

      natureza_projeto_gestao_sustentabilidade:
        type: array
        title: "Naturezas do projeto de gestão institucional da sustentabilidade"
        description: "Indica as naturezas do projeto de gestão e desenvolvimento institucional relacionadas à temática da sustentabilidade."
        items:
          type: string
          enum:
            - "Construções sustentáveis"
            - "Transformação digital e redução do uso de papel"
            - "Acessibilidade e inclusão sustentável"
            - "Mobilidade sustentável"
            - "Relação com a Agenda Ambiental na Administração Pública (A3P)"
            - "Relação com o Plano de Logística Sustentável (PLS)"
            - "Mitigação e adaptação às mudanças climáticas"
            - "Relação com os Objetivos de Desenvolvimento Sustentável (ODS)"
            - "Respostas institucionais a situações de calamidade pública"
            - "Outro projeto de gestão institucional da sustentabilidade"
        required: false

      titulo_projeto:
        type: string
        title: "Título do Projeto"
        required: true
        description: "Título do projeto de gestão e desenvolvimento institucional."

      resumo_projeto:
        type: string
        title: "Resumo do Projeto"
        description: "Resumo do projeto de gestão e desenvolvimento institucional."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os projetos de gestão e desenvolvimento institucional"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      nome_coordenador:
        type: string
        required: true
        title: "Nome do Coordenador"
        description: "Nome do coordenador responsável pelo projeto de gestão e desenvolvimento institucional."

      data_inicio:
        type: date
        required: true
        title: "Data de início"
        description: "Data em que o projeto de gestão e desenvolvimento institucional teve início."

      data_termino:
        type: date
        required: false
        title: "Data de término"
        description: "Data em que o projeto de gestão e desenvolvimento institucional foi concluído ou cancelado. Pode ser nula se o projeto ainda estiver em andamento."

      situacao_projeto:
        type: string
        required: true
        title: "Situação do projeto"
        enum: ["Em andamento", "Finalizado", "Cancelado"]
        description: "Situação atual do projeto de gestão e desenvolvimento institucional."

      entidade_financiadora:
        type: string
        title: "Qual a principal entidade financiadora?"
        description: "Nome da entidade financiadora do projeto de gestão e desenvolvimento institucional."
        enum:
          - "sem fomento externo (própria instituição)"
          - "MEC"
          - "outro órgão do poder executivo federal"
          - "órgão do poder executivo municipal ou estadual"
          - "instituição de fomento nacional"
          - "organização ou instituição internacional"
          - "outro"

      contrapartida_financeira_institucional:
        type: double
        required: false
        title: "Valor da contrapartida financeira institucional"
        description: "Valor da contrapartida financeira fornecida pela instituição, em reais. Deve ser 0 se não houver contrapartida."

      contrapartida_financeira_externa:
        type: double
        required: false
        title: "Valor da contrapartida financeira externa"
        description: "Valor da contrapartida financeira fornecida pela instituição parceira, em reais. Deve ser 0 se não houver contrapartida."

      produto:
        type: string
        title: "Produto final"
        description: "Descrição do produto final do projeto de gestão e desenvolvimento institucional."
    additionalFields: false
```

