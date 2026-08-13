---
layout: default
title: "Projetos de Pesquisa"
toc: true
---
# Projetos de Pesquisa

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `projetos_de_pesquisa` · **Versão:** `1.0.0` · **Owner:** SETEC

**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Pesquisa e Inovação


## Resumo de negócio

Este **Contrato de Dados** descreve as **iniciativas de investigação científica e tecnológica** conduzidas por servidores e estudantes da rede federal — projetos de pesquisa básica e aplicada, com fomento próprio ou externo (CNPq, CAPES, FINEP, FAPs estaduais).

A **PNP** coleta este contrato para mensurar a **produção em P&D** da rede federal: orçamento, fomento, área temática CNPq, vigência e participação de docentes, TAEs, estudantes e externos. Os dois modelos cobrem o projeto em si e as pessoas envolvidas (com PII).

Este contrato é também o destino lógico do vínculo declarado textualmente em `acordos_parceria.objeto_acordo` — embora não haja `references` formal entre os dois contratos, o `id_projeto_pesquisa` daqui é o que aparece naquele campo.

## Modelos contidos

- **`projetos_pesquisa`** *(obrigatório no fluxo)* — projetos de pesquisa institucionais, com natureza, vigência, situação, orçamento, entidade financiadora e área temática CNPq.
- **`pessoas_envolvidas_projeto_pesquisa`** *(obrigatório no fluxo)* — pessoas vinculadas a cada projeto (docentes, TAEs, estudantes, externos). Contém PII (`cpf`, `nome`).

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Modelo `projetos_pesquisa`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela principal do contrato. Cada linha é um projeto de pesquisa identificado por `id_projeto_pesquisa`. A tabela `pessoas_envolvidas_projeto_pesquisa` referencia-a por chave estrangeira. **Atenção ao slug do modelo**: `projetos_pesquisa` (sem o `de_`), embora o `id` do contrato e o nome do arquivo sejam `projetos_de_pesquisa`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_projeto_pesquisa` | `integer` | sim | `primaryKey` | ID projeto de pesquisa |
| `natureza_projeto` | `string` | sim | `enum: [Básica, Aplicada]` | Natureza do projeto |
| `titulo_projeto` | `string` | sim | — | Título do Projeto |
| `resumo_projeto` | `string` | não | — | Resumo do Projeto |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se os projetos de pesquisa. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `projeto_pesquisa_sustentavel` | `boolean` | sim | — | Aborda a temática da sustentabilidade? Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `nome_orientador` | `string` | não | — | Nome do Orientador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | sim | — | Data de término |
| `situacao_projeto` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação do projeto |
| `entidade_financiadora` | `string` | não | `enum: [Capes, CNPq, FINEP, sem fomento externo, outras]` | Entidade financiadora |
| `orcamento_projeto` | `double` | não | — | Valor numérico em reais (R$) |
| `area_tematica_cnpq` | `string` | sim | `referencia_pnp: areas_tematicas_cnpq` (declarativo — ver nota) | Área Temática CNPq. Formato: `{codigo}` |
| `produto` | `string` | não | — | Produto final |


### Exemplo válido

```json
{
  "id_projeto_pesquisa": 3147,
  "natureza_projeto": "Aplicada",
  "titulo_projeto": "Caracterização de catalisadores para refino de petróleo pesado",
  "resumo_projeto": "Estudo de catalisadores Ni/Mo suportados para hidrocraqueamento de frações pesadas oriundas do pré-sal.",
  "estrutura": "12",
  "projeto_pesquisa_sustentavel": false,
  "nome_orientador": "Patrícia Oliveira Santos",
  "data_inicio": "2024-09-01",
  "data_termino": "2027-08-31",
  "situacao_projeto": "Em andamento",
  "entidade_financiadora": "CNPq",
  "orcamento_projeto": 480000.00,
  "area_tematica_cnpq": "30700001",
  "produto": "Relatório técnico e artigo publicado em periódico Qualis A1"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"natureza_projeto": "Aplicada", "titulo_projeto": "..."}` (sem `id_projeto_pesquisa`) | `Required field 'id_projeto_pesquisa' is missing` |
| `{"id_projeto_pesquisa": 3147, "titulo_projeto": "..."}` (sem `natureza_projeto`) | `Required field 'natureza_projeto' is missing` |
| `{..., "natureza_projeto": "Experimental"}` (valor fora do `enum`) | `Value 'Experimental' for field 'natureza_projeto' not in enum [Básica, Aplicada]` |
| `{..., "entidade_financiadora": "FAPESP"}` (valor fora do `enum`) | `Value 'FAPESP' for field 'entidade_financiadora' not in enum [Capes, CNPq, FINEP, sem fomento externo, outras]` |
| `{..., "orcamento_projeto": "480000"}` (`string` em vez de `double`) | `Type mismatch on 'orcamento_projeto': expected double, got string` |
| `{..., "lattes_orientador": "..."}` (coluna não declarada) | `Field 'lattes_orientador' not in schema (additionalFields: false)` |

## Modelo `pessoas_envolvidas_projeto_pesquisa`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Pessoas diretamente vinculadas a um projeto de pesquisa (docentes, TAEs, estudantes ou externos), com período de participação e situação. Contém PII (`cpf`, `nome`) classificados como `sensitive`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_envolvido` | `integer` | sim | `primaryKey` | ID envolvido |
| `cpf` | `string` | sim | `pii`, `classification: sensitive`, `referencia_pnp: pessoas` (declarativo — ver nota) | CPF |
| `nome` | `string` | sim | `pii`, `classification: sensitive` | Nome |
| `categoria` | `string` | sim | `enum: [docente, TAE, externo, estudante]` | Categoria |
| `id_projeto_pesquisa` | `integer` | sim | `references projetos_pesquisa.id_projeto_pesquisa` | ID projeto de pesquisa |
| `data_ingresso` | `date` | sim | — | Data de ingresso no projeto |
| `data_saida` | `date` | não | — | Data de saída do projeto |
| `situacao_envolvido` | `string` | sim | `enum: [Ativo, Inativo]` | Situação do envolvido |
| `matricula` | `string` | sim | — | Matrícula |


