---
layout: default
title: "Ações de Extensão"
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

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve as **ações de extensão acadêmica** — programas, projetos, cursos, eventos e prestações de serviço — executadas pela instituição em interação com a comunidade externa, conforme prevê a LDB e a política nacional de extensão da Rede Federal.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar o impacto social da extensão (alcance comunitário, atendimento a populações vulneráveis, parcerias institucionais e financiamento) e o engajamento da rede federal com a sociedade. Os quatro modelos cobrem os **programas** que agrupam as ações, a ação em si, as **pessoas atendidas** (público-alvo, com PII) e as **pessoas envolvidas** na execução (docentes, TAEs, estudantes, externos).

## Modelos contidos

- **`programa`** *(opcional no fluxo)* — programas de extensão institucionais, aos quais as ações podem estar vinculadas por `acoes_extensao.programa`.
- **`acoes_extensao`** *(obrigatório no fluxo)* — ações de extensão (projeto, curso, evento, prestação de serviço) com escopo, vigência, parceria, financiamento e área temática CNPq.
- **`pessoas_atendidas_acoes_extensao`** *(opcional no fluxo)* — pessoas impactadas diretamente pelas ações (público-alvo). Contém PII (`cpf`, `nome`).
- **`pessoas_envolvidas_acoes_extensao`** *(obrigatório no fluxo)* — pessoas formalmente envolvidas na execução (docentes, TAEs, estudantes, externos). Contém PII.

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

## Modelo `programa`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo.

### Resumo do modelo

O programa de extensão é o guarda-chuva sob o qual as ações se organizam. Cada linha é um programa institucional identificado por `id_programa`; `acoes_extensao.programa` aponta para cá. Deixou de ser um valor do `enum` de `acoes_extensao.tipo` (onde `Programa` convivia com `Projeto`, `Curso`…) e virou modelo próprio.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_programa` | `integer` | sim | `primaryKey` | ID do programa de extensão |
| `titulo_programa` | `string` | sim | — | Título do programa |
| `descricao_programa` | `string` | não | — | Descrição do programa |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os programas de extensão. Formato: `{codigo}`, fornecido pelo Coletor PNP |

### Regras de qualidade

Não declaradas para este modelo (bloco `quality` ausente). A validação ativa é apenas o schema (colunas obrigatórias, tipos, e rejeição de colunas extras via `additionalFields: false`).

### Exemplo válido

```json
{
  "id_programa": 900,
  "titulo_programa": "Programa de Inclusão Digital",
  "descricao_programa": "Guarda-chuva das ações de letramento digital.",
  "estrutura": "12"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"titulo_programa": "..."}` (sem `id_programa`) | `Required field 'id_programa' is missing` |
| `{"id_programa": 900, "titulo_programa": "..."}` (sem `estrutura`) | `Required field 'estrutura' is missing` |

## Modelo `acoes_extensao`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela principal do contrato. Cada linha é uma ação de extensão única, identificada por `id_acao_extensao`. As tabelas `pessoas_atendidas_acoes_extensao` e `pessoas_envolvidas_acoes_extensao` referenciam-na por chave estrangeira.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_acao_extensao` | `integer` | sim | `primaryKey` | ID da Ação de Extensão fornecido pela Instituição |
| `tipo` | `string` | sim | `enum: [Projeto, Curso, Evento, Prestação de serviços]` | Tipo |
| `programa` | `integer` | não | `references programa.id_programa` | ID do programa de extensão ao qual a ação está vinculada |
| `titulo_acao` | `string` | sim | — | Título da ação |
| `resumo_acao` | `string` | não | — | Resumo da ação |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se as ações de extensão. Formato: `{codigo}`, fornecido pelo Coletor PNP |
| `projeto_extensao_sustentavel` | `boolean` | não | — | Se projeto, aborda a temática da sustentabilidade? Aplicável quando `tipo = "Projeto"` — só pode ser `true` nesse caso (ver *Regras de qualidade*) |
| `parceria_institucional` | `boolean` | sim | — | Ação com parceria institucional? |
| `instrumento_parceria` | `string` | não | `enum: [Contrato, Convênio, Acordo, Nenhum]` | Instrumento de parceria, quando houver parceria institucional |
| `nome_coordenador` | `string` | não | — | Nome do Coordenador |
| `data_inicio` | `date` | sim | — | Data de início |
| `data_termino` | `date` | não | — | Data de término. Pode ficar em branco enquanto a ação estiver em andamento |
| `situacao_acao` | `string` | sim | `enum: [Em andamento, Finalizado, Cancelado]` | Situação da ação |
| `data_ultima_situacao` | `date` | não | — | Data da última situação |
| `municipios_atendidos` | `array` (de `bigint`) | não | `referencia_pnp: municipios` (conferido na extração — ver nota) | Municípios atendidos, por código IBGE — lista de números, ex. `[2408102, 2403103]`. Ver a ressalva sobre o formato abaixo |
| `entidade_financiadora` | `string` | não | — | Entidade financiadora |
| `contrapartida_financeira_institucional` | `double` | não | — | Valor da contrapartida financeira institucional em reais (R$). Usar `0` quando não houver |
| `contrapartida_financeira_externa` | `double` | não | — | Valor da contrapartida financeira externa em reais (R$). Usar `0` quando não houver |
| `area_tematica_cnpq` | `string` | sim | `referencia_pnp: areas_tematicas_cnpq` (conferido na extração — ver nota) | Área temática CNPq. Formato: `{codigo}` |
| `subeixo_tecnologico` | `string` | sim | `referencia_pnp: subeixos_tecnologicos` (conferido na extração — ver nota) | Subeixo tecnológico. Formato: `{codigo}` |
| `populacao_vulneravel` | `boolean` | sim | — | Destinado à população em vulnerabilidade? |
| `tipo_vulnerabilidade` | `array` (de `string`) | não | `enum: [Socioeconômica, Educacional, Gênero e Raça, Deficiência ou Condição de Saúde, Geracional, Territorial]` | Tipos de vulnerabilidade atendidos — lista, obrigatória quando `populacao_vulneravel` é `true` e vazia quando é `false` (ver *Regras de qualidade*) |
| `produto` | `string` | não | — | Produto |

