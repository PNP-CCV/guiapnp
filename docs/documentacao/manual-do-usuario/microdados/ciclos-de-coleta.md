---
layout: default
title: "Ciclos de Coleta"
toc: true
---
# Ciclos de Coleta

O ciclo de coleta é a janela anual em que as instituições enviam
microdados: o ano e as datas de início e de fim. Cada contrato de dados
pertence a um ciclo (ver [Contratos de Dados]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/contratos-de-dados)).

Esta tela está disponível para os perfis Administrador, Gestor CCV e
Suporte CCV. Cadastrar, editar e excluir ciclos é só do Administrador e do
Gestor CCV; o Suporte CCV apenas consulta.

## Ver os ciclos cadastrados

Em **Microdados → Ciclos de Coleta**, a plataforma lista os ciclos já
cadastrados, com o ano, o status (Ativa ou Inativa) e as datas de cada um:
início, fim, envio e o início e o fim do período de correção. A busca do
bloco **Filtros** procura pelo status do ciclo.

![Listagem de ciclos de coleta]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/ciclos-de-coleta/lista.png)

## Cadastrar um ciclo

O botão **Cadastrar**, no canto superior direito da lista, abre o
formulário de cadastro, dividido em **Informações Gerais**, **Datas do
Ciclo** e **Período de Correção**. Ano, Status, Data de Início e Data de
Fim são obrigatórios; a data de envio pode ficar em branco, e as duas
datas do período de correção também, desde que juntas.

![Formulário de cadastro de ciclo de coleta]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/ciclos-de-coleta/cadastrar.png)

Três regras valem ao salvar, no cadastro e na edição:

- **Só um ciclo pode estar ativo.** Se já houver um ciclo com status Ativa,
  a plataforma recusa um segundo com a mensagem "Já existe um ciclo ativo.
  Inative-o antes." — edite o ciclo atual para Inativa primeiro.
- **A data de fim não pode ser anterior à de início.**
- **O período de correção tem as duas datas, ou nenhuma,** e a de fim não
  vem antes da de início. Com uma só, a plataforma pede a que falta — inclusive
  ao editar um ciclo antigo para inativá-lo.

## O prazo de envio {#o-prazo-de-envio}

As datas do ciclo ativo são o prazo dos três canais por onde a instituição
envia microdados: o Coletor, a tela [Enviar Planilha]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/enviar-planilha) e a
tela [Preencher pelo Formulário]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/preencher-pelo-formulario). A regra é a
mesma nos três:

- antes da Data de Início, o envio é recusado com "O ciclo de coleta ainda
  não começou.";
- da Data de Início até a Data de Fim, inclusive, o envio é aceito;
- depois da Data de Fim, o envio só é aceito dentro do período de correção,
  quando ele está preenchido, das duas datas inclusive. Entre o fim do ciclo
  e o início da correção, e depois do fim da correção, o envio é recusado com
  "O prazo de coleta e correção deste ciclo já encerrou.";
- com o ciclo inativo, o envio é recusado com "O ciclo de coleta está
  inativo.".

Cada data vale pelo dia inteiro, até 23:59, no horário de Recife. A data de
envio não entra nessa conta.

O prazo não inativa o ciclo: ele continua ativo até alguém inativá-lo. Uma
validação que começou dentro do prazo termina e publica mesmo que acabe
depois dele. Para reabrir o envio nos três canais, estenda a data de fim do
período de correção.

## Inativar um ciclo {#inativar-um-ciclo}

Para inativar o ciclo, edite-o — pelo ícone de edição na lista ou pelo
detalhe do ciclo — e mude o Status de Ativa para Inativa. Ao salvar, antes
de gravar, a plataforma abre a confirmação **Inativar ciclo de coleta** com o
que a inativação afeta:

- quantos rascunhos de [Preencher pelo Formulário]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/preencher-pelo-formulario)
  serão descartados, e de quantas instituições;
- quantos rascunhos do formulário estão em validação;
- quantos envios de planilha do ciclo estão em andamento;
- quantos datasets enviados pelo Coletor estão em validação.

![Confirmação da inativação de um ciclo de coleta]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/ciclos-de-coleta/inativar.png)

**Inativar ciclo** grava a mudança e descarta, na mesma hora, os rascunhos
contados. Os operadores das instituições não recebem aviso. **Cancelar**
volta ao formulário de edição sem mudar nada.

> **⚠️ O descarte não tem volta**
>
> Os rascunhos descartados não voltam, nem se o ciclo for reativado. Nenhum
> dado deles chega ao CCV.

Se, entre a confirmação e a gravação, surgirem mais rascunhos a descartar, a
plataforma não inativa o ciclo: a confirmação volta com os números novos e
pede de novo.

### Quando a inativação precisa esperar

Um rascunho do formulário em validação, um envio de planilha em andamento ou
um dataset do Coletor em validação impedem a inativação. Nesse caso a
confirmação mostra as contagens, explica que é preciso esperar o veredito da
validação e só oferece **Fechar**.

![Confirmação que pede para esperar o fim da validação]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/ciclos-de-coleta/inativar-bloqueada.png)

A validação termina sozinha; tente inativar de novo depois. Enquanto isso o
ciclo continua ativo.

## Excluir um ciclo

A plataforma não exclui um ciclo ativo: o ícone de exclusão não aparece
na linha dele. Para excluir, inative o ciclo antes.

A confirmação da exclusão avisa o que será apagado junto e quantos
contratos de dados estão vinculados ao ciclo naquele momento.

> **⚠️ Excluir um ciclo apaga o que depende dele**
>
> Os contratos de dados do ciclo são excluídos junto, e com eles todos os
> datasets recebidos para esses contratos — inclusive os já homologados ou
> aprovados. Não há como desfazer.
