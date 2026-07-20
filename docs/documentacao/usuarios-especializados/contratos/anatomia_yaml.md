---
layout: default
title: "Anatomia do YAML do Contrato"
toc: true
---
# Anatomia do YAML do Contrato

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página é a referência chave-a-chave do YAML usado nos **[Contratos de Dados](/documentacao/coletor/glossario#contrato-de-dados)** da PNP. Os exemplos vêm dos dez contratos reais do catálogo. Use-a junto com [Conceito](/documentacao/usuarios-especializados/contratos/conceito) (visão geral) e [Validação e qualidade](/documentacao/usuarios-especializados/contratos/validacao_e_qualidade) (como os checks rodam).

## Estrutura de alto nível

Os dez contratos compartilham o mesmo esqueleto:

```yaml
dataContractSpecification: "1.2.0"     # versão da spec datacontract.com
id: acoes_extensao                     # slug único do contrato
info:
  title: "Ações de Extensão"
  version: "1.0.0"
  status: "active"
  description: >
    ...

servers:                               # gerenciado pelo Coletor; ver nota abaixo
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/acoes-de-extensao/{model}/*.parquet"
    format: "parquet"

models:
  acoes_extensao:                      # slug bate com o slug do Modelo de Dados
    type: table
    title: "Ações de Extensão"
    description: "..."
    fields:
      id_acao_extensao:
        type: integer
        primaryKey: true
        required: true
      # ...
    additionalFields: false
```

A spec aceita também blocos `terms`, `quality`, `examples`, `links`, `tags` etc. Os dez contratos atuais não populam nenhum deles — a seção [Bloco `quality`](#bloco-quality) abaixo descreve a sintaxe para quando esses checks forem adicionados.

## `dataContractSpecification`

Versão da especificação [datacontract.com](https://datacontract.com/). Os dez contratos usam `"1.2.0"`.

## `id`

Slug único do contrato. Convenção crítica: deve bater com o `slug` do contrato cadastrado no Coletor — é por ele que o sistema localiza os arquivos de cada modelo. Exemplo: `id: acoes_extensao` ↔ contrato `acoes_extensao` no painel.

## `info`

Metadados de descoberta:

- `title` — nome humano. É o que aparece no painel do Coletor.
- `version` — SemVer (ex.: `"1.0.0"`). Deve subir junto com mudanças no schema; ver [Ciclo de vida do contrato](/documentacao/usuarios-especializados/contratos/ciclo_de_vida).
- `status` — `"active"` nos dez contratos atuais. Outros valores comuns na spec: `draft`, `proposed`, `deprecated`, `retired`.
- `description` — texto livre, multilinha. Renderizado nas páginas do catálogo.

A spec aceita também `owner`, `contact`, `tags` — úteis quando o contrato for compartilhado entre múltiplas instituições.

## `terms`

Condições de uso, finalidade e limitações. Importante para integradores quando o contrato envolve dados sensíveis ou compartilhamento entre instituições. Os dez contratos atuais **não populam** este bloco — a relação contratual entre instituição e PNP é regida fora do YAML.

## `servers`

Configuração de onde os dados ficam. Nos dez contratos, declara-se um server `local` apontando para uma pasta de arquivos **[Parquet](/documentacao/coletor/glossario#parquet)**.

> ⚠️ **O server `local` é gerenciado pelo Coletor em tempo de execução.** Ao rodar os testes, o Coletor substitui o `local` declarado no YAML por um caminho montado dinamicamente a partir do slug do contrato. Declarar `servers.local` no YAML é tolerado (e necessário para rodar a `datacontract-cli` standalone, fora do Coletor), mas o que está lá **não** é honrado quando o Coletor executa os testes.

## `models`

Cada entrada representa um dataset (tabela lógica) e vira um **[Modelo de Dados](/documentacao/coletor/glossario#modelo-de-dados)** no Coletor com slug correspondente. Atributos por modelo:

- `type: table` — único valor usado nos contratos atuais.
- `title` — nome humano.
- `description` — texto curto.
- `fields` — dicionário de colunas (próxima seção).
- `additionalFields: false` — **importante**: declara que o dataset deve ter exatamente as colunas listadas em `fields`. É o que faz a validação rejeitar extrações com colunas extras.

## Tipos de campo

Tipos efetivamente usados nos dez contratos da PNP:

| Tipo no contrato | O que representa | Onde aparece |
|---|---|---|
| `string` | Texto livre | nomes, títulos, CPF, descrições |
| `integer` | Número inteiro | IDs, ano de publicação |
| `double` | Número decimal | orçamento de projeto, matrícula equivalente |
| `boolean` | Verdadeiro/falso | `parceria_institucional`, `populacao_vulneravel` |
| `date` | Data | datas de início, término, atendimento |
| `array` | Lista de valores | `municipios_atendidos` em ações de extensão |

A spec aceita também `decimal`, `timestamp`, `numeric`, `text`, `varchar`, `bigint`, `float` — suportados pelo Coletor, mas não usados nos contratos atuais.

## Constraints de campo

Constraints **efetivamente usadas** nos dez contratos:

- `primaryKey: true` — chave primária do modelo. Único campo com essa flag por modelo. Exemplo: `id_acao_extensao`.
- `required: true` — coluna obrigatória. Se a fonte não devolver a coluna, a extração é rejeitada antes de gravar qualquer arquivo.
- `enum: [...]` — domínio fechado. Exemplo: `tipo: ["Programa", "Projeto", "Curso", "Evento", "Prestação de serviços"]` em `acoes_extensao`.
- `references: "<modelo>.<campo>"` — chave estrangeira lógica para outro modelo do mesmo contrato. Exemplo: em `pessoas_atendidas_acoes_extensao`, `id_acao_extensao` referencia `acoes_extensao.id_acao_extensao`.
- `pii: true` — flag de informação pessoal identificável. Aplicada a `cpf` e `nome` em todos os modelos de pessoas.
- `classification: "sensitive"` — nível de classificação. Acompanha `pii: true` nos campos de pessoa.
- `title` — nome humano da coluna. Sempre presente.
- `description` — descrição livre. Recomendada, ainda que opcional; é usada nas páginas do catálogo.

Constraints **suportadas pela spec mas não usadas hoje**: `unique`, `pattern` (regex), `minLength`, `maxLength`, `examples`, `tags`.

## Bloco `quality` {#bloco-quality}

Sintaxe **[SodaCL](/documentacao/coletor/glossario#sodacl)** aceita pela `datacontract-cli`. Os dez contratos atuais **não populam** este bloco — quando populado, o Coletor executa os checks contra o Parquet local na hora do teste de qualidade.

Esqueleto típico:

```yaml
quality:
  type: SodaCL
  specification: |
    checks for acoes_extensao:
      - row_count > 0
      - duplicate_count(id_acao_extensao) = 0
      - missing_count(titulo_acao) = 0
      - invalid_count(tipo) = 0:
          valid values: ["Programa", "Projeto", "Curso", "Evento", "Prestação de serviços"]
```

Tipos de check úteis para a PNP:

- `row_count > 0` — rejeita arquivos vazios.
- `duplicate_count(<col>) = 0` — garante chave primária única.
- `missing_count(<col>) = 0` — coluna não pode ter nulos.
- `invalid_count(<col>)` com `valid values` ou `valid regex` — domínio fechado mais fino que o `enum` do schema.
- `freshness(<timestamp_col>) < 30d` — dado precisa ser recente.

Sintaxe completa em [docs.soda.io](https://docs.soda.io/soda-cl/soda-cl-overview.html). Como os resultados aparecem para o operador está em [Validação e qualidade](/documentacao/usuarios-especializados/contratos/validacao_e_qualidade).

## Convenções que o Coletor exige

Três convenções que o YAML precisa respeitar para o Coletor funcionar:

1. **`id`** do YAML ↔ slug do contrato no Coletor.
2. **`models.<slug>`** ↔ slug do Modelo de Dados correspondente — a extração procura o schema pelo nome.
3. **`additionalFields: false`** em cada modelo, para que a checagem de "colunas extras" tenha referência clara.

Se qualquer uma quebrar, a extração falha ("Schema não encontrado para o modelo") ou os testes leem zero linhas.

## Exemplo real completo

O YAML íntegro de cada contrato está embutido na respectiva página do catálogo (seção "YAML completo") e versionado no [repositório do Coletor](https://github.com/PNP-CCV/coletor-pnp-microdados/tree/master/base/fixtures/contratos).

## Veja também

- [Conceito de Contrato de Dados](/documentacao/usuarios-especializados/contratos/conceito)
- [Validação e qualidade](/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)
- [Ações de Extensão](/documentacao/usuarios-especializados/contratos/acoes_de_extensao) — exemplo de página do catálogo
