---
layout: default
title: "Acordos de Parceria"
toc: true
---
# Acordos de Parceria

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `acordos_parceria` · **Versão:** `1.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Pesquisa e Inovação

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **acordos e parcerias formais** firmados pela instituição com entidades externas (públicas ou privadas) — convênios, ACTs, TEDs, contratos e instrumentos correlatos — com **foco em projetos de pesquisa**. Cada registro representa um instrumento jurídico vigente, com vigência, contrapartida financeira, fundação de apoio interveniente e vínculo a um projeto.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar o engajamento da rede federal com o setor produtivo e o setor público, e o volume de cooperação institucionalizada por trás dos projetos de pesquisa declarados.

Este é o único contrato do catálogo composto por **um único [Modelo de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-de-dados)**.

## Modelos contidos

- **`acordos_parceria`** *(opcional no fluxo)* — instrumentos jurídicos formais (acordo/parceria) firmados com instituições externas, com vigência, contrapartida e referência ao projeto de pesquisa associado.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `acordos_parceria`.

## Modelo `acordos_parceria`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é um instrumento jurídico (acordo, convênio etc.) identificado por `id_acordo`, com o objeto pactuado descrito em `descricao_objeto` e a vigência delimitada por duas datas. Não há referência declarativa (`references`) entre este contrato e `projetos_de_pesquisa`.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_acordo` | `integer` | sim | `primaryKey` | ID acordo/parceria |
| `data_formalizacao` | `date` | sim | — | Data em que o acordo foi oficialmente firmado |
| `instituicao_parceira` | `string` | sim | — | Nome da organização parceira |
| `descricao_objeto` | `string` | sim | — | Descrição do objeto pactuado no acordo |
| `data_inicio_vigencia` | `date` | sim | — | Data em que o acordo entra em vigor |
| `data_fim_vigencia` | `date` | sim | — | Data em que o acordo deixa de ter efeito |
| `numero_acordo` | `string` | sim | — | Número identificador do instrumento jurídico |
| `contrapartida_financeira_institucional` | `double` | não | — | Valor da contrapartida fornecida pela instituição, em reais. Usar `0` quando não houver |
| `contrapartida_financeira_externa` | `double` | não | — | Valor da contrapartida fornecida pela instituição parceira, em reais. Usar `0` quando não houver |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os acordos de parceria. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `fundacao_interveniente` | `string` | não | — | Nome da fundação responsável pela gestão |

