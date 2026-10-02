---
layout: default
title: "Configurações"
toc: true
---
# Configurações

Uma configuração é o ano de coleta: as datas do ano e a janela de correção
das inconsistências. A cada configuração pertencem os arquivos do SISTEC, um
por unidade, com as linhas de matrícula que a plataforma baixa, processa e
transforma em inconsistências. Esta tela cadastra os anos e acompanha a carga
desses arquivos.

Esta tela está disponível só para o perfil Administrador.

## Consultar as configurações

Em **Cadastros Gerais → Configurações**, a plataforma lista um ano por linha,
com:

- **Ano**;
- **Data de Início**, **Data de Fim** e **Data de Envio** — a Data de Envio
  é opcional e aparece como "-" quando não foi preenchida;
- **Data de Início da Correção** e **Data de Fim da Correção** — a janela de
  correção (ver [Cadastrar uma configuração](#cadastrar-uma-configuracao));
- **Arquivos do SISTEC** — a situação da lista de arquivos do ano (ver
  [Arquivos do SISTEC](#arquivos-do-sistec)).

Os **Filtros**, no alto, restringem a lista por intervalo de Data de Início,
de Data de Fim ou de Data de Envio. Na coluna **Ação**, cada linha tem
**Visualizar**, **Editar** e **Excluir**.

![Lista de configurações]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/lista.png)

### Arquivos do SISTEC {#arquivos-do-sistec}

A coluna **Arquivos do SISTEC** mostra em que pé está a lista de arquivos do
ano:

- **Não sincronizada** — a lista ainda não foi buscada no SISTEC;
- **Na fila** e **Consultando o SISTEC…** — a busca foi pedida e está em
  andamento; quando ela começa a criar os arquivos, a célula passa a mostrar
  a porcentagem concluída;
- **7 arquivos**, por exemplo — a busca terminou; ao lado, a data e a hora
  da última sincronização;
- **Falhou** — a busca não terminou; o motivo aparece ao parar o mouse sobre
  a etiqueta.

A sincronização consulta o SISTEC e cria um arquivo para cada unidade cujo
**Código SISTEC** está cadastrado em [Unidades]({{site.baseurl}}/documentacao/manual-do-usuario/configuracoes-iniciais/unidades). Unidade que o
SISTEC devolve sem cadastro correspondente fica sem arquivo, e arquivo que já
existia na configuração não é alterado.

## Cadastrar uma configuração {#cadastrar-uma-configuracao}

Clique em **Cadastrar** e preencha:

- **Ano** — com quatro dígitos;
- **Data de início** e **Data de fim** — a de fim precisa ser posterior à
  de início;
- **Data de envio** — opcional;
- **Data de início da Correção** e **Data de fim da Correção** — a de fim
  precisa ser posterior à de início.

Todos os campos são obrigatórios, exceto a Data de envio. Cada ano tem uma
configuração só.

As correções das inconsistências do ano só são aceitas entre a Data de início
da Correção e a Data de fim da Correção: fora dessa janela, os perfis que
tratam as inconsistências não conseguem corrigi-las.

Quando o ano cadastrado é o mais recente, a plataforma pede sozinha a
sincronização dos arquivos do SISTEC, e a coluna **Arquivos do SISTEC**
passa a acompanhá-la. Um ano anterior ao mais recente é cadastrado sem
sincronização.

![Formulário de cadastro de configuração]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/cadastrar.png)

Para alterar as datas de um ano, use **Editar**, na linha da lista ou no alto
do detalhe da configuração. O formulário e as regras são os mesmos do
cadastro.

> **⚠️ Excluir uma configuração apaga o ano inteiro**
>
> Com a configuração vão os arquivos do SISTEC e as linhas deles, as
> inconsistências do ano com o histórico de cada uma, e os arquivos
> institucionais e de integração daquele ano. Não há como desfazer.

## Arquivos por unidade

**Visualizar**, na lista, abre o detalhe do ano. Em **Dados Gerais** ficam o
Ano e as datas de Início, Fim e Envio. Em **Arquivos**, um arquivo por
unidade, com:

- **Situação** — a etapa em que o arquivo está (ver abaixo);
- **Número de Linhas** — quantas linhas o SISTEC tem para a unidade;
- **Unidade** e **Instituição**;
- **Carregado (%)** — o progresso do arquivo.

A tabela rola por dentro quando há mais arquivos do que cabem na tela.

![Arquivos da configuração de 2026]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/detalhe.png)

A **Situação** segue as etapas da carga:

- **Aguardando** → **Carregado** → **Processado** → **Registros
  Identificados** → **Inconsistências Geradas**;
- enquanto uma etapa roda: **Carga em andamento**, **Processamento em
  andamento**, **Identificação em andamento** ou **Geração de inconsistências
  em andamento**;
- quando uma etapa falha: **Erro ao Carregar**, **Erro no Processamento**,
  **Erro na Identificação** ou **Erro ao Gerar Inconsistências**.

As abas separam os arquivos pela situação, com a quantidade de cada uma
abaixo do nome:

- **Tudo** — todos os arquivos;
- **Pendente** — os que estão em Aguardando;
- **A corrigir** — os que pararam num erro;
- **Finalizados** — os que chegaram a Inconsistências Geradas.

Arquivo numa etapa intermediária ou com uma etapa em andamento aparece só em
**Tudo**. Nessa aba, a Situação e o Carregado (%) se atualizam sozinhos
enquanto a carga roda.

### Realizar a carga do SISTEC

A carga leva cada arquivo pelas etapas que faltam, a partir da situação em
que ele está: baixar as linhas do SISTEC, processá-las, identificar os
registros e gerar as inconsistências. Ela roda em segundo plano; acompanhe
pela Situação.

Na aba **Pendente**, marque os arquivos e clique em **Realizar Carga
Sistec**, ou use **Realizar Carga Sistec em todas as unidades** para pedir a
carga de todos os arquivos que ainda têm etapa a cumprir. A janela seguinte
pede a confirmação em **Realizar Carga**.

![Aba Pendente com um arquivo marcado]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/pendente.png)

