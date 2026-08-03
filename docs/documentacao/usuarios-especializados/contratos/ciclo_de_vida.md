---
layout: default
title: "Ciclo de vida do Contrato"
toc: true
---
# Ciclo de vida do Contrato

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página descreve como um **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** evolui ao longo do tempo: versionamento, classificação de mudanças como breaking ou não-breaking, relação com o **[Ciclo de Coleta]({{ site.baseurl }}/documentacao/coletor/glossario#ciclo-de-coleta)** e o que vale fazer durante a janela de correção. Os dez contratos atuais estão em `1.0.0` — esta é a referência para quando alguém propuser a primeira mudança.

## Versionamento do contrato

Cada contrato declara `info.version` no YAML, no formato **SemVer** (`MAJOR.MINOR.PATCH`). Alinhar a versão do YAML com a versão publicada é o que permite às instituições (e à própria PNP) detectarem mudanças.

A regra prática:

- **MAJOR** — quebra compatibilidade com dados ou clientes que já consomem o contrato.
- **MINOR** — adiciona capacidade sem quebrar nada existente.
- **PATCH** — correções textuais (descrições, exemplos, tags) que não alteram nem schema nem regras.

## Mudanças breaking vs não-breaking

A tabela abaixo classifica cada mudança comum no YAML. "MAJOR — só em novo ciclo" significa que aquela mudança não deve ser aplicada ao contrato vigente: cria-se uma nova versão maior em um novo ciclo de coleta.

| Mudança | Tipo | Quando aplicar |
|---|---|---|
| Adicionar campo opcional novo | MINOR | Qualquer ciclo |
| Adicionar campo `required: true` novo | MAJOR | Só em novo ciclo, com aviso aos integradores |
| Mudar `type` de campo existente | MAJOR | Só em novo ciclo |
| Renomear campo | MAJOR | Só em novo ciclo |
| Adicionar valor a `enum` | MINOR | Qualquer ciclo |
| Remover valor de `enum` | MAJOR | Só em novo ciclo |
| Trocar `additionalFields: false` → `true` (afrouxar) | MINOR | Qualquer ciclo |
| Trocar `additionalFields: true` → `false` (apertar) | MAJOR | Só em novo ciclo |
| Adicionar check em `quality:` que dados atuais passam | MINOR | Qualquer ciclo |
| Adicionar check que dados atuais falham | MAJOR | Só em novo ciclo |
| Editar `description`, `title`, `tags` | PATCH | Qualquer ciclo |
| `meta.required: true` → `false` (modelo vira opcional) | MINOR | Qualquer ciclo |
| `meta.required: false` → `true` (modelo vira obrigatório) | MAJOR | Só em novo ciclo, com aviso aos integradores |
| `meta.disabled: false` → `true` (desligar o modelo) | MINOR | Qualquer ciclo, com aviso aos integradores |
| `meta.disabled: true` → `false` (religar um modelo desligado) | MAJOR | Só em novo ciclo |

> ℹ️ **Lembrete:** "MINOR em qualquer ciclo" não significa "no mesmo dia da janela final". Mesmo MINORs precisam ser comunicados aos integradores — eles podem precisar atualizar SQLs ou mapeamentos.

### Por que as mudanças de `meta` caem assim

O critério é o mesmo das demais linhas: a mudança **invalida dado já entregue** ou **passa a exigir trabalho que antes não era exigido**?

- **Tornar um modelo opcional (`required: false`) é MINOR.** Nada do que já foi entregue deixa de valer, e quem já coletava aquele modelo continua exatamente igual — um modelo opcional **com** configuração de extração é cobrado como qualquer obrigatório. O efeito prático é só aliviar quem ainda não o coletava.
- **Tornar um modelo obrigatório (`required: true`) é MAJOR.** Instituições que legitimamente não coletavam aquele modelo passam a ser cobradas por ele: nova origem de dados, nova configuração de extração e nova extração para o contrato fechar. É o análogo, em nível de modelo, de adicionar um campo `required: true`.
- **Desligar um modelo (`disabled: true`) é MINOR do ponto de vista do dado** — ninguém precisa produzir nada novo e nada já entregue é invalidado —, mas **exige comunicação**: o modelo some do painel na sincronização seguinte (por exclusão lógica, sem apagar histórico nem arquivos gerados) e, se for o último modelo habilitado, o contrato inteiro desaparece da tela. Quem vê um contrato sumir sem aviso abre chamado.
- **Religar um modelo (`disabled: false`) é MAJOR.** Ele volta **zerado**: a configuração de extração anterior não é recuperada e precisa ser refeita — trabalho novo para todas as instituições, que é justamente o que caracteriza uma mudança maior.

O detalhamento das duas flags está em [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta).

## Relação Contrato ↔ Ciclo

Cada contrato pertence a exatamente um ciclo de coleta; o ciclo, por sua vez, agrupa vários contratos do mesmo ano. Migrar um contrato entre ciclos não é "mudar de pasta": é criar uma **nova versão** (geralmente MAJOR) ligada ao novo ciclo, mantendo a anterior como histórico.

| Ciclo | Contrato | Versão |
|---|---|---|
| Ciclo 2025 | `acoes_extensao` | `1.0.0` |
| Ciclo 2025 | `acordos_parceria` | `1.0.0` |
| Ciclo 2026 | `acoes_extensao` | `2.0.0` (evolução MAJOR) |
| Ciclo 2026 | `acordos_parceria` | `1.1.0` (evolução MINOR) |

A versão antiga não some imediatamente. Ela continua viva enquanto o ciclo dela ainda aceita correções e como histórico para auditoria.

## Janela de correção: o que dá para mudar

Durante o **[Período de Correção]({{ site.baseurl }}/documentacao/coletor/glossario#periodo-de-correcao)**, o contrato vigente pode receber **mudanças corretivas** — não evolutivas. A linha divisória é se a mudança invalida ou não dados que integradores já submeteram.

Permitido durante a correção:

- Ajustar `description` errada ou ambígua.
- Adicionar `description` ausente em campo existente.
- Corrigir `enum` que tinha valor digitado errado (sem remover valores que já apareceram nos dados).
- Adicionar campo opcional novo (não-required), se algum integrador precisa registrar uma informação que ficou faltando.
- Marcar um modelo como opcional (`meta.required: false`), aliviando quem ainda não conseguiu coletá-lo — quem já o coletava não é afetado.

Não permitido durante a correção:

- Adicionar campo `required: true` que rejeita extrações já enviadas.
- Mudar `type` de campo existente.
- Trocar `additionalFields` sem comunicação prévia.
- Adicionar check de qualidade que reprova dados já aceitos.
- Tornar obrigatório (`meta.required: true`) um modelo que era opcional: quem já fechou o contrato passaria a ter trabalho novo no meio da janela.
- Religar (`meta.disabled: false`) um modelo desabilitado: ele volta zerado e exige nova configuração de extração de todo mundo.

A regra prática: se a mudança força reextração de quem já sincronizou com sucesso, **não é correção** — é nova versão MAJOR no próximo ciclo. Detalhes operacionais em [Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta).

## Exclusão é lógica, histórico é preservado

Excluir um contrato ou modelo pelo painel do Coletor **não remove os registros**: a exclusão é lógica, e os registros de extração, teste e sincronização daquele contrato continuam consultáveis para auditoria. Na prática, a evolução normal é sempre "nova versão em novo ciclo" — exclusão só faz sentido para corrigir um cadastro malfeito antes de qualquer extração.

Vale o mesmo para o desligamento vindo do contrato: um modelo marcado com `meta.disabled: true` (ou um contrato que fica sem nenhum modelo habilitado) é recolhido pela sincronização por **exclusão lógica**. Os registros de extração, os resultados de teste, os envios e os arquivos já gerados **continuam existindo** — continuam listados nas telas de **Extrações** e **Envios**; o que sai de vista são as listagens de **Contratos** e **Modelos de Dados**, porque o registro que os ancorava foi recolhido. Não se perde histórico; não há, porém, tela de restauração no painel.

## Veja também

- [Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta)
- [Anatomia do YAML do Contrato]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Conceito de Contrato de Dados]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/conceito)
