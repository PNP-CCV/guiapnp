---
layout: default
title: "Inconsistências"
toc: true
---
# Inconsistências

A tela lista, numa tabela só, as **inconsistências** que a plataforma
marcou nos dados — em cursos, ciclos, matrículas, servidores e unidades
organizacionais —, uma por linha, com o tipo, a situação e o registro a
que cada uma se refere. É uma tela de consulta: aqui não se corrige, não
se justifica e não se conclui nada.

A correção acontece nas telas do grupo **Inconsistências** do menu, que
mostram os registros com as inconsistências de cada um e onde cada perfil
corrige a sua parte:

- [Inconsistências de Ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino),
  para cursos, ciclos e matrículas;
- [Inconsistências de Gestão de Pessoas]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas),
  para unidades organizacionais e servidores.

No menu, a tela fica em **Dados Institucionais → Inconsistências** e
aparece para Registrador Acadêmico, Executor Acadêmico, Pesquisador
Institucional, Reitor, Gestão de Pessoas, Recursos Humanos, Suporte CCV e
Administrador. O card **Inconsistências** do Painel leva à mesma tela,
para os mesmos perfis. O Gestor CCV não tem esta tela: ele acompanha a
rede pelas telas de monitoramento, como
[Monitorar Inconsistências do Ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/monitorar-inconsistencias-do-ensino).

Só o Administrador edita a situação e importa inconsistências; os demais
perfis consultam.

## Quando a tela abre

A tela só abre durante o **período de correção**, para todos os perfis,
inclusive o Administrador. Fora dele, o card do Painel fica desabilitado
e quem tenta abrir a tela volta ao Painel.

## O que cada perfil vê

- **Registrador Acadêmico** e **Executor Acadêmico** veem as
  inconsistências de ensino da sua unidade;
- **Pesquisador Institucional** vê as inconsistências de ensino da sua
  instituição;
- **Gestão de Pessoas** e **Recursos Humanos** veem as inconsistências de
  gestão de pessoas da sua instituição;
- **Reitor** vê todas as inconsistências da sua instituição;
- **Suporte CCV** e **Administrador** veem as da rede inteira.

O detalhe de uma inconsistência segue o mesmo alcance: fora dele, a
inconsistência não abre.

## Ver as inconsistências

Cada linha da tabela mostra o ano-base (**Configuração**), a unidade, o
tipo da inconsistência e a **Situação** — em que ponto do caminho de
correção ela está, de *Inconsistente* a *Validado*, em cada etapa
(RA, PI e RE). O caminho está explicado em
[Inconsistências de Ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino#o-caminho-de-uma-inconsistencia).

As colunas seguintes dizem se a inconsistência está **Ignorada**, se o
registro já tinha sido alterado antes (**Alteração Anterior**) e a que
ela se refere: **Objeto** é o tipo do registro — curso, ciclo,
matrícula, servidor ou unidade organizacional —, e **Referência** e
**Identificador** apontam qual é o registro. Na coluna **Ação**, o botão
de visualizar abre o detalhe.

O bloco **Filtros** filtra por **Situação da Inconsistência** e por
**Tipo de Inconsistência**, e o campo **Código/Matrícula da Referência**
busca pelo código do curso, do ciclo, da matrícula ou da unidade
organizacional, ou pela matrícula do servidor.

![Listagem geral de inconsistências, com os botões Editar situação e Importar do Administrador]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/inconsistencias/lista.png)

## Ver o detalhe

O botão de visualizar abre a página da inconsistência, em três blocos:

- **Dados Gerais**: o tipo, o ano-base, a situação, a data em que a
  inconsistência foi gerada, se está ignorada e se houve alteração
  anterior;
- **Responsáveis**: quem validou e quando, em cada etapa — RA, PI e RE.
  Enquanto uma etapa não foi concluída, os dois campos dela mostram N/A;
- **Referência**: o registro a que a inconsistência se refere, com o ID,
  o tipo e o identificador.

![Detalhe de uma inconsistência validada pelo Registrador Acadêmico]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/inconsistencias/detalhe.png)

## Editar a situação

Só o Administrador edita a situação, e a edição sempre **volta** a
inconsistência a uma etapa anterior do caminho. Cada situação tem um
único destino possível:

| Situação atual | Volta para |
|---|---|
| Alterado RA | Inconsistente RA |
| Validado RA | Alterado RA |
| Inconsistente PI | Validado RA |
| Alterado PI | Alterado RA |
| Validado PI | Validado RA |
| Alterado RE | Validado PI |
| Validado RE | Validado PI |

*Inconsistente RA* e *Inconsistente RE* não têm para onde voltar: filtradas
por uma delas, a tela avisa que a situação não permite alterações.

Para editar várias linhas de uma vez:

1. Em **Filtros**, escolha a **Situação da Inconsistência** e clique em
   **Filtrar**. Até lá, a tela avisa que é preciso filtrar por uma
   situação.
2. Marque as linhas na tabela e clique em **Editar situação**.
3. Na janela, marque a situação de destino e clique em **Editar**.

O botão de editar da coluna **Ação** faz o mesmo para uma linha só, sem
precisar do filtro. A plataforma processa a alteração em segundo plano.

![Janela de edição de situação: de Validado RA, a inconsistência só pode voltar para Alterado RA]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/inconsistencias/editar-situacao.png)

## Importar inconsistências

O botão **Importar**, também só do Administrador, recebe uma planilha
`.xlsx` ou `.xls` que manda a plataforma gerar inconsistências em
registros escolhidos. A janela tem o link para baixar o arquivo modelo,
com as colunas:

- **objeto**: o tipo do registro, como `curso`, `ciclo` ou `matricula`;
- **campo_identificador** e **identificador**: o campo e o valor que
  encontram o registro — por exemplo, `codigo` e o código do ciclo;
- **inconsistencias**: os números dos tipos de inconsistência a gerar,
  separados por vírgula.

Se alguma linha aponta para um registro ou um tipo de inconsistência que
não existe, a plataforma recusa o arquivo inteiro e lista as linhas com
erro. Aceito, o arquivo é processado em segundo plano.

![Janela de importação de inconsistências]({{site.baseurl}}/assets/img/docs/manual-do-usuario/dados-institucionais/inconsistencias/importar.png)
