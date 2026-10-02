---
layout: default
title: "Preencher pelo Formulário"
toc: true
---
# Preencher pelo Formulário

O formulário é um dos três canais por onde a instituição envia microdados ao
CCV, ao lado do Coletor e da [planilha]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/enviar-planilha). Em vez de montar
um arquivo, o operador preenche os registros de um contrato de dados direto
na plataforma, num rascunho, e envia quando terminar.

Esta tela é só do perfil Operador de Área Temática: no menu, em
**Microdados → Preencher pelo Formulário**, ou pelo card **Preencher pelo
Formulário** do Painel. O operador trabalha nos contratos da área temática do
seu perfil, em nome da instituição do perfil.

## Escolher o contrato

A tela lista os contratos de dados da sua área cujo ciclo de coleta está
ativo e que podem ser preenchidos pelo formulário. Para cada um, a tabela
traz o ciclo, se há rascunho em andamento e o prazo: "No prazo", ou a
mensagem que diz por que o ciclo não aceita envio agora (ver
[O prazo](#o-prazo)).

![Contratos disponíveis no formulário]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/preencher-pelo-formulario/contratos.png)

Na coluna **Ação**:

- o ícone de edição abre o rascunho em andamento do contrato;
- o ícone **+** cria um rascunho novo. Ele só aparece quando o contrato não
  tem rascunho em andamento e o ciclo está no prazo.

Cada contrato tem no máximo um rascunho em andamento por instituição.

## Criar o rascunho

Se o contrato já tem dados da instituição, a plataforma pergunta como
começar:

- **Partir do dado mais recente**: cada modelo começa com os registros do
  dado mais recente dele, venha do Coletor, da planilha ou do formulário.
  Modelo sem dado começa vazio. Registros com referência inexistente ou valor
  fora do contrato vigente aparecem como pendência no rascunho.
- **Começar vazio**: o rascunho começa sem registros.

Se o contrato já tem dados enviados por outro canal, a mesma janela avisa que
o envio do rascunho vai substituí-los.

![Escolha de como começar o rascunho]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/preencher-pelo-formulario/criar-rascunho.png)

Contrato sem dado nenhum cria o rascunho vazio direto, sem perguntar. Criado
o rascunho, a tela dele abre em seguida.

## Preencher os registros

A tela do rascunho mostra o status, quando ele foi criado e enviado, e a
versão do contrato. Cada modelo do contrato é uma aba, com o número de
registros ao lado do nome.

![Rascunho de um contrato, no prazo]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/preencher-pelo-formulario/rascunho.png)

Na tabela de cada aba, **Novo registro** abre o formulário de um registro
novo; na coluna **Ação**, os ícones editam e excluem o registro da linha.

O bloco **Filtros** procura registros na aba. A **Busca livre** procura nos
campos de texto; abaixo dela vem um filtro por campo do modelo — texto por
"contém", data por intervalo ("de" e "até"), lista de opções e cadastro pela
mesma lista do formulário. Campo numérico só tem filtro quando é a chave do
registro, um identificador ou um ano, e aí num campo só, pelo valor exato.
Valores e quantidades — em reais, consumo, totais — não têm filtro, mas a
coluna deles continua ordenável.

### Buscar pessoa

Nos modelos em que o contrato prevê, o formulário do registro abre com o
campo **Buscar pessoa**, acima dos demais. Digite ao menos 3 caracteres do
nome, do SIAPE ou do CPF de um servidor, ou da matrícula ou do CPF de um
estudante. A lista traz as pessoas da instituição do seu perfil: servidores
ativos e matrículas atendidas, com nome, SIAPE ou matrícula, a categoria do
servidor ou o curso do estudante, a unidade e o CPF parcialmente escondido.

![Busca de pessoa no formulário de um registro]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/preencher-pelo-formulario/buscar-pessoa.png)

Escolher uma pessoa preenche o CPF, a matrícula, a categoria e, quando o
modelo tem, o nome. Os campos continuam editáveis, e nada é gravado até
**Salvar**. Quando a categoria já está escolhida, a busca procura só nela;
numa categoria que a busca não atende, como "externo", ela fica desabilitada
e um aviso pede para digitar os campos.

Sem resultado, a lista diz "Nenhuma pessoa encontrada" — ou, quando a
instituição não tem ninguém publicado, "Nenhum servidor publicado para a
instituição" ou "Nenhuma matrícula atendida publicada". Para conferir um
código fora do formulário, use as [Consultas]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/consultas).

Quando há registros que o envio não aceitaria — referência para um registro
que não existe, ou valor fora do que o contrato vigente permite —, a tela
avisa no topo e lista cada um na seção **Pendências**, abaixo da tabela.
Corrija-os antes de enviar.

## Enviar o rascunho

**Enviar** pede confirmação. Os registros são validados contra o contrato e,
se passarem, viram os dados deste contrato no CCV e **substituem** os
enviados antes, por qualquer canal. Enquanto a validação roda, o rascunho
fica somente leitura, e a tela se atualiza sozinha quando ela termina.

| Status | O que significa |
|---|---|
| Aberto | em edição; também é o status de volta quando o envio é recusado |
| Enviado e Validando | em validação; somente leitura |
| Concluído | publicado; os dados seguem para a [homologação da área]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/fila-de-homologacao) |
| Erro | a validação não pôde ser concluída; os registros continuam editáveis |
| Descartado | descartado; nenhum dado dele chegou ao CCV |

Quando o envio é recusado, o rascunho volta a Aberto com o relatório da
validação abaixo da tabela: corrija os registros apontados e envie de novo.

## Descartar o rascunho

Enquanto o rascunho está Aberto ou com Erro, **Descartar rascunho** pede
confirmação e descarta o rascunho com todos os registros dele. Nenhum dado
dele chega ao CCV, e a ação não pode ser desfeita. Descartar vale também fora
do prazo.

## O prazo {#o-prazo}

O rascunho segue o prazo do ciclo de coleta, o mesmo do Coletor e da
planilha: as datas do ciclo e, quando existe, o período de correção, cada
dia até 23:59 no horário de Recife. A regra completa está em
[Ciclos de Coleta]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/ciclos-de-coleta#o-prazo-de-envio).

Fora do prazo, a lista de contratos mostra na coluna **Prazo** a mensagem do
caso — "O ciclo de coleta ainda não começou.", "O prazo de coleta e correção
deste ciclo já encerrou." ou "O ciclo de coleta está inativo." — e não
oferece rascunho novo. Dentro do rascunho, um aviso com a mesma mensagem
explica que os registros só podem ser lidos e o rascunho, descartado:
**Enviar** e **Novo registro** ficam desabilitados, e editar e excluir
registro deixam de aparecer.

![Rascunho fora do prazo do ciclo]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/preencher-pelo-formulario/rascunho-fora-do-prazo.png)

Uma validação que começou dentro do prazo termina mesmo depois dele. Um
rascunho que volta a Aberto ou vai a Erro depois do prazo só pode ser lido e
descartado.

Quando o ciclo de coleta é inativado, os rascunhos Aberto e Erro do ciclo são
descartados (ver
[Inativar um ciclo]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/ciclos-de-coleta#inativar-um-ciclo)).
