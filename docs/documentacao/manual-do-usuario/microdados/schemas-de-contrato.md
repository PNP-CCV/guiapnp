---
layout: default
title: "Schemas de Contrato"
toc: true
---
# Schemas de Contrato

O schema de contrato descreve, em YAML, o que a instituição precisa
enviar: os modelos (as tabelas) e os campos de cada um, com o tipo e se o
campo é obrigatório. O formato é o da especificação Data Contract
Specification. Um mesmo schema pode servir a vários contratos de dados
(ver [Contratos de Dados]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/contratos-de-dados)).

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV. Cadastrar, editar e excluir schemas é só do Administrador e
do Gestor CCV; o Suporte CCV apenas consulta.

## Ver os schemas cadastrados

Em **Microdados → Schemas de Contrato**, a plataforma lista os schemas já
cadastrados, com o nome, o slug, a descrição e a versão de cada um. A
busca do bloco **Filtros** procura por nome, slug ou versão. Na coluna
**Ação**, o ícone de olho abre o detalhe do schema, com o YAML completo.

![Listagem de schemas de contrato]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/schemas-de-contrato/lista.png)

## Cadastrar ou editar um schema

O botão **Cadastrar** abre a página **Novo Schema de Contrato**; o ícone
de edição, na lista, abre a mesma página já preenchida. Nome, Slug e
Schema são obrigatórios; a descrição pode ficar em branco. A versão, no
formato `1.0.0`, é opcional no cadastro: em branco, o schema começa na
`1.0.0`. Na edição, uma versão apagada é mantida como estava. No cadastro, o slug é preenchido
sozinho a partir do nome; na edição, ele não é recalculado.

O YAML é escrito no editor à esquerda. Ao lado, a **Pré-visualização**
diz se o YAML é válido e resume o que ele declara: a versão, quantos
modelos e quantos campos, e os tipos usados.

![Edição de um schema de contrato, com o editor e a pré-visualização]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/schemas-de-contrato/editar.png)

Ao salvar, a plataforma confere o YAML contra a especificação e recusa um
schema inválido mostrando o motivo da recusa.

### A versão sobe sozinha

Quando uma edição altera o YAML, a plataforma incrementa a versão ao
salvar, a partir da que está no campo **Versão**:

| O que mudou no YAML | Versão | Exemplo |
|---|---|---|
| alguma linha com `type`, `required` ou `removed` entrou, saiu ou mudou — o que inclui acrescentar ou retirar um campo | sobe o primeiro número | 1.2.0 → 2.0.0 |
| só linhas com `description`, `title` ou `example` | sobe o segundo número | 1.2.0 → 1.3.0 |
| qualquer outra coisa | sobe o terceiro número | 1.2.0 → 1.2.1 |

Os contratos de dados usam sempre a versão atual do schema: editar um
schema muda o que é exigido em todos os contratos que o usam.

## Excluir um schema

A plataforma não exclui um schema que esteja em uso por algum contrato de
dados: exclua ou altere os contratos antes.
