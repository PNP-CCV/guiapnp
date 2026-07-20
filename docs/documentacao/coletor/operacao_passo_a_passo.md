---
layout: default
title: "Operação passo a passo"
toc: true
---

# Operação passo a passo

* TOC
{:toc}

> **Para quem é:** 🔌 integradores · 👔 gestores

Esta página conduz uma coleta completa pelo painel, na ordem dos 8 passos do *wizard* — do cadastro do **Provedor de Dados** à **Aprovação do Reitor** — com as telas reais de uma coleta do ciclo 2026.

## O wizard é o seu checklist

O Dashboard exibe o funil de 8 passos calculado sobre **todos** os contratos do ciclo ativo. Um passo só é dado como concluído quando todos os contratos passam daquele estágio — um único contrato parado segura o passo inteiro, e o progresso parcial aparece como `7/9`.

![Wizard de 8 passos no dashboard]({{ site.baseurl }}/assets/img/docs/coletor/02-dashboard-wizard-passo1.png)

O badge de status de cada contrato é recalculado em tempo real e a tela se atualiza sozinha (10 s no contrato, 120 s no wizard) — não é preciso dar refresh. O significado de cada badge está em [Status do contrato](/documentacao/coletor/status_do_contrato) (e resumido em [Referência rápida](/documentacao/coletor/referencia_rapida)).

## Passo 1 — Sincronizar com a PNP

