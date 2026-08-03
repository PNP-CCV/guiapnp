---
layout: default
title: Ações de Extensão
toc: true
---
# Ações de Extensão

* TOC
  {:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `acoes_extensao` · **Versão:** `1.0.0` · **Owner:** SETEC

**Status:** `Ativo` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Extensão

## Resumo de negócio

Este Contrato de Dados descreve as **ações de extensão acadêmica** — programas, projetos, cursos, eventos e prestações de serviço — executadas pela instituição em interação com a comunidade externa.

A PNP coleta este contrato para mensurar o impacto social da extensão (alcance comunitário, atendimento a populações vulneráveis, parcerias institucionais e financiamento) e o engajamento da rede federal com a sociedade. Os três modelos cobrem a ação em si, as **pessoas atendidas** (público-alvo, com PII) e as **pessoas envolvidas** na execução (docentes, TAEs, estudantes, externos).

## Modelos contidos

- **`acoes_extensao`** *(obrigatório no fluxo)* — ações de extensão (programa, projeto, curso, evento, prestação de serviço) com escopo, vigência, parceria, financiamento e área temática CNPq.
- **`pessoas_atendidas_acoes_extensao`** *(opcional no fluxo)* — pessoas impactadas diretamente pelas ações (público-alvo). Contém PII (`cpf`, `nome`).
- **`pessoas_envolvidas_acoes_extensao`** *(obrigatório no fluxo)* — pessoas formalmente envolvidas na execução (docentes, TAEs, estudantes, externos). Contém PII.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Modelo `acoes_extensao`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela principal do contrato. Cada linha é uma ação de extensão única, identificada por `id_acao_extensao`. As tabelas `pessoas_atendidas_acoes_extensao` e `pessoas_envolvidas_acoes_extensao` referenciam-na por chave estrangeira.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_acao_extensao` | `integer` | sim | `primaryKey` | ID da Ação de Extensão fornecido pela Instituição |
| `tipo` | `string` | sim | `enum: [Programa, Projeto, Curso, Evento, Prestação de serviços]` | Tipo |
| `titulo_acao` | `string` | sim | — | Título da ação |
| `resumo_acao` | `string` | não | — | Resumo da ação |
| `estrutura` | `string` | não | `referencia_pnp: campi` (declarativo — ver nota) | Estrutura à qual vinculam-se as ações de extensão. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `projeto_extensao_sustentavel` | `boolean` | não | — | Se projeto, aborda a temática da sustentabilidade? Aplicável quando `tipo = "Projeto"`. Origem: Dados ou sistemas institucionais → Coletor PNP Microdados |
| `parceria_institucional` | `boolean` | não | — | Ação com parceria institucional? |
| `instrumento_parceria` | `string` | não | `enum: [Contrato, Convênio, Acordo, Nenhum]` | Instrumento de parceria |
| `nome_coordenador` | `string` | não | — | Nome do Coordenador |
| `data_inicio` | `date` | não | — | Data de início |
| `data_termino` | `date` | não | — | Data de término |
| `situacao_acao` | `string` | não | `enum: [Em andamento, Finalizado, Cancelado]` | Situação da ação |
| `data_ultima_situacao` | `date` | não | — | Data da última situação |
| `municipios_atendidos` | `array` (de `bigint`) | não | `referencia_pnp: municipios` (declarativo — ver nota) | Municípios atendidos, por código IBGE — lista de números, ex. `[2408102, 2403103]`. Ver a ressalva sobre o formato abaixo |
| `entidade_financiadora` | `string` | não | — | Entidade financiadora |
| `contrapartida_financeira` | `string` | não | — | Contrapartida financeira institucional |
| `area_tematica_cnpq` | `string` | não | `referencia_pnp: areas_tematicas_cnpq` (declarativo — ver nota) | Área temática CNPq. Formato: `{codigo}` |
| `subeixo_tecnologico` | `string` | não | `referencia_pnp: subeixos_tecnologicos` (declarativo — ver nota) | Subeixo tecnológico. Formato: `{codigo}` |
| `populacao_vulneravel` | `boolean` | não | — | Destinado à população em vulnerabilidade? |
| `tipo_vulnerabilidade` | `string` | não | `enum: [Socioeconômica, Educacional, Gênero e Raça, Deficiência ou Condição de Saúde, Geracional, Territorial]` | Tipo de vulnerabilidade |
| `produto` | `string` | não | — | Produto |

> ⚠️ **`tipo_vulnerabilidade` deixou de ser texto livre.** O campo passou a ter domínio fechado com seis valores. Descrições em prosa que funcionavam antes (por exemplo, "Idosos em situação de vulnerabilidade socioeconômica") agora reprovam a validação — é preciso mapear a informação da origem para um dos seis valores do `enum`.

> **`municipios_atendidos`:**  O que a validação de schema aceita é **uma lista de números** — `[2408102, 2403103]` —, não `"2408102; 2403103"`. A notação `{codigo; codigo}` ali é a taquigrafia do autor para "vários códigos", herdada dos campos que são mesmo string (`vigencia`, `objeto_acordo`). Mandar string aqui reprova por tipo.

### Exemplo válido

```json
{
  "id_acao_extensao": 1042,
  "tipo": "Projeto",
  "titulo_acao": "Inclusão Digital na Comunidade do Bairro Nordeste",
  "resumo_acao": "Oficinas semanais de letramento digital para idosos em parceria com ONG local.",
  "estrutura": "12",
  "projeto_extensao_sustentavel": false,
  "parceria_institucional": true,
  "instrumento_parceria": "Convênio",
  "nome_coordenador": "Maria da Silva Souza",
  "data_inicio": "2025-03-01",
  "data_termino": "2025-11-30",
  "situacao_acao": "Em andamento",
  "data_ultima_situacao": "2025-03-01",
  "municipios_atendidos": [2408102, 2403103],
  "entidade_financiadora": "Pró-Reitoria de Extensão",
  "contrapartida_financeira": "R$ 12.000,00",
  "area_tematica_cnpq": "60900007",
  "subeixo_tecnologico": "08",
  "populacao_vulneravel": true,
  "tipo_vulnerabilidade": "Socioeconômica",
  "produto": "Cartilha de letramento digital"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"tipo": "Projeto", "titulo_acao": "..."}` (sem `id_acao_extensao`) | `Required field 'id_acao_extensao' is missing` |
| `{..., "tipo": "Workshop"}` (valor fora do `enum`) | `Value 'Workshop' for field 'tipo' not in enum [Programa, Projeto, Curso, Evento, Prestação de serviços]` |
| `{..., "data_inicio": "01/03/2025"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_inicio': expected date, got string '01/03/2025'` |
| `{..., "tipo_vulnerabilidade": "Idosos em situação de vulnerabilidade socioeconômica"}` (texto livre, fora do `enum`) | `Value 'Idosos em situação de vulnerabilidade socioeconômica' for field 'tipo_vulnerabilidade' not in enum` |
| `{..., "observacoes": "qualquer coisa"}` (coluna não declarada) | `Field 'observacoes' not in schema (additionalFields: false)` |

## Modelo `pessoas_atendidas_acoes_extensao`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`) — o único modelo opcional deste contrato. Enquanto ninguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Pessoas impactadas diretamente por uma ação de extensão (público-alvo). Cada linha é vinculada a uma ação via `id_acao_extensao`. Contém PII (`cpf` e `nome`) classificados como `sensitive`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo              | Tipo      | Obrigatório | Constraints                                  | Descrição           |
| ------------------ | --------- | ----------- | -------------------------------------------- | ------------------- |
| `id_atendido`      | `integer` | sim         | `primaryKey`                                 | ID atendido         |
| `cpf`              | `string`  | não         | `pii`, `classification: sensitive`           | CPF                 |
| `nome`             | `string`  | não         | `pii`, `classification: sensitive`           | Nome                |
| `id_acao_extensao` | `integer` | sim         | `references acoes_extensao.id_acao_extensao` | ID ação de extensão |
| `data_atendimento` | `date`    | não         | —                                            | Data de atendimento |

### Exemplo válido

```json
{
  "id_atendido": 87012,
  "cpf": "12345678901",
  "nome": "João Pereira de Almeida",
  "id_acao_extensao": 1042,
  "data_atendimento": "2025-04-15"
}
```

### Exemplos inválidos

| Payload (resumido)                                              | Erro                                                           |
| --------------------------------------------------------------- | -------------------------------------------------------------- |
| `{"cpf": "...", "id_acao_extensao": 1042}` (sem `id_atendido`)  | `Required field 'id_atendido' is missing`                      |
| `{"id_atendido": 87012, "cpf": "..."}` (sem `id_acao_extensao`) | `Required field 'id_acao_extensao' is missing`                 |
| `{"id_atendido": "87012", ...}` (`string` em vez de `integer`)  | `Type mismatch on 'id_atendido': expected integer, got string` |

## Modelo `pessoas_envolvidas_acoes_extensao`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Pessoas formalmente envolvidas na execução de uma ação (docentes, TAEs, estudantes ou externos), com período de participação e situação. Contém (`cpf`, `nome`).

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_envolvido` | `integer` | sim | `primaryKey` | ID envolvido |
| `cpf` | `string` | não | `pii`, `classification: sensitive`, `referencia_pnp: pessoas` (declarativo — ver nota) | CPF |
| `nome` | `string` | não | `pii`, `classification: sensitive` | Nome |
| `categoria` | `string` | sim | `enum: [docente, TAE, externo, estudante]` | Categoria |
| `id_acao_extensao` | `integer` | sim | `references acoes_extensao.id_acao_extensao` | ID ação de extensão |
| `data_ingresso` | `date` | não | — | Data de ingresso na ação |
| `data_saida` | `date` | não | — | Data de saída da ação |
| `situacao_envolvido` | `string` | não | `enum: [Ativo, Inativo]` | Situação do envolvido |
| `data_ultima_situacao` | `date` | não | — | Data da última situação |
| `matricula` | `string` | não | — | Matrícula |


### Exemplo válido

```json
{
  "id_envolvido": 50214,
  "cpf": "98765432100",
  "nome": "Carla Mendes Lima",
  "categoria": "docente",
  "id_acao_extensao": 1042,
  "data_ingresso": "2025-03-01",
  "data_saida": null,
  "situacao_envolvido": "Ativo",
  "data_ultima_situacao": "2025-03-01",
  "matricula": "1548923"
}
```

### Exemplos inválidos

| Payload (resumido)                                                    | Erro                                                                                     |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `{"id_envolvido": 50214, "id_acao_extensao": 1042}` (sem `categoria`) | `Required field 'categoria' is missing`                                                  |
| `{..., "categoria": "professor"}` (valor fora do `enum`)              | `Value 'professor' for field 'categoria' not in enum [docente, TAE, externo, estudante]` |
| `{..., "extra_field": "x"}` (coluna não declarada)                    | `Field 'extra_field' not in schema (additionalFields: false)`                            |

## `referencia_pnp` — metadado declarativo

Este é o contrato que mais usa a chave `referencia_pnp`, e ela aponta para quatro recursos distintos da PNP:

| Campo                  | Modelo                              | `recurso`               | `tipo`          | `severidade` |
| ---------------------- | ----------------------------------- | ----------------------- | --------------- | ------------ |
| `estrutura`            | `acoes_extensao`                    | `campi`                 | `codigo`        | `erro`       |
| `municipios_atendidos` | `acoes_extensao`                    | `municipios`            | `array_codigo`  | `erro`       |
| `area_tematica_cnpq`   | `acoes_extensao`                    | `areas_tematicas_cnpq`  | `codigo`        | `erro`       |
| `subeixo_tecnologico`  | `acoes_extensao`                    | `subeixos_tecnologicos` | `codigo`        | `erro`       |
| `cpf`                  | `pessoas_envolvidas_acoes_extensao` | `pessoas`               | `chave_simples` | `erro`       |

> **Consequência:** Apenas os dados que encontram referência na PNP são validados, ou seja, caso seja informado uma `area_tematica_cnpq` que não esteja dentro da Base da PNP, a respectiva ação de extensão será rejeitada, até que seja fornecido o dado correto.

## Contrato de Dados - Formato YAML

```yaml
dataContractSpecification: "1.2.0"
id: "acoes_extensao"
info:
  title: "Ações de Extensão"
  version: "1.0.0"
  status: "active"
  description: >
    Este contrato de dados descreve a estrutura das informações relativas às ações de extensão,
    seus participantes e as pessoas atendidas, promovidas por uma instituição pública de ensino.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/acoes-de-extensao/{model}/*.parquet"
    format: "parquet"

models:
  acoes_extensao:
    type: table
    title: "Ações de Extensão"
    description: "Informações estruturadas sobre as ações de extensão desenvolvidas institucionalmente."
    meta:
      required: true
      disabled: false
    fields:
      id_acao_extensao:
        type: integer
        title: "ID ação de extensão"
        description: >
          ID da Ação de Extensão fornecido pela Instituição
        primaryKey: true
        required: true

      tipo:
        type: string
        title: "Tipo"
        enum: ["Programa", "Projeto", "Curso", "Evento", "Prestação de serviços"]
        required: true

      titulo_acao:
        type: string
        title: "Título da ação"
        required: true

      resumo_acao:
        type: string
        title: "Resumo da ação"

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se as ações de extensão"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_extensao_sustentavel:
        type: boolean
        title: "Se projeto, aborda a temática da sustentabilidade?"
        description: >
          Aplicável quando tipo = "Projeto". Origem: Dados ou sistemas
          institucionais -> Coletor PNP Microdados.

      parceria_institucional:
        type: boolean
        title: "Ação com parceria institucional?"

      instrumento_parceria:
        type: string
        title: "Instrumento de parceria"
        enum: ["Contrato", "Convênio", "Acordo", "Nenhum"]

      nome_coordenador:
        type: string
        title: "Nome do Coordenador"

      data_inicio:
        type: date
        title: "Data de início"

      data_termino:
        type: date
        title: "Data de término"

      situacao_acao:
        type: string
        title: "Situação da ação"
        enum: ["Em andamento", "Finalizado", "Cancelado"]

      data_ultima_situacao:
        type: date
        title: "Data da última situação"

      municipios_atendidos:
        type: array
        items:
          type: bigint
        title: "Municípios atendidos"
        description: "Formato: {codigo; codigo}"
        referencia_pnp:
          recurso: municipios
          tipo: array_codigo
          severidade: erro

      entidade_financiadora:
        type: string
        title: "Entidade financiadora"

      contrapartida_financeira:
        type: string
        title: "Contrapartida financeira institucional"

      area_tematica_cnpq:
        type: string
        title: "Área temática CNPq"
        description: "Formato: {codigo}"
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: erro

      subeixo_tecnologico:
        type: string
        title: "Subeixo tecnológico"
        description: "Formato: {codigo}"
        referencia_pnp:
          recurso: subeixos_tecnologicos
          tipo: codigo
          severidade: erro

      populacao_vulneravel:
        type: boolean
        title: "Destinado à população em vulnerabilidade?"

      tipo_vulnerabilidade:
        type: string
        title: "Tipo de vulnerabilidade"
        enum: ["Socioeconômica", "Educacional", "Gênero e Raça", "Deficiência ou Condição de Saúde", "Geracional", "Territorial"]

      produto:
        type: string
        title: "Produto"
    additionalFields: false

  pessoas_atendidas_acoes_extensao:
    type: table
    title: "Pessoas Atendidas em Ações de Extensão"
    description: "Registros de pessoas impactadas diretamente por ações de extensão."
    meta:
      required: false
      disabled: false
    fields:
      id_atendido:
        type: integer
        title: "ID atendido"
        primaryKey: true
        required: true

      cpf:
        type: string
        title: "CPF"
        pii: true
        classification: "sensitive"

      nome:
        type: string
        title: "Nome"
        pii: true
        classification: "sensitive"

      id_acao_extensao:
        type: integer
        title: "ID ação de extensão"
        references: "acoes_extensao.id_acao_extensao"
        required: true

      data_atendimento:
        type: date
        title: "Data de atendimento"
    additionalFields: false

  pessoas_envolvidas_acoes_extensao:
    type: table
    title: "Pessoas Envolvidas em Ações de Extensão"
    description: "Registros de participantes formalmente envolvidos na execução das ações."
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

      id_acao_extensao:
        type: integer
        title: "ID ação de extensão"
        references: "acoes_extensao.id_acao_extensao"
        required: true

      data_ingresso:
        type: date
        title: "Data de ingresso na ação"

      data_saida:
        type: date
        title: "Data de saída da ação"

      situacao_envolvido:
        type: string
        title: "Situação do envolvido"
        enum: ["Ativo", "Inativo"]

      data_ultima_situacao:
        type: date
        title: "Data da última situação"

      matricula:
        type: string
        title: "Matrícula"
    additionalFields: false
```
