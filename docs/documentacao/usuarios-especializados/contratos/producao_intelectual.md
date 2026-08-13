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

Este **Contrato de Dados** descreve a **produção intelectual acadêmica e técnica** dos servidores da instituição: publicações (artigos, livros, capítulos, anais), produções técnico-tecnológicas, artístico-culturais e demais categorias da taxonomia Lattes/CNPq, com classificação Qualis-CAPES quando aplicável.

A **PNP** coleta este contrato para mensurar a **produção acadêmica e técnica** da rede federal e a participação de docentes e TAEs em cada produção. Os dois modelos cobrem a produção em si e os participantes vinculados a ela (com PII).

## Modelos contidos

- **`producao_intelectual`** *(obrigatório no fluxo)* — produções acadêmicas, técnicas, tecnológicas e culturais registradas institucionalmente, com tipo, classificação, ano e área CNPq.
- **`participantes_producao_intelectual`** *(obrigatório no fluxo)* — pessoas envolvidas em cada produção (docentes e TAEs). Contém PII (`cpf`, `nome`).

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** das tabelas de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Modelo `producao_intelectual`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Tabela principal do contrato. Cada linha é uma produção intelectual única, identificada por `id_producao`. A tabela `participantes_producao_intelectual` referencia-a por chave estrangeira.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_producao` | `integer` | sim | `primaryKey` | ID produção |
| `tipo_producao` | `string` | sim | `enum: [Acadêmica, Técnica]` | Tipo de produção |
| `classificacao_producao` | `string` | sim | `enum` (28 valores — ver legenda) | Categoria de produção conforme taxonomia da base Lattes (técnico-tecnológica, artístico-cultural, etc.) |
| `titulo_producao` | `string` | sim | — | Título da produção |
| `ano_publicacao` | `integer` | sim | — | Ano de publicação. Formato: `AAAA` |
| `avaliacao_capes` | `string` | não | `enum: [Qualis, NA]` | Avaliação Capes |
| `area_tematica_cnpq` | `string` | sim | `referencia_pnp: areas_tematicas_cnpq` (declarativo) | Área Temática CNPq. Formato: `{codigo}` |

#### Valores de `classificacao_producao`

Os 28 valores são os tokens da taxonomia Lattes, em caixa alta e separados por hífen. Só `CAPÍTULO-DE-LIVRO-PUBLICADO` tem acento; os demais são ASCII sem acentuação (`PREFACIO-POSFACIO`, `TRADUCAO`, `PRODUTO-TECNOLOGICO`, `RELATORIO-DE-PESQUISA`…).

**Bibliográfica:** `TRABALHO-EM-EVENTOS`, `ARTIGO-PUBLICADO`, `LIVRO-PUBLICADO-OU-ORGANIZADO`, `CAPÍTULO-DE-LIVRO-PUBLICADO`, `TEXTO-EM-JORNAL-OU-REVISTA`, `OUTRA-PRODUCAO-BIBLIOGRAFICA`, `PREFACIO-POSFACIO`, `PARTITURA-MUSICAL`, `TRADUCAO`, `ARTIGO-ACEITO-PARA-PUBLICACAO`.

**Técnica:** `SOFTWARE`, `PRODUTO-TECNOLOGICO`, `PROCESSOS-OU-TECNICAS`, `TRABALHO-TECNICO`, `APRESENTACAO-DE-TRABALHO`, `CARTA-MAPA-OU-SIMILAR`, `CURSO-DE-CURTA-DURACAO-MINISTRADO`, `DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL`, `EDITORACAO`, `MANUTENCAO-DE-OBRA-ARTISTICA`, `MAQUETE`, `ORGANIZACAO-DE-EVENTO`, `OUTRA-PRODUCAO-TECNICA`, `PROGRAMA-DE-RADIO-OU-TV`, `RELATORIO-DE-PESQUISA`.

**Propriedade intelectual:** `PATENTE`, `MARCA`, `DESENHO-INDUSTRIAL`.

> ⚠️ **`classificacao_producao` deixou de ser texto livre.** O campo aceitava prosa (por exemplo, "Artigo completo publicado em periódico") e agora só aceita os 28 tokens acima. Quem já enviava a descrição por extenso precisa mapear a origem para o token correspondente antes de extrair.


### Exemplo válido

```json
{
  "id_producao": 7402,
  "tipo_producao": "Acadêmica",
  "classificacao_producao": "ARTIGO-PUBLICADO",
  "titulo_producao": "Aprendizado profundo aplicado à classificação de imagens médicas em redes neurais convolucionais",
  "ano_publicacao": 2024,
  "avaliacao_capes": "Qualis",
  "area_tematica_cnpq": "10300007"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"tipo_producao": "Acadêmica", "titulo_producao": "..."}` (sem `id_producao`) | `Required field 'id_producao' is missing` |
| `{"id_producao": 7402, "tipo_producao": "Acadêmica"}` (sem `titulo_producao`) | `Required field 'titulo_producao' is missing` |
| `{"id_producao": 7402, "tipo_producao": "Patente", "titulo_producao": "..."}` (valor fora do `enum`) | `Value 'Patente' for field 'tipo_producao' not in enum [Acadêmica, Técnica]` |
| `{..., "ano_publicacao": "2024"}` (`string` em vez de `integer`) | `Type mismatch on 'ano_publicacao': expected integer, got string` |
| `{..., "classificacao_producao": "Artigo completo publicado em periódico"}` (texto livre, fora do `enum`) | `Value 'Artigo completo publicado em periódico' for field 'classificacao_producao' not in enum` |
| `{..., "doi": "10.1234/exemplo"}` (coluna não declarada) | `Field 'doi' not in schema (additionalFields: false)` |

## Modelo `participantes_producao_intelectual`

> ℹ️ **No fluxo do Coletor:** modelo **obrigatório** (`meta.required: true`) e **habilitado** (`meta.disabled: false`). O Coletor cobra a configuração e a extração dele: enquanto isso não acontece, o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) não avança.

### Resumo do modelo

Pessoas envolvidas em cada produção intelectual (autoria, coautoria, orientação, participação técnica), com vínculo, período e situação. Contém PII (`cpf`, `nome`) classificados como `sensitive`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_participante` | `integer` | sim | `primaryKey` | ID participante |
| `cpf` | `string` | sim | `pii`, `classification: sensitive` | CPF do participante da produção intelectual |
| `nome` | `string` | sim | `pii`, `classification: sensitive` | Nome completo do participante da produção |
| `categoria` | `string` | sim | `enum: [docente, TAE]` | Tipo de vínculo com a produção (ex.: docente, TAE) |
| `id_producao` | `integer` | sim | `references producao_intelectual.id_producao` | Referência à produção intelectual cadastrada |
| `data_ingresso` | `date` | não | — | Data de início da participação na produção |
| `data_saida` | `date` | não | — | Data de encerramento da participação, se aplicável |
| `situacao_participante` | `string` | não | `enum: [Ativo, Inativo]` | Status atual do vínculo do participante com a produção |
| `matricula` | `string` | não | — | Matrícula |

