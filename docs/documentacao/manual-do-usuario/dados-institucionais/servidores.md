---
layout: default
title: "Servidores"
toc: true
---
# Servidores

A tela lista os servidores da rede com a matrícula SIAPE, o nome, o CPF,
a lotação, o cargo e a situação funcional. É sobre esses servidores que a
plataforma aponta as
[inconsistências de gestão de pessoas]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas).

No menu, a tela fica em **Dados Institucionais → Servidores** e aparece
para Gestão de Pessoas, Recursos Humanos, Reitor, Gestor CCV e
Administrador. Só o Administrador e o Gestor CCV cadastram, editam,
excluem e importam servidores; os demais perfis consultam.

## O que cada perfil vê

- **Gestão de Pessoas**, **Recursos Humanos** e **Reitor** veem os
  servidores lotados na sua instituição;
- **Gestor CCV** e **Administrador** veem os da rede inteira.

## Ver os servidores

A tabela mostra a situação, a lotação (o código da unidade organizacional,
o campus e a sigla da instituição), a matrícula, o nome, o sexo, o CPF e a
data de nascimento. Na coluna **Ação**, os botões abrem o detalhe e, para
o Administrador e o Gestor CCV, a edição e a exclusão.

O bloco **Filtros** busca por palavra-chave, no nome, no CPF ou na
matrícula, e filtra por sexo, situação, lotação, cargo, jornada de
trabalho, escolaridade, titulação, RSC e classe.

![Listagem de servidores, com os botões Cadastrar e Importar]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/servidores/lista.png)

## Ver o detalhe

O botão de visualizar abre a página do servidor, com os **Dados Gerais**
— matrícula, nome, sexo, CPF, situação e data de nascimento — e o
**Detalhamento**: lotação, jornada, escolaridade, titulação, RSC, cargo e
classe. Para o Administrador e o Gestor CCV, o botão **Editar**, no alto,
abre o mesmo formulário da edição.

![Detalhe de um servidor]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/servidores/detalhe.png)

## Cadastrar e editar

O botão **Cadastrar**, acima da tabela, abre o formulário. São
obrigatórios:

- **Matrícula**, **Nome** e **Sexo**;
- **CPF**, com 11 dígitos;
- **Situação** e **Data de Nascimento**;
- **Lotação**, **Jornada de Trabalho** e **Cargo**.

Escolaridade, titulação, RSC e classe são opcionais — o formulário marca
esses campos com "(Opcional)". A edição usa o mesmo formulário, já
preenchido.

![Formulário de cadastro de servidor]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/servidores/cadastrar.png)

## Importar servidores

O botão **Importar** recebe uma planilha `.xlsx` no formato do extrato de
servidores, com colunas como ÓRGÃO, NOME SERVIDOR, CPF, CARGO, LOTAÇÃO e
JORNADA. A plataforma recebe o arquivo e o processa em segundo plano.

![Janela de importação de servidores]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/servidores/importar.png)

## Excluir um servidor

O botão de excluir, na coluna **Ação**, pede confirmação antes de
excluir o servidor.