Já descrito em [Primeiro acesso](/documentacao/coletor/primeiro_acesso#importar-os-contratos-da-pnp): o botão **"Sincronizar com a PNP"** importa ciclos, **Contratos de Dados** e **Modelos de Dados**. A instituição não cria nada disso à mão — os contratos chegam prontos da PNP, e o restante da coleta consiste em dizer de onde vem cada dado.

## Passo 2 — Cadastrar os provedores

Na tela **Provedores**, cadastre cada fonte concreta de microdados. Um provedor = uma fonte; o cadastro guarda o endereço e as credenciais de acesso.

![Cadastro de provedor de planilha online]({{ site.baseurl }}/assets/img/docs/coletor/03-provedor-planilha.png)

Formas de extração disponíveis:

| Forma | Variantes |
|---|---|
| API HTTP | Sem autenticação, HTTP Basic, OAuth2, token simples, JWT |
| Banco de dados | PostgreSQL, MySQL, SQL Server, SQLite, IBM Db2, MongoDB, CouchDB |
| Planilha online | Google Docs, Dropbox, SharePoint |
| Upload de planilha | XLS, XLSX, ODS |

Duas dicas evitam as falhas mais comuns com planilhas:

- **Planilha do Google: use a URL de export**, não a de edição. Uma URL `/edit` devolve HTML e a extração falha com "O formato do arquivo não é suportado". Também não use o link temporário de `googleusercontent.com` — ele é assinado, expira, e a coleta quebra dias depois sem ninguém ter mexido em nada.

  ```text
  ❌ https://docs.google.com/spreadsheets/d/<ID>/edit?gid=...
  ✅ https://docs.google.com/spreadsheets/d/<ID>/export?format=xlsx
  ```

- **Planilha de exemplo:** `GET /base/planilha_exemplo/` baixa um XLSX com uma aba por modelo cadastrado — slug da aba, colunas do schema e dados fictícios (`?linhas=N` controla o volume). É o jeito mais rápido de montar uma planilha que casa com os contratos importados.

## Passo 3 — Configurar a extração

A **Configuração de Extração** liga um modelo a um provedor e diz *como* achar o dado lá dentro. É uma por modelo, e é o registro que o operador mais edita.

![Lista de configurações de extração]({{ site.baseurl }}/assets/img/docs/coletor/16-configs-extracao-lista.png)

O campo específico muda com a forma de extração: **aba** na planilha, **endpoint** na API, **tabela ou query SQL** no banco, **caminho** no compartilhamento.

Antes de salvar, use **"Testar extração"**: o Coletor lê a fonte de verdade, na hora, e mostra as 20 primeiras linhas — sem gravar nada.

![Modal de teste de extração]({{ site.baseurl }}/assets/img/docs/coletor/04-config-testar-extracao.png)

> 💡 **O botão mais barato do sistema.** Um teste de segundos evita uma extração falha, uma ida ao histórico e um diagnóstico. Errar aqui não custa nada — é o momento mais seguro para descobrir que a fonte não é a que se pensava.

## Passo 4 — Extrair os dados

**"Extrair todos"** (no Dashboard) dispara a extração de todos os contratos do ciclo ativo; cada contrato e cada modelo também têm seu botão individual **"Extrair Dados"**. A execução roda em background — o navegador não trava e a tela se atualiza conforme os resultados chegam.

![Dashboard com extração em andamento]({{ site.baseurl }}/assets/img/docs/coletor/14-dashboard-configs-completas.png)

Para cada modelo, a extração lê a fonte, normaliza colunas e tipos para o schema do contrato e grava um arquivo **Parquet** local — que pode ser pré-visualizado e baixado na tela do modelo:

![Pré-visualização do parquet gerado]({{ site.baseurl }}/assets/img/docs/coletor/24-modelo-previa-parquet.png)

Os **testes de qualidade do contrato rodam dentro da própria extração** — não há passo separado. Cada campo é conferido (presença, tipo, completude) junto com as regras declarativas do contrato (enum, unicidade, faixas). Um contrato só chega a "Pronto para Sincronizar" quando extração **e** testes passam; o resultado detalhado fica em **"Ver resultados de teste"**:

![Resultados dos testes por campo]({{ site.baseurl }}/assets/img/docs/coletor/28-resultados-testes-contrato.png)

Cada tentativa — sucesso ou falha — gera um **Registro de Extração** com motivo do erro e detalhes técnicos, consultável na tela **Extrações**. Se algo falhar, o roteiro de diagnóstico está em [Quando algo falha](/documentacao/coletor/quando_algo_falha).

## Passo 5 — Enviar à PNP

Com os contratos em "Pronto para Sincronizar", **"Enviar todos"** (ou o botão "Enviar" de cada contrato) sobe os Parquets à PNP. Cada tentativa gera um **Registro de Sincronização** com status HTTP e resposta da API — a trilha de auditoria do que foi efetivamente entregue.

![Contrato pronto para sincronizar]({{ site.baseurl }}/assets/img/docs/coletor/06-contrato-pronto-sincronizar.png)

Enviar **não encerra o fluxo**: o contrato entra em "Aguardando Validação PNP" e o Coletor passa a acompanhar o que acontece do outro lado.

## Passo 6 — Aguardar a validação da PNP

A PNP confere cada Parquet recebido por conta própria: além do schema, roda uma **validação referencial** — campus, área temática e município citados no dado precisam existir no cadastro da Rede.

![Modelo validado aguardando aprovação]({{ site.baseurl }}/assets/img/docs/coletor/23-modelo-detalhe.png)

O acompanhamento é automático: com o Dashboard aberto, o Coletor consulta a PNP a cada 2 minutos; sem ninguém olhando, uma tarefa agendada serve de rede de segurança. O botão **"Verificar agora"** força a consulta imediata. Se a PNP rejeitar, o caminho de correção está em [Quando algo falha](/documentacao/coletor/quando_algo_falha#validacao-rejeitada-pela-pnp).

## Passos 7 e 8 — Homologação da Área e Aprovação do Reitor {#passos-7-e-8}

Daqui em diante o Coletor só observa: **não existe botão de homologar nem de aprovar no Coletor**. As duas etapas são decisões humanas tomadas **na PNP**, e o painel apenas reflete o resultado.

![Contrato aguardando aprovação do reitor]({{ site.baseurl }}/assets/img/docs/coletor/10-coletor-aguardando-reitor.png)

Na PNP, o fluxo é sequencial:

1. **Homologação da Área** — o Gestor de Área Temática revisa a "Fila de Homologação" da sua área e homologa ou **rejeita com justificativa** (que volta ao Coletor para correção). Antes de decidir, ele pode pré-visualizar o conteúdo real do dataset.

   ![Fila de homologação na PNP]({{ site.baseurl }}/assets/img/docs/coletor/07-pnp-fila-homologacao.png)

2. **Aprovação do Reitor** — só chega ao Reitor o que a área já homologou. A visão é institucional (todas as áreas de uma vez) e a decisão é terminal: neste nível só existe aprovar.

   ![Fila de aprovação do reitor na PNP]({{ site.baseurl }}/assets/img/docs/coletor/11-pnp-fila-reitor.png)

> ⚠️ **Na PNP, confira o papel ativo.** A Fila de Homologação filtra pelo **papel ativo** (instituição × área) de quem está logado. Quem acumula vínculos em várias áreas precisa trocar em "Alterar Papel" — senão a fila aparece vazia, sem indicar o motivo. O papel volta ao padrão a cada login. Se a coleta travou nos passos 7 ou 8, o problema não é técnico: fale com o gestor da área ou com a reitoria.

## Estado final

Com a aprovação do Reitor, o contrato chega a **"Sincronizado com Sucesso"** — e o botão de reextração desaparece: dado aceito oficialmente não pode ser substituído por baixo. Trocar exige um novo **Ciclo de Coleta**.

![Contrato aprovado pelo reitor]({{ site.baseurl }}/assets/img/docs/coletor/13-coletor-aprovado-reitor.png)

Quando todos os contratos fecham, o wizard marca 8/8:

![Dashboard com o fluxo completo]({{ site.baseurl }}/assets/img/docs/coletor/29-dashboard-fluxo-completo.png)

## A rotina do operador

Entre o disparo inicial e o fechamento, a operação é de acompanhamento diário:

- Abrir o painel e percorrer a lista de contratos do ciclo ativo, lendo o badge dos que não estão em "Sincronizado com Sucesso".
- Re-extrair os modelos com falha — depois de ler o motivo no Registro de Extração.
- Enviar os contratos que chegaram a "Pronto para Sincronizar".
- Nos já enviados, acompanhar a validação do lado da PNP.

Re-extraia quando o provedor ou a configuração mudarem, quando o sistema marcar "Reextração Necessária" ou quando um problema na origem for corrigido. Evite disparar dezenas de extrações no mesmo minuto (a fila de tarefas é compartilhada) e não edite um contrato com extração em curso. O detalhamento dessa rotina está em [Operação corrente](/documentacao/coletor/operacao_corrente).

## Janelas do ciclo

O **Ciclo de Coleta** delimita quando cada operação é aceita. Fora da janela, extração e envio são **bloqueados** pelo sistema — a ação é recusada antes de qualquer tarefa entrar na fila:

| Operação | Janela normal | Período de Correção | Fora de qualquer janela |
|---|---|---|---|
| Extrair / re-extrair | ✅ | ✅ | ❌ |
| Enviar à PNP | ✅ | ✅ | ❌ |

O calendário completo do ciclo está em [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta).

## Veja também

- [Quando algo falha](/documentacao/coletor/quando_algo_falha) — diagnóstico de cada tipo de falha
- [Status do contrato](/documentacao/coletor/status_do_contrato) — a referência de todos os badges
- [Sincronização com a PNP](/documentacao/usuarios-especializados/contratos/sincronizacao_pnp) — o protocolo de envio em detalhe
