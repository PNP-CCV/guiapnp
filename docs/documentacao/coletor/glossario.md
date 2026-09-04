---
layout: default
title: "Glossário do Coletor"
toc: true
---

# Glossário do Coletor

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página define a terminologia do **Coletor de Microdados**. Cada entrada linka para a página onde o conceito é detalhado. Para os termos gerais da PNP (matrícula, ciclo, curso, campus…), consulte a [Lista de termos]({{ site.baseurl }}/documentacao/termos/termos) do guia.

## Aprovação do Reitor {#aprovacao-do-reitor}

Aceite final e oficial dos microdados de uma instituição, dado pelo Reitor **na [PNP](#pnp)** — não no Coletor. É o último elo da cadeia de validação (estrutural → [Homologação da Área](#homologacao-da-area) → Aprovação do Reitor) e só alcança datasets já homologados pela área. Neste nível **só existe aprovar**: rejeitar é atribuição da área, um degrau antes.

É um estado **terminal**: o Coletor o reflete via [Registro de Validação de Modelo](#registro-de-validacao-de-modelo) e passa a bloquear a reextração do [Modelo de Dados](#modelo-de-dados), porque substituir dado já aceito exige abrir um novo [Ciclo de Coleta](#ciclo-de-coleta). Veja [Fluxo de negócio]({{ site.baseurl }}/documentacao/coletor/fluxo_de_negocio).

É também o **único** estágio terminal da cadeia: enquanto o dado está aguardando validação, validado ou apenas homologado pela área, uma reextração ainda destrava o reenvio. Ver [Só a Aprovação do Reitor é definitiva]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#so-a-aprovacao-do-reitor-e-definitiva).

## Ciclo de Coleta {#ciclo-de-coleta}

Período anual em que os microdados de uma edição da PNP são coletados, delimitado por uma janela principal e uma janela de correção. Um ciclo agrega um ou mais [Contratos de Dados](#contrato-de-dados), e apenas um ciclo é considerado ativo por vez. Veja [Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta).

## Configuração de Extração {#configuracao-de-extracao}

Registro que conecta um [Provedor de Dados](#provedor-de-dados) a um [Modelo de Dados](#modelo-de-dados), definindo *como* aquele modelo é obtido daquele provedor (endpoint da API, query SQL, nome da aba da planilha etc.). É a unidade configurável que o operador manipula no painel para mapear cada tabela lógica à sua fonte real.

## Contrato de Dados {#contrato-de-dados}

Especificação versionada que descreve um conjunto de [Modelos de Dados](#modelo-de-dados) relacionados, incluindo schema, regras de qualidade e metadados de governança, expressa em um arquivo YAML no padrão [Data Contract](#data-contract). Veja [Conceito de Contrato de Dados]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/conceito).

## Data Contract {#data-contract}

Termo do ecossistema [datacontract.com](https://datacontract.com/) que designa o arquivo YAML de especificação de um contrato (schema, servers, quality, terms etc.). No Coletor, cada [Contrato de Dados](#contrato-de-dados) materializa-se como um Data Contract validado automaticamente; os dois termos são usados como sinônimos quando o contexto está claro.

## Homologação da Área {#homologacao-da-area}

Aceite de um dataset pelo **Gestor de Área Temática** da instituição, feito **na [PNP](#pnp)** — não no Coletor. Acontece depois da validação estrutural automática e antes da [Aprovação do Reitor](#aprovacao-do-reitor). Cada área responde pelos seus próprios dados: o escopo do gestor é *instituição × área temática*, então Extensão homologa Extensão, Pesquisa homologa Pesquisa, e assim por diante.

Diferente do Reitor, a área pode **homologar ou rejeitar com justificativa** — a rejeição volta ao Coletor e a instituição corrige e reenvia. Veja [Fluxo de negócio]({{ site.baseurl }}/documentacao/coletor/fluxo_de_negocio).

## IFRN {#ifrn}

Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte. Instituição responsável pelo desenvolvimento e manutenção do Coletor em parceria com a SETEC/[MEC](#mec).

## MEC {#mec}

Ministério da Educação do Brasil. Órgão federal que mantém a [Plataforma Nilo Peçanha](#pnp) através da Secretaria de Educação Profissional e Tecnológica (SETEC) e é o destinatário final dos microdados sincronizados pelo Coletor.

## Modelo de Dados {#modelo-de-dados}

Tabela lógica única dentro de um [Contrato de Dados](#contrato-de-dados), correspondendo a uma entidade do schema (ex.: `acoes_extensao`, `projetos_de_pesquisa`). Cada modelo tem um schema próprio (colunas, tipos, restrições) e é extraído por uma [Configuração de Extração](#configuracao-de-extracao) específica, gerando um arquivo [Parquet](#parquet) por execução.

O contrato também diz, para cada modelo, **se ele é cobrado e se está ligado**: um modelo pode ser [obrigatório](#modelo-obrigatorio), [opcional](#modelo-opcional) ou [desabilitado](#modelo-desabilitado). Isso é decidido pela [PNP](#pnp) no YAML do contrato — a instituição não altera essa marcação no painel.

## Modelo desabilitado {#modelo-desabilitado}

[Modelo de Dados](#modelo-de-dados) que a [PNP](#pnp) desligou nesta versão do [Contrato de Dados](#contrato-de-dados) — no YAML, `meta.disabled: true`. Um modelo desabilitado **não é importado** pelo Coletor: ele simplesmente não aparece na lista de modelos, e não há nada a configurar nem a fazer.

Se o modelo já existia de sincronizações anteriores, ele é **retirado de vista** na próxima sincronização. A remoção é lógica: extrações, envios e arquivos [Parquet](#parquet) já gerados continuam guardados, e continuam listados nas telas de **Extrações** e **Envios**, que mostram o histórico por conta própria; o que sai de vista são as listagens de **Contratos** e **Modelos de Dados**. Contrato que fica sem **nenhum** modelo habilitado também desaparece do painel, pelo mesmo mecanismo. Veja [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Modelo obrigatório {#modelo-obrigatorio}

[Modelo de Dados](#modelo-de-dados) que o Coletor cobra da instituição — no YAML do contrato, `meta.required: true`, que é também o comportamento padrão quando o contrato não traz a marcação. Enquanto ele não tiver [Configuração de Extração](#configuracao-de-extracao), não for extraído, enviado e aprovado, o contrato **não fecha** e o passo correspondente do *wizard* fica em aberto.

Todo modelo é obrigatório salvo declaração em contrário: contratos antigos, sem os metadados, continuam se comportando exatamente como antes.

## Modelo opcional {#modelo-opcional}

[Modelo de Dados](#modelo-de-dados) que a [PNP](#pnp) marcou como não exigido nesta versão do contrato — no YAML, `meta.required: false`. Ele **existe normalmente** no Coletor: aparece na lista de modelos, pode ser configurado e extraído. A diferença é que, **enquanto ninguém criar uma [Configuração de Extração](#configuracao-de-extracao) para ele**, ele não conta no status do contrato, nos contadores do dashboard nem no *wizard* — não segura o progresso.

Assim que ganha uma configuração, passa a ser cobrado como qualquer outro: o contrato volta a "Aguardando Extração" e só fecha quando aquele modelo também for extraído, enviado e aprovado. Para desistir de coletá-lo, basta remover a(s) configuração(ões) — não existe botão de "desativar modelo". Veja [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

## Parquet {#parquet}

Formato de arquivo colunar otimizado para leitura analítica, mantido pela Apache Software Foundation. É o formato usado para persistir cada extração bem-sucedida e é o que a validação de qualidade lê durante os testes. É também o arquivo efetivamente enviado à [PNP](#pnp) na [Sincronização](#sincronizacao).

## Período de Correção {#periodo-de-correcao}

Janela do [Ciclo de Coleta](#ciclo-de-coleta), normalmente posterior à janela principal, em que o operador pode reextrair e ajustar dados antes do fechamento definitivo. Veja [Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta).

## PNP {#pnp}

Plataforma Nilo Peçanha. Sistema oficial do [MEC](#mec) que consolida e publica os microdados da Rede Federal de Educação Profissional, Científica e Tecnológica. É o destino das sincronizações do Coletor.

## Provedor de Dados {#provedor-de-dados}

Fonte concreta de microdados cadastrada no Coletor. Quatro tipos são selecionáveis na interface: **API HTTP**, **banco de dados**, **planilha online** (Google Docs / Dropbox / SharePoint) e **upload de planilha** (XLS / XLSX / ODS). O cadastro guarda o endereço e as credenciais de acesso de cada fonte. Veja [Operação passo a passo]({{ site.baseurl }}/documentacao/coletor/operacao_passo_a_passo).

## Registro de Extração {#registro-de-extracao}

Log persistente gravado a cada execução de extração, bem-sucedida ou não. Armazena status, motivo do erro, métricas de desempenho e detalhes técnicos, e é a fonte primária para auditoria e diagnóstico de extrações com falha. Consultável na tela **Extrações** do painel.

## Registro de Sincronização {#registro-de-sincronizacao}

Log persistente que registra cada tentativa de envio de um Parquet à [PNP](#pnp), incluindo status HTTP, resposta da API e timestamps. Permite rastrear quais [Modelos de Dados](#modelo-de-dados) de quais ciclos foram efetivamente entregues ao [MEC](#mec). Consultável na tela **Envios** do painel.

## Registro de Validação de Modelo {#registro-de-validacao-de-modelo}

Log persistente que espelha, dentro do Coletor, o estado de um [Modelo de Dados](#modelo-de-dados) **do lado da [PNP](#pnp)** após a [Sincronização](#sincronizacao). Guarda o identificador do dataset na PNP e o status traduzido: aguardando → validado → homologado pela área → aprovado pelo Reitor, com os ramos de rejeição e tempo esgotado.

É atualizado por **consulta**, não por notificação: o Coletor pergunta o status à PNP periodicamente e sob demanda ("Verificar agora"). Só a validação **mais recente** de um modelo vale — é o que permite que uma rejeição antiga, superada por um reenvio, deixe de bloquear o fluxo.

## Sincronização {#sincronizacao}

Ato de enviar um arquivo [Parquet](#parquet) já validado para a [PNP](#pnp). Cada sincronização gera um [Registro de Sincronização](#registro-de-sincronizacao) e só é permitida para modelos cujo contrato esteja com testes de qualidade aprovados no [Ciclo de Coleta](#ciclo-de-coleta) ativo. Veja [Sincronização com a PNP]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

## Validação referencial {#validacao-referencial}

Conferência de que os valores que apontam para entidades da Rede — código de campus, município, área temática do CNPq, CPF — existem de fato no cadastro da [PNP](#pnp). Roda **dos dois lados**: a PNP a executa depois do envio, e é a dela que vale; o Coletor a antecipa na extração, contra os cadastros que ele sincroniza da PNP, antes de gravar o [Parquet](#parquet).

De fábrica a conferência local **reprova**: uma referência declarada no contrato como `severidade: erro` derruba o teste do contrato e barra o envio, aparecendo em **Ver resultados de teste** com o campo e as linhas envolvidas. A extração em si conclui — o que muda é o veredito do contrato. É o que permite ver, no dia da extração, o erro que antes só voltava como rejeição da PNP dias depois. Referências declaradas como `severidade: aviso` viram alerta e não reprovam. Veja [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

## SodaCL {#sodacl}

[Soda Checks Language](https://docs.soda.io/soda-cl/soda-cl-overview.html). Linguagem declarativa para testes de qualidade de dados. No Coletor, expressões SodaCL aparecem na seção `quality:` do YAML do contrato e são executadas a cada teste de qualidade. Veja [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml).

## Veja também

- [Lista de termos]({{ site.baseurl }}/documentacao/termos/termos) — terminologia geral da PNP
- [Visão geral do Coletor]({{ site.baseurl }}/documentacao/coletor/visao_geral)
