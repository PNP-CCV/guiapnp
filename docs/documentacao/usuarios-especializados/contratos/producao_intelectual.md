---
layout: default
title: "Produção Intectual"
toc: true
---
# Produção Intelectual

* TOC
{:toc}


> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

**Slug:** `producao_intelectual` · **Versão:** `1.0.0` · **Owner:** SETEC

**Status:** `active` · **Spec:** `dataContractSpecification: "1.2.0"`

**Área Temática:** Pesquisa e Inovação

## Resumo de negócio

Este **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** descreve a **produção intelectual acadêmica e técnica** dos servidores da instituição: publicações (artigos, livros, capítulos, anais), produções técnico-tecnológicas, artístico-culturais e demais categorias da taxonomia Lattes/CNPq, com classificação Qualis-CAPES quando aplicável.

A **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** coleta este contrato para mensurar a **produção acadêmica e técnica** da rede federal e a participação de docentes e TAEs em cada produção. Modelo único: a autoria deixou de ser tabela à parte e passou a viver na própria linha da produção (`cpf`, `categoria`, `matricula`), o que torna a granularidade **uma linha por autoria**, não por produção.

## Modelos contidos

- **`producao_intelectual`** *(obrigatório no fluxo)* — produções acadêmicas, técnicas, tecnológicas e culturais registradas institucionalmente, com tipo, classificação, ano, área CNPq e a autoria vinculada. Contém PII (`cpf`).

