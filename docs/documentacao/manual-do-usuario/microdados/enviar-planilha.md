---
layout: default
title: "Enviar Planilha"
toc: true
---
# Enviar Planilha

A planilha é um dos três canais por onde a instituição envia microdados ao
CCV, ao lado do Coletor e do [formulário]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/preencher-pelo-formulario). O
operador baixa a planilha-modelo de um contrato de dados, preenche e envia o
arquivo; a plataforma valida contra o contrato e devolve um relatório.

Esta tela é só do perfil Operador de Área Temática: no menu, em
**Microdados → Enviar Planilha**, ou pelo card **Enviar Planilha** do Painel.
O operador envia para os contratos da área temática do seu perfil, em nome da
instituição do perfil.

## Enviar uma planilha

Em **Contrato de dados**, escolha o contrato. A lista traz os contratos da
sua área cujo ciclo de coleta está ativo; sem nenhum, a tela avisa "Nenhum
contrato da sua área com ciclo de coleta ativo.".

![Tela de envio, com o contrato escolhido e os envios da instituição]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/enviar-planilha/envio.png)

**Baixar planilha-modelo** baixa um arquivo XLSX com uma aba por modelo do
contrato — o cabeçalho e linhas de exemplo — e uma aba de instruções.

Em **Planilha**, escolha o arquivo: .xlsx ou .ods, de até 50 MB, com uma aba
por modelo do contrato e o nome de cada aba igual ao da planilha-modelo.
**Enviar** fica habilitado quando há contrato e arquivo escolhidos e o ciclo
está no prazo. Recebida a planilha, a validação começa e o envio aparece em
**Meus envios**.

## Acompanhar os envios

**Meus envios** lista os envios da sua instituição para a sua área, do mais
recente ao mais antigo, com o contrato, o arquivo, quando foi enviado e o
status. Enquanto há envio em validação, a lista se atualiza sozinha.

| Status | O que significa |
|---|---|
| Recebido e Validando | em validação; o envio ainda pode ser cancelado |
| Aprovado | passou na validação; os dados seguem para a [homologação da área]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/fila-de-homologacao) |
| Rejeitado | a validação encontrou erros; a coluna **Erros** diz quantos |
| Erro | a validação não pôde ser concluída; envie de novo |
| Cancelado | cancelado pelo operador; nenhum dado chegou ao CCV |

Na coluna **Ação**, o ícone de olho abre o relatório do envio, e o **X**
cancela um envio Recebido ou Validando.

## Cancelar um envio

O cancelamento pede confirmação. A validação é interrompida e a planilha,
apagada; nenhum dado do envio chega ao CCV, e a ação não pode ser desfeita.

![Confirmação do cancelamento de um envio]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/enviar-planilha/cancelar.png)

Cancelar vale também fora do prazo do ciclo.

## Ler o relatório

O relatório mostra o contrato, o arquivo, quem enviou, quando e o status. De
um envio Aprovado, ele lista os datasets gerados, um por modelo, com o status
e o número de linhas de cada um.

![Relatório de um envio rejeitado]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/enviar-planilha/relatorio.png)

**Relatório da validação** agrupa o que a validação encontrou por modelo.
Cada item tem a marca **Erro** ou **Aviso**, o campo, o motivo e exemplos das
linhas afetadas. Só erro faz a planilha ser rejeitada; aviso não.

Quando a validação aponta linhas com erro, **Baixar relatório completo
(XLSX)** baixa todas elas, uma aba por modelo. O relatório completo fica só no
envio mais recente de cada contrato; nos anteriores, a tela avisa que ele não
está mais disponível.

## O prazo

O envio de planilha segue o prazo do ciclo de coleta, o mesmo do Coletor e do
formulário: as datas do ciclo e, quando existe, o período de correção, cada
dia até 23:59 no horário de Recife. A regra completa está em
[Ciclos de Coleta]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/ciclos-de-coleta#o-prazo-de-envio).

Fora do prazo, ao escolher o contrato, a tela mostra um aviso com a mensagem
do caso — "O ciclo de coleta ainda não começou.", "O prazo de coleta e
correção deste ciclo já encerrou." ou "O ciclo de coleta está inativo." — e
**Enviar** fica desabilitado. Envios em andamento ainda podem ser cancelados.

![Envio de planilha fora do prazo do ciclo]({{site.baseurl}}/assets/img/docs/manual-do-usuario/microdados/enviar-planilha/fora-do-prazo.png)

Uma planilha recebida dentro do prazo termina a validação mesmo depois dele.

Enquanto houver envio de planilha em andamento no ciclo, o ciclo não pode ser
inativado (ver [Inativar um ciclo]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/ciclos-de-coleta#inativar-um-ciclo)).