> ℹ️ **`referencia_pnp` agora é conferido na extração.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`, e o Coletor confere esse código contra o espelho local de estruturas antes de gravar o Parquet — a mesma checagem que a PNP faz depois do envio, antecipada. O padrão de fábrica é o **modo bloqueante**: como a `severidade` declarada é `erro`, um código que não existe no espelho reprova a extração ali mesmo, com o campo e o valor no Registro de Extração. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### Regras de qualidade

Além do schema (colunas obrigatórias, tipos e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `numero_acordo` deve ser único, e ele, `instituicao_parceira`, `descricao_objeto` e `estrutura` não podem ser texto vazio | `mustBe: 0` |
| `data_fim_vigencia` não pode anteceder `data_inicio_vigencia`, e `data_formalizacao` não pode ser posterior ao fim da vigência | `mustBe: 0` |
| `contrapartida_financeira_externa` não pode ser negativa | `mustBe: 0` |

Essas regras rodam uma vez, sobre o contrato inteiro, ao fim da extração ([validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)) — uma violação **não** reprova a extração (o Parquet fica gravado normalmente); ela deixa o contrato em "Qualidade Reprovada" e bloqueia o envio até a linha ser corrigida na origem.

### Exemplo válido

```json
{
  "id_acordo": 5021,
  "data_formalizacao": "2024-08-15",
  "instituicao_parceira": "Petrobras S.A.",
  "descricao_objeto": "Caracterização de catalisadores para refino de petróleo pesado",
  "data_inicio_vigencia": "2024-09-01",
  "data_fim_vigencia": "2027-08-31",
  "numero_acordo": "TED 042/2024-IFRN",
  "contrapartida_financeira_institucional": 120000.0,
  "contrapartida_financeira_externa": 480000.0,
  "estrutura": "12",
  "fundacao_interveniente": "FUNCERN — Fundação de Apoio à Educação e ao Desenvolvimento Tecnológico do RN"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"data_formalizacao": "2024-08-15", "descricao_objeto": "..."}` (sem `id_acordo`) | `Required field 'id_acordo' is missing` |
| `{"id_acordo": 5021, "data_formalizacao": "2024-08-15"}` (sem `descricao_objeto`) | `Required field 'descricao_objeto' is missing` |
| `{"id_acordo": 5021, "descricao_objeto": "...", "data_formalizacao": "15/08/2024"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_formalizacao': expected date, got string '15/08/2024'` |
| `{..., "data_inicio_vigencia": "2027-01-01", "data_fim_vigencia": "2024-01-01"}` (vigência invertida) | `Vigência e formalização do acordo devem ser cronologicamente coerentes.: Actual custom_sql(acordos_parceria) was 1, expected = 0` |
| `{..., "valor_total": 480000}` (coluna não declarada) | `Field 'valor_total' not in schema (additionalFields: false)` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-01-21 | Versão inicial documentada nesta data. | — |

> ℹ️ **Uma linha só — e é esse o problema.** `info.version` está em `1.0.0` desde o início, mas `campus_origem_projeto` virou `estrutura` (formato `{id; nome}` → `{codigo}`) depois disso. Para quem já integrava é uma mudança **breaking**, e ela não bumpou a versão. Esta página foi corrigida em 2026-07-16 para reacompanhar o contrato.

## Contrato de Dados - Formato YAML

```yaml
dataContractSpecification: "1.2.0"
id: "acordos_parceria"
info:
  title: "Acordos de Parceria"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve os acordos e parcerias formais estabelecidos com instituições externas,
    com foco em projetos de pesquisa. Inclui dados de vigência, contrapartidas e fundações intervenientes.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/acordos-de-parceria/{model}/*.parquet"
    format: "parquet"

models:
  acordos_parceria:
    type: table
    title: "Acordos de Parceria"
    description: "Registros formais de parcerias com instituições externas vinculadas a projetos de pesquisa."
    meta:
      required: false
      disabled: false
    quality:
      - type: sql
        description: "Número do acordo deve ser único e textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM (
            SELECT id_acordo FROM acordos_parceria
            WHERE NULLIF(TRIM(numero_acordo), '') IS NULL
               OR NULLIF(TRIM(instituicao_parceira), '') IS NULL
               OR NULLIF(TRIM(descricao_objeto), '') IS NULL
               OR NULLIF(TRIM(estrutura), '') IS NULL
            UNION ALL
            SELECT MIN(id_acordo) FROM acordos_parceria
            GROUP BY numero_acordo HAVING COUNT(*) > 1
          ) violacoes
        mustBe: 0
      - type: sql
        description: "Vigência e formalização do acordo devem ser cronologicamente coerentes."
        query: >
          SELECT COUNT(*) FROM acordos_parceria
          WHERE data_fim_vigencia < data_inicio_vigencia
             OR data_formalizacao > data_fim_vigencia
        mustBe: 0
      - type: sql
        description: "Contrapartida financeira não pode ser negativa."
        query: >
          SELECT COUNT(*) FROM acordos_parceria WHERE contrapartida_financeira_externa < 0
        mustBe: 0
    fields:
      id_acordo:
        type: integer
        title: "ID acordo/parceria"
        primaryKey: true
        required: true
        description: "Identificador único do registro de acordo ou parceria formal."

      data_formalizacao:
        type: date
        required: true
        title: "Data de formalização"
        description: "Data em que o acordo foi oficialmente firmado."

      instituicao_parceira:
        type: string
        required: true
        title: "Instituição parceira"
        description: "Nome da organização parceira."

      descricao_objeto:
        type: string
        title: "Objeto do acordo"
        description: "Descrição do objeto pactuado no acordo."
        required: true

      data_inicio_vigencia:
        type: date
        title: "Data de início da vigência"
        description: "Data em que o acordo entra em vigor."
        required: true

      data_fim_vigencia:
        type: date
        title: "Data de fim da vigência"
        description: "Data em que o acordo deixa de ter efeito."
        required: true

      numero_acordo:
        type: string
        title: "Número do acordo"
        required: true
        description: "Número identificador do instrumento jurídico."

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

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os acordos de parceria"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      fundacao_interveniente:
        type: string
        title: "Fundação de apoio interveniente"
        description: "Nome da fundação responsável pela gestão."

    additionalFields: false
```

