---
layout: default
title: "Anatomia do YAML do Contrato"
toc: true
---
# Anatomia do YAML do Contrato

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página é a referência chave-a-chave do YAML usado nos **[Contratos de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** da PNP. Os exemplos vêm dos onze contratos reais do catálogo. Use-a junto com [Conceito]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/conceito) (visão geral) e [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade) (como os checks rodam).

## Estrutura de alto nível

Os onze contratos compartilham o mesmo esqueleto:

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
    meta:                              # extensão fora da spec; ver abaixo
      required: true
      disabled: false
    fields:
      id_acao_extensao:
        type: integer
        primaryKey: true
        required: true
      # ...
    additionalFields: false
```

A spec aceita também blocos `terms`, `quality`, `examples`, `links`, `tags` etc. Os onze contratos atuais não populam nenhum deles — a seção [Bloco `quality`](#bloco-quality) abaixo descreve a sintaxe para quando esses checks forem adicionados. O bloco [`meta`](#bloco-meta), por outro lado, **é populado hoje em todos os modelos dos onze contratos** — mas ele não vem da spec: é uma extensão da PNP, descrita mais adiante.

## `dataContractSpecification`

Versão da especificação [datacontract.com](https://datacontract.com/). Os onze contratos usam `"1.2.0"`.

## `id`

Slug único do contrato. Convenção crítica: deve bater com o `slug` do contrato cadastrado no Coletor — é por ele que o sistema localiza os arquivos de cada modelo. Exemplo: `id: acoes_extensao` ↔ contrato `acoes_extensao` no painel.

## `info`

Metadados de descoberta:

- `title` — nome humano. É o que aparece no painel do Coletor.
- `version` — SemVer (ex.: `"1.0.0"`). Deve subir junto com mudanças no schema; ver [Ciclo de vida do contrato]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/ciclo_de_vida).
- `status` — `"active"` nos onze contratos atuais. Outros valores comuns na spec: `draft`, `proposed`, `deprecated`, `retired`.
- `description` — texto livre, multilinha. Renderizado nas páginas do catálogo.

A spec aceita também `owner`, `contact`, `tags` — úteis quando o contrato for compartilhado entre múltiplas instituições.

## `terms`

Condições de uso, finalidade e limitações. Importante para integradores quando o contrato envolve dados sensíveis ou compartilhamento entre instituições. Os onze contratos atuais **não populam** este bloco — a relação contratual entre instituição e PNP é regida fora do YAML.

## `servers`

Configuração de onde os dados ficam. Nos onze contratos, declara-se um server `local` apontando para uma pasta de arquivos **[Parquet]({{ site.baseurl }}/documentacao/coletor/glossario#parquet)**.

> ⚠️ **O server `local` é gerenciado pelo Coletor em tempo de execução.** Ao rodar os testes, o Coletor substitui o `local` declarado no YAML por um caminho montado dinamicamente a partir do slug do contrato. Declarar `servers.local` no YAML é tolerado (e necessário para rodar a `datacontract-cli` standalone, fora do Coletor), mas o que está lá **não** é honrado quando o Coletor executa os testes.

## `models`

Cada entrada representa um dataset (tabela lógica) e vira um **[Modelo de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-de-dados)** no Coletor com slug correspondente. Atributos por modelo:

- `type: table` — único valor usado nos contratos atuais.
- `title` — nome humano.
- `description` — texto curto.
- `meta` — extensão fora da spec, com as flags `required` e `disabled` (próxima seção).
- `fields` — dicionário de colunas.
- `additionalFields: false` — **importante**: declara que o dataset deve ter exatamente as colunas listadas em `fields`. É o que faz a validação rejeitar extrações com colunas extras.

## Bloco `meta` {#bloco-meta}

`meta` é um bloco de **nível de modelo** — irmão de `title`, `description` e `fields`, dentro de cada entrada de `models`. Ele **não faz parte da `dataContractSpecification` 1.2.0**: passa pelo leitor porque a spec tolera chaves extras, e quem o interpreta é o Coletor. Hoje **todos os modelos dos onze contratos** declaram o bloco.

```yaml
models:
  acoes_extensao:
    type: table
    title: "Ações de Extensão"
    description: "..."
    meta:
      required: true      # o modelo segura o progresso do contrato
      disabled: false     # o modelo é importado da PNP
    fields:
      # ...
