---
layout: default
title: "Ciclo de coleta"
toc: true
---

# Ciclo de coleta

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página descreve como o calendário anual da coleta é organizado dentro do Coletor, com ênfase na janela de correção. Para ver onde o ciclo se encaixa no fluxo de ponta a ponta, leia antes a [Visão geral]({{ site.baseurl }}/documentacao/coletor/visao_geral) e o [Fluxo de negócio]({{ site.baseurl }}/documentacao/coletor/fluxo_de_negocio).

## O que é um Ciclo de Coleta

Um **[Ciclo de Coleta]({{ site.baseurl }}/documentacao/coletor/glossario#ciclo-de-coleta)** é o período anual em que a **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** consolida os microdados das instituições da Rede Federal. No Coletor, cada ciclo agrupa um ou mais **Contratos de Dados**, e cada contrato pertence a exatamente um ciclo. O ciclo também delimita quando uma **[Sincronização]({{ site.baseurl }}/documentacao/coletor/glossario#sincronizacao)** com a PNP é aceita: fora da janela, o envio é bloqueado.

## Anatomia do ciclo

Cada ciclo é caracterizado por seis marcos de calendário, expressos em linguagem de negócio:

- **Ano de referência.** O ano-base ao qual os microdados se referem (exemplo: ciclo de 2025 cobre os dados do exercício 2025).
- **Início da janela principal.** Data em que a coleta abre. Antes dela, o sistema não aceita extrações nem sincronizações daquele ciclo.
- **Fim da janela principal.** Data em que a coleta normal se encerra. A partir desse momento, só correções pontuais são esperadas.
- **Início da janela de correção.** Data em que a fase de correção começa. Permite reabrir o ciclo para ajustes localizados sem precisar reabrir tudo.
- **Fim da janela de correção.** Data em que a fase de correção termina e o ciclo se torna efetivamente inalterável do lado do Coletor.
- **Data de envio final ao MEC.** Prazo administrativo em que os dados consolidados precisam estar entregues ao **[MEC]({{ site.baseurl }}/documentacao/coletor/glossario#mec)**.

## Linha do tempo

```text
Abertura ──▶ Janela normal de coleta ──▶ Fechamento ──▶ Janela de correção ──▶ Envio final ao MEC
(início)                                 (fim)          (início ▸ fim da correção)
```

## Período de Correção: o que muda

O **[Período de Correção]({{ site.baseurl }}/documentacao/coletor/glossario#periodo-de-correcao)** é a fase em que o ciclo já fechou para coleta nova, mas continua aberto para ajustes pontuais antes da entrega final. As regras operacionais mudam dependendo de onde o calendário está hoje:

| Operação | Janela normal | Período de correção | Fora de qualquer janela |
|---|---|---|---|
| Extrair / re-extrair Modelo | ✅ | ✅ | ❌ |
| Enviar à PNP | ✅ | ✅ | ❌ |

> ⚠️ **Fora da janela, a extração é bloqueada — não apenas inútil.** O sistema aplica a mesma regra da sincronização e recusa a ação antes de qualquer tarefa entrar na fila: o operador recebe "Extração não permitida: …". Não é o caso de "roda mas não serve para nada" — não roda. Um contrato **sem ciclo de coleta** associado também conta como bloqueado.

Não há "Editar Contrato" no painel: contratos, modelos e ciclos chegam da PNP via **Sincronizar com a PNP**, não são cadastrados à mão.

## Múltiplos ciclos

O Coletor mantém o histórico completo dos ciclos passados. Cada Contrato pertence a um ciclo específico, então ao navegar pelo painel é normal ver contratos de ciclos diferentes lado a lado — o mais recente costuma estar em coleta ativa, enquanto os anteriores aparecem como referência. O ciclo "ativo" para fins operacionais é aquele cuja data de hoje cai dentro da janela principal ou da janela de correção; um ciclo encerrado preserva contratos, **[Registros de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-extracao)** e Registros de Sincronização para auditoria, mas não aceita novas operações de envio.

## Veja também

- [Operação corrente]({{ site.baseurl }}/documentacao/coletor/operacao_corrente)
- [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato)
- [Ciclo de vida do contrato]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/ciclo_de_vida)