> ℹ️ **Atenção ao vocabulário:** *obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml) e [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

## Modelo `producao_intelectual`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela única do contrato. Cada linha é uma autoria de uma produção intelectual: `id_producao` identifica a produção e os campos `cpf`, `categoria` e `matricula` identificam quem assina. Uma produção com vários autores aparece em várias linhas.

> ℹ️ **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_producao` | `integer` | sim | `primaryKey` | ID produção |
| `tipo_producao` | `string` | sim | `enum: [Acadêmica, Técnica]` | Tipo de produção |
| `classificacao_producao` | `string` | sim | `enum` (ver legenda abaixo) | Categoria de produção conforme taxonomia da base Lattes (técnico-tecnológica, artístico-cultural, etc.) |
| `titulo_producao` | `string` | sim | — | Título da produção |
| `ano_publicacao` | `integer` | sim | — | Ano de publicação. Formato: `AAAA` |
| `avaliacao_capes` | `string` | não | `enum: [A1, A2, A3, A4, B1, B2, B3, B4, B5, C, Não classificado]` | Avaliação Capes |
| `area_tematica_cnpq` | `string` | sim | `referencia_pnp: areas_tematicas_cnpq` (conferido na extração — ver nota) | Área Temática CNPq. Formato: `{codigo}` |
| `cpf` | `string` | sim | `pii`, `classification: sensitive` | CPF de quem assina a produção |
| `categoria` | `string` | sim | `enum: [docente, TAE]` | Tipo de vínculo do autor/co-autor |
| `matricula` | `string` | sim | `referencia_pnp: servidores`, chave composta `[cpf, matricula]` (conferida na extração — ver nota) | Matrícula SIAPE do autor/co-autor |

#### Valores de `classificacao_producao`

Bibliográfica: `TRABALHO-EM-EVENTOS`, `ARTIGO-PUBLICADO`, `LIVRO-PUBLICADO-OU-ORGANIZADO`, `CAPÍTULO-DE-LIVRO-PUBLICADO`, `TEXTO-EM-JORNAL-OU-REVISTA`, `OUTRA-PRODUCAO-BIBLIOGRAFICA`, `PREFACIO-POSFACIO`, `PARTITURA-MUSICAL`, `TRADUCAO`, `ARTIGO-ACEITO-PARA-PUBLICACAO`.

Técnica: `SOFTWARE`, `PRODUTO-TECNOLOGICO`, `PROCESSOS-OU-TECNICAS`, `TRABALHO-TECNICO`, `APRESENTACAO-DE-TRABALHO`, `CARTA-MAPA-OU-SIMILAR`, `CURSO-DE-CURTA-DURACAO-MINISTRADO`, `DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL`, `EDITORACAO`, `MANUTENCAO-DE-OBRA-ARTISTICA`, `MAQUETE`, `ORGANIZACAO-DE-EVENTO`, `OUTRA-PRODUCAO-TECNICA`, `PROGRAMA-DE-RADIO-OU-TV`, `RELATORIO-DE-PESQUISA`.

Propriedade intelectual: `PATENTE`, `MARCA`, `DESENHO-INDUSTRIAL`.

### Regras de qualidade

Além do schema (colunas obrigatórias, tipos e rejeição de colunas extras via `additionalFields: false`), o modelo declara regras `quality` do tipo `sql`:

| Regra | Espera |
|---|---|
| `titulo_producao` não pode ser texto vazio | `mustBe: 0` |
| `tipo_producao` tem de ser `Acadêmica` para as classificações bibliográficas e `Técnica` para as demais | `mustBe: 0` |
| `ano_publicacao` tem de ser o **ano de referência** da coleta | `mustBe: 0` |

> ℹ️ **Ano de referência.** A última consulta usa o token `#ANO_REFERENCIA#`, substituído pelo Coletor antes de o contrato chegar ao motor: é o **ano-base** da coleta, `ciclo.ano - 1` (o ciclo de 2026 coleta o que foi publicado em 2025). Contrato que usa o token sem ciclo de coleta associado falha com erro explícito, em vez de mandar SQL quebrado ao motor.

### Exemplo válido

```json
{
  "id_producao": 7402,
  "tipo_producao": "Acadêmica",
  "classificacao_producao": "ARTIGO-PUBLICADO",
  "titulo_producao": "Aprendizado profundo aplicado à classificação de imagens médicas em redes neurais convolucionais",
  "ano_publicacao": 2024,
  "avaliacao_capes": "A1",
  "area_tematica_cnpq": "10300007",
  "cpf": "98765432100",
  "categoria": "docente",
  "matricula": "1548923"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"tipo_producao": "Acadêmica", "titulo_producao": "..."}` (sem `id_producao`) | `Required field 'id_producao' is missing` |
| `{"id_producao": 7402, "tipo_producao": "Acadêmica"}` (sem `titulo_producao`) | `Required field 'titulo_producao' is missing` |
| `{"id_producao": 7402, "tipo_producao": "Patente", "titulo_producao": "..."}` (valor fora do `enum`) | `Value 'Patente' for field 'tipo_producao' not in enum [Acadêmica, Técnica]` |
| `{..., "ano_publicacao": "2024"}` (`string` em vez de `integer`) | `Type mismatch on 'ano_publicacao': expected integer, got string` |
| `{..., "doi": "10.1234/exemplo"}` (coluna não declarada) | `Field 'doi' not in schema (additionalFields: false)` |
| `{..., "tipo_producao": "Técnica", "classificacao_producao": "ARTIGO-PUBLICADO"}` (tipo incompatível com a classificação) | `O tipo deve ser compatível com a classificação da produção.: Actual custom_sql(producao_intelectual) was 1, expected = 0` |

## `referencia_pnp` — conferido na extração

| Campo | Modelo | `recurso` | `tipo` | `severidade` |
|---|---|---|---|---|
| `area_tematica_cnpq` | `producao_intelectual` | `areas_tematicas_cnpq` | `codigo` | **`aviso`** |
| `matricula` (`docente`, `TAE`) | `producao_intelectual` | `servidores` | `chave_composta: [cpf, matricula]` | `erro` |

O Coletor **confere esses valores contra os espelhos locais da PNP** antes de gravar o Parquet, no **modo bloqueante** por padrão — uma referência que não existe no cadastro reprova o **teste do contrato** e barra o envio, aparecendo em **Ver resultados de teste** com o campo e as linhas envolvidas. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial). Para a autoria, a validação confere o par `[cpf, matricula]` no cadastro de `servidores`, evitando aceitar o CPF de uma pessoa combinado com a matrícula de outra.

### `matricula` confere só contra `servidores`

