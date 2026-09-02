---
layout: default
title: "Projetos de Pesquisa"
toc: true
---
# Projetos de Pesquisa

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `projetos_de_pesquisa` · **Versão:** `2.0.0` · **Owner:** SETEC

**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Pesquisa e Inovação

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve as **iniciativas de investigação científica e tecnológica** conduzidas por servidores e estudantes da rede federal — projetos de pesquisa básica e aplicada, com fomento próprio ou externo (CNPq, CAPES, FINEP, FAPs estaduais).

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar a **produção em P&D** da rede federal: orçamento, fomento, área temática CNPq, vigência e participação de docentes, TAEs, estudantes e externos. Os dois modelos cobrem o projeto em si e as pessoas envolvidas (com PII).

Este contrato é também o destino lógico do vínculo declarado textualmente em `acordos_parceria.objeto_acordo` — embora não haja `references` formal entre os dois contratos, o `id_projeto_pesquisa` daqui é o que aparece naquele campo.

## Modelos contidos

- **`projetos_pesquisa`** *(obrigatório no fluxo)* — projetos de pesquisa institucionais, com natureza, vigência, situação, orçamento, entidade financiadora e área temática CNPq.
- **`pessoas_envolvidas_projeto_pesquisa`** *(obrigatório no fluxo)* — pessoas vinculadas a cada projeto (docentes, TAEs, estudantes, externos). Contém PII (`cpf`, `nome`).

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

## Modelo `projetos_pesquisa`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela principal do contrato. Cada linha é um projeto de pesquisa identificado por `id_projeto_pesquisa`. A tabela `pessoas_envolvidas_projeto_pesquisa` referencia-a por chave estrangeira. **Atenção ao slug do modelo**: `projetos_pesquisa` (sem o `de_`), embora o `id` do contrato e o nome do arquivo sejam `projetos_de_pesquisa`.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_projeto_pesquisa` | `integer` | sim | `primaryKey` | ID projeto de pesquisa |
| `natureza_projeto` | `string` | sim | `enum: [Básica, Aplicada]` | Natureza do projeto |
| `titulo_projeto` | `string` | sim | — | Título do Projeto |
| `resumo_projeto` | `string` | não | — | Resumo do Projeto |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os projetos de pesquisa. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `projeto_pesquisa_sustentavel` | `boolean` | sim | — | Aborda a temática da sustentabilidade? |
| `nome_orientador` | `string` | não | — | Nome do Orientador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | não | — | Data de término. Obrigatória para projeto `Finalizado`/`Cancelado` (ver *Regras de qualidade*), pode ficar em branco enquanto estiver em andamento |
| `situacao_projeto` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação do projeto |
| `entidade_financiadora` | `string` | não | `enum: [Capes, CNPq, FINEP, sem fomento externo, outras]` | Entidade financiadora |
| `contrapartida_financeira_institucional` | `double` | não | — | Valor da contrapartida financeira institucional em reais (R$). Usar `0` quando não houver |
| `contrapartida_financeira_externa` | `double` | não | — | Valor da contrapartida financeira externa em reais (R$). Usar `0` quando não houver |
| `area_tematica_cnpq` | `string` | sim | `referencia_pnp: areas_tematicas_cnpq` (conferido na extração — ver nota) | Área Temática CNPq. Formato: `{codigo}` |
| `produto` | `string` | não | — | Produto final |

### Regras de qualidade

