---
layout: default
title: "Instituições"
toc: true
---
# Instituições

A instituição é o topo da estrutura da rede: cada [unidade]({{site.baseurl}}/documentacao/manual-do-usuario/configuracoes-iniciais/unidades)
pertence a uma instituição. Pela instituição também se definem as pessoas
que respondem por ela na plataforma — o Reitor, os Pesquisadores
Institucionais, a Gestão de Pessoas e os Recursos Humanos.

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV. Cadastrar, editar e excluir instituições é só do
Administrador e do Gestor CCV; o Suporte CCV apenas consulta.

## Ver as instituições cadastradas

Em **Cadastros Gerais → Instituições**, a plataforma lista as instituições
com o tipo, o código, o nome, a sigla, a UF e o reitor de cada uma. O bloco
**Filtros**, acima da lista, permite buscar por palavra-chave e restringir
por tipo e por reitor. Na coluna **Ação**, os ícones abrem o detalhe, a
edição e a exclusão da instituição.

![Listagem de instituições]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/instituicoes/lista.png)

## Cadastrar ou editar uma instituição

O botão **Cadastrar**, no canto superior direito da lista, abre o
formulário, em dois blocos:

- **Dados Gerais** — Nome, Tipo, Código (até 6 caracteres), Sigla (até 25)
  e UF, todos obrigatórios;
- **Detalhamento** — o Reitor, obrigatório no formulário, e, opcionais, os
  Pesquisadores Institucionais, a Gestão de Pessoas e os Recursos Humanos.

![Formulário de cadastro de instituição]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/instituicoes/cadastrar.png)

Salvar o **Detalhamento** atribui e retira perfis:

- a instituição tem um único Reitor: escolher outra pessoa tira o perfil de
  quem era reitor;
- em cada uma das três listas, quem entra ganha o perfil naquela
  instituição, e quem sai o perde;
- o Pesquisador Institucional ganha também o perfil Executor Acadêmico em
  todas as unidades da instituição — e o perde junto, ao sair da lista.

## Ver o detalhe de uma instituição

O ícone de detalhe abre a página da instituição, com os dados gerais, as
datas de cadastro e de atualização, o reitor, a **Equipe Técnica** — abas
com os Pesquisadores Institucionais, a Gestão de Pessoas e os Recursos
Humanos, cada uma com o nome e o CPF — e a tabela das **Unidades** da
instituição, com filtros por palavra-chave, tipo e município. O ícone de
detalhe de cada unidade abre a página dela. O botão **Editar**, no alto,
altera a instituição.

![Detalhe de uma instituição]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/instituicoes/detalhe.png)

> **⚠️ Excluir uma instituição apaga as unidades dela**
>
> Todas as unidades da instituição excluída são excluídas junto, e com elas o
> que depende delas. Não há como desfazer.
