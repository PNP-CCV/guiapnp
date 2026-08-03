---
layout: default
title: "Acadêmico"
toc: true
---
# Acadêmico

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `academico` · **Versão:** `1.0.0` · **Owner:** SETEC
**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`
**Área Temática:** Acadêmico

> ⚠️ **Este contrato não é coletado hoje.** O único modelo do contrato, `comunidade_interna_mat_equiv`, está declarado no YAML com `meta.disabled: true`. Um contrato cujo schema não tem nenhum modelo habilitado **não é criado no Coletor**: "Acadêmico" não aparece no painel, não tem modelo para configurar e não entra em nenhuma contagem. Se ele já existia de sincronizações anteriores, a sincronização com a PNP o remove — junto com seus modelos — por **exclusão lógica**: nada é apagado, nem os registros de extração e envio, nem os arquivos já gerados; eles continuam listados nas telas de **Extrações** e **Envios**, que mostram o histórico por conta própria; o que sai de vista são as listagens de **Contratos** e **Modelos de Dados**.
>
> Não é erro nem falha de sincronização. Se você sincronizou e o contrato não apareceu, é exatamente este o motivo — e não há nada a fazer.
>
> **A página continua aqui como referência do contrato.** A PNP pode reabilitar o modelo numa versão futura do schema, e nesse dia tudo o que está descrito abaixo volta a valer.

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve os **indicadores acadêmicos institucionais**, organizados por subconjuntos temáticos. Hoje o contrato carrega um único subconjunto: a **matrícula equivalente** da comunidade interna.

Matrícula equivalente não é contagem de alunos. É a matrícula **ponderada** por FECH (Fator de Equiparação de Carga Horária) e pelo Fator de Esforço — a métrica que a **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** usa para comparar cursos de durações e cargas horárias diferentes numa base única, alimentando indicadores legais e o cálculo de orçamento da Rede Federal.

A origem do dado é a própria PNP (PBIP), não um sistema acadêmico da instituição: ele volta para o Coletor como insumo já calculado.

## Modelos contidos

- **`comunidade_interna_mat_equiv`** *(desabilitado — não é coletado)* — matrícula equivalente por estrutura (campus), ponderada por FECH e Fator de Esforço.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Modelo `comunidade_interna_mat_equiv`

> ⚠️ **Modelo desabilitado — não é coletado hoje.** O contrato declara `meta.required: false` e `meta.disabled: true` para este modelo. A sincronização com a PNP **não o importa**: ele não aparece na lista de modelos do painel e não há como configurar extração para ele. Como é o único modelo do contrato, é ele que faz o contrato "Acadêmico" inteiro deixar de existir no Coletor — ver o aviso no topo desta página.
>
> Se um dia a PNP reabilitar o modelo, ele volta **zerado**: a configuração de extração anterior não volta junto e precisa ser refeita.

### Resumo do modelo

Tabela única do contrato. Cada linha associa uma **estrutura** (campus) ao seu total de matrícula equivalente. Não há chave de negócio além do `id` sintético — a granularidade real é dada por `estrutura`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id` | `integer` | sim | `primaryKey` | Identificador |
| `estrutura` | `string` | não | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se as matrículas equivalentes. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `matricula_equivalente` | `double` | não | — | Matrícula ponderada por FECH e Fator de Esforço para fins de orçamento e indicadores legais. Origem: PNP [PNP PBIP], Tabela "Técnicos %", Pasta "MedidasIndicadores" |

> **`referencia_pnp` é metadado declarativo, não validação local.** O campo `estrutura` declara `referencia_pnp: {recurso: campi, tipo: codigo, severidade: erro}`, mas o Coletor não checa esse vínculo na extração — localmente `estrutura` é validada apenas como `string`. A conferência de que o código de campus existe acontece na **validação referencial do lado da PNP**, após o envio.

### Regras de qualidade

Atualmente não declaradas neste contrato (bloco `quality` ausente). A validação ativa hoje é apenas o schema (colunas obrigatórias, tipos, e rejeição de colunas extras via `additionalFields: false`).

### Exemplo válido

```json
{
  "id": 1,
  "estrutura": "12",
  "matricula_equivalente": 4821.75
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"estrutura": "12", "matricula_equivalente": 4821.75}` (sem `id`) | `Required field 'id' is missing` |
| `{"id": "1", ...}` (`string` em vez de `integer`) | `Type mismatch on 'id': expected integer, got string` |
| `{..., "matricula_equivalente": "4821,75"}` (decimal com vírgula, `double` espera número) | `Type mismatch on 'matricula_equivalente': expected double, got string '4821,75'` |
| `{..., "ano_referencia": 2026}` (coluna não declarada) | `Field 'ano_referencia' not in schema (additionalFields: false)` |

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2026-07-16 | Versão inicial documentada nesta data. | — |

## YAML completo

```yaml
dataContractSpecification: "1.2.0"
id: "academico"
info:
  title: "Acadêmico"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato descreve a estrutura de dados dos indicadores acadêmicos institucionais,
    organizados por subconjuntos temáticos.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/academico/{model}/*.parquet"
    format: "parquet"

models:
  comunidade_interna_mat_equiv:
    type: table
    title: "Comunidade Interna - Matrículas Equivalentes"
    description: "Indicadores de matrícula equivalente da comunidade interna, ponderados por FECH e Fator de Esforço."
    meta:
      required: false
      disabled: true
    fields:
      id:
        type: integer
        title: "Identificador"
        primaryKey: true
        required: true

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se as matrículas equivalentes"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      matricula_equivalente:
        type: double
        title: "Matrícula equivalente"
        description: >
          Matrícula ponderada por FECH e Fator de Esforço para fins de orçamento
          e indicadores legais. Origem: PNP [PNP PBIP], Tabela "Técnicos %",
          Pasta "MedidasIndicadores".
    additionalFields: false
```

## Veja também

- [Conceito de Contrato de Dados]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/conceito)
- [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)
