---
layout: default
title: "Quando algo falha"
toc: true
---

# Quando algo falha

* TOC
{:toc}

> **Para quem é:** 🔌 integradores

Esta página é o roteiro de diagnóstico do operador: onde investigar cada tipo de falha, como ler as mensagens de erro e o que fazer em cada caso — dos problemas de extração aos de infraestrutura.

## Onde investigar

O Coletor registra tudo. Cinco telas respondem a praticamente qualquer "por que travou?":

| Tela | Serve para |
|---|---|
| **Extrações** | Toda tentativa de extração, com motivo do erro e a configuração usada |
| **Envios** | O que foi enviado e o que a PNP respondeu |
| **Tarefas Assíncronas** | Se o job rodou, falhou ou ainda está na fila |
| **Tarefas Agendadas** | O que roda sozinho e quando |
| **Ver resultados de teste** (no contrato) | Qual regra do contrato reprovou |

![Histórico de extrações]({{ site.baseurl }}/assets/img/docs/coletor/25-extracoes-historico.png)

Para extrações grandes, espere alguns minutos antes de concluir que algo travou — a execução é assíncrona e a tela se atualiza sozinha.

## Falha na extração: fonte inacessível

Credencial inválida, endpoint fora do ar, banco recusando conexão, planilha movida de lugar. O contrato vai para "Falha na Extração" e o motivo fica no **Registro de Extração**. A correção é no **Provedor de Dados** ou na **Configuração de Extração** — corrija, use "Testar extração" para confirmar, e re-extraia.

## Falha na extração: schema divergente

A fonte respondeu, mas as colunas não batem com o contrato. A extração é rejeitada **antes** de gerar o arquivo Parquet, e o motivo descreve a divergência:

```text
Extração rejeitada para o modelo acoes_extensao.
Colunas obrigatórias ausentes nos dados extraídos:
{'id_acao_extensao', 'titulo_acao', 'tipo', 'municipios_atendidos', ...}
```

Colunas a mais também reprovam. A causa é quase sempre uma destas três: **aba/endpoint/query errados** na configuração · a **fonte mudou** de estrutura · o **contrato foi atualizado** na PNP e a fonte não acompanhou.

O bloco **Detalhes** do Registro de Extração mostra exatamente de onde o sistema tentou ler (aba, URL, query) — é por ali que se descobre o erro em segundos:

![Registro de extração com falha por colunas ausentes]({{ site.baseurl }}/assets/img/docs/coletor/15-registro-extracao-falha.png)

O ciclo de correção é sempre o mesmo — corrigir, testar, re-extrair:

1. Corrija a configuração e rode "Testar extração" até ver as colunas certas.

   ![Teste OK após correção]({{ site.baseurl }}/assets/img/docs/coletor/17-config-corrigida-teste-ok.png)

2. O contrato muda para **"Reextração Necessária"** — o sistema detecta que a configuração mudou depois da última extração. Dispare a nova extração; nenhuma etapa anterior é perdida.

   ![Contrato pedindo reextração]({{ site.baseurl }}/assets/img/docs/coletor/18-contrato-reextracao-necessaria.png)

## Teste de qualidade reprovado

Os testes do contrato rodam **dentro** da extração, então uma reprovação também leva o contrato a "Falha na Extração" — não existe um estado separado "Testes com Falha". A diferença está no diagnóstico: o Parquet chegou a ser avaliado e **"Ver resultados de teste"** mostra qual regra reprovou (enum, unicidade, faixa, completude). A correção é no **dado de origem**, seguida de nova extração.

## Validação rejeitada pela PNP {#validacao-rejeitada-pela-pnp}

Passar no contrato não garante passar na PNP: ela ainda roda a **validação referencial** — campus, área temática e município citados precisam existir no cadastro da Rede.

![Dashboard com validação rejeitada]({{ site.baseurl }}/assets/img/docs/coletor/19-dashboard-validacao-rejeitada.png)

```text
Validação referencial PNP reprovada — (campi, campo 'estrutura'):
20 com id inexistente em 'campi': '26419.4300604.01.001'
```

Caso real da coleta 2026: duas abas da planilha haviam sido copiadas do arquivo de outro Instituto, e ninguém trocou o código do campus. O contrato aceitou (o campo é `string` válida), a PNP não. A correção é sempre no **dado de origem** — corrigido lá, o conteúdo muda, e o reenvio segue o fluxo normal.

> ⚠️ **Reenviar dado idêntico não reseta a validação.** A PNP identifica cada dataset pelo **conteúdo** (checksum). Reextrair e reenviar um dado que não mudou faz a PNP devolver o **mesmo dataset, com o status antigo** — inclusive uma rejeição anterior. O sintoma é "reenviei e continua rejeitado". Para mudar o estado na PNP, o dado precisa mudar de verdade.

## Rejeição pela área (passo 7)

O Gestor de Área Temática pode devolver o dataset com uma justificativa. Aqui não há defeito técnico: é uma discordância sobre o conteúdo. A justificativa fica registrada no Coletor e orienta a correção — que, de novo, é no dado de origem.

## Problemas de infraestrutura

O executável `coletor` verifica o ambiente antes de agir e reporta mensagens claras:

| Mensagem | O que fazer |
|---|---|
| `Docker não encontrado` | Instalar o Docker — ver [Instalação](/documentacao/coletor/instalacao#instalar-o-docker) |
| `Docker daemon não está rodando` | Linux: `sudo systemctl start docker`. Windows/macOS: abrir o Docker Desktop |
| `permission denied` ao falar com o Docker | Adicionar o usuário ao grupo `docker` e reabrir a sessão. **Não** contornar com `sudo` |
| `plugin docker compose ausente` | Linux: reinstalar pelo script oficial. Windows/macOS: atualizar o Docker Desktop |
| `sem permissão para criar ...` | Verificar as permissões do diretório pessoal do usuário — e não usar `sudo` |

Para problemas dentro da stack, `coletor status` mostra a saúde de cada serviço e `coletor logs <serviço>` mostra o que ele está reportando.

> ℹ️ **PNP fora do ar quando a stack subiu.** A ativação da instância roda a cada boot do serviço `web`. Se a PNP estava inacessível nesse momento, o painel sobe mesmo assim, mas as sincronizações falham e as tarefas agendadas ficam desativadas até a próxima ativação. Quando a PNP voltar, reinicie a stack (`coletor down` seguido de `coletor up` — os dados são preservados).

## Quando o problema não é técnico

Coleta parada em "Aguardando Homologação da Área" ou "Aguardando Aprovação do Reitor" não tem solução no sistema: são decisões humanas pendentes **na PNP**. O caminho é falar com o gestor da área ou com a reitoria — antes disso, confira se quem vai decidir está com o **papel ativo** correto na PNP (ver [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo#passos-7-e-8)).

## Veja também

- [Referência rápida](/documentacao/coletor/referencia_rapida) — todos os status e a ação esperada em cada um
- [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo) — o fluxo completo sem falhas
- [Contratos de Dados](/documentacao/usuarios-especializados/contratos/acoes_de_extensao) — as regras que os testes de qualidade aplicam
