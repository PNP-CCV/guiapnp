---
layout: default
title: "Gerenciamento de Usuários"
toc: true
---
# Gerenciamento de Usuários

Aqui se cadastram as pessoas que usam a plataforma e se atribuem e retiram
os papéis delas. O papel é o que define o acesso: cada papel vale numa
instituição, numa unidade, numa área temática ou na rede inteira, e uma
mesma pessoa pode ter vários.

No menu, a tela fica em **Central de Atividades → Gerenciamento de
Usuários**, e o card **Gerenciamento de Usuários** do Painel também leva a
ela. Aparece para Administrador, Gestor CCV, Suporte CCV, Reitor,
Pesquisador Institucional, Gestão de Pessoas, Registrador Acadêmico, Gestor
Setec e Gestor de Área Temática. Cada perfil vê só as pessoas do seu alcance e atribui só
alguns papéis — as duas coisas estão nas seções abaixo.

## Quem aparece na lista

A lista mostra as pessoas que têm algum papel dentro do alcance do perfil
com que você está na sessão:

| Perfil | Vê as pessoas que são |
|---|---|
| Administrador, Gestor CCV e Suporte CCV | todas as pessoas cadastradas |
| Reitor | Pesquisador Institucional, Gestão de Pessoas, Recursos Humanos, Gestor e Operador de Área Temática, Pró-Reitor e Diretor Executivo na sua instituição; Registrador Acadêmico, Executor Acadêmico e Diretor-Geral nas unidades dela |
| Pesquisador Institucional | Gestão de Pessoas, Recursos Humanos, Gestor e Operador de Área Temática, Gestor Rede, Pró-Reitor e Diretor Executivo na sua instituição; Registrador Acadêmico, Executor Acadêmico e Diretor-Geral nas unidades dela |
| Gestão de Pessoas | Gestão de Pessoas, Recursos Humanos, Pró-Reitor e Diretor Executivo na sua instituição; Diretor-Geral nas unidades dela |
| Registrador Acadêmico | Registrador Acadêmico, Executor Acadêmico e Diretor-Geral na sua unidade |
| Gestor Setec | Operador SETEC |
| Gestor de Área Temática | Operador de Área Temática na sua instituição e na sua área temática |

Quem entra na lista aparece com todos os papéis que tem, não só com os
que o trouxeram para ela.

## A lista de usuários

A tabela traz o **CPF**, o **Nome**, o **E-mail**, a **Capacitação** (se a
pessoa concluiu a capacitação da plataforma, que as telas de correção de
[inconsistências]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino) exigem
de alguns perfis), o **Cadastro** (se está ativo), os **Papéis** e o
**Telefone**. Cada papel vem numa etiqueta com o lugar dele — a
instituição, a unidade ou a área temática. Quando a pessoa tem mais de dois
papéis, a célula mostra os dois primeiros e um **+N** com quantos faltam; a
lista completa está no detalhe.

![Lista de usuários vista pelo Administrador]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/gerenciamento-de-usuarios/lista.png)

A figura foi feita numa tela larga. Em telas mais estreitas, a tabela rola
para a direita e a coluna **Ação** fica fixa, por cima das últimas colunas
— o **Telefone** aparece rolando.

O bloco **Filtros** recorta a lista:

- **Busca** — procura pelo nome ou pelo CPF;
- **Instituição** e **Unidade**, escolhidas numa lista;
- **Capacitação** e **Cadastro** — *Sim* ou *Não*;
- **Papel** — só os papéis que o seu perfil enxerga.

Na coluna **Ação**, os ícones de cada linha são:

- **Visualizar** (olho) — abre o detalhe da pessoa;
- **Editar** — altera os dados cadastrais; aparece para Administrador,
  Gestor CCV, Suporte CCV, Pesquisador Institucional e Gestor de Área
  Temática
  ([Editar os dados de uma pessoa](#editar-os-dados-de-uma-pessoa));
- **Excluir** — aparece para Administrador, Gestor CCV e Suporte CCV
  ([Excluir uma pessoa](#excluir-uma-pessoa));
- **Adicionar papel** — atribui mais um papel à pessoa
  ([Atribuir um papel](#atribuir-um-papel));
- **Acessar como este usuário** — só para o Administrador, quando a
  impersonação está ligada no ambiente, e só nas pessoas que têm papel de
  Reitor, Pró-Reitor, Diretor Executivo, Pesquisador Institucional, Gestão
  de Pessoas, Recursos Humanos, Diretor-Geral, Registrador Acadêmico,
  Executor Acadêmico, Gestor de Área Temática ou Operador de Área Temática.
  A sessão só abre se **todos** os papéis da pessoa estiverem nessa lista;
  senão, a janela avisa "Pessoa não elegível para uma sessão de suporte.".
  Abre uma sessão de suporte, registrada em
  [Sessões de suporte]({{site.baseurl}}/documentacao/manual-do-usuario/configuracoes-iniciais/sessoes-de-suporte).

Para um Reitor, a mesma tela mostra só as pessoas da sua instituição, sem
**Importar** e, na coluna **Ação**, só o detalhe e o **Adicionar papel**:

![Lista de usuários vista por um Reitor]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/gerenciamento-de-usuarios/lista-reitor.png)

## Quem atribui e retira cada papel {#quem-atribui-e-retira-cada-papel}

Cada perfil atribui só alguns papéis, e só dentro do próprio alcance. A
mesma regra vale para retirar:

| Perfil | Atribui e retira |
|---|---|
| Administrador | todos os papéis |
| Gestor CCV | todos, menos Gestor CCV |
| Suporte CCV | Reitor, Pesquisador Institucional, Gestão de Pessoas, Recursos Humanos, Registrador Acadêmico, Executor Acadêmico, Gestor e Operador de Área Temática, Pró-Reitor, Diretor Executivo e Diretor-Geral, em qualquer instituição |
| Reitor | Pesquisador Institucional, Gestor e Operador de Área Temática, Pró-Reitor, Diretor Executivo e Diretor-Geral, na sua instituição |
| Pesquisador Institucional | Gestor Rede, Gestor e Operador de Área Temática, Gestão de Pessoas, Recursos Humanos, Registrador Acadêmico e Executor Acadêmico, na sua instituição |
| Gestão de Pessoas | Recursos Humanos, na sua instituição |
| Registrador Acadêmico | Executor Acadêmico, na sua unidade |
| Gestor Setec | Operador SETEC |
| Gestor de Área Temática | Operador de Área Temática, na sua instituição e na sua área temática |

Dois papéis mexem em outros ao serem atribuídos ou retirados — é a mesma
regra do **Detalhamento** de [Instituições]({{site.baseurl}}/documentacao/manual-do-usuario/configuracoes-iniciais/instituicoes):

- **Reitor** — a instituição tem um único Reitor. Atribuir o papel a
  alguém tira o de quem era reitor da instituição.
- **Pesquisador Institucional** — quem recebe o papel ganha também o de
  Executor Acadêmico em todas as unidades da instituição. Quem o perde
  perde junto todos os papéis de Executor Acadêmico nas unidades da
  instituição, inclusive os que tenham sido atribuídos à parte.

## Cadastrar uma pessoa

O botão **Cadastrar**, acima da lista, abre o formulário. Ele cadastra a
pessoa já com um papel:

- **CPF**, **Nome** e **Email** são obrigatórios; o CPF precisa ser
  válido. O **Telefone** é opcional e, se preenchido, tem 11 dígitos.
- **Papel** é obrigatório. A lista traz só os papéis que o seu perfil
  atribui (tabela acima).
- **Instituição**, **Unidade** e **Área Temática** se habilitam conforme o
  papel escolhido, e as que se habilitam são obrigatórias. Todo papel pede
  a instituição, menos Gestor CCV, Suporte CCV, Gestor Setec e Operador
  SETEC; Registrador Acadêmico, Executor Acadêmico e Diretor-Geral pedem
  também a unidade, que se habilita depois da instituição; Gestor e
  Operador de Área Temática pedem também a área temática. Para quem não é Administrador,
  Gestor CCV nem Suporte CCV, a instituição oferecida é a sua.

![Formulário de cadastro com o papel Registrador Acadêmico escolhido]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/gerenciamento-de-usuarios/cadastrar.png)

Se o CPF já é de alguém cadastrado, a plataforma não cria outra pessoa:
atribui o papel a quem já existe e mantém o nome, o e-mail e o telefone
dela. Quando essa pessoa está na sua lista, o formulário já traz esses
dados ao digitar o CPF.

## Importar pessoas de uma planilha

O botão **Importar** aparece para Administrador, Gestor CCV e Suporte CCV.
Ele abre o envio de um arquivo, com um link para baixar o **arquivo
modelo**, que tem as colunas Nome, E-mail, CPF, Papel, Instituição e
Unidade. Cada linha cadastra uma pessoa com um papel, pelas mesmas regras
do cadastro: se alguma linha atribui um papel que o seu perfil não
atribui, ou deixa sem instituição ou unidade um papel que precisa delas, o
arquivo inteiro é recusado e nada é gravado.

## Ver o detalhe de uma pessoa

O ícone de olho abre a página da pessoa. Em **Dados Gerais**, ela mostra o
CPF, o nome, o e-mail, o telefone e se a capacitação está concluída e o
cadastro, ativo. Abaixo, a tabela **Papéis** lista cada papel com a
instituição, a unidade e a área temática dele.

![Detalhe de uma pessoa com três papéis]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/gerenciamento-de-usuarios/detalhe.png)

No alto, o botão **Editar** aparece para os mesmos perfis que o ícone de
edição da lista, e **Acessar como este usuário**, nas mesmas condições da
lista.

## Atribuir um papel {#atribuir-um-papel}

O botão **Adicionar papel**, na tabela de papéis do detalhe, e o ícone de
mesmo nome na lista abrem o formulário. Ele tem os mesmos campos **Papel**,
**Instituição**, **Unidade** e **Área Temática** do cadastro, com as
mesmas regras: a lista de papéis traz só os que o seu perfil atribui, e
cada campo de lugar se habilita conforme o papel. O botão **Adicionar** só
se libera quando o que o papel exige está preenchido.

![Formulário de adicionar papel aberto por um Reitor, com os cinco papéis que ele atribui]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/gerenciamento-de-usuarios/adicionar-papel-reitor.png)

## Retirar um papel

Na tabela de papéis do detalhe, o ícone **Remover Papel** aparece na linha
de cada papel que o seu perfil retira. Ele pede confirmação, dizendo qual
papel, e em que lugar, será removido. A remoção não pode ser desfeita; os
outros papéis da pessoa continuam como estão — com a exceção do
Pesquisador Institucional, que leva junto os papéis de Executor
Acadêmico, e o aviso diz isso:

![Confirmação de remoção do papel Pesquisador Institucional]({{site.baseurl}}/assets/img/docs/manual-do-usuario/central-de-atividades/gerenciamento-de-usuarios/remover-pesquisador-institucional.png)

## Editar os dados de uma pessoa {#editar-os-dados-de-uma-pessoa}

O ícone de edição da lista e o botão **Editar** do detalhe abrem o
formulário com o CPF, o nome, o e-mail, o telefone e as marcações
**Capacitação Concluída** e **Cadastro Ativo**. CPF, nome e e-mail são
obrigatórios. Só o Administrador altera o CPF e a capacitação; para os
demais, os dois campos ficam travados.

A plataforma recusa a edição quando:

- a pessoa é Gestor CCV, Suporte CCV ou Gestor Setec, e quem edita não é o
  Administrador nem o Gestor CCV;
- a pessoa não tem papel nenhum, e quem edita não é o Administrador nem o
  Gestor CCV;
- quem edita é Pesquisador Institucional e a pessoa tem algum papel fora
  da instituição dele;
- quem edita é Gestor de Área Temática e a pessoa tem algum papel que não
  seja o de Operador de Área Temática na instituição e na área dele.

## Excluir uma pessoa {#excluir-uma-pessoa}

O ícone de lixeira, para Administrador, Gestor CCV e Suporte CCV, exclui
a pessoa com todos os papéis dela, em todas as instituições. Por isso a
exclusão segue a tabela de [quem retira cada
papel](#quem-atribui-e-retira-cada-papel): só exclui quem poderia retirar
cada papel que a pessoa tem. O Gestor CCV não exclui outro Gestor CCV; o
Suporte CCV não exclui quem é Gestor CCV, Suporte CCV, Gestor Setec,
Operador SETEC ou Gestor Rede. O Administrador exclui qualquer pessoa, e
uma pessoa sem papel nenhum pode ser excluída pelos três.

Para tirar alguém só da sua equipe, sem apagar o cadastro, retire o papel.