```

São duas chaves, ambas booleanas:

| Chave | Padrão | Efeito quando **`true`** | Efeito quando **`false`** |
|---|---|---|---|
| `required` | `true` | Modelo **obrigatório**: entra no status do contrato, no contador do assistente do dashboard e na extração em lote. | Modelo **opcional**: enquanto não tiver nenhuma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)**, fica fora do status do contrato, dos contadores e da extração em lote. |
| `disabled` | `false` | Modelo **desabilitado**: nunca é importado da PNP. Se já existia no Coletor, é recolhido por exclusão lógica na sincronização seguinte. | Modelo habilitado: comportamento normal. |

### `required` — o modelo é cobrado ou não

`meta.required: false` **não** esconde o modelo: ele é importado normalmente e aparece na lista de modelos, como qualquer outro. O que muda é apenas quem o Coletor cobra:

- **Sem nenhuma Configuração de Extração**, o modelo opcional é ignorado pelo [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato), pelos contadores dos cards e pela extração em lote do contrato. Ele não vira "pendência".
- **Assim que ganha uma configuração**, passa a contar como qualquer obrigatório: o contrato volta para *Aguardando Extração* e só fecha quando esse modelo for extraído, testado, enviado e aprovado.
- O cálculo é feito na hora, então o caminho é reversível: removidas todas as configurações do modelo, ele sai do fluxo de novo. Não existe botão de "desativar modelo" no painel — remover a configuração é a forma de desistir da coleta.

> ⚠️ **Não clique em "Extrair" num modelo sem configuração de extração.** O botão de extração individual do modelo não checa se existe configuração: a execução vai até o fim e falha com *"Nenhum dataset foi gerado"*. O registro de falha fica no histórico do modelo. Se o modelo for opcional e não configurado, isso não muda o status do contrato — mas polui o histórico à toa.

Um contrato cujos modelos são **todos opcionais e nenhum configurado** aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente. Quatro contratos do catálogo estão nessa situação hoje: [Acordos de Parceria]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acordos_de_parceria), [Projetos de Desenvolvimento Institucional]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_desenvolvimento_institucional), [Orçamento]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/orcamento) e [Projetos de Ensino]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_ensino).

### `disabled` — o modelo existe ou não

`meta.disabled: true` significa "a PNP desligou este modelo nesta versão do contrato". Ele **nunca é importado**: não aparece na lista de modelos e não há o que configurar. Um modelo já importado que passe a ser `disabled` é recolhido na sincronização seguinte por **exclusão lógica** — o histórico de extrações e os arquivos já gerados não são apagados, e continuam listados nas telas de **Extrações** e **Envios**, que mostram o histórico por conta própria; o que sai de vista são as listagens de **Contratos** e **Modelos de Dados**.


> ⚠️ **Reabilitar um modelo não devolve a configuração.** Se a PNP reabilitar um modelo antes desabilitado, ele volta **zerado**: a configuração de extração anterior não volta junto e precisa ser refeita.

### Defaults conservadores

Quando o bloco `meta` está ausente, incompleto, ou traz um valor que não é um booleano puro, valem os padrões `required: true` e `disabled: false` — a opção conservadora. Duas consequências práticas:

- **Contrato antigo, sem `meta`, continua se comportando exatamente como antes**: todos os modelos obrigatórios e habilitados. A extensão é retrocompatível.
- **Escreva booleanos YAML puros**: `true` / `false`, sem aspas. `required: "false"` (string) e `disabled: 1` (número) são **silenciosamente ignorados** e caem no padrão.

> ⚠️ **Dois `required` diferentes, em níveis diferentes.** `meta.required` é obrigatoriedade **do modelo** (se o Coletor cobra aquele dataset). O `required: true` dentro de `fields:` é obrigatoriedade **da coluna** (se aquele campo precisa vir preenchido). São conceitos independentes, e um não implica o outro.

## Tipos de campo

Tipos efetivamente usados nos onze contratos da PNP:

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

Constraints **efetivamente usadas** nos onze contratos:

- `primaryKey: true` — chave primária do modelo. Único campo com essa flag por modelo. Exemplo: `id_acao_extensao`.
- `required: true` — coluna obrigatória. Se a fonte não devolver a coluna, a extração é rejeitada antes de gravar qualquer arquivo.
- `enum: [...]` — domínio fechado. Exemplo: `tipo: ["Programa", "Projeto", "Curso", "Evento", "Prestação de serviços"]` em `acoes_extensao`.
- `references: "<modelo>.<campo>"` — chave estrangeira lógica para outro modelo do mesmo contrato. Exemplo: em `pessoas_atendidas_acoes_extensao`, `id_acao_extensao` referencia `acoes_extensao.id_acao_extensao`.
- `pii: true` — flag de informação pessoal identificável. Aplicada a `cpf` e `nome` em todos os modelos de pessoas.
- `classification: "sensitive"` — nível de classificação. Acompanha `pii: true` nos campos de pessoa.
- `title` — nome humano da coluna. Sempre presente.
- `description` — descrição livre. Recomendada, ainda que opcional; é usada nas páginas do catálogo.

Constraints **suportadas pela spec mas não usadas hoje**: `unique`, `pattern` (regex), `minLength`, `maxLength`, `examples`, `tags`.

## Bloco `referencia_pnp` {#bloco-referencia-pnp}

Extensão da PNP fora da especificação, declarada **por campo**: diz que aquele valor aponta para uma entidade do cadastro da Rede — um campus, um município, uma área do CNPq, o CPF de alguém da instituição.

```yaml
estrutura:
  type: string
  referencia_pnp:
    recurso: campi
    tipo: codigo
    severidade: erro
