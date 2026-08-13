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

Este **Contrato de Dados** descreve os **projetos de gestão e desenvolvimento institucional** conduzidos pela instituição — projetos voltados à própria instituição (gestão, processos, infraestrutura, governança), e não ao ensino, à pesquisa ou à extensão.

A **PNP** coleta este contrato para mensurar o esforço de desenvolvimento interno da Rede Federal e, em especial, **quanto desse esforço é dirigido à sustentabilidade** — recorte que aparece duas vezes no schema, em `natureza_projeto` e em `projeto_gestao_di_sustentavel`.



## Modelos contidos

- **`projetos_gestao_di`** *(opcional no fluxo)* — projetos de gestão e desenvolvimento institucional, com natureza, vigência, fomento, orçamento e produto final.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `projetos_gestao_di`.

## Modelo `projetos_gestao_di`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é um projeto de gestão/desenvolvimento institucional identificado por `id_projeto_gestao_di`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_projeto_gestao_di` | `integer` | sim | `primaryKey` | ID projeto de gestão institucional |
| `natureza_projeto` | `string` | sim | `enum` (2 valores — ver abaixo) | Natureza do projeto |
| `titulo_projeto` | `string` | sim | — | Título do Projeto |
| `resumo_projeto` | `string` | não | — | Resumo do Projeto |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se os projetos. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `projeto_gestao_di_sustentavel` | `boolean` | sim | — | Aborda a temática da sustentabilidade? Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `nome_coordenador` | `string` | sim | — | Nome do Coordenador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | sim | — | Data de término |
| `situacao_projeto` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação do projeto |
| `fomento_tipo` | `string` | não | `enum: [Interno, Externo, Ambos]` | O projeto é executado com que forma de fomento? |
| `entidade_financiadora` | `string` | não | `enum` (7 valores — ver abaixo) | Qual a principal entidade financiadora? |
| `orcamento_projeto` | `double` | não | — | Orçamento do projeto. Valor numérico em reais (R$) |
| `produto` | `string` | não | — | Produto final |

#### Valores de `natureza_projeto`

- `Projeto de gestão institucional sustentabilidade`
- `Projeto de gestão e desenvolvimento institucional (não voltado à sustentabilidade)`

#### Valores de `entidade_financiadora`

- `sem fomento externo (própria instituição)`
- `MEC`
- `outro órgão do poder executivo federal`
- `órgão do poder executivo municipal ou estadual`
- `instituição de fomento nacional`
- `organização ou instituição internacional`
- `outro`

> **`referencia_pnp` é metadado declarativo, não validação.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`.


> **A sustentabilidade é declarada em dois lugares, e nada os concilia.** `natureza_projeto` distingue projeto sustentável de não-sustentável, e `projeto_gestao_di_sustentavel` repete a mesma informação como `boolean`. Não há regra de qualidade declarada que impeça a combinação incoerente (`natureza_projeto: "…sustentabilidade"` com `projeto_gestao_di_sustentavel: false`). Quem integra deve garantir a consistência na origem — a validação não vai pegar.

### Exemplo válido

```json
{
  "id_projeto_gestao_di": 318,
  "natureza_projeto": "Projeto de gestão institucional sustentabilidade",
  "titulo_projeto": "Digitalização do acervo de processos administrativos",
  "resumo_projeto": "Eliminação do fluxo de papel nos processos da Diretoria de Administração, com trilha de auditoria eletrônica.",
  "estrutura": "12",
  "projeto_gestao_di_sustentavel": true,
  "nome_coordenador": "Roberto Álvares Pinto",
  "data_inicio": "2026-02-02",
  "data_termino": "2026-12-18",
  "situacao_projeto": "Em andamento",
  "fomento_tipo": "Interno",
  "entidade_financiadora": "sem fomento externo (própria instituição)",
  "orcamento_projeto": 74500.0,
  "produto": "Acervo digitalizado e norma de processo eletrônico publicada"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"titulo_projeto": "...", "natureza_projeto": "..."}` (sem `id_projeto_gestao_di`) | `Required field 'id_projeto_gestao_di' is missing` |
| `{"id_projeto_gestao_di": 318, "natureza_projeto": "..."}` (sem `titulo_projeto`) | `Required field 'titulo_projeto' is missing` |
| `{..., "natureza_projeto": "Projeto de sustentabilidade"}` (valor fora do `enum`) | `Value 'Projeto de sustentabilidade' for field 'natureza_projeto' not in enum` |
| `{..., "fomento_tipo": "Misto"}` (valor fora do `enum`) | `Value 'Misto' for field 'fomento_tipo' not in enum [Interno, Externo, Ambos]` |
| `{..., "orcamento_projeto": "R$ 74.500,00"}` (`double` espera número, não string formatada) | `Type mismatch on 'orcamento_projeto': expected double, got string 'R$ 74.500,00'` |
| `{..., "data_inicio": "02/02/2026"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_inicio': expected date, got string '02/02/2026'` |
| `{..., "area_tematica": "Gestão"}` (coluna não declarada) | `Field 'area_tematica' not in schema (additionalFields: false)` |



## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "desenvolvimento_institucional"
info:
  title: "Desenvolvimento Institucional"
  version: "1.0.0"
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
    fields:
      id_projeto_gestao_di:
        type: integer
        title: "ID projeto de gestão institucional"
        primaryKey: true
        required: true

      natureza_projeto:
        type: string
        title: "Natureza do projeto"
        enum:
          - "Projeto de gestão institucional sustentabilidade"
          - "Projeto de gestão e desenvolvimento institucional (não voltado à sustentabilidade)"
        required: true

      titulo_projeto:
        type: string
        title: "Título do Projeto"
        required: true

      resumo_projeto:
        type: string
        title: "Resumo do Projeto"

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os projetos de gestão e desenvolvimento institucional"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_gestao_di_sustentavel:
        type: boolean
        title: "Aborda a temática da sustentabilidade?"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      nome_coordenador:
        type: string
        title: "Nome do Coordenador"

      data_inicio:
        type: date
        title: "Data de início"

      data_termino:
        type: date
        title: "Data de término"

      situacao_projeto:
        type: string
        title: "Situação do projeto"
        enum: ["Em andamento", "Finalizado", "Cancelado"]

      fomento_tipo:
        type: string
        title: "O projeto é executado com que forma de fomento?"
        enum: ["Interno", "Externo", "Ambos"]

      entidade_financiadora:
        type: string
        title: "Qual a principal entidade financiadora?"
        enum:
          - "sem fomento externo (própria instituição)"
          - "MEC"
          - "outro órgão do poder executivo federal"
          - "órgão do poder executivo municipal ou estadual"
          - "instituição de fomento nacional"
          - "organização ou instituição internacional"
          - "outro"

      orcamento_projeto:
        type: double
        title: "Orçamento do projeto"
        description: "Valor numérico em reais (R$)."

      produto:
        type: string
        title: "Produto final"
    additionalFields: false
```

