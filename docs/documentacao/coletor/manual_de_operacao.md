---
layout: default
title: "Manual de Operação do Coletor"
---

# Manual de Operação do Coletor

> **Para quem é:** 🔌 integradores · 👔 gestores

O **Coletor de Microdados** (Coletor:PNP) é o sistema que cada instituição da Rede Federal executa para extrair microdados dos seus sistemas internos, validá-los contra os **Contratos de Dados** definidos pela PNP e enviá-los à Plataforma. Este manual reúne, em um roteiro único e sequencial, tudo o que uma instituição precisa para colocar o Coletor em produção e conduzir uma coleta completa: requisitos técnicos, instalação, primeiro acesso e a operação passo a passo — do cadastro do **Provedor de Dados** até a **Aprovação do Reitor** na PNP.

## Como usar este manual

As páginas foram escritas para serem lidas em ordem, como um tutorial. Quem chega sem nenhuma instalação começa pelos requisitos; quem já tem o sistema no ar pode ir direto à operação.

| Página | Pergunta que responde |
|---|---|
| [Requisitos técnicos](/documentacao/coletor/requisitos_tecnicos) | O que preciso ter antes de instalar? |
| [Instalação](/documentacao/coletor/instalacao) | Como coloco o sistema no ar? |
| [Primeiro acesso](/documentacao/coletor/primeiro_acesso) | O que configuro na primeira vez que abro o painel? |
| [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo) | Como conduzo uma coleta do início ao fim? |
| [Quando algo falha](/documentacao/coletor/quando_algo_falha) | Como diagnostico e corrijo cada tipo de falha? |
| [Referência rápida](/documentacao/coletor/referencia_rapida) | Onde consulto comandos, telas e o checklist do operador? |

## O caminho em 8 passos

Depois de instalado, o dashboard do Coletor guia a coleta por um *wizard* de 8 passos. Os cinco primeiros acontecem no Coletor, dentro da instituição; os três últimos acontecem na PNP, do lado do MEC.

| Passos | Onde | Quem |
|---|---|---|
| 1–5 · configurar, extrair, enviar | Coletor (na instituição) | 🔌 Equipe de TI / integradores |
| 6 · validação estrutural | PNP | Automático |
| 7 · homologação da área | PNP | Gestor de Área Temática |
| 8 · aprovação final | PNP | 👔 Reitor |

> ℹ️ **Os passos 7 e 8 não têm botão no Coletor.** Homologação e aprovação são decisões humanas tomadas na PNP. O Coletor apenas consulta o resultado e o reflete no status de cada contrato. O manual detalha isso em [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo#passos-7-e-8).

## Relação com o restante da documentação

- Os **conceitos** por trás de cada passo estão nas demais páginas desta seção: [Visão geral](/documentacao/coletor/visao_geral), [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio), [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta), [Operação corrente](/documentacao/coletor/operacao_corrente) e [Status do contrato](/documentacao/coletor/status_do_contrato) — além das [Perguntas frequentes](/documentacao/coletor/faq) e do [Glossário do Coletor](/documentacao/coletor/glossario).
- Os **Contratos de Dados** que o Coletor valida e envia estão especificados, campo a campo, na seção [Usuários Especializados › Contratos de Dados](/documentacao/usuarios-especializados/contratos/conceito) deste guia.
- Os **executáveis** do Coletor são distribuídos na [página de releases do repositório PNP-CCV/coletor](https://github.com/PNP-CCV/coletor/releases); a documentação técnica interna (arquitetura, código, extensão) está no [site de documentação do Coletor](https://pnp-ccv.github.io/coletor-pnp-microdados/).

As capturas de tela usadas neste manual vêm de uma coleta real do ciclo 2026.

## Veja também

- [Requisitos técnicos](/documentacao/coletor/requisitos_tecnicos) — a próxima página do roteiro
- [Visão geral](/documentacao/coletor/visao_geral) — o que é o Coletor e seu papel na cadeia de coleta
- [Processo CCV](/documentacao/ccv/processo_ccv) — o ciclo de coleta e validação no contexto metodológico da PNP