```

O motor de teste do contrato ignora a chave. Quem a lê é a validação referencial do Coletor, que confere o valor contra o cadastro local sincronizado da PNP **antes de gravar o Parquet** — de fábrica em modo sombra, apenas registrando. A gramática completa (incluindo a forma em lista, que roteia por categoria, e a `chave_composta`) está em [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

## Bloco `quality` {#bloco-quality}

Sintaxe **[SodaCL]({{ site.baseurl }}/documentacao/coletor/glossario#sodacl)** aceita pela `datacontract-cli`. Os onze contratos atuais **não populam** este bloco — quando populado, o Coletor executa os checks contra o Parquet local na hora do teste de qualidade.

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

Sintaxe completa em [docs.soda.io](https://docs.soda.io/soda-cl/soda-cl-overview.html). Como os resultados aparecem para o operador está em [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade).

## Convenções que o Coletor exige

Três convenções que o YAML precisa respeitar para o Coletor funcionar:

1. **`id`** do YAML ↔ slug do contrato no Coletor.
2. **`models.<slug>`** ↔ slug do Modelo de Dados correspondente — a extração procura o schema pelo nome.
3. **`additionalFields: false`** em cada modelo, para que a checagem de "colunas extras" tenha referência clara.

Se qualquer uma quebrar, a extração falha ("Schema não encontrado para o modelo") ou os testes leem zero linhas.

## Exemplo real completo

O YAML íntegro de cada contrato está embutido na respectiva página do catálogo (seção "YAML completo") e versionado no [repositório do Coletor](https://github.com/PNP-CCV/coletor-pnp-microdados/tree/master/base/fixtures/contratos).

## Veja também

- [Conceito de Contrato de Dados]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/conceito)
- [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)
- [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial)
- [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) — exemplo de página do catálogo