Além do schema (colunas obrigatórias, tipos e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `titulo_projeto`, `estrutura` e `area_tematica_cnpq` não podem ser texto vazio | `mustBe: 0` |
| `data_termino` não pode anteceder `data_inicio`, e projeto `Finalizado`/`Cancelado` precisa de `data_termino` | `mustBe: 0` |
| As contrapartidas não podem ser negativas; contrapartida externa maior que zero exige entidade financiadora externa, e entidade financiadora externa exige contrapartida externa maior que zero | `mustBe: 0` |

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
  "contrapartida_financeira_institucional": 0.0,
  "contrapartida_financeira_externa": 480000.00,
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
| `{..., "contrapartida_financeira_externa": "480000"}` (`string` em vez de `double`) | `Type mismatch on 'contrapartida_financeira_externa': expected double, got string` |
| `{..., "entidade_financiadora": "CNPq", "contrapartida_financeira_externa": 0}` (fomento externo sem contrapartida externa) | `As contrapartidas financeiras não podem ser negativas e o financiamento externo deve ser coerente com a entidade financiadora.: Actual custom_sql(projetos_pesquisa) was 1, expected = 0` |
| `{..., "lattes_orientador": "..."}` (coluna não declarada) | `Field 'lattes_orientador' not in schema (additionalFields: false)` |

## Modelo `pessoas_envolvidas_projeto_pesquisa`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Pessoas diretamente vinculadas a um projeto de pesquisa (docentes, TAEs, estudantes ou externos), com período de participação e situação. Contém PII (`cpf`, `nome`) classificados como `sensitive`.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_envolvido` | `integer` | sim | `primaryKey` | ID envolvido |
| `cpf` | `string` | sim | `pii`, `classification: sensitive` | CPF |
| `nome` | `string` | sim | `pii`, `classification: sensitive` | Nome |
| `categoria` | `string` | sim | `enum: [docente, TAE, externo, estudante]` | Categoria |
| `id_projeto_pesquisa` | `integer` | sim | `references projetos_pesquisa.id_projeto_pesquisa` | ID projeto de pesquisa |
| `data_ingresso` | `date` | sim | — | Data de ingresso no projeto |
| `data_saida` | `date` | não | — | Data de saída do projeto |
| `situacao_envolvido` | `string` | sim | `enum: [Ativo, Inativo]` | Situação do envolvido |
| `matricula` | `string` | não | `referencia_pnp` roteada por categoria, com chave composta `[cpf, matricula]` (conferida na extração — ver nota) | Matrícula SIAPE para docentes e TAEs ou SISTEC para estudantes. Exigida para participantes internos e proibida para `externo` (ver *Regras de qualidade*) |

### Regras de qualidade

Além do schema, o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| A mesma pessoa (`cpf`) não pode aparecer duas vezes no mesmo projeto | `mustBe: 0` |
| `cpf` deve conter 11 dígitos, `nome` não pode ser vazio, e `matricula` é exigida para `docente`/`TAE`/`estudante` e proibida para `externo` | `mustBe: 0` |
| `data_saida` não pode anteceder `data_ingresso`; envolvido `Ativo` não pode ter `data_saida` e `Inativo` precisa ter | `mustBe: 0` |
| Não pode existir pessoa envolvida sem o projeto correspondente em `projetos_pesquisa` | `mustBe: 0` |
| O período de participação tem de caber na vigência do projeto, e projeto `Finalizado`/`Cancelado` não pode ter participante `Ativo` | `mustBe: 0` |

> As duas últimas regras fazem `JOIN` com `projetos_pesquisa`. Quando esse modelo fica fora do teste (opcional sem configuração, ou `meta.disabled`), a regra é descartada em vez de reprovar o contrato por tabela ausente.

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
  "matricula": "2024123456"
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

## `referencia_pnp` — conferido na extração

| Campo | Modelo | `recurso` | `tipo` | `severidade` |
|---|---|---|---|---|
| `estrutura` | `projetos_pesquisa` | `campi` | `codigo` | `erro` |
| `area_tematica_cnpq` | `projetos_pesquisa` | `areas_tematicas_cnpq` | `codigo` | **`aviso`** |
| `matricula` (`docente`, `TAE`) | `pessoas_envolvidas_projeto_pesquisa` | `servidores` | `chave_composta: [cpf, matricula]` | `erro` |
| `matricula` (`estudante`) | `pessoas_envolvidas_projeto_pesquisa` | `matriculas` | `chave_composta: [cpf, matricula]` | `erro` |

O Coletor **confere esses valores contra os espelhos locais da PNP** antes de gravar o Parquet, no **modo bloqueante** por padrão — uma referência que não existe no espelho reprova a extração, com o campo e o valor no Registro de Extração. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial). A matrícula usa roteamento por categoria: o par `[cpf, matricula]` de docentes e TAEs é conferido em `servidores`, enquanto o de estudantes é conferido em `matriculas`. Participantes externos não são submetidos a essas regras.