Só os arquivos da configuração corrente entram na carga: os de um ciclo
anterior são recusados, porque reprocessar um ciclo anterior não é
suportado. Na carga de todas as unidades, quando algum arquivo não é
agendado, a janela diz quantos foram agendados e lista os que ficaram de fora,
com o motivo.

### Retomar um arquivo que parou num erro

Na aba **A corrigir**, marque os arquivos e clique em **Reprocessar**. A
janela é a mesma da carga, e cada arquivo recomeça da etapa em que falhou.

![Aba A corrigir]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/a-corrigir.png)

## Linhas de um arquivo

**Visualizar**, na linha de um arquivo, abre o detalhe dele. Em **Dados
Gerais** ficam a Unidade, o Número de linhas, a Situação e quantos registros
já foram carregados e processados. Abaixo, as linhas do arquivo, em três
abas:

- **Tudo** — todas as linhas;
- **Processadas sem Sucesso** — as que o processamento recusou, com o
  **Erro** e o **Tipo de Erro**;
- **Processadas com Sucesso**.

Linha que ainda não foi processada aparece só em **Tudo**. A tabela é larga:
as últimas colunas, com a ação **Visualizar** da linha, aparecem rolando para
a direita.

![Linhas de um arquivo]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/arquivo.png)

**Visualizar**, numa linha, mostra todos os campos que vieram do SISTEC e, em
**Erros**, o erro e o tipo de erro do processamento.

![Detalhe de uma linha]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/linha.png)

### Tratar as linhas processadas sem sucesso

Na aba **Processadas sem Sucesso**, a linha pode ser corrigida, reprocessada
ou excluída.

![Linhas processadas sem sucesso]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/linhas-sem-sucesso.png)

**Corrigir Linhas** troca um valor em várias linhas de uma vez. Escolha o
**Tipo do Erro** e o **Campo**, e informe o **Valor atual** e o **Novo
valor**. A correção vale para todas as linhas do arquivo que têm esse tipo de
erro e esse valor no campo, marcadas ou não; a janela diz quantas são, e
**Corrigir** fica desabilitado quando nenhuma linha é afetada.

![Correção de linhas]({{site.baseurl}}/assets/img/docs/manual-do-usuario/configuracoes-iniciais/configuracoes/corrigir-linhas.png)

> **⚠️ Por enquanto, só campos de data**
>
> A correção funciona só nos campos de data, os que trazem "(dd/mm/aaaa)" no
> nome: Data de Início, Data Fim Previsto, Data de Nascimento e Data de
> Ocorrência da Matrícula. Nos demais campos, não use a correção.

Corrigir não reprocessa: a linha continua em **Processadas sem Sucesso** até
ser processada de novo. Para isso, marque as linhas e clique em **Reprocessar
Linhas**; a janela mostra o andamento até o processamento terminar.

**Excluir**, na coluna Ação da linha, apaga a linha do arquivo. Não há como
desfazer.
