---
layout: default
title: "Glossário do Coletor"
toc: true
---

# Glossário do Coletor

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página define a terminologia do **Coletor de Microdados**. Cada entrada linka para a página onde o conceito é detalhado. Para os termos gerais da PNP (matrícula, ciclo, curso, campus…), consulte a [Lista de termos](/documentacao/termos/termos) do guia.

## Aprovação do Reitor {#aprovacao-do-reitor}

Aceite final e oficial dos microdados de uma instituição, dado pelo Reitor **na [PNP](#pnp)** — não no Coletor. É o último elo da cadeia de validação (estrutural → [Homologação da Área](#homologacao-da-area) → Aprovação do Reitor) e só alcança datasets já homologados pela área. Neste nível **só existe aprovar**: rejeitar é atribuição da área, um degrau antes.

É um estado **terminal**: o Coletor o reflete via [Registro de Validação de Modelo](#registro-de-validacao-de-modelo) e passa a bloquear a reextração do [Modelo de Dados](#modelo-de-dados), porque substituir dado já aceito exige abrir um novo [Ciclo de Coleta](#ciclo-de-coleta). Veja [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio).

## Ciclo de Coleta {#ciclo-de-coleta}

Período anual em que os microdados de uma edição da PNP são coletados, delimitado por uma janela principal e uma janela de correção. Um ciclo agrega um ou mais [Contratos de Dados](#contrato-de-dados), e apenas um ciclo é considerado ativo por vez. Veja [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta).

## Configuração de Extração {#configuracao-de-extracao}

Registro que conecta um [Provedor de Dados](#provedor-de-dados) a um [Modelo de Dados](#modelo-de-dados), definindo *como* aquele modelo é obtido daquele provedor (endpoint da API, query SQL, nome da aba da planilha etc.). É a unidade configurável que o operador manipula no painel para mapear cada tabela lógica à sua fonte real.

## Contrato de Dados {#contrato-de-dados}

Especificação versionada que descreve um conjunto de [Modelos de Dados](#modelo-de-dados) relacionados, incluindo schema, regras de qualidade e metadados de governança, expressa em um arquivo YAML no padrão [Data Contract](#data-contract). Veja [Conceito de Contrato de Dados](/documentacao/usuarios-especializados/contratos/conceito).

## Data Contract {#data-contract}

Termo do ecossistema [datacontract.com](https://datacontract.com/) que designa o arquivo YAML de especificação de um contrato (schema, servers, quality, terms etc.). No Coletor, cada [Contrato de Dados](#contrato-de-dados) materializa-se como um Data Contract validado automaticamente; os dois termos são usados como sinônimos quando o contexto está claro.

## Homologação da Área {#homologacao-da-area}

Aceite de um dataset pelo **Gestor de Área Temática** da instituição, feito **na [PNP](#pnp)** — não no Coletor. Acontece depois da validação estrutural automática e antes da [Aprovação do Reitor](#aprovacao-do-reitor). Cada área responde pelos seus próprios dados: o escopo do gestor é *instituição × área temática*, então Extensão homologa Extensão, Pesquisa homologa Pesquisa, e assim por diante.

Diferente do Reitor, a área pode **homologar ou rejeitar com justificativa** — a rejeição volta ao Coletor e a instituição corrige e reenvia. Veja [Fluxo de negócio](/documentacao/coletor/fluxo_de_negocio).

## IFRN {#ifrn}

Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte. Instituição responsável pelo desenvolvimento e manutenção do Coletor em parceria com a SETEC/[MEC](#mec).

## MEC {#mec}

Ministério da Educação do Brasil. Órgão federal que mantém a [Plataforma Nilo Peçanha](#pnp) através da Secretaria de Educação Profissional e Tecnológica (SETEC) e é o destinatário final dos microdados sincronizados pelo Coletor.

## Modelo de Dados {#modelo-de-dados}

Tabela lógica única dentro de um [Contrato de Dados](#contrato-de-dados), correspondendo a uma entidade do schema (ex.: `acoes_extensao`, `projetos_de_pesquisa`). Cada modelo tem um schema próprio (colunas, tipos, restrições) e é extraído por uma [Configuração de Extração](#configuracao-de-extracao) específica, gerando um arquivo [Parquet](#parquet) por execução.

## Parquet {#parquet}

Formato de arquivo colunar otimizado para leitura analítica, mantido pela Apache Software Foundation. É o formato usado para persistir cada extração bem-sucedida e é o que a validação de qualidade lê durante os testes. É também o arquivo efetivamente enviado à [PNP](#pnp) na [Sincronização](#sincronizacao).

## Período de Correção {#periodo-de-correcao}

Janela do [Ciclo de Coleta](#ciclo-de-coleta), normalmente posterior à janela principal, em que o operador pode reextrair e ajustar dados antes do fechamento definitivo. Veja [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta).

## PNP {#pnp}

Plataforma Nilo Peçanha. Sistema oficial do [MEC](#mec) que consolida e publica os microdados da Rede Federal de Educação Profissional, Científica e Tecnológica. É o destino das sincronizações do Coletor.

## Provedor de Dados {#provedor-de-dados}

Fonte concreta de microdados cadastrada no Coletor. Quatro tipos são selecionáveis na interface: **API HTTP**, **banco de dados**, **planilha online** (Google Docs / Dropbox / SharePoint) e **upload de planilha** (XLS / XLSX / ODS). O cadastro guarda o endereço e as credenciais de acesso de cada fonte. Veja [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo).

## Registro de Extração {#registro-de-extracao}

Log persistente gravado a cada execução de extração, bem-sucedida ou não. Armazena status, motivo do erro, métricas de desempenho e detalhes técnicos, e é a fonte primária para auditoria e diagnóstico de extrações com falha. Consultável na tela **Extrações** do painel.

## Registro de Sincronização {#registro-de-sincronizacao}

Log persistente que registra cada tentativa de envio de um Parquet à [PNP](#pnp), incluindo status HTTP, resposta da API e timestamps. Permite rastrear quais [Modelos de Dados](#modelo-de-dados) de quais ciclos foram efetivamente entregues ao [MEC](#mec). Consultável na tela **Envios** do painel.

## Registro de Validação de Modelo {#registro-de-validacao-de-modelo}

Log persistente que espelha, dentro do Coletor, o estado de um [Modelo de Dados](#modelo-de-dados) **do lado da [PNP](#pnp)** após a [Sincronização](#sincronizacao). Guarda o identificador do dataset na PNP e o status traduzido: aguardando → validado → homologado pela área → aprovado pelo Reitor, com os ramos de rejeição e tempo esgotado.

É atualizado por **consulta**, não por notificação: o Coletor pergunta o status à PNP periodicamente e sob demanda ("Verificar agora"). Só a validação **mais recente** de um modelo vale — é o que permite que uma rejeição antiga, superada por um reenvio, deixe de bloquear o fluxo.

## Sincronização {#sincronizacao}

Ato de enviar um arquivo [Parquet](#parquet) já validado para a [PNP](#pnp). Cada sincronização gera um [Registro de Sincronização](#registro-de-sincronizacao) e só é permitida para modelos cujo contrato esteja com testes de qualidade aprovados no [Ciclo de Coleta](#ciclo-de-coleta) ativo. Veja [Sincronização com a PNP](/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

## SodaCL {#sodacl}

[Soda Checks Language](https://docs.soda.io/soda-cl/soda-cl-overview.html). Linguagem declarativa para testes de qualidade de dados. No Coletor, expressões SodaCL aparecem na seção `quality:` do YAML do contrato e são executadas a cada teste de qualidade. Veja [Anatomia do YAML](/documentacao/usuarios-especializados/contratos/anatomia_yaml).

## Veja também

- [Lista de termos](/documentacao/termos/termos) — terminologia geral da PNP
- [Visão geral do Coletor](/documentacao/coletor/visao_geral)