### Exemplo válido

```json
{
  "id_envolvido": 60931,
  "cpf": "55566677788",
  "nome": "Lucas Henrique Barbosa",
  "categoria": "estudante",
  "id_projeto_pesquisa": 3147,
  "data_ingresso": "2024-09-01",
  "data_saida": null,
  "situacao_envolvido": "Ativo",
  "matricula": "20241012345"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"cpf": "...", "categoria": "docente"}` (sem `id_envolvido`) | `Required field 'id_envolvido' is missing` |
| `{"id_envolvido": 60931, "categoria": "docente"}` (sem `id_projeto_pesquisa`) | `Required field 'id_projeto_pesquisa' is missing` |
| `{"id_envolvido": 60931, "id_projeto_pesquisa": 3147}` (sem `categoria`) | `Required field 'categoria' is missing` |
| `{..., "categoria": "bolsista"}` (valor fora do `enum`) | `Value 'bolsista' for field 'categoria' not in enum [docente, TAE, externo, estudante]` |
| `{..., "carga_horaria": 20}` (coluna não declarada) | `Field 'carga_horaria' not in schema (additionalFields: false)` |

## `referencia_pnp` — metadado declarativo, não validação

| Campo | Modelo | `recurso` | `tipo` | `severidade` |
|---|---|---|---|---|
| `estrutura` | `projetos_pesquisa` | `campi` | `codigo` | `erro` |
| `area_tematica_cnpq` | `projetos_pesquisa` | `areas_tematicas_cnpq` | `codigo` | **`aviso`** |
| `cpf` | `pessoas_envolvidas_projeto_pesquisa` | `pessoas` | `chave_simples` | `erro` |


> **`area_tematica_cnpq` é o único `aviso` deste contrato — e a severidade do mesmo campo diverge entre contratos.** Aqui e em [Produção Intelectual]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/producao_intelectual) ele é `aviso`; em [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao), o mesmo `area_tematica_cnpq` apontando para o mesmo `recurso: areas_tematicas_cnpq` é `erro`.



## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "projetos_de_pesquisa"
info:
  title: "Projetos de Pesquisa"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados dos projetos de pesquisa conduzidos na instituição,
    incluindo informações básicas dos projetos e dados sobre os indivíduos envolvidos.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/projetos-de-pesquisa/{model}/*.parquet"
    format: "parquet"

models:
  projetos_pesquisa:
    type: table
    title: "Projetos de Pesquisa"
    description: "Informações estruturadas sobre projetos de pesquisa acadêmica institucional."
    meta:
      required: true
      disabled: false
    fields:
      id_projeto_pesquisa:
        type: integer
        title: "ID projeto de pesquisa"
        primaryKey: true
        required: true

      natureza_projeto:
        type: string
        title: "Natureza do projeto"
        enum: ["Básica", "Aplicada"]
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
        title: "Estrutura à qual vinculam-se os projetos de pesquisa"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_pesquisa_sustentavel:
        type: boolean
        title: "Aborda a temática da sustentabilidade?"
        description: "Origem: Dados ou sistemas institucionais -> Coletor PNP Microdados."

      nome_orientador:
        type: string
        title: "Nome do Orientador"

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
        enum: ["Capes", "CNPq", "FINEP", "sem fomento externo", "outras"]

      orcamento_projeto:
        type: double
        title: "Orçamento do projeto"
        description: "Valor numérico em reais (R$)."

      area_tematica_cnpq:
        type: string
        title: "Área Temática CNPq"
        description: "Formato: {codigo}"
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: aviso

      produto:
        type: string
        title: "Produto final"
    additionalFields: false

  pessoas_envolvidas_projeto_pesquisa:
    type: table
    title: "Pessoas Envolvidas em Projetos de Pesquisa"
    description: "Subconjunto de dados contendo as pessoas diretamente vinculadas aos projetos de pesquisa."
    meta:
      required: true
      disabled: false
    fields:
      id_envolvido:
        type: integer
        title: "ID envolvido"
        primaryKey: true
        required: true

      cpf:
        type: string
        title: "CPF"
        pii: true
        classification: "sensitive"
        referencia_pnp:
          recurso: pessoas
          tipo: chave_simples
          chave: cpf
          severidade: erro
          filtro_categoria_campo: categoria
          categorias_validar: ["docente", "TAE", "estudante"]

      nome:
        type: string
        title: "Nome"
        pii: true
        classification: "sensitive"

      categoria:
        type: string
        title: "Categoria"
        enum: ["docente", "TAE", "externo", "estudante"]
        required: true

      id_projeto_pesquisa:
        type: integer
        title: "ID projeto de pesquisa"
        references: "projetos_pesquisa.id_projeto_pesquisa"
        required: true

      data_ingresso:
        type: date
        title: "Data de ingresso no projeto"

      data_saida:
        type: date
        title: "Data de saída do projeto"

      situacao_envolvido:
        type: string
        title: "Situação do envolvido"
        enum: ["Ativo", "Inativo"]

      matricula:
        type: string
        title: "Matrícula"
    additionalFields: false
```

