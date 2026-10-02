---
layout: default
title: "Contratos de Dados"
toc: true
---
# Contratos de Dados

O contrato de dados junta três cadastros: uma
[área temática]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/areas-tematicas), um [ciclo de
coleta]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/ciclos-de-coleta) e um [schema de
contrato]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/schemas-de-contrato). Ele diz o que cada instituição envia
(o schema), em que ciclo e sob qual área. Os datasets que as instituições
enviam chegam sempre em nome de um contrato.

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV. Cadastrar, editar e excluir contratos é só do Administrador e
do Gestor CCV; o Suporte CCV apenas consulta.

## Ver os contratos cadastrados

Em **Microdados → Contratos de Dados**, a plataforma lista os contratos já
cadastrados, com o ciclo, o schema (nome e versão), a área temática, o
slug e as tags de cada um. O slug é montado pela plataforma a partir da
área, do ano do ciclo e do schema. O campo **Busca** procura no slug, no
nome e na versão do schema e no nome da área.

Na coluna **Ação** ficam o detalhe, a edição e a exclusão.

![Listagem de contratos de dados]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/contratos-de-dados/lista.png)

## Cadastrar um contrato

O botão **Cadastrar**, no canto superior direito da lista, abre o
formulário de cadastro. Área Temática, Ciclo de Coleta e Schema de Contrato
são obrigatórios; as tags podem ficar em branco e, se preenchidas, são
separadas por vírgula. A plataforma não aceita dois contratos com a mesma
combinação de área, ciclo e schema.

![Formulário de cadastro de contrato de dados]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/contratos-de-dados/cadastrar.png)

## Excluir um contrato

> **⚠️ Excluir um contrato apaga os datasets dele**
>
> Todos os datasets recebidos para o contrato são excluídos junto —
> inclusive os já homologados ou aprovados. Não há como desfazer.
