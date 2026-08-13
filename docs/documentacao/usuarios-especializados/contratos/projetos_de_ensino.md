---
layout: default
title: "Projetos de Ensino"
toc: true
---
# Projetos de Ensino

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `projetos_de_ensino` · **Versão:** `1.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Ensino (Apoio a Sustentabilidade)

## Resumo de negócio

Este **Contrato de Dados** descreve os **projetos de ensino** conduzidos pela instituição — monitoria, tutoria, intervenção pedagógica, material didático, tecnologia assistiva, eventos de ensino e ações de inclusão. É o terceiro pé do tripé acadêmico, ao lado de [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) e [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao). Nesse momento, será necessário enviar apenas projetos de ensino que tenham a temática de sustentabilidade

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para,  via `projeto_ensino_sustentavel`, quanto desse investimento toca a temática da sustentabilidade.


## Modelos contidos

- **`projetos_ensino`** *(opcional no fluxo)* — projetos de ensino, com natureza, vigência, financiamento, orçamento e produto final.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `projetos_ensino`.

## Modelo `projetos_ensino`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é um projeto de ensino identificado por `id_projeto_ensino`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_projeto_ensino` | `integer` | sim | `primaryKey` | ID projeto de ensino |
| `natureza_projeto` | `string` | sim | `enum` (7 valores — ver abaixo) | Natureza do projeto |
| `titulo_projeto` | `string` | sim | — | Título do Projeto |
| `resumo_projeto` | `string` | não | — | Resumo do Projeto |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se os projetos de ensino. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `projeto_ensino_sustentavel` | `boolean` | sim | — | Aborda a temática da sustentabilidade? Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `nome_coordenador` | `string` | sim | — | Nome do Coordenador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | sim | — | Data de término |
| `situacao_projeto` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação do projeto |
| `entidade_financiadora` | `string` | não | `enum` (7 valores — ver abaixo) | Entidade financiadora |
| `orcamento_projeto` | `double` | não | — | Orçamento do projeto. Valor numérico em reais (R$) |
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

> **`referencia_pnp` é metadado declarativo, não validação.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`.

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
  "orcamento_projeto": 18000.0,
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
| `{..., "fomento_tipo": "Interno"}` (coluna não declarada neste contrato) | `Field 'fomento_tipo' not in schema (additionalFields: false)` |



## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "projetos_de_ensino"
info:
  title: "Projetos de Ensino"
  version: "1.0.0"
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
    fields:
      id_projeto_ensino:
        type: integer
        title: "ID projeto de ensino"
        primaryKey: true
        required: true

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

      titulo_projeto:
        type: string
        title: "Título do Projeto"
        required: true

      resumo_projeto:
        type: string
        title: "Resumo do Projeto"

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os projetos de ensino"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_ensino_sustentavel:
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

      entidade_financiadora:
        type: string
        title: "Entidade financiadora"
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

