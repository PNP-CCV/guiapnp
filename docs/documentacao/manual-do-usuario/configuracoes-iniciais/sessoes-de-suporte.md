---
layout: default
title: "Sessões de suporte"
toc: true
---
# Sessões de suporte

Para atender um chamado, o Administrador pode entrar na plataforma como
outra pessoa (**impersonação**) ou assumir um perfil sem ser ninguém em
particular (**papel assumido**). Cada vez que isso acontece, a plataforma
registra uma sessão de suporte. Esta tela é a consulta dessa trilha: não
inicia nem encerra sessões — a sessão começa pela ação na linha da listagem
de usuários.

Esta tela está disponível só para o perfil Administrador.

## Consultar a trilha

Em **Cadastros Gerais → Sessões de suporte**, a plataforma lista as sessões
registradas, da mais recente para a mais antiga, com:

- **Situação** — **● Ativa** (em andamento e dentro do prazo), **Encerrada**
  (alguém a encerrou) ou **Expirada** (o prazo passou sem encerramento);
- **Modo** — Impersonação ou Papel assumido;
- **Ator** — quem iniciou a sessão;
- **Sujeito** — a pessoa impersonada, com o CPF mascarado; no papel
  assumido fica "—", porque ninguém foi impersonado;
- **Papel** e **Escopo** — o perfil usado na sessão e a instituição,
  unidade ou área temática dele;
- **Motivo** — o que o ator informou ao iniciar;
- **Início**, **Fim** e **Motivo do fim**.

A tabela é larga: as últimas colunas aparecem rolando para a direita.

![Trilha de sessões de suporte]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/sessoes-de-suporte/lista.png)

## Por que uma sessão termina

O **Motivo do fim** diz como a sessão acabou:

- **Saída do administrador** — o ator saiu da sessão;
- **Revogação** — a sessão foi revogada;
- **Nova sessão do mesmo ator** — o ator abriu outra sessão, e a anterior
  foi encerrada: cada ator tem no máximo uma sessão ativa;
- **Ator ou sujeito desativado**;
- **Teto atingido** — a sessão chegou ao tempo máximo;
- **Regime desabilitado**.
