---
layout: default
title: "Primeiro acesso"
toc: true
---

# Primeiro acesso

* TOC
{:toc}

> **Para quem é:** 🔌 integradores · 👔 gestores

Esta página descreve o que acontece na primeira vez que o painel é aberto: a tela de setup, a ativação da instância junto à PNP e a importação dos contratos.

## A tela de setup

Com a stack no ar, acesse `http://<servidor>:8000/painel/`. Enquanto **não existir nenhum usuário**, o painel apresenta a tela de configuração inicial em vez do login — uma única tela, preenchida uma única vez:

![Tela de setup inicial]({{ site.baseurl }}/assets/img/docs/coletor/01-setup-inicial.png)

| Campo | O que informar |
|---|---|
| Usuário / E-mail / Senha | As credenciais do primeiro administrador do painel |
| URL da API PNP | A URL fornecida pela equipe da PNP à sua instituição |
| Secret da API PNP | O secret de integração fornecido junto com a URL |
| Hostname da instância | Já vem preenchido e **travado** com o nome da máquina onde o Coletor roda |

## O que o setup faz

Enviar o formulário dispara três ações em sequência, dentro de uma única transação:

1. Cria o **superusuário** do painel.
2. Grava a configuração da instância (URL, secret, hostname).
3. **Ativa a instância na PNP** — obtém o token de acesso, busca os dados da instituição (sigla, nome, responsável) e registra as tarefas agendadas.

É tudo ou nada: se a ativação falhar (PNP fora do ar, secret incorreto), a transação inteira é desfeita — nenhum usuário é criado e a mesma tela volta com o motivo do erro. O corolário é útil no diagnóstico: **se o setup passou, a integração com a PNP já está provada**. Não existe o estado "criou o usuário mas a PNP não respondeu".

## O secret é casado com o hostname {#secret-casado-com-hostname}

No primeiro registro, a PNP vincula o secret da instituição ao hostname da máquina. A partir daí, o mesmo secret usado de outra máquina é recusado:

```text
409 — Secret already bound to another instance
```

> ⚠️ **Trocar o Coletor de servidor não é só copiar os arquivos.** Em outra máquina o hostname muda, o secret deixa de conferir e a ativação falha com o erro acima. Migrar a instância exige contato com a equipe da PNP para desvincular o secret. Planeje o servidor definitivo **antes** de rodar o setup — ver [Requisitos técnicos]({{ site.baseurl }}/documentacao/coletor/requisitos_tecnicos#servidor).

## Importar os contratos da PNP {#importar-os-contratos-da-pnp}

Concluído o setup, o painel abre direto no **Dashboard**, com o *wizard* de 8 passos posicionado no passo 1. A primeira ação é o botão **"Sincronizar com a PNP"**, que importa os **Ciclos de Coleta**, os **Contratos de Dados** e os **Modelos de Dados** definidos pela PNP para o ciclo vigente:

![Modelos de dados importados da PNP]({{ site.baseurl }}/assets/img/docs/coletor/22-modelos-lista.png)

Nada disso é digitado à mão: a instituição **não cria** contrato nem modelo. Eles chegam prontos da PNP — o trabalho da instituição, nos passos seguintes, é dizer **de onde vem** cada dado. A [Operação passo a passo]({{ site.baseurl }}/documentacao/coletor/operacao_passo_a_passo) continua a partir daqui.

> ℹ️ **A lista importada pode ser menor que o catálogo.** Cada contrato diz quais modelos estão habilitados nesta edição: modelos **desabilitados** pela PNP não são importados, e um contrato cujos modelos estão todos desabilitados não chega a aparecer. Também é normal ver, logo na primeira sincronização, contratos com o badge **"Somente Modelos Opcionais"** — são os que só têm [modelos opcionais]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-opcional), sem nada a coletar até que alguém configure uma extração. Ver [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Usuários adicionais

O primeiro usuário é o administrador. Para a operação cotidiana, crie contas individuais na tela **Usuários** (menu *Sistema*, visível apenas para administradores). Contas comuns operam a coleta; contas de administrador também acessam **Tarefas Agendadas**, **Configurações** e a própria gestão de usuários.

## Veja também

- [Operação passo a passo]({{ site.baseurl }}/documentacao/coletor/operacao_passo_a_passo) — a coleta do passo 2 em diante
- [Requisitos técnicos]({{ site.baseurl }}/documentacao/coletor/requisitos_tecnicos#credenciais-junto-a-pnp) — as credenciais que o setup exige
- [Sincronização com a PNP]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp) — o que a importação traz, em detalhe
