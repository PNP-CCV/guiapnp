---
layout: default
title: "Chaves de Integração"
toc: true
---
# Chaves de Integração

A chave de integração é a credencial com que um sistema da instituição — o
sistema acadêmico ou o extrator de microdados — se conecta à PNP sem o
login de uma pessoa. Cada chave pertence a uma instituição, tem um tipo, os
escopos que dizem o que o sistema pode ler, gravar ou excluir, e uma
validade.

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV, que também cadastram e revogam chaves.

## Ver as chaves cadastradas

Em **Cadastros Gerais → Chaves de Integração**, a plataforma lista as
chaves com o identificador, a descrição, o tipo, o código da instituição,
os escopos, a validade, a situação e quem a criou. A tabela é larga: as
últimas colunas aparecem rolando para a direita. A situação é uma de
quatro:

- **Válida** — ativa e dentro da validade;
- **Expirada** — passou da validade;
- **Inativa** — desativada;
- **Revogada** — invalidada de vez.

O bloco **Filtros**, acima da lista, permite restringir por tipo de
entidade e pelo código da instituição.

![Listagem de chaves de integração]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/chaves-de-integracao/lista.png)

## Cadastrar uma chave

O botão **Cadastrar**, no canto superior direito da lista, abre o
formulário de cadastro. São obrigatórios:

- **Identificador (key_id)** — de 3 a 64 caracteres, só letras minúsculas,
  números, hífen e sublinhado;
- **Tipo de Entidade** — Sistema Acadêmico ou Microdados;
- **Instituição**;
- **Escopos** — ao menos um;
- **Validade (dias)** — de 1 a 3650.

A descrição pode ficar em branco.

![Formulário de cadastro de chave de integração]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/chaves-de-integracao/cadastrar.png)

Cadastrada a chave, a plataforma mostra o segredo dela uma única vez, com o
botão **Copiar secret**. Copie e entregue ao responsável pelo sistema antes
de fechar: o segredo não pode ser consultado depois. Se ele se perder, a
saída é revogar a chave e cadastrar outra.

### Chave de Microdados

Cada instituição tem no máximo uma chave de Microdados válida por vez: a
plataforma recusa cadastrar a segunda enquanto a primeira for válida. E a
chave de Microdados atende uma máquina por vez — enquanto um extrator a
usa, outra máquina com a mesma chave é recusada.

## Revogar uma chave

Nas chaves ativas, o ícone **Revogar**, na coluna **Ação**, pede
confirmação e invalida a chave de vez. Uma chave revogada não volta a
valer.

![Confirmação de revogação de chave de integração]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/chaves-de-integracao/revogar.png)