> ℹ️ **`municipios_atendidos`: o "Formato: `{codigo; codigo}`" do YAML engana.** A descrição no fixture sugere uma string com `;` separando códigos, mas o campo é declarado `type: array` com `items: {type: bigint}`. O que a validação de schema aceita é **uma lista de números** — `[2408102, 2403103]` —, não `"2408102; 2403103"`. A notação `{codigo; codigo}` ali é a taquigrafia do autor para "vários códigos", herdada dos campos que são mesmo string (`vigencia`, `objeto_acordo`). Mandar string aqui reprova por tipo.

### Regras de qualidade

Além do schema (colunas obrigatórias, tipos e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `titulo_acao`, `estrutura` e `subeixo_tecnologico` não podem ser texto vazio | `mustBe: 0` |
| `data_termino` e `data_ultima_situacao` têm de ser posteriores a `data_inicio`, e ação `Finalizado`/`Cancelado` precisa de `data_termino` | `mustBe: 0` |
| `instrumento_parceria` tem de ser `Nenhum` quando não há parceria, e diferente de `Nenhum` quando há | `mustBe: 0` |
| `projeto_extensao_sustentavel` só pode ser `true` quando `tipo = Projeto`; `tipo_vulnerabilidade` tem de vir preenchido quando `populacao_vulneravel` é `true` e vazio quando é `false` | `mustBe: 0` |
| As contrapartidas não podem ser negativas, e contrapartida externa maior que zero exige `entidade_financiadora` preenchida | `mustBe: 0` |
| A ação precisa ter sido executada por pelo menos um dia no **ano de referência** — `data_inicio` não pode ser posterior a 31/12 e `data_termino`, quando informada, não pode ser anterior a 01/01 | `mustBe: 0` |

> ℹ️ **Ano de referência.** As duas últimas consultas usam o token `#ANO_REFERENCIA#`, substituído pelo Coletor antes de o contrato chegar ao motor: é o **ano-base** da coleta, `ciclo.ano - 1` (o ciclo de 2026 coleta o que aconteceu em 2025). Contrato que usa o token sem ciclo de coleta associado falha com erro explícito, em vez de mandar SQL quebrado ao motor.

Essas regras rodam uma vez, sobre o contrato inteiro, ao fim da extração ([validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)) — uma violação **não** reprova a extração deste modelo (o Parquet fica gravado normalmente); ela deixa o contrato em "Qualidade Reprovada" e bloqueia o envio até a linha ser corrigida na origem.

### Exemplo válido

```json
{
  "id_acao_extensao": 1042,
  "tipo": "Projeto",
  "programa": 900,
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
  "contrapartida_financeira_institucional": 12000.0,
  "contrapartida_financeira_externa": 0.0,
  "area_tematica_cnpq": "60900007",
  "subeixo_tecnologico": "08",
  "populacao_vulneravel": true,
  "tipo_vulnerabilidade": ["Socioeconômica"],
  "produto": "Cartilha de letramento digital"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"tipo": "Projeto", "titulo_acao": "..."}` (sem `id_acao_extensao`) | `Required field 'id_acao_extensao' is missing` |
| `{..., "tipo": "Workshop"}` (valor fora do `enum`) | `Value 'Workshop' for field 'tipo' not in enum [Projeto, Curso, Evento, Prestação de serviços]` |
| `{..., "data_inicio": "01/03/2025"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_inicio': expected date, got string '01/03/2025'` |
| `{..., "observacoes": "qualquer coisa"}` (coluna não declarada) | `Field 'observacoes' not in schema (additionalFields: false)` |
| `{..., "populacao_vulneravel": true, "tipo_vulnerabilidade": []}` (vulnerabilidade sem tipo) | `Sustentabilidade e vulnerabilidade devem respeitar seus campos condicionantes.: Actual custom_sql(acoes_extensao) was 1, expected = 0` |
| `{..., "parceria_institucional": false, "instrumento_parceria": "Acordo"}` (instrumento sem parceria) | `O instrumento deve ser coerente com a existência de parceria.: Actual custom_sql(acoes_extensao) was 1, expected = 0` |

## Modelo `pessoas_atendidas_acoes_extensao`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`) — o único modelo opcional deste contrato. Enquanto ninguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote do contrato. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Pessoas impactadas diretamente por uma ação de extensão (público-alvo). Cada linha é vinculada a uma ação via `id_acao_extensao`. Contém PII (`cpf` e `nome`) classificados como `sensitive`.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_atendido` | `integer` | sim | `primaryKey` | ID atendido |
| `cpf` | `string` | sim | `pii`, `classification: sensitive` | CPF |
| `nome` | `string` | sim | `pii`, `classification: sensitive` | Nome |
| `id_acao_extensao` | `integer` | sim | `references acoes_extensao.id_acao_extensao` | ID ação de extensão |

### Regras de qualidade

Além do schema, o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| A mesma pessoa (`cpf`) não pode aparecer duas vezes na mesma ação | `mustBe: 0` |
| `cpf` deve conter 11 dígitos e `nome` não pode ser texto vazio | `mustBe: 0` |
| Não pode existir pessoa atendida sem a ação correspondente em `acoes_extensao` | `mustBe: 0` |

> A última regra faz `JOIN` com `acoes_extensao`. Quando esse modelo fica fora do teste (opcional sem configuração, ou `meta.disabled`), a regra é descartada em vez de reprovar o contrato por tabela ausente.

### Exemplo válido

```json
{
  "id_atendido": 87012,
  "cpf": "12345678901",
  "nome": "João Pereira de Almeida",
  "id_acao_extensao": 1042
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"cpf": "...", "id_acao_extensao": 1042}` (sem `id_atendido`) | `Required field 'id_atendido' is missing` |
| `{"id_atendido": 87012, "cpf": "..."}` (sem `id_acao_extensao`) | `Required field 'id_acao_extensao' is missing` |
| `{"id_atendido": "87012", ...}` (`string` em vez de `integer`) | `Type mismatch on 'id_atendido': expected integer, got string` |

## Modelo `pessoas_envolvidas_acoes_extensao`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Pessoas formalmente envolvidas na execução de uma ação (docentes, TAEs, estudantes ou externos), com período de participação e situação. Contém PII (`cpf`, `nome`).

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_envolvido` | `integer` | sim | `primaryKey` | ID envolvido |
| `cpf` | `string` | sim | `pii`, `classification: sensitive`, `referencia_pnp: pessoas` (conferido na extração — ver nota) | CPF |
| `nome` | `string` | sim | `pii`, `classification: sensitive` | Nome |
| `categoria` | `string` | sim | `enum: [docente, TAE, externo, estudante]` | Categoria |
| `id_acao_extensao` | `integer` | sim | `references acoes_extensao.id_acao_extensao` | ID ação de extensão |
| `data_ingresso` | `date` | sim | — | Data de ingresso na ação |
| `data_saida` | `date` | não | — | Data de saída da ação |
| `situacao_envolvido` | `string` | sim | `enum: [Ativo, Inativo]` | Situação do envolvido |
| `data_ultima_situacao` | `date` | sim | — | Data da última situação |
| `matricula` | `string` | não | — | Matrícula SIAPE (servidor) ou Sistec (aluno). Exigida para `docente`, `TAE` e `estudante`; proibida para `externo` (ver *Regras de qualidade*) |

### Regras de qualidade

Além do schema, o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| A mesma pessoa (`cpf`) não pode aparecer duas vezes na mesma ação | `mustBe: 0` |
| `cpf` deve conter 11 dígitos; `matricula` é exigida para `docente`/`TAE`/`estudante` e tem de vir vazia para `externo` | `mustBe: 0` |
| `data_saida` e `data_ultima_situacao` têm de ser posteriores a `data_ingresso`; envolvido `Ativo` não pode ter `data_saida` e `Inativo` precisa ter | `mustBe: 0` |
| Não pode existir pessoa envolvida sem a ação correspondente em `acoes_extensao` | `mustBe: 0` |

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
  "data_ultima_situacao": "2025-03-01"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"id_envolvido": 50214, "id_acao_extensao": 1042}` (sem `categoria`) | `Required field 'categoria' is missing` |
| `{..., "categoria": "professor"}` (valor fora do `enum`) | `Value 'professor' for field 'categoria' not in enum [docente, TAE, externo, estudante]` |
| `{..., "extra_field": "x"}` (coluna não declarada) | `Field 'extra_field' not in schema (additionalFields: false)` |

## `referencia_pnp` — conferido na extração

Este é o contrato que mais usa a chave `referencia_pnp`, e ela aponta para quatro recursos distintos da PNP:

| Campo | Modelo | `recurso` | `tipo` | `severidade` |
|---|---|---|---|---|
| `estrutura` | `programa` | `campi` | `codigo` | `erro` |
| `estrutura` | `acoes_extensao` | `campi` | `codigo` | `erro` |
| `municipios_atendidos` | `acoes_extensao` | `municipios` | `array_codigo` | `erro` |
| `area_tematica_cnpq` | `acoes_extensao` | `areas_tematicas_cnpq` | `codigo` | `aviso` |
| `subeixo_tecnologico` | `acoes_extensao` | `subeixos_tecnologicos` | `codigo` | `erro` |
| `cpf` | `pessoas_envolvidas_acoes_extensao` | `pessoas` | `chave_simples` | `erro` |

Todas declaram `severidade: erro`, menos `area_tematica_cnpq`, que é `aviso` — como também é em [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) e em [Produção Intelectual]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/producao_intelectual). O Coletor **confere esses valores contra os espelhos locais da PNP** antes de gravar o Parquet, antecipando a checagem que antes só acontecia depois do envio. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

