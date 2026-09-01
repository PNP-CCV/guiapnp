---
layout: default
title: "Projetos de Ensino"
toc: true
---
# Projetos de Ensino

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `projetos_de_ensino` · **Versão:** `2.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Ensino (Apoio a Sustentabilidade)

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **projetos de ensino** conduzidos pela instituição — monitoria, tutoria, intervenção pedagógica, material didático, tecnologia assistiva, eventos de ensino e ações de inclusão. É o terceiro pé do tripé acadêmico, ao lado de [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) e [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao).

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar o investimento da Rede Federal na qualidade do próprio ensino — e, via `projeto_ensino_sustentavel`, quanto desse investimento toca a temática da sustentabilidade.

Diferente de [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao), este contrato **não registra as pessoas envolvidas nem as atendidas**: é uma tabela única sobre o projeto, sem PII.

## Modelos contidos

- **`projetos_ensino`** *(opcional no fluxo)* — projetos de ensino, com natureza, vigência, financiamento, orçamento e produto final.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `projetos_ensino`.

## Modelo `projetos_ensino`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é um projeto de ensino identificado por `id_projeto_ensino`.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_projeto_ensino` | `integer` | sim | `primaryKey` | ID projeto de ensino |
| `natureza_projeto` | `string` | sim | `enum` (7 valores — ver abaixo) | Natureza do projeto |
| `titulo_projeto` | `string` | sim | — | Título do Projeto |
| `resumo_projeto` | `string` | não | — | Resumo do Projeto |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os projetos de ensino. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `projeto_ensino_sustentavel` | `boolean` | sim | — | Aborda a temática da sustentabilidade? |
| `nome_coordenador` | `string` | sim | — | Nome do Coordenador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | não | — | Data de término. Obrigatória para projeto `Finalizado`/`Cancelado` (ver *Regras de qualidade*), pode ficar em branco enquanto estiver em andamento |
| `situacao_projeto` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação do projeto |
| `entidade_financiadora` | `string` | não | `enum` (7 valores — ver abaixo) | Entidade financiadora |
| `contrapartida_financeira_institucional` | `double` | não | — | Valor da contrapartida financeira institucional em reais (R$). Usar `0` quando não houver |
| `contrapartida_financeira_externa` | `double` | não | — | Valor da contrapartida financeira externa em reais (R$). Usar `0` quando não houver |
| `produto` | `string` | não | — | Produto final |

#### Valores de `natureza_projeto`

- `Formação ou qualificação`
- `Intervenção pedagógica`
- `Monitoria, tutoria ou apoio à aprendizagem`
- `Eventos de ensino`
- `Materiais didáticos e tecnologias educacionais`
- `Tecnologias assistivas e recursos de acessibilidade`
- `Inclusão, pertencimento e orientação`

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
| As contrapartidas não podem ser negativas; contrapartida externa maior que zero exige entidade financiadora externa, e entidade financiadora externa exige contrapartida externa maior que zero | `mustBe: 0` |

### Exemplo válido

```json
{
  "id_projeto_ensino": 774,
  "natureza_projeto": "Monitoria, tutoria ou apoio à aprendizagem",
  "titulo_projeto": "Monitoria de Cálculo I para os cursos de Engenharia",
  "resumo_projeto": "Atendimento semanal em grupos reduzidos, conduzido por estudantes monitores, para reduzir a retenção na disciplina.",
  "estrutura": "12",
  "projeto_ensino_sustentavel": false,
  "nome_coordenador": "Ana Beatriz Fontes",
  "data_inicio": "2026-03-09",
  "data_termino": "2026-12-11",
  "situacao_projeto": "Em andamento",
  "entidade_financiadora": "sem fomento externo (própria instituição)",
  "contrapartida_financeira_institucional": 18000.0,
  "contrapartida_financeira_externa": 0.0,
  "produto": "Caderno de exercícios resolvidos e relatório de retenção"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"titulo_projeto": "...", "natureza_projeto": "..."}` (sem `id_projeto_ensino`) | `Required field 'id_projeto_ensino' is missing` |
