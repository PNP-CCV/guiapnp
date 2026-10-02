---
layout: default
title: "Grupos de Permissão"
toc: true
---
# Grupos de Permissão

O grupo de permissão controla quem vê um [conteúdo]({{site.baseurl}}/documentacao/manual-do-usuario/pnp-gestor/conteudos) do PNP Gestor que não é
público. No portal da PNP, o conteúdo associado a um grupo ativo aparece
para as pessoas desse grupo e para quem o criou; o conteúdo que não é
público e não tem grupo ativo só aparece para quem o criou e para o
Administrador.

Esta tela está disponível para os perfis Administrador, Operador SETEC e
Gestor Setec. Cadastrar, editar, excluir grupos e associar pessoas é do
Administrador e do Gestor Setec; o Operador SETEC apenas consulta, para
escolher qual grupo associar a um conteúdo.

## Ver os grupos cadastrados

Em **PNP Gestor → Grupos de Permissão**, a plataforma lista os grupos já
cadastrados, com o nome, a descrição, quantos usuários e quantos conteúdos
cada um tem, se está ativo e as datas de criação e de atualização. O bloco
**Filtros**, acima da lista, permite buscar por palavra-chave. Na coluna
**Ação**, os ícones abrem o detalhe, a edição, a exclusão e a associação de
pessoas ao grupo.

![Listagem de grupos de permissão]({{site.baseurl}}/assets/img/docs/manual-do-usuario/pnp-gestor/grupos-de-permissao/lista.png)

## Cadastrar um grupo

O botão **Cadastrar**, no canto superior direito da lista, abre o
formulário de cadastro. O nome é obrigatório e a descrição pode ficar em
branco. Dois grupos não podem ter o mesmo nome.

![Formulário de cadastro de grupo de permissão]({{site.baseurl}}/assets/img/docs/manual-do-usuario/pnp-gestor/grupos-de-permissao/cadastrar.png)

## Associar pessoas

O ícone de associar pessoas, na coluna **Ação**, abre a seleção das pessoas
do grupo: a lista traz os usuários da plataforma, pelo nome.

## Ver o detalhe de um grupo

O ícone de detalhe abre a página do grupo: a descrição e as quantidades de
usuários e de conteúdos, a tabela dos conteúdos associados ao grupo e a
tabela dos usuários que fazem parte dele, cada uma com busca por
palavra-chave. O botão **Editar** altera o nome e a descrição.

![Detalhe de um grupo de permissão]({{site.baseurl}}/assets/img/docs/manual-do-usuario/pnp-gestor/grupos-de-permissao/detalhe.png)

## O grupo Gestor Rede

O grupo **Gestor Rede** é mantido pela própria plataforma: fazem parte dele
todas as pessoas com o perfil Gestor Rede, de todas as instituições. A
plataforma recusa acrescentar ou retirar pessoas dele à mão — para mudar
quem está no grupo, conceda ou revogue o perfil — e recusa excluí-lo. Ele
pode ser renomeado e associado a conteúdos como qualquer outro grupo.
