---
layout: default
title: "Cursos"
toc: true
---
# Cursos

A tela lista os cursos que as unidades têm na plataforma, com o tipo, a
modalidade, o eixo e o curso do catálogo a que cada um está associado.
É sobre esses cursos que a plataforma aponta as
[inconsistências de ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino).

No menu, a tela fica em **Dados Institucionais → Cursos** e aparece para
Registrador Acadêmico, Executor Acadêmico, Pesquisador Institucional,
Reitor, Gestor CCV, Suporte CCV e Administrador. Só o Administrador e o
Gestor CCV editam um curso; os demais perfis consultam.

## O que cada perfil vê

- **Registrador Acadêmico** e **Executor Acadêmico** veem os cursos da
  sua unidade;
- **Pesquisador Institucional** e **Reitor** veem os cursos de todas as
  unidades da sua instituição;
- **Gestor CCV**, **Suporte CCV** e **Administrador** veem os cursos da
  rede inteira.

## Ver os cursos

A tabela mostra, para cada curso, o **Código PNP** — o código SISTEC da
unidade seguido do código do curso —, o nome, se é de formação de
professores, se está excluído ou ativo, a unidade, o tipo, a modalidade,
o eixo e o catálogo. A tabela é mais larga que a tela: role para o lado
para ver as últimas colunas.

O bloco **Filtros** busca por palavra-chave, no código ou no nome do
curso, e filtra por modalidade. O Pesquisador Institucional e o Reitor
filtram também pela unidade; o Administrador, pela instituição e pela
unidade.

![Listagem de cursos]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/cursos/lista.png)

## Ações da linha

A última coluna, **Ação**, traz os botões de cada curso:

- **Editar** — para o Administrador e o Gestor CCV;
- **Ativar Curso** — só para o Administrador: ativa as matrículas do
  curso a partir dos dados já carregados da unidade. Curso excluído não
  pode ser ativado;
- **Gerar Inconsistências** — só para o Administrador: confere de novo o
  curso contra as regras de inconsistência de ensino.

![Coluna Ação, no fim da tabela, vista pelo Administrador]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/cursos/acoes.png)

## Editar um curso

O botão **Editar** abre o formulário com o nome, o tipo, a modalidade, o
eixo, o curso do catálogo e as caixas **Ativo** e **Excluído**. Só o
**Nome** é obrigatório, com até 255 caracteres.

![Formulário de edição de curso]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/cursos/editar.png)