Diferente dos outros dois contratos de pessoas, aqui não há roteamento a fazer: `categoria` só aceita `docente` e `TAE`, e ambos estão no cadastro de servidores. A regra tem uma entrada só.

```yaml
matricula:
  referencia_pnp:
    - recurso: servidores
      chaves: [cpf, matricula]
      filtro_categoria_campo: categoria
      categorias_validar: ["docente", "TAE"]
```

A conferência é do par `(cpf, matricula)`, não dos dois campos soltos — conferir cada um por si aceitaria o CPF de uma pessoa com a matrícula de outra.

> ℹ️ **Este contrato não cobre estudante.** O `enum` de `categoria` aceita só `docente` e `TAE`, e `categorias_validar` acompanha esse recorte. Em [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) e em [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) os modelos de pessoas aceitam também `externo` e `estudante`, e por isso lá a regra é roteada entre dois cadastros.

## Histórico de versões

| Versão | Data | Mudança | Breaking? |
|---|---|---|---|
| `1.0.0` | 2025-09-02 | Versão inicial documentada nesta data. | — |
| `1.0.0` | 2026-09-01 | Modelo `participantes_producao_intelectual` absorvido por `producao_intelectual` (`cpf_autoria`, `categoria_autoria`, `matricula_autoria`); regras `quality` acrescentadas. `info.version` não foi bumpada. | **sim** |
| `1.0.0` | 2026-09-02 | Campos de autoria renomeados para `cpf`, `categoria` e `matricula`; validação do par `[cpf, matricula]` passou a usar o cadastro de servidores. `info.version` não foi bumpada. | **sim** |

## Contrato de Dados - Formato YAML