> ℹ️ **Duas ressalvas de leitura.** A primeira: o padrão de fábrica é o **modo sombra** — um `subeixo_tecnologico: "99"` inexistente ainda passa, mas agora aparece apontado no Registro de Extração, em vez de só voltar como rejeição da PNP dias depois. A segunda: `recurso: pessoas` não corresponde a uma tabela — a PNP mantém dois cadastros (`servidores` e `matriculas`), e o Coletor resolve `pessoas` pela união dos dois. É a conferência certa para o CPF sozinho; conferir a **matrícula** exige a forma com roteamento por categoria.

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2025-09-02 | Versão inicial documentada nesta data. | — |

> ℹ️ **Uma linha só — e é esse o problema.** `info.version` está em `1.0.0` desde o início, mas o contrato mudou depois: `campus_vinculado` virou `estrutura`, `municipios_atendidos` trocou de string para `array` de `bigint`, `area_tematica_cnpq`/`subeixo_tecnologico` perderam o nome e viraram `{codigo}`, e `projeto_extensao_sustentavel` foi acrescentado. Para quem já integrava, as três primeiras são **breaking** — e nenhuma bumpou a versão. A tabela tem uma linha porque o contrato nunca versionou essas mudanças, não porque elas não aconteceram. Esta página foi corrigida em 2026-07-16 para reacompanhar o contrato.

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
  programa:
    type: table
    title: "Programa"
    description: "Informações estruturadas sobre os programas de extensão desenvolvidos institucionalmente."
    meta:
      required: false
      disabled: false
    fields:
      id_programa:
        type: integer
        title: "ID programa"
        primaryKey: true
        required: true

      titulo_programa:
        type: string
        title: "Título do programa"
        required: true

      descricao_programa:
        type: string
        title: "Descrição do programa"

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os programas de extensão"
        required: true
        description: >
          Formato: {codigo}. Código fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

  acoes_extensao:
    type: table
    # externalUrl: "./storage/extracoes/acoes-de-extensao/acoes_extensao.parquet"
    title: "Ações de Extensão"
    description: "Informações estruturadas sobre as ações de extensão desenvolvidas institucionalmente."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM acoes_extensao
          WHERE NULLIF(TRIM(titulo_acao), '') IS NULL
             OR NULLIF(TRIM(estrutura), '') IS NULL
             OR NULLIF(TRIM(subeixo_tecnologico), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Datas e situação da ação devem ser coerentes."
        query: >
          SELECT COUNT(*) FROM acoes_extensao
          WHERE data_termino <= data_inicio
             OR data_ultima_situacao <= data_inicio
             OR (situacao_acao IN ('Finalizado', 'Cancelado') AND data_termino IS NULL)
        mustBe: 0
      - type: sql
        description: "O instrumento deve ser coerente com a existência de parceria."
        query: >
          SELECT COUNT(*) FROM acoes_extensao
          WHERE (parceria_institucional = FALSE AND instrumento_parceria <> 'Nenhum')
             OR (parceria_institucional = TRUE AND instrumento_parceria = 'Nenhum')
        mustBe: 0
      - type: sql
        description: "Sustentabilidade e vulnerabilidade devem respeitar seus campos condicionantes."
        query: >
          SELECT COUNT(*) FROM acoes_extensao
          WHERE (tipo <> 'Projeto' AND projeto_extensao_sustentavel = TRUE)
             OR (populacao_vulneravel = TRUE AND len(list_filter(coalesce(tipo_vulnerabilidade, []), x -> NULLIF(TRIM(x), '') IS NOT NULL)) = 0)
             OR (populacao_vulneravel = FALSE AND len(coalesce(tipo_vulnerabilidade, [])) > 0)
        mustBe: 0
      - type: sql
        description: "Ações com entidade financiadora devem ter contrapartida financeira externa maior que zero."
        query: >
          SELECT COUNT(*) FROM acoes_extensao
          WHERE contrapartida_financeira_institucional < 0
          OR contrapartida_financeira_externa < 0
          OR (
              contrapartida_financeira_externa > 0
              AND NULLIF(TRIM(entidade_financiadora), '') IS NULL
            )
        mustBe: 0
      - type: sql
        description: "A ação de extensão deve ter sido executada por pelo menos um dia no ano de referência."
        query: >
          SELECT COUNT(*) FROM acoes_extensao
          WHERE data_inicio > DATE '#ANO_REFERENCIA#-12-31'
             OR (data_termino IS NOT NULL AND data_termino < DATE '#ANO_REFERENCIA#-01-01')
        mustBe: 0
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
        enum: ["Projeto", "Curso", "Evento", "Prestação de serviços"]
        description: >
          Tipo de ação de extensão, conforme lista pré-definida.
        required: true
      programa:
        type: integer
        title: "Programa"
        description: "ID do programa de extensão ao qual a ação está vinculada."
        references: "programa.id_programa"
        required: false

      titulo_acao:
        type: string
        title: "Título da ação"
        description: "Título da ação de extensão."
        required: true

      resumo_acao:
        type: string
        title: "Resumo da ação"
        description: "Resumo da ação de extensão."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se as ações de extensão"
        required: true
        description: >
          Formato: {codigo}. Código Fornecido pelo Coletor PNP.
        referencia_pnp:
          recurso: campi
          tipo: codigo
          severidade: erro

      projeto_extensao_sustentavel:
        type: boolean
        title: "Se projeto, aborda a temática da sustentabilidade?"
        required: false
        description: >
          Aplicável quando tipo = "Projeto". Avaliar se o projeto de extensão aborda a temática da sustentabilidade.

      parceria_institucional:
        type: boolean
        title: "Ação com parceria institucional?"
        description: >
          Avaliar se a ação de extensão é realizada em parceria.
        required: true

      instrumento_parceria:
        type: string
        title: "Instrumento de parceria"
        required: false
        enum: ["Contrato", "Convênio", "Acordo", "Nenhum"]
        description: >
          Instrumento de parceria utilizado na ação de extensão, caso haja parceria institucional.

      nome_coordenador:
        type: string
        title: "Nome do Coordenador"
        description: "Nome do coordenador da ação de extensão."

      data_inicio:
        type: date
        title: "Data de início"
        required: true
        description: "Data de início da ação de extensão."

      data_termino:
        type: date
        title: "Data de término"
        required: false
        description: "Data de término da ação de extensão. Pode ficar em branco se a ação estiver em andamento."

      situacao_acao:
        type: string
        title: "Situação da ação"
        required: true
        enum: ["Em andamento", "Finalizado", "Cancelado"]
        description: "Situação atual da ação de extensão."

      data_ultima_situacao:
        type: date
        title: "Data da última situação"
        description: "Data da última atualização da situação da ação de extensão."

      municipios_atendidos:
        type: array
        items:
          type: bigint
        title: "Municípios atendidos"
        description: "Formato: {codigo; codigo}. O código dos municípios é fornecido pelo Coletor PNP."
        referencia_pnp:
          recurso: municipios
          tipo: array_codigo
          severidade: erro

      entidade_financiadora:
        type: string
        required: false
        title: "Entidade financiadora"
        description: "Entidade que fornece recursos financeiros para a ação."

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
        title: "Área temática CNPq"
        description: "Formato: {codigo}. O código da área temática CNPq é fornecido pelo Coletor PNP."
        required: true
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: aviso

      subeixo_tecnologico:
        type: string
        title: "Subeixo tecnológico"
        description: "Formato: {codigo}. O código do subeixo tecnológico é fornecido pelo Coletor PNP."
        required: true
        referencia_pnp:
          recurso: subeixos_tecnologicos
          tipo: codigo
          severidade: erro

      populacao_vulneravel:
        type: boolean
        title: "Destinado à população em vulnerabilidade?"
        description: >
          Avaliar se a ação de extensão é destinada à população em situação de vulnerabilidade.
        required: true

      tipo_vulnerabilidade:
        type: array
        title: "Tipo de vulnerabilidade"
        required: false
        description: >
          Permite selecionar vários elementos da lista de tipos de vulnerabilidade. Aplicável apenas quando populacao_vulneravel = TRUE.
        items:
          type: string
          enum:
            [
              "Socioeconômica",
              "Educacional",
              "Gênero e Raça",
              "Deficiência ou Condição de Saúde",
              "Geracional",
              "Territorial",
            ]

      produto:
        type: string
        title: "Produto"
        description: "Produto final da ação de extensão, caso haja."

    additionalFields: false

  pessoas_atendidas_acoes_extensao:
    type: table
    # externalUrl: "./storage/extracoes/acoes-de-extensao/pessoas_atendidas_acoes_extensao.parquet"
    title: "Pessoas Atendidas em Ações de Extensão"
    description: "Registros de pessoas impactadas diretamente por ações de extensão."
    meta:
      required: false
      disabled: false
    quality:
      - type: sql
        description: "Não pode haver atendimento duplicado da mesma pessoa na mesma ação"
        query: >
          SELECT COUNT(*) FROM (
            SELECT cpf, id_acao_extensao
            FROM pessoas_atendidas_acoes_extensao
            GROUP BY cpf, id_acao_extensao HAVING COUNT(*) > 1
          ) duplicados
        mustBe: 0
      - type: sql
        description: "CPF deve conter 11 dígitos e textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM pessoas_atendidas_acoes_extensao
          WHERE NOT regexp_full_match(cpf, '[0-9]{11}')
             OR NULLIF(TRIM(nome), '') IS NULL
        mustBe: 0
      - type: sql
        description: "Não pode existir pessoa atendida sem ação correspondente."
        query: >
          SELECT COUNT(*)
          FROM pessoas_atendidas_acoes_extensao p
          LEFT JOIN acoes_extensao a ON a.id_acao_extensao = p.id_acao_extensao
          WHERE a.id_acao_extensao IS NULL
        mustBe: 0
    fields:
      id_atendido:
        type: integer
        title: "ID atendido"
        primaryKey: true
        required: true
        description: "ID do registro de pessoa atendida diretamente pela ação de extensão."

      cpf:
        type: string
        title: "CPF"
        pii: true
        required: true
        classification: "sensitive"
        description: "CPF da pessoa atendida diretamente pela ação de extensão."

      nome:
        type: string
        title: "Nome"
        pii: true
        required: true
        classification: "sensitive"
        description: "Nome da pessoa atendida diretamente pela ação de extensão."

      id_acao_extensao:
        type: integer
        title: "ID ação de extensão"
        references: "acoes_extensao.id_acao_extensao"
        description: "ID da ação de extensão à qual a pessoa atendida está vinculada."
        required: true

    additionalFields: false

  pessoas_envolvidas_acoes_extensao:
    type: table
    # externalUrl: "./storage/extracoes/acoes-de-extensao/pessoas_envolvidas_acoes_extensao.parquet"
    title: "Pessoas Envolvidas em Ações de Extensão"
    description: "Registros de participantes formalmente envolvidos na execução das ações."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Não pode haver participante duplicado na mesma ação."
        query: >
          SELECT COUNT(*) FROM (
            SELECT cpf, id_acao_extensao
            FROM pessoas_envolvidas_acoes_extensao
            GROUP BY cpf, id_acao_extensao HAVING COUNT(*) > 1
          ) duplicados
        mustBe: 0
      - type: sql
        description: "CPF deve conter 11 dígitos e matrícula é exigida apenas para participantes internos."
        query: >
          SELECT COUNT(*) FROM pessoas_envolvidas_acoes_extensao
          WHERE NOT regexp_full_match(cpf, '[0-9]{11}')
             OR (categoria IN ('docente', 'TAE', 'estudante')
                 AND NULLIF(TRIM(matricula), '') IS NULL)
             OR (categoria = 'externo' AND NULLIF(TRIM(matricula), '') IS NOT NULL)
        mustBe: 0
      - type: sql
        description: "Datas e situação da participação devem ser coerentes."
        query: >
          SELECT COUNT(*) FROM pessoas_envolvidas_acoes_extensao
          WHERE data_saida <= data_ingresso
             OR data_ultima_situacao <= data_ingresso
             OR (situacao_envolvido = 'Ativo' AND data_saida IS NOT NULL)
             OR (situacao_envolvido = 'Inativo' AND data_saida IS NULL)
        mustBe: 0
      - type: sql
        description: "Não pode existir pessoas envolvidas sem ação correspondente."
        query: >
          SELECT COUNT(*)
          FROM pessoas_envolvidas_acoes_extensao p
          LEFT JOIN acoes_extensao a ON a.id_acao_extensao = p.id_acao_extensao
          WHERE a.id_acao_extensao IS NULL
        mustBe: 0
    fields:
      id_envolvido:
        type: integer
        title: "ID envolvido"
        primaryKey: true
        required: true
        description: "ID do registro de pessoa envolvida na ação de extensão."

      cpf:
        type: string
        title: "CPF"
        pii: true
        required: true
        classification: "sensitive"
        description: "CPF da pessoa envolvida na ação de extensão."
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
        required: true
        classification: "sensitive"
        description: "Nome completo da pessoa."
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
        description: "ID da ação de extensão à qual a pessoa envolvida está vinculada."

      data_ingresso:
        type: date
        required: true
        title: "Data de ingresso na ação"
        description: "Data de ingresso da pessoa envolvida na ação de extensão."

      data_saida:
        type: date
        title: "Data de saída da ação"
        description: "Data de saída da pessoa envolvida na ação de extensão. Pode ficar em branco se a pessoa ainda estiver envolvida."

      situacao_envolvido:
        type: string
        required: true
        title: "Situação do envolvido"
        enum: ["Ativo", "Inativo"]
        description: "Situação atual da pessoa envolvida na ação de extensão."

      data_ultima_situacao:
        type: date
        required: true
        title: "Data da última situação"
        description: "Data da última atualização da situação da pessoa envolvida na ação de extensão."

      matricula:
        type: string
        title: "Matrícula"
        required: false
        description: "Número de matrícula SIAPE (servidor) ou Sistec (aluno), a depender do tipo de vínculo do registro."
    additionalFields: false
```