| `{"id_projeto_ensino": 774, "titulo_projeto": "..."}` (sem `natureza_projeto`) | `Required field 'natureza_projeto' is missing` |
| `{..., "natureza_projeto": "Monitoria"}` (valor fora do `enum`) | `Value 'Monitoria' for field 'natureza_projeto' not in enum` |
| `{..., "projeto_ensino_sustentavel": "não"}` (`boolean` espera `true`/`false`) | `Type mismatch on 'projeto_ensino_sustentavel': expected boolean, got string 'não'` |
| `{..., "data_termino": "11/12/2026"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_termino': expected date, got string '11/12/2026'` |
| `{..., "orcamento_projeto": 18000}` (coluna não declarada neste contrato) | `Field 'orcamento_projeto' not in schema (additionalFields: false)` |
| `{..., "situacao_projeto": "Finalizado", "data_termino": null}` (finalizado sem data de término) | `Datas e situação do projeto devem ser coerentes.: Actual custom_sql(projetos_ensino) was 1, expected = 0` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-16 | Versão inicial documentada nesta data. | — |
| `2.0.0` | 2026-09-01 | `orcamento_projeto` virou o par `contrapartida_financeira_institucional`/`contrapartida_financeira_externa`; `data_termino` deixou de ser obrigatória; regras `quality` acrescentadas. | **sim** |

## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "projetos_de_ensino"
info:
  title: "Projetos de Ensino"
  version: "2.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados dos projetos de ensino conduzidos na instituição,
    incluindo aqueles voltados à temática da sustentabilidade.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/projetos-de-ensino/{model}/*.parquet"
    format: "parquet"

models:
  projetos_ensino:
    type: table
    title: "Projetos de Ensino"
    description: "Informações estruturadas sobre projetos de ensino institucional."
    meta:
      required: false
      disabled: false
    quality:
      - type: sql
        description: "Textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM projetos_ensino
          WHERE NULLIF(TRIM(titulo_projeto), '') IS NULL
             OR NULLIF(TRIM(estrutura), '') IS NULL
             OR NULLIF(TRIM(nome_coordenador), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Datas e situação do projeto devem ser coerentes."
        query: >
          SELECT COUNT(*) FROM projetos_ensino
          WHERE data_termino < data_inicio
             OR (situacao_projeto IN ('Finalizado', 'Cancelado') AND data_termino IS NULL)
        mustBe: 0
      - type: sql
        description: "As contrapartidas financeiras não podem ser negativas e o financiamento externo deve ser coerente com a entidade financiadora."
        query: >
          SELECT COUNT(*) FROM projetos_ensino
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
      id_projeto_ensino:
        type: integer
        title: "ID projeto de ensino"
        primaryKey: true
        required: true
        description: "Identificador único do registro de projeto de ensino."

      natureza_projeto:
        type: string
        title: "Natureza do projeto"
        enum:
          - "Formação ou qualificação"
          - "Intervenção pedagógica"
          - "Monitoria, tutoria ou apoio à aprendizagem"
          - "Eventos de ensino"
          - "Materiais didáticos e tecnologias educacionais"
          - "Tecnologias assistivas e recursos de acessibilidade"
          - "Inclusão, pertencimento e orientação"
        required: true
        description: "Natureza do projeto de ensino, conforme classificação."

      titulo_projeto:
        type: string
        title: "Título do Projeto"
        required: true
        description: "Título do projeto de ensino, conforme registro institucional."

      resumo_projeto:
        type: string
        title: "Resumo do Projeto"
        description: "Resumo do projeto de ensino, conforme registro institucional."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os projetos de ensino"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_ensino_sustentavel:
        type: boolean
        required: true
        title: "Aborda a temática da sustentabilidade?"
        description: "Indica se o projeto de ensino aborda a temática da sustentabilidade: true quando abordar e false quando não abordar."

      nome_coordenador:
        type: string
        required: true
        title: "Nome do Coordenador"
        description: "Nome do coordenador do projeto de ensino, conforme registro institucional."

      data_inicio:
        type: date
        required: true
        title: "Data de início"
        description: "Data em que o projeto de ensino iniciou suas atividades."

      data_termino:
        type: date
        required: false
        title: "Data de término"
        description: "Data prevista ou efetiva de término do projeto. É obrigatória para projetos finalizados ou cancelados e pode ser nula para projetos em andamento."

      situacao_projeto:
        type: string
        required: true
        title: "Situação do projeto"
        enum: ["Em andamento", "Finalizado", "Cancelado"]
        description: "Situação atual do projeto de ensino, conforme registro institucional."

      entidade_financiadora:
        type: string
        title: "Entidade financiadora"
        description: "Qual a principal entidade financiadora do projeto de ensino?"
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
        title: "Valor da contrapartida financeira institucional em reais (R$)"
        description: "Valor da contrapartida financeira institucional em reais (R$). Usar 0 ou deixar nulo quando não houver."

      contrapartida_financeira_externa:
        type: double
        required: false
        title: "Valor da contrapartida financeira externa em reais (R$)"
        description: "Valor da contrapartida financeira externa em reais (R$). Usar 0 ou deixar nulo quando não houver."

      produto:
        type: string
        title: "Produto final"
        description: "Descrição do produto final do projeto de ensino, conforme registro institucional."
    additionalFields: false
```