> ⚠️ **`categoria` foi estreitada para dois valores.** O `enum` aceitava `docente`, `TAE`, `externo` e `estudante`; agora aceita apenas **`docente`** e **`TAE`**. Participação de estudantes e de pessoas externas deixa de ser representável neste modelo — linhas com esses valores reprovam a validação. **O estreitamento vale só para Produção Intelectual**: em [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) e [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) o mesmo campo continua com os quatro valores.


### Exemplo válido

```json
{
  "id_participante": 33108,
  "cpf": "11122233344",
  "nome": "Ricardo Almeida Costa",
  "categoria": "docente",
  "id_producao": 7402,
  "data_ingresso": "2023-09-01",
  "data_saida": "2024-06-30",
  "situacao_participante": "Inativo",
  "matricula": "1548923"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"cpf": "...", "id_producao": 7402}` (sem `id_participante`) | `Required field 'id_participante' is missing` |
| `{"id_participante": 33108, "categoria": "docente"}` (sem `id_producao`) | `Required field 'id_producao' is missing` |
| `{..., "categoria": "estudante"}` (valor removido do `enum`) | `Value 'estudante' for field 'categoria' not in enum [docente, TAE]` |
| `{..., "orcid": "0000-0000-..."}` (coluna não declarada) | `Field 'orcid' not in schema (additionalFields: false)` |


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
    fields:
      id_producao:
        type: integer
        title: "ID produção"
        primaryKey: true
        required: true

      tipo_producao:
        type: string
        title: "Tipo de produção"
        enum: ["Acadêmica", "Técnica"]
        required: true

      classificacao_producao:
        type: string
        title: "Classificação da produção"
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

      ano_publicacao:
        type: integer
        title: "Ano de publicação"
        description: "Formato: AAAA"

      avaliacao_capes:
        type: string
        title: "Avaliação Capes"
        enum: ["Qualis", "NA"]

      area_tematica_cnpq:
        type: string
        title: "Área Temática CNPq"
        description: "Formato: {codigo}"
        referencia_pnp:
          recurso: areas_tematicas_cnpq
          tipo: codigo
          severidade: aviso
    additionalFields: false

  participantes_producao_intelectual:
    type: table
    title: "Participantes da Produção Intelectual"
    description: "Tabela contendo dados dos indivíduos envolvidos nas produções intelectuais cadastradas institucionalmente."
    meta:
      required: true
      disabled: false
    fields:
      id_participante:
        type: integer
        title: "ID participante"
        primaryKey: true
        required: true

      cpf:
        type: string
        title: "CPF"
        description: "CPF do participante da produção intelectual."
        pii: true
        classification: "sensitive"
        referencia_pnp:
          recurso: pessoas
          tipo: chave_simples
          chave: cpf
          severidade: erro
          filtro_categoria_campo: categoria
          categorias_validar: ["docente", "TAE"]

      nome:
        type: string
        title: "Nome"
        description: "Nome completo do participante da produção."
        pii: true
        classification: "sensitive"

      categoria:
        type: string
        title: "Categoria"
        description: "Tipo de vínculo com a produção (ex.: docente, TAE)."
        enum: ["docente", "TAE"]

      id_producao:
        type: integer
        title: "ID produção"
        description: "Referência à produção intelectual cadastrada."
        references: "producao_intelectual.id_producao"
        required: true

      data_ingresso:
        type: date
        title: "Data de ingresso"
        description: "Data de início da participação na produção."

      data_saida:
        type: date
        title: "Data de saída"
        description: "Data de encerramento da participação, se aplicável."

      situacao_participante:
        type: string
        title: "Situação do participante"
        enum: ["Ativo", "Inativo"]
        description: "Status atual do vínculo do participante com a produção."

      matricula:
        type: string
        title: "Matrícula"
    additionalFields: false

```

