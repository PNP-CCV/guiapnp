---
layout: default
title: "Sincronização com a PNP"
toc: true
---
# Sincronização com a PNP

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página descreve o fluxo de envio dos **[Parquets]({{ site.baseurl }}/documentacao/coletor/glossario#parquet)** locais para a **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** — o que sai do Coletor, com qual autenticação, e o que acontece **depois** do envio, que é metade da história. Cobre também a direção inversa: o que "Sincronizar com a PNP" traz para dentro do Coletor.

> ⚠️ **Enviar não encerra o fluxo.** O envio bem-sucedido não significa "dado aceito". Ele coloca o Parquet numa fila de validação **do lado da PNP**, que passa por validação estrutural, homologação da área e aprovação do Reitor — todas ações fora do Coletor.

## Fluxo de envio

Começa quando o operador clica **Enviar** no contrato (status "Pronto para Sincronizar") e termina com um **[Registro de Sincronização]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-sincronizacao)** consultável na tela **Envios**:

1. O clique dispara uma tarefa em background — o navegador não trava.
2. A tarefa localiza, para cada modelo do contrato, o Parquet da última extração bem-sucedida.
3. Modelos sem extração bem-sucedida ou sem arquivo em disco são pulados. Se nenhum for elegível, o envio é abortado.
4. Cada modelo é enviado em uma requisição separada à PNP — não há lote. O tempo limite é de 5 minutos por arquivo.
5. Para cada modelo aceito, a PNP devolve um identificador de dataset, que o Coletor guarda em um **[Registro de Validação de Modelo]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-validacao-de-modelo)** — é por ele que a validação será acompanhada.
6. Falhas individuais não interrompem o restante: a tarefa tenta todos os modelos e agrega o resultado no Registro de Sincronização (total, sucessos, erros e a resposta completa da PNP por modelo).

## Autenticação

Não há "chave de ativação" manual. A autenticação da instância com a PNP é **automática, entre servidores**, com tokens de vida curta renovados pelo próprio Coletor. O vínculo foi estabelecido uma única vez no [Primeiro acesso]({{ site.baseurl }}/documentacao/coletor/primeiro_acesso), quando o secret da instituição foi casado com o hostname do servidor. Se a instância perder a autenticação (respostas 401/403 em todos os envios), reiniciar a stack (`coletor down` e `coletor up`) refaz a ativação.

## A cadeia de validação do lado da PNP

Depois do envio, o Coletor só **observa**. O estado remoto de cada dataset é espelhado no Registro de Validação de Modelo:

```text
RECEBIDO / VALIDANDO ──▶ DISPONIVEL ──▶ HOMOLOGADO_AREA ──▶ APROVADO_REITOR
          │                                    │
          ▼                                    ▼
        ERRO                            REJEITADO_AREA
```

| Status na PNP | Status no Coletor | Terminal? |
|---|---|---|
| `RECEBIDO`, `VALIDANDO` | Aguardando validação | não |
| `DISPONIVEL` | Validado | não |
| `HOMOLOGADO_AREA` | Homologado pela área | não |
| `APROVADO_REITOR` | Aprovado pelo Reitor | **sim** |
| `ERRO` | Rejeitado | sim |
| `REJEITADO_AREA` | Rejeitado pela área | sim |
| `SUPERSEDED` | Substituído | sim |

O acompanhamento é por **consulta**: com o dashboard aberto, o Coletor verifica a cada 2 minutos; sem ninguém olhando, uma tarefa agendada serve de rede de segurança (a cada 30 minutos, por padrão). Uma validação pendente por mais de 24 horas é marcada como tempo esgotado. O botão **"Verificar agora"** força a consulta imediata.

**Homologação da Área e Aprovação do Reitor são ações humanas na PNP.** Não existe botão para elas no Coletor.

> ⚠️ **Reenviar dado idêntico não reseta a validação.** A PNP deduplica dataset por conteúdo (checksum). Reenviar um Parquet idêntico devolve o **identificador do dataset já existente, com o status antigo** — inclusive uma rejeição anterior. Ou seja: re-extrair sem que o dado mude não limpa uma rejeição. Para destravar, o dado na origem precisa efetivamente mudar.

## Padrões de erro e tratamento

| Cenário | Sintoma | Ação |
|---|---|---|
| Instância sem autenticação | HTTP 401/403 em todos os modelos | Reiniciar a stack (`coletor down` e `coletor up`) |
| PNP fora do ar | Envio registrado como falha, erro de conexão | Aguardar e re-disparar |
| Rejeição na validação | Status "Rejeitado" ou "Rejeitado pela área" no modelo | Corrigir o dado **na origem** e re-extrair — reenviar o mesmo conteúdo não adianta |
| Tempo limite no upload (>5 min) | Falha em um modelo muito grande | Reduzir o volume na consulta da fonte |
| Parquet ausente em disco | Modelo pulado; total de modelos menor que o esperado | Re-extrair o modelo |

O envio tolera falhas parciais: se 3 de 4 modelos sincronizam e 1 falha, os 3 sucessos ficam reconhecidos. Re-disparar tenta tudo de novo.

## Direção inversa: o que "Sincronizar com a PNP" traz

O botão **Sincronizar com a PNP** no dashboard puxa os metadados da PNP para o Coletor — usado na primeira instalação e para ressincronizar quando a PNP publica atualizações:

1. Os **Ciclos de Coleta** vigentes, com suas janelas.
2. Os **schemas** dos contratos (o YAML de cada um).
3. Os **Contratos de Dados**, apontando para os schemas.
4. Um **Modelo de Dados** por entrada de `models` de cada contrato — exceto os modelos marcados com `meta.disabled: true`, que **não são importados**. Modelo que deixou de existir no contrato (ou que passou a ser `disabled`) é removido por exclusão lógica, recuperável.
5. A marcação de **obrigatório/opcional** de cada modelo, lida de `meta.required`. É aqui que ela é atualizada quando a PNP publica uma nova versão do schema.
6. As tabelas de apoio (estruturas/campi, áreas temáticas, subeixos, municípios) e os dados de referência de matrículas e servidores.

É por aqui que contratos, modelos e ciclos entram no Coletor — **não** há cadastro manual deles no painel.

> ⚠️ **Contrato que não aparece depois de sincronizar.** Um contrato cujos modelos estão **todos desabilitados** não é criado; se já existia, é removido (também por exclusão lógica) e o motivo fica registrado no log. Não é falha de sincronização.

> ℹ️ **Depois de atualizar o Coletor, sincronize uma vez.** As marcações de modelo obrigatório/opcional só passam a valer depois de uma sincronização com a PNP. Numa instalação recém-atualizada, e antes dessa sincronização, todos os modelos são tratados como obrigatórios — o comportamento anterior.

## Veja também

- [Operação corrente]({{ site.baseurl }}/documentacao/coletor/operacao_corrente)
- [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato)
- [Perguntas frequentes]({{ site.baseurl }}/documentacao/coletor/faq)
