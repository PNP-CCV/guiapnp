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

Este **Contrato de Dados** descreve os **acordos e parcerias formais** firmados pela instituição com entidades externas (públicas ou privadas) — convênios, ACTs, TEDs, contratos e instrumentos correlatos — com **foco em projetos de pesquisa**. Cada registro representa um instrumento jurídico vigente, com vigência, contrapartida financeira, fundação de apoio interveniente e vínculo a um projeto.

A **PNP** coleta este contrato para mensurar o engajamento da rede federal com o setor produtivo e o setor público, e o volume de cooperação institucionalizada por trás dos projetos de pesquisa declarados.

Este é o único contrato do catálogo composto por **um único Modelo de Dados**.

## Modelos contidos

- **`acordos_parceria`** *(opcional no fluxo)* — instrumentos jurídicos formais (acordo/parceria) firmados com instituições externas, com vigência, contrapartida e referência ao projeto de pesquisa associado.

> ℹ️ **Atenção ao vocabulário.** *Obrigatório / opcional / desabilitado* acima é atributo do **modelo**, declarado no bloco `meta` do contrato — não confundir com a coluna **Obrigatório** da tabela de campos, que diz se aquela *coluna* precisa vir preenchida. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e [Modelos obrigatórios, opcionais e desabilitados]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

> ℹ️ **Este contrato nasce em "Somente Modelos Opcionais".** Como o único modelo é opcional, logo depois da primeira sincronização o contrato aparece no painel com o badge **Somente Modelos Opcionais** e fica fora do progresso do assistente e das ações em lote — não é erro nem falha de sincronização, é o esperado. Ele entra no fluxo assim que alguém cadastrar uma **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** para `acordos_parceria`.

## Modelo `acordos_parceria`

> ℹ️ **No fluxo do Coletor:** modelo **opcional** (`meta.required: false`) e **habilitado** (`meta.disabled: false`). Enquanto ninguém cadastrar uma Configuração de Extração para ele, o Coletor não o cobra: não vira pendência, não segura o [status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato) e é pulado pela extração em lote. Assim que ganha uma configuração, passa a contar como qualquer outro modelo — o contrato volta para *Aguardando Extração* e só fecha quando este modelo for extraído, testado, enviado e aprovado. Para desistir dele, basta remover a(s) configuração(ões) de extração.

### Resumo do modelo

Tabela única do contrato. Cada linha é um instrumento jurídico (acordo, convênio etc.) identificado por `id_acordo`. O vínculo com o projeto de pesquisa é feito de forma textual no campo `objeto_acordo` (formato: `id_projeto_pesq; título_projetopesq`) — não há referência declarativa (`references`) entre este contrato e `projetos_de_pesquisa`.

> **Modelo fechado:** `additionalFields: false` — qualquer coluna não declarada abaixo é rejeitada na validação de schema.

### Tabela de campos

| Campo | Tipo | Obrigatório | Constraints | Descrição |
|---|---|---|---|---|
| `id_acordo` | `integer` | sim | `primaryKey` | ID acordo/parceria |
| `data_formalizacao` | `date` | sim | — | Data em que o acordo foi oficialmente firmado |
| `instituicao_parceira` | `string` | sim | — | Nome da organização parceira |
| `objeto_acordo` | `string` | sim | — | Descrição do projeto de pesquisa vinculado. Formato: `id_projeto_pesq; título_projetopesq` |
| `vigencia` | `string` | sim | — | Período de validade do acordo. Formato: `Ano de início; Ano de fim` |
| `numero_acordo` | `string` | sim | — | Número identificador do instrumento jurídico |
| `contrapartida_financeira` | `string` | não | — | Valor em R$ ou indicação de que não há |
| `estrutura` | `string` | sim | `referencia_pnp: campi` (conferido na extração — ver nota) | Estrutura à qual vinculam-se os acordos de parceria. Formato: `{codigo}`. Filtro: `pnp_tipounidade` — todos exceto id 9, código 10 (Outros) |
| `fundacao_interveniente` | `string` | não | — | Nome da fundação responsável pela gestão |

> **referencia_pnp:** Apenas os dados que encontram referência na PNP são validados, ou seja, caso seja informado uma `estrutura` que não esteja dentro da Base da PNP, a respectiva ação de extensão será rejeitada, até que seja fornecido o dado correto.

> ℹ️ **O Coletor antecipa essa conferência.** O mesmo código de estrutura é checado contra o cadastro local sincronizado da PNP ainda na extração, antes de gravar o Parquet. De fábrica em **modo sombra**: a divergência aparece no Registro de Extração, mas ainda não reprova. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).


### Exemplo válido

```json
{
  "id_acordo": 5021,
  "data_formalizacao": "2024-08-15",
  "instituicao_parceira": "Petrobras S.A.",
  "objeto_acordo": "3147; Caracterização de catalisadores para refino de petróleo pesado",
  "vigencia": "2024; 2027",
  "numero_acordo": "TED 042/2024-IFRN",
  "contrapartida_financeira": "R$ 480.000,00",
  "estrutura": "12",
  "fundacao_interveniente": "FUNCERN — Fundação de Apoio à Educação e ao Desenvolvimento Tecnológico do RN"
}
```

### Exemplos inválidos

| Payload (resumido) | Erro |
|---|---|
| `{"data_formalizacao": "2024-08-15", "objeto_acordo": "..."}` (sem `id_acordo`) | `Required field 'id_acordo' is missing` |
| `{"id_acordo": 5021, "data_formalizacao": "2024-08-15"}` (sem `objeto_acordo`) | `Required field 'objeto_acordo' is missing` |
| `{"id_acordo": 5021, "objeto_acordo": "...", "data_formalizacao": "15/08/2024"}` (formato errado, `date` espera ISO 8601) | `Type mismatch on 'data_formalizacao': expected date, got string '15/08/2024'` |
| `{..., "valor_total": 480000}` (coluna não declarada) | `Field 'valor_total' not in schema (additionalFields: false)` |



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
    fields:
      id_acordo:
        type: integer
        title: "ID acordo/parceria"
        primaryKey: true
        required: true

      data_formalizacao:
        type: date
        title: "Data de formalização"
        description: "Data em que o acordo foi oficialmente firmado."

      instituicao_parceira:
        type: string
        title: "Instituição parceira"
        description: "Nome da organização parceira."

      objeto_acordo:
        type: string
        title: "Objeto do acordo"
        description: "Descrição do projeto de pesquisa vinculado (formato: id_projeto_pesq; título_projetopesq)."
        required: true

      vigencia:
        type: string
        title: "Vigência"
        description: "Período de validade do acordo (formato: Ano de início; Ano de fim)."

      numero_acordo:
        type: string
        title: "Número do acordo"
        description: "Número identificador do instrumento jurídico."

      contrapartida_financeira:
        type: string
        title: "Contrapartida Financeira"
        description: "Valor em R$ ou indicação de que não há."

      estrutura:
        type: string
        title: "Estrutura à qual vinculam-se os acordos de parceria"
        description: >
          Formato: {codigo}. Filtro: pnp_tipounidade - todos exceto id 9,
          código 10 (Outros).
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