```yaml
dataContractSpecification: "1.2.0"
id: "producao_intelectual"
info:
  title: "Produção Intelectual"
  version: "1.0.0"
  status: "active"
  description: >
    Contrato de dados para registrar as produções intelectuais acadêmicas e técnicas realizadas
    pelos servidores da instituição, com classificação, ano de publicação e participação de docentes e TAEs.

servers:
  local:
    type: "local"
    description: "Datalake local do PNP:Coletor"
    path: "./storage/extracoes/producao-intelectual/{model}/*.parquet"
    format: "parquet"

models:
  producao_intelectual:
    type: table
    title: "Produção Intelectual"
    description: "Modelo de dados para produções acadêmicas, técnicas, tecnológicas e culturais registradas institucionalmente."
    meta:
      required: true
      disabled: false
    quality:
      - type: sql
        description: "Textos obrigatórios não podem ser vazios."
        query: >
          SELECT COUNT(*) FROM producao_intelectual
          WHERE NULLIF(TRIM(titulo_producao), '') IS NULL
        mustBe: 0
      - type: sql
        description: "O tipo deve ser compatível com a classificação da produção."
        query: >
          SELECT COUNT(*) FROM producao_intelectual
          WHERE (
            classificacao_producao IN (
              'TRABALHO-EM-EVENTOS', 'ARTIGO-PUBLICADO',
              'LIVRO-PUBLICADO-OU-ORGANIZADO',
              'CAPÍTULO-DE-LIVRO-PUBLICADO',
              'TEXTO-EM-JORNAL-OU-REVISTA',
              'OUTRA-PRODUCAO-BIBLIOGRAFICA', 'PREFACIO-POSFACIO',
              'PARTITURA-MUSICAL', 'TRADUCAO',
              'ARTIGO-ACEITO-PARA-PUBLICACAO'
            )
            AND tipo_producao <> 'Acadêmica'
          )
          OR (
            classificacao_producao NOT IN (
              'TRABALHO-EM-EVENTOS', 'ARTIGO-PUBLICADO',
              'LIVRO-PUBLICADO-OU-ORGANIZADO',
              'CAPÍTULO-DE-LIVRO-PUBLICADO',
              'TEXTO-EM-JORNAL-OU-REVISTA',
              'OUTRA-PRODUCAO-BIBLIOGRAFICA', 'PREFACIO-POSFACIO',
              'PARTITURA-MUSICAL', 'TRADUCAO',
              'ARTIGO-ACEITO-PARA-PUBLICACAO'
            )
            AND tipo_producao <> 'Técnica'
          )
        mustBe: 0
      - type: sql
        description: "O ano de publicação deve ser no ano de referência."
        query: >
          SELECT COUNT(*) FROM producao_intelectual
          WHERE ano_publicacao <> #ANO_REFERENCIA#
        mustBe: 0
    fields:
      id_producao:
        type: integer
        title: "ID produção"
        primaryKey: true
        required: true
        description: "Identificador único do registro de produção intelectual."

      tipo_producao:
        type: string
        title: "Tipo de produção"
        enum: ["Acadêmica", "Técnica"]
        required: true
        description: "Classificação da produção intelectual como acadêmica ou técnica."

      classificacao_producao:
        type: string
        title: "Classificação da produção"
        required: true
        description: "Categoria de produção conforme taxonomia da base Lattes (técnico-tecnológica, artístico-cultural, etc)."
        enum:
          - "TRABALHO-EM-EVENTOS"
          - "ARTIGO-PUBLICADO"
          - "LIVRO-PUBLICADO-OU-ORGANIZADO"
          - "CAPÍTULO-DE-LIVRO-PUBLICADO"
          - "TEXTO-EM-JORNAL-OU-REVISTA"
          - "OUTRA-PRODUCAO-BIBLIOGRAFICA"
          - "PREFACIO-POSFACIO"
          - "PARTITURA-MUSICAL"
          - "TRADUCAO"
          - "ARTIGO-ACEITO-PARA-PUBLICACAO"
          - "SOFTWARE"
          - "PRODUTO-TECNOLOGICO"
          - "PROCESSOS-OU-TECNICAS"
          - "TRABALHO-TECNICO"
          - "APRESENTACAO-DE-TRABALHO"
          - "CARTA-MAPA-OU-SIMILAR"
          - "CURSO-DE-CURTA-DURACAO-MINISTRADO"
          - "DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL"
          - "EDITORACAO"
          - "MANUTENCAO-DE-OBRA-ARTISTICA"
          - "MAQUETE"
          - "ORGANIZACAO-DE-EVENTO"
          - "OUTRA-PRODUCAO-TECNICA"
          - "PROGRAMA-DE-RADIO-OU-TV"
          - "RELATORIO-DE-PESQUISA"
          - "PATENTE"
          - "MARCA"
          - "DESENHO-INDUSTRIAL"

      titulo_producao:
        type: string
        title: "Título da produção"
        required: true
        description: "Título da produção intelectual, conforme registro institucional."

      ano_publicacao:
        type: integer
        required: true
        title: "Ano de publicação"
        description: "Formato: AAAA"

      avaliacao_capes:
        type: string
        title: "Avaliação Capes"
        description: "Classificação da produção conforme a avaliação da CAPES."
        enum:
          [
            "A1",
            "A2",
            "A3",
            "A4",
            "B1",
            "B2",
            "B3",
            "B4",
            "B5",
            "C",
            "Não classificado",
          ]

      area_tematica_cnpq:
        type: string
        title: "Área Temática CNPq"
        description: "Formato: {codigo}. Código fornecido pelo Coletor PNP."
        required: true
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: aviso

      cpf:
        type: string
        title: "CPF"
        description: "CPF de autoria/co-autoria da produção intelectual"
        pii: true
        classification: "sensitive"
        required: true

      categoria:
        type: string
        title: "Categoria"
        required: true
        description: "Tipo de vínculo de autoria/co-autoria da produção intelectual (ex.: docente, TAE)."
        enum: ["docente", "TAE"]

      matricula:
        type: string
        title: "Matrícula"
        required: true
        description: "Matrícula SIAPE da pessoa servidora envolvida na produção intelectual."
        referencia_pnp:
          - recurso: servidores
            tipo: chave_composta
            chaves: [cpf, matricula]
            filtro_categoria_campo: categoria
            categorias_validar: ["docente", "TAE"]
            severidade: erro

    additionalFields: false
```