### `matricula` é roteada por `categoria`

`matricula` guarda coisas diferentes conforme o vínculo: SIAPE para servidor, Sistec para estudante. A regra é declarada em **lista**, e cada entrada leva o próprio filtro de categoria — `docente`/`TAE` conferem contra `servidores`, `estudante` contra `matriculas`. A conferência é do par `(cpf, matricula)`: conferir os dois campos em separado aceitaria o CPF de uma pessoa com a matrícula de outra.

`externo` fica de fora por não estar em nenhuma das entradas, e está certo — quem é externo não tem matrícula na instituição. Matrícula vazia também não é violação: o campo é opcional, e quem cobra preenchimento é a regra `quality`.

> ℹ️ **`externo` saiu do `categorias_validar` do `cpf`.** Ele estava listado, e como externo não consta de cadastro nenhum da instituição, a regra apontaria **todo participante externo** como CPF inexistente. Era o único dos três contratos de pessoas a incluí-lo.

> ℹ️ **`area_tematica_cnpq` é o único `aviso` deste contrato — e a severidade do mesmo campo diverge entre contratos.** Aqui e em [Produção Intelectual]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/producao_intelectual) ele é `aviso`; em [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao), o mesmo `area_tematica_cnpq` apontando para o mesmo `recurso: areas_tematicas_cnpq` é `erro`. A divergência deixou de ser inócua: quando o modo `bloqueante` for ligado, o mesmo código de área reprovaria a extração de Ações de Extensão e passaria como aviso aqui. É uma decisão da PNP, no YAML — o Coletor honra o que cada contrato declara.

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2025-09-02 | Versão inicial documentada nesta data. | — |
| `2.0.0` | 2026-09-01 | `orcamento_projeto` virou o par `contrapartida_financeira_institucional`/`contrapartida_financeira_externa`; `data_termino` e `matricula` deixaram de ser obrigatórias; regras `quality` acrescentadas. | **sim** |

> ℹ️ **Uma linha só — e é esse o problema.** `info.version` está em `1.0.0` desde o início, mas o contrato mudou depois: `campus_vinculado` virou `estrutura`, `produto_final` virou `produto`, `area_tematica_cnpq` passou a `{codigo}`, e `projeto_pesquisa_sustentavel` foi acrescentado. As três primeiras são **breaking** para quem já integrava, e nenhuma bumpou a versão. Esta página foi corrigida em 2026-07-16 para reacompanhar o contrato.

## Contrato de Dados - Formato YAML


