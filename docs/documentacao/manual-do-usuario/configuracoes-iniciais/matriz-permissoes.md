---
layout: default
title: "Matriz de Permissões"
toc: true
---
# Matriz de Permissões

A Matriz de Permissões mostra, numa única tabela, o que cada perfil de
acesso da PNP pode fazer na plataforma: em cada linha, uma capacidade (uma
ação ou uma área do sistema); em cada coluna, um perfil. O cruzamento diz
se aquele perfil tem aquela capacidade.

Esta tela é restrita: só aparece no menu para o perfil Administrador, e só
abre de fato para quem é superusuário da plataforma — quem não for
superusuário é redirecionado para o Painel ao tentar acessá-la.

## Ler os três estados

Cada célula da tabela mostra um dos três estados, explicados na legenda no
topo da tela:

- **Permitido** — o perfil tem a capacidade, sem condição.
- **Condicional** — a própria tela explica: "depende do contexto em tempo
  de execução". São seis capacidades marcadas assim: Gestão acadêmica,
  Resolver inconsistência, Concluir inconsistências, Restaurar, Homologar
  microdados e Aprovar microdados (Reitor). Ter a capacidade condicional
  não garante a ação em qualquer situação — o sistema ainda confere o
  contexto (por exemplo, a que instituição, unidade ou registro a ação se
  aplica) no momento em que ela é executada.
- **—** — o perfil não tem a capacidade.

![Legenda e início da tabela da Matriz de Permissões]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/matriz-permissoes/tabela.png)

A tabela é mais larga do que a tela: a figura acima mostra a legenda e as
primeiras colunas e linhas, mas a tela tem mais perfis à direita e mais
capacidades abaixo do que a figura consegue mostrar — role a tabela para o
lado e para baixo para ver o restante.

## Os 15 perfis

A tabela a seguir resume o que a matriz concede a cada perfil, com o nome
de cada um exatamente como a tela o exibe. Perfis com muitas capacidades
têm a lista resumida por área. A coluna Vínculo diz por onde o perfil se
liga à estrutura da rede — veja o que isso significa em
[Alcance de cada perfil](#alcance-de-cada-perfil), logo abaixo da tabela.

| Perfil | Vínculo | O que a matriz concede |
| --- | --- | --- |
| Gestor CCV | Nenhum (alcance nacional) | Quase tudo: gerir arquivos institucionais, cadastros gerais, estrutura institucional e chaves de integração; gerir e consultar microdados; consultar pessoas, cadastrar pessoas, atribuir papéis e baixar arquivos de pessoas; acesso ao portal; e Gestão acadêmica (condicional). |
| Suporte CCV | Nenhum (alcance nacional) | Como o Gestor CCV nas pessoas (consultar, cadastrar, atribuir papéis, baixar arquivos) e em arquivos institucionais (só consulta) e chaves de integração, além de consultar microdados e acesso ao portal — mas sem gerir cadastros gerais, estrutura institucional, microdados nem Gestão acadêmica. |
| Gestor Setec | Nenhum (alcance nacional) | Gerir conteúdos, gerir grupos de conteúdo, provisionar Operador SETEC e acesso ao portal. |
| Gestor Rede | Instituição (mas alcance nacional — veja a nota abaixo) | Só acesso ao portal. |
| Operador SETEC | Nenhum (alcance nacional) | Só gerir conteúdos. |
| Reitor | Instituição | Consultar arquivos institucionais; consultar pessoas, cadastrar pessoas, atribuir papéis e baixar arquivos de pessoas; acesso ao portal; e, como condicionais, Gestão acadêmica, Resolver/Concluir/Restaurar inconsistências e Aprovar microdados (Reitor). |
| Pesquisador Institucional | Instituição | O mesmo que o Reitor, exceto Aprovar microdados (Reitor). |
| Gestão de Pessoas | Instituição | Consultar pessoas, cadastrar pessoas e atribuir papéis; e, como condicionais, Resolver, Concluir e Restaurar inconsistências. Não tem acesso ao portal marcado nesta matriz — veja por quê logo abaixo da tabela. |
| Recursos Humanos | Instituição | Consultar e cadastrar pessoas; e, como condicional, Resolver inconsistência. |
| Registrador Acadêmico | Unidade | Consultar pessoas, cadastrar pessoas e atribuir papéis; e, como condicionais, Gestão acadêmica e Resolver/Concluir/Restaurar inconsistências. |
| Executor Acadêmico | Unidade | Consultar pessoas; e, como condicionais, Gestão acadêmica e Resolver/Restaurar inconsistências. |
| Gestor de Área Temática | Instituição e área temática | Só Homologar microdados (condicional). |
| Pró-Reitor | Instituição | Nenhuma capacidade aparece marcada para este perfil nesta matriz — veja por quê logo abaixo da tabela. |
| Diretor Executivo | Instituição | Nenhuma capacidade aparece marcada para este perfil nesta matriz — veja por quê logo abaixo da tabela. |
| Diretor-Geral | Unidade | Nenhuma capacidade aparece marcada para este perfil nesta matriz — veja por quê logo abaixo da tabela. |

Três perfis — Pró-Reitor, Diretor Executivo e Diretor-Geral — fazem parte
da estrutura de governança da rede, e existem na PNP para registrar quem
ocupa cada cargo, não para conceder acesso ao sistema. A linha vazia deles
na matriz é o estado esperado, não uma falha de cadastro. O Diretor-Geral
é o único dos três cujo vínculo já recorta dados normalmente (por unidade,
do mesmo jeito que o Registrador Acadêmico) — falta só a capacidade em si,
que ainda não foi concedida a esse perfil.

A capacidade "Acesso ao portal" é concedida a uma lista fechada de
perfis — Gestor CCV, Suporte CCV, Gestor Setec, Gestor Rede, Reitor e
Pesquisador Institucional —, além do superusuário. Gestão de Pessoas e
Recursos Humanos não aparecem com essa capacidade porque não fazem parte
dessa lista, não por omissão no cadastro.

## Alcance de cada perfil {#alcance-de-cada-perfil}

Cinco perfis têm alcance nacional: o que a matriz concede a eles vale
para a rede inteira, e não para uma instituição, unidade ou área temática
específica. São eles: Gestor CCV, Suporte CCV, Gestor Setec, Gestor
Rede e Operador SETEC.

Os demais perfis são vinculados por instituição, por unidade, ou pelas
duas coisas ao mesmo tempo — instituição e área temática, no caso do
Gestor de Área Temática —, e é esse vínculo que recorta o que a pessoa
enxerga: mesmo tendo uma capacidade concedida pela matriz, ela só a
exerce sobre os dados aos quais está vinculada. A coluna Vínculo da
tabela acima mostra o caso de cada perfil.

O Gestor Rede é um caso à parte: por trás da tela, o perfil registra
uma instituição — a que identifica a rede à qual ele pertence —, mas
isso não limita o que ele enxerga. O alcance dele continua nacional,
igual aos outros quatro perfis sem vínculo. Para quem usa a plataforma,
o que importa é isso: o Gestor Rede vê a rede inteira, apesar de ter
uma instituição registrada.
