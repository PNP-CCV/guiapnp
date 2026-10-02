---
layout: default
title: "Áreas Temáticas"
toc: true
---
# Áreas Temáticas

A área temática é o assunto a que um contrato de dados pertence — Ensino,
Gestão de Pessoas, e assim por diante. Ela também recorta o trabalho do
perfil Gestor de Área Temática: ele homologa apenas os datasets dos
contratos da sua área, na sua instituição (ver
[Fila de Homologação]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/fila-de-homologacao)).

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV. Cadastrar, editar e excluir áreas é só do Administrador e do
Gestor CCV; o Suporte CCV apenas consulta.

## Ver as áreas cadastradas

Em **Microdados → Áreas Temáticas**, a plataforma lista as áreas já
cadastradas, com o nome, a descrição e o slug de cada uma.
O bloco **Filtros**, acima da lista, permite buscar por palavra-chave. Na
coluna **Ação**, os ícones abrem o detalhe da área, a edição e a exclusão.

![Listagem de áreas temáticas]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/areas-tematicas/lista.png)

## Cadastrar uma área

O botão **Cadastrar**, no canto superior direito da lista, abre o
formulário de cadastro. Nome e Slug são obrigatórios; a descrição pode
ficar em branco. O slug é preenchido sozinho a partir do nome, em
minúsculas, sem acento e com hífen no lugar do espaço — e pode ser
alterado antes de salvar. Duas áreas não podem ter o mesmo slug.

![Formulário de cadastro de área temática]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/areas-tematicas/cadastrar.png)

## Excluir uma área

A plataforma não exclui uma área que ainda tenha um Gestor de Área
Temática vinculado a ela.

A confirmação da exclusão avisa o que será apagado junto e quantos
contratos de dados estão vinculados à área naquele momento.

> **⚠️ Excluir uma área apaga o que depende dela**
>
> Os contratos de dados da área são excluídos junto, e com eles todos os
> datasets recebidos para esses contratos — inclusive os já homologados ou
> aprovados. Não há como desfazer.