```yaml
dataContractSpecification: "1.2.0"
id: "projetos_de_pesquisa"
info:
  title: "Projetos de Pesquisa"
  version: "2.0.0"
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
    description: "Informações estruturadas sobre projetos de pesquisa institucional."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM projetos_pesquisa
          WHERE NULLIF(TRIM(titulo_projeto), '') IS NULL
             OR NULLIF(TRIM(estrutura), '') IS NULL
             OR NULLIF(TRIM(area_tematica_cnpq), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Datas e situação do projeto devem ser coerentes."
        query: >
          SELECT COUNT(*) FROM projetos_pesquisa
          WHERE data_termino < data_inicio
             OR (situacao_projeto IN ('Finalizado', 'Cancelado') AND data_termino IS NULL)
        mustBe: 0
      - type: sql
        description: "As contrapartidas financeiras não podem ser negativas e o financiamento externo deve ser coerente com a entidade financiadora."
        query: >
          SELECT COUNT(*) FROM projetos_pesquisa
          WHERE contrapartida_financeira_institucional < 0
             OR contrapartida_financeira_externa < 0
             OR (
               contrapartida_financeira_externa > 0
               AND (
                 NULLIF(TRIM(entidade_financiadora), '') IS NULL
                 OR entidade_financiadora = 'sem fomento externo'
               )
             )
             OR (
               NULLIF(TRIM(entidade_financiadora), '') IS NOT NULL
               AND entidade_financiadora <> 'sem fomento externo'
               AND coalesce(contrapartida_financeira_externa, 0) <= 0
             )
        mustBe: 0
    fields:
      id_projeto_pesquisa:
        type: integer
        title: "ID projeto de pesquisa"
        primaryKey: true
        required: true
        description: "Identificador único do registro de projeto de pesquisa."

      natureza_projeto:
        type: string
        title: "Natureza do projeto"
        enum: ["Básica", "Aplicada"]
        required: true
        description: "Classificação do projeto de pesquisa como básica ou aplicada."

      titulo_projeto:
        type: string
        title: "Título do Projeto"
        required: true
        description: "Título do projeto de pesquisa institucional."

      resumo_projeto:
        type: string
        title: "Resumo do Projeto"
        description: "Resumo do projeto de pesquisa institucional, descrevendo seus objetivos e metodologia."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os projetos de pesquisa"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_pesquisa_sustentavel:
        type: boolean
        required: true
        title: "Aborda a temática da sustentabilidade?"
        description: "Indica se o projeto de pesquisa aborda a temática da sustentabilidade: true quando abordar e false quando não abordar."

      nome_orientador:
        type: string
        title: "Nome do Orientador"
        description: "Nome do orientador do projeto de pesquisa, conforme registro institucional."

      data_inicio:
        type: date
        required: true
        title: "Data de início"
        description: "Data em que o projeto de pesquisa foi oficialmente iniciado."

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
        description: "Situação atual do projeto de pesquisa institucional."

      entidade_financiadora:
        type: string
        title: "Entidade financiadora"
        enum: ["Capes", "CNPq", "FINEP", "sem fomento externo", "outras"]
        description: "Qual a principal entidade financiadora do projeto de pesquisa institucional."

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

      area_tematica_cnpq:
        type: string
        title: "Área Temática CNPq"
        description: "Formato: {codigo}. O código da área temática CNPq é fornecido pelo Coletor PNP."
        required: true
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: aviso

      produto:
        type: string
        title: "Produto final"
        description: "Descrição do produto final do projeto de pesquisa, caso aplicável."
    additionalFields: false

  pessoas_envolvidas_projeto_pesquisa:
    type: table
    title: "Pessoas Envolvidas em Projetos de Pesquisa"
    description: "Subconjunto de dados contendo as pessoas diretamente vinculadas aos projetos de pesquisa."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Não pode haver pessoas envolvidas duplicadas no mesmo projeto."
        query: >
          SELECT COUNT(*) FROM (
            SELECT cpf, id_projeto_pesquisa
            FROM pessoas_envolvidas_projeto_pesquisa
            GROUP BY cpf, id_projeto_pesquisa HAVING COUNT(*) > 1
          ) duplicados
        mustBe: 0
      - type: sql
        description: "CPF deve conter 11 dígitos, nome não pode ser vazio e matrícula é exigida apenas para participantes internos."
        query: >
          SELECT COUNT(*) FROM pessoas_envolvidas_projeto_pesquisa
          WHERE NOT regexp_full_match(cpf, '[0-9]{11}')
             OR NULLIF(TRIM(nome), '') IS NULL
             OR (categoria IN ('docente', 'TAE', 'estudante')
                 AND NULLIF(TRIM(matricula), '') IS NULL)
             OR (categoria = 'externo' AND NULLIF(TRIM(matricula), '') IS NOT NULL)
        mustBe: 0
      - type: sql
        description: "Datas e situação da participação devem ser coerentes."
        query: >
          SELECT COUNT(*) FROM pessoas_envolvidas_projeto_pesquisa
          WHERE data_saida < data_ingresso
             OR (situacao_envolvido = 'Ativo' AND data_saida IS NOT NULL)
             OR (situacao_envolvido = 'Inativo' AND data_saida IS NULL)
        mustBe: 0
      - type: sql
        description: "Não pode existir pessoa envolvida sem projeto correspondente."
        query: >
          SELECT COUNT(*)
          FROM pessoas_envolvidas_projeto_pesquisa p
          LEFT JOIN projetos_pesquisa pr
            ON pr.id_projeto_pesquisa = p.id_projeto_pesquisa
          WHERE pr.id_projeto_pesquisa IS NULL
        mustBe: 0
      - type: sql
        description: "O período de participação deve estar contido na vigência do projeto, e projetos encerrados não podem possuir participantes ativos."
        query: >
          SELECT COUNT(*)
          FROM pessoas_envolvidas_projeto_pesquisa p
          INNER JOIN projetos_pesquisa pr
            ON pr.id_projeto_pesquisa = p.id_projeto_pesquisa
          WHERE p.data_ingresso < pr.data_inicio
             OR (
               pr.data_termino IS NOT NULL
               AND p.data_ingresso > pr.data_termino
             )
             OR (
               p.data_saida IS NOT NULL
               AND pr.data_termino IS NOT NULL
               AND p.data_saida > pr.data_termino
             )
             OR (
               pr.situacao_projeto IN ('Finalizado', 'Cancelado')
               AND p.situacao_envolvido = 'Ativo'
             )
        mustBe: 0
    fields:
      id_envolvido:
        type: integer
        title: "ID envolvido"
        primaryKey: true
        required: true
        description: "Identificador único do registro de pessoa envolvida em projeto de pesquisa."

      cpf:
        type: string
        title: "CPF"
        pii: true
        classification: "sensitive"
        required: true
        description: "CPF da pessoa envolvida no projeto de pesquisa."

      nome:
        type: string
        title: "Nome"
        pii: true
        required: true
        classification: "sensitive"
        description: "Nome da pessoa envolvida no projeto de pesquisa, conforme registro institucional."

      categoria:
        type: string
        title: "Categoria"
        enum: ["docente", "TAE", "externo", "estudante"]
        required: true
        description: "Categoria da pessoa envolvida no projeto de pesquisa, conforme classificação institucional."

      id_projeto_pesquisa:
        type: integer
        title: "ID projeto de pesquisa"
        references: "projetos_pesquisa.id_projeto_pesquisa"
        required: true
        description: "Identificador do projeto de pesquisa ao qual a pessoa está vinculada."

      data_ingresso:
        type: date
        required: true
        title: "Data de ingresso no projeto"
        description: "Data em que a pessoa começou a participar do projeto de pesquisa."

      data_saida:
        type: date
        required: false
        title: "Data de saída do projeto"
        description: "Data em que a pessoa deixou de participar do projeto de pesquisa. Pode ser nula se a pessoa ainda estiver envolvida no projeto."

      situacao_envolvido:
        type: string
        required: true
        title: "Situação do envolvido"
        enum: ["Ativo", "Inativo"]
        description: "Situação atual da pessoa envolvida no projeto de pesquisa, indicando se ainda está participando ou não."

      matricula:
        type: string
        title: "Matrícula"
        description: "Matrícula da pessoa envolvida no projeto de pesquisa, caso seja participante interno. Siape para docentes e TAE, matrícula SISTEC para estudantes."
        referencia_pnp:
          - recurso: servidores
            tipo: chave_composta
            chaves: [cpf, matricula]
            filtro_categoria_campo: categoria
            categorias_validar: ["docente", "TAE"]
            severidade: erro
          - recurso: matriculas
            tipo: chave_composta
            chaves: [cpf, matricula]
            filtro_categoria_campo: categoria
            categorias_validar: ["estudante"]
            severidade: erro
    additionalFields: false
```

