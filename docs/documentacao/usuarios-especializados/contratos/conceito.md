---
layout: default
title: "Conceito de Contrato de Dados"
toc: true
---
# Conceito de Contrato de Dados

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página explica o que é um **[Data Contract]({{ site.baseurl }}/documentacao/coletor/glossario#data-contract)**, por que o Coletor de Microdados o adota como artefato central e de onde os contratos vêm. É o ponto de partida da trilha de contratos: as páginas seguintes ([Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml), [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)) e o catálogo por área temática detalham cada aspecto.

## O que é um Data Contract

Um **contrato de API** formaliza a interface entre dois serviços que trocam mensagens. Um **Data Contract** faz o mesmo para dois sistemas que trocam **arquivos ou datasets**: define schema, regras de qualidade, finalidade de uso e responsável pelo dado. É um YAML versionado que serve simultaneamente como documentação, contrato leve e fonte de validação automatizada.

O Coletor usa a especificação aberta do ecossistema [datacontract.com](https://datacontract.com/), na versão `1.2.0`. A leitura e os testes são feitos pela ferramenta `datacontract-cli`, executada automaticamente pelo próprio Coletor.

## Por que o Coletor usa contratos

Quatro motivos práticos:

- **Padronização entre instituições.** A Rede Federal tem dezenas de instituições, cada uma com bancos, planilhas e APIs diferentes. O contrato define um formato único de entrega — o trabalho de mapear "como sai do meu sistema" para "o que a PNP espera" fica isolado em uma só camada (a **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)**).
- **Validação automática.** O sistema rejeita dados que não batem com o schema esperado **antes** de gravar o **[Parquet]({{ site.baseurl }}/documentacao/coletor/glossario#parquet)**. Colunas faltando, tipos errados ou valores fora do `enum` impedem a extração de avançar (ver [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)).
- **Documentação executável.** O YAML é a fonte da verdade. As páginas do catálogo e a validação derivam dele — não há risco da documentação divergir do schema em execução.
- **Auditoria.** O **[MEC]({{ site.baseurl }}/documentacao/coletor/glossario#mec)** e a **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** podem rastrear, por contrato e por versão, exatamente o que foi acordado com cada instituição e o que foi efetivamente entregue. Cada **[Registro de Sincronização]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-sincronizacao)** carrega esse vínculo.

## De onde os contratos vêm

A instituição **não escreve** contratos: eles são definidos pela equipe da PNP e chegam ao Coletor pelo botão **"Sincronizar com a PNP"**, que importa os ciclos, contratos, schemas e modelos do ciclo vigente. Os contratos canônicos da PNP hoje são dez:

| Contrato | Página no catálogo | Como aparece no painel |
|---|---|---|
| Acadêmico | [Acadêmico]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/academico) | **Não aparece** — único modelo desabilitado |
| Ações de Extensão | [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) | Normal (um dos três modelos é opcional) |
| Acordos de Parceria | [Acordos de Parceria]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acordos_de_parceria) | Somente Modelos Opcionais |
| Desenvolvimento Institucional | [Projetos de Desenvolvimento Institucional]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_desenvolvimento_institucional) | Somente Modelos Opcionais |
| Orçamento | [Documentos de Orçamento]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/orcamento) | Somente Modelos Opcionais |
| Pessoal | [Pessoal Terceirizado]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/pessoal_terceirizado) | Normal, com um único modelo (dois desabilitados) |
| Produção Intelectual | [Produção Intelectual]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/producao_intelectual) | Normal |
| Projetos de Ensino | [Projetos de Ensino]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_ensino) | Somente Modelos Opcionais |
| Projetos de Pesquisa | [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) | Normal |
| Sustentabilidade | [Sustentabilidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/sustentabilidade) | Normal |

> ℹ️ **Dez contratos publicados, nove no painel.** Cada modelo do contrato traz dois metadados — `meta.required` e `meta.disabled` — que dizem se o Coletor cobra aquele dataset e se ele é sequer importado. Um contrato cujos modelos estão **todos desabilitados** não é criado: é o caso do **Acadêmico**, que por isso não aparece no painel. E quatro contratos, cujo único modelo é **opcional**, aparecem com o badge *Somente Modelos Opcionais* até que alguém configure a extração deles. Nada disso é erro de sincronização. Detalhes em [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta) e em [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

A referência versionada dos YAMLs vive no [repositório do Coletor](https://github.com/PNP-CCV/coletor-pnp-microdados/tree/master/base/fixtures/contratos), e uma verificação automática impede que as páginas do catálogo divirjam do YAML.

## Como o contrato é usado no fluxo

```text
YAML do contrato (definido pela PNP)
        │  "Sincronizar com a PNP"
        ▼
Coletor da instituição
        │  extração: confere colunas e tipos antes de gravar
        ▼
Arquivo Parquet local
        │  teste de qualidade: regras do contrato contra o Parquet
        ▼
Resultado do teste  →  habilita (ou bloqueia) o envio à PNP
```

Dois momentos usam o contrato:

1. **Na extração** — o schema do contrato dita as colunas e tipos esperados; divergência rejeita a extração antes de qualquer arquivo ser gravado.
2. **No teste de qualidade** — a `datacontract-cli` lê o Parquet gerado e executa as regras declaradas no YAML. O teste roda automaticamente ao fim de cada extração bem-sucedida.

## Veja também

- [Anatomia do YAML do contrato]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)
- [Ciclo de vida do contrato]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/ciclo_de_vida)
