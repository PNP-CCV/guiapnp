---
layout: default
title: "Perguntas frequentes"
---

# Perguntas frequentes

> **Para quem é:** 👔 gestores · 🔌 integradores

Respostas às dúvidas frequentes sobre acesso, instalação, operação e envio de dados pelo Coletor, organizadas por assunto. Os links indicam as páginas com orientações detalhadas. As datas e os exemplos com ano-base 2025 se referem ao ciclo de coleta de 2026.

## 1. Credenciais e acesso à homologação

### Como peço as credenciais do ambiente de testes (homologação) do Coletor PNP?

Quem pede é o responsável pela TI, pelo e-mail institucional da área (por exemplo, dti@instituicao.edu.br). O pedido vai para **pnp.suporte@mec.gov.br**, com cópia para o responsável por Desenvolvimento Institucional. Use o modelo de texto do Guia e preencha a tabela com nome completo, CPF e e-mail do gestor de cada área temática: Pesquisa, Extensão, Orçamento, Sustentabilidade, Desenvolvimento Institucional e Ensino.

Sem o CPF ou sem a área de cada pessoa, o cadastro não é concluído. Uma área pode ter mais de um responsável.

*Saiba Mais:* [Solicitação de Credenciais]({{site.baseurl}}/documentacao/coletor/solicitar_credenciais) › Abertura de Chamado; Modelo do Chamado

### O que recebo, e onde uso cada coisa?

- **URL da API,** que vai no setup do Coletor. Na homologação é `https://pnp-homolog.pnp.ifrn.edu.br/api/v2/`; na produção, `https://pnpccv.mec.gov.br/api/v2/`.
- **Secret de integração,** que vai no campo "Secret da API PNP" do setup. É um texto contínuo, sem espaços nem quebras de linha.
- **Acesso dos gestores ao ambiente web,** onde eles homologam os dados. Na homologação, o endereço é https://pnp-homolog.pnp.ifrn.edu.br/; o gestor entra com o CPF e a senha temporária fornecida à instituição, e troca a senha no primeiro acesso.

Sem a URL e o Secret, a instância não ativa: o setup testa a ligação com a PNP na hora. Se o setup passou, a integração está funcionando.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › A tela de setup; O que o setup faz · [Requisitos técnicos]({{site.baseurl}}/documentacao/coletor/requisitos_tecnicos#credenciais-junto-a-pnp) › Credenciais junto à PNP

### Abri a URL da API no navegador e deu erro. Ela está errada?

Não. Essa URL serve para ser cadastrada no setup do Coletor, não para ser aberta no navegador. Para ver a lista de endpoints, use https://pnp-homolog.pnp.ifrn.edu.br/api/v2/docs.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › A tela de setup

### A senha temporária expirou. Podem redefinir?

A senha temporária não expira com o tempo. O gestor entra com o CPF, só números, e a senha temporária; o sistema pede a senha nova no primeiro login. As credenciais saem em lote para a TI, que repassa as instruções a cada gestor.

### Ao ativar a instância, aparece "Secret already bound to another instance" (erro 409)

No primeiro registro, a PNP liga o Secret ao hostname da máquina. O mesmo Secret usado em outra máquina, ou depois de trocar o hostname, é recusado. Peça à equipe da PNP para desvincular o Secret ou gerar um novo. Por isso, escolha o servidor definitivo antes de rodar o setup.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso#secret-casado-com-hostname) › O secret é casado com o hostname · [Requisitos técnicos]({{site.baseurl}}/documentacao/coletor/requisitos_tecnicos#servidor) › Servidor

### Por que o Diretor de TI não ganhou usuário na PNP?

O ambiente web da PNP não tem nenhuma função para a TI. Lá só atuam os perfis de microdados: Operador e Gestor de Área Temática e Reitor. A TI administra o Coletor localmente, com usuários próprios (veja a seção 5).

*Saiba Mais:* [Manual do usuário › Gestor de Área Temática]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/gestor-area-tematica) · [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › Usuários adicionais

### Como troco um gestor já cadastrado ou corrijo o reitor?

Abra um chamado com nome, CPF, e-mail e área da pessoa nova. Para o reitor, mande o CPF. Depois que o suporte atualizar, abra Configurações no Coletor e clique em Salvar, para que os dados da instituição sejam lidos de novo.

## 2. Ambiente de produção

### Como consigo acesso ao ambiente de produção?

Peça pelo mesmo canal usado para as credenciais de testes. Antes, a instituição precisa ter enviado pelo menos um conjunto de dados no ambiente de testes, porque é isso que mostra que o Coletor está funcionando. Na liberação, o suporte cadastra os gestores em produção e envia:

- **URL da API:** `https://pnpccv.mec.gov.br/api/v2/`
- **Um Secret novo,** só para produção.
- **Endereço do ambiente web:** https://pnpccv.mec.gov.br/. Os gestores e o reitor entram com a conta gov.br.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › A tela de setup (URL de Produção)

### Preciso instalar o Coletor de novo para usar a produção?

Sim. Instale um Coletor separado para produção, como se faz com qualquer aplicação que tem homologação e produção. O banco do Coletor de homologação não é aproveitado quando se troca de ambiente.

O Secret fica ligado ao hostname da máquina. Se a ideia for reaproveitar o servidor da homologação, fale antes com a equipe da PNP.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso#secret-casado-com-hostname) › O secret é casado com o hostname · [Instalação]({{site.baseurl}}/documentacao/coletor/instalacao) › Desligar e apagar dados

### Pedi a produção, mas ninguém aqui recebeu as credenciais

Veja se outro servidor da instituição já fez o pedido. A resposta vai para os e-mails informados na solicitação original.

## 3. Instalação, atualização e infraestrutura do Coletor

### Que servidor preciso? Tem regra de hostname, rede ou acesso externo?

| Item | O que o Guia pede |
| --- | --- |
| Sistema | Linux em `linux/amd64` (x86-64) para a instância definitiva. Windows e macOS servem só para testes |
| vCPU | 2 no mínimo, 4 recomendadas |
| Memória | 4 GB no mínimo, 8 GB recomendados |
| Disco | 20 GB livres no mínimo, 50 GB recomendados (SSD) |
| Software | Docker Engine com Docker Compose v2 |
| Saída de rede | API da PNP, `ghcr.io`, `github.com` e as fontes de dados da instituição |
| Entrada de rede | Porta 8000/tcp, para os operadores abrirem o painel |
| Hostname | Precisa ser estável, porque o Secret fica ligado a ele |

O Guia não exige nome específico de hostname nem acesso ao Coletor pela internet; basta que os operadores alcancem a porta 8000. Rode o `coletor` com um usuário comum do grupo `docker`, nunca com `sudo`.

*Saiba Mais:* [Requisitos técnicos]({{site.baseurl}}/documentacao/coletor/requisitos_tecnicos) › Servidor; Software; Rede; Usuário de operação

### Onde estão o instalador e o passo a passo?

O executável está nas releases de https://github.com/PNP-CCV/coletor. O roteiro tem três etapas: instalar o Docker, instalar o executável `coletor` e subir a stack com `coletor up`. Depois, abra `http://<servidor>:8000/painel/` e faça o setup.

*Saiba Mais:* [Instalação]({{site.baseurl}}/documentacao/coletor/instalacao) › 1. Instalar o Docker; 2. Instalar o executável; 3. Subir a stack · [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › A tela de setup

### Dá para instalar sem a CLI? Estamos esbarrando no limite de downloads do Docker Hub.

O Guia aceita instalar sem a CLI, usando o `cli/docker-compose.yml` do repositório da aplicação com a imagem `ghcr.io/pnp-ccv/coletor`. Nesse caso, a equipe fica responsável pelo que a CLI faria: pasta de dados, `HOST_NAME`, UID/GID e atualização das imagens.

Para o limite do Docker Hub, a saída mais simples é baixar a CLI mais recente. A imagem principal vem do GHCR, e as imagens do PostgreSQL e do Redis vêm de um espelho no GCR, sem esse limite.

*Saiba Mais:* [Instalação]({{site.baseurl}}/documentacao/coletor/instalacao) › Instalação sem a CLI · [Requisitos técnicos]({{site.baseurl}}/documentacao/coletor/requisitos_tecnicos#o-que-a-instalacao-sobe) › O que a instalação sobe

### Como atualizo o Coletor? Apareceu "erro de sintaxe próximo ao token inesperado newline".

O `coletor update` baixa as imagens novas e reinicia a stack. Se houver um executável mais novo, ele avisa, mostra o link e não atualiza: troque o executável primeiro e rode `update` de novo. O erro de sintaxe aparece quando se baixa a página da versão (`.../releases/tag/...`) em vez do arquivo. Use o link de download:

```
curl -fL -o coletor https://github.com/PNP-CCV/coletor/releases/download/<versão>/coletor
chmod +x coletor
sudo mv coletor /usr/local/bin/coletor
coletor --version
coletor update
```

Depois de atualizar, clique uma vez em "Sincronizar com a PNP". Sem isso, todos os modelos continuam sendo tratados como obrigatórios.

*Saiba Mais:* [Instalação]({{site.baseurl}}/documentacao/coletor/instalacao) › Atualização

### Como levo o Coletor para outra VM?

Copiar os arquivos não basta. O hostname muda, o Secret deixa de conferir e a ativação falha. É preciso pedir à equipe da PNP para desvincular o Secret ou mandar um novo. Os dados ficam em dois lugares: a pasta `~/.local/share/coletor` e o volume do Postgres `coletorpnp_db-data`. O backup precisa cobrir os dois.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso#secret-casado-com-hostname) › O secret é casado com o hostname · [Requisitos técnicos]({{site.baseurl}}/documentacao/coletor/requisitos_tecnicos) › Onde os dados ficam

A partir da versão 0.0.14, os comandos `coletor backup` e `coletor restore` estão documentados no repositório do Coletor.

### Consigo trazer as configurações do PNP Data Extractor para o Coletor?

Não existe procedimento para isso. As duas ferramentas têm arquitetura e estrutura de dados diferentes.

### Dá para ligar o Coletor ao SUAP ou a outro sistema?

Sim. O Coletor lê de API HTTP (sem autenticação, HTTP Basic, OAuth2, token simples ou JWT), de bancos de dados (PostgreSQL, MySQL/MariaDB, SQL Server, SQLite, IBM Db2, MongoDB, CouchDB), de planilhas online (Google Docs, Dropbox e SharePoint) e de upload de planilha (XLS/XLSX/ODS). No caso da API, a TI cria endpoints no sistema da instituição que devolvem os dados no formato de cada modelo do contrato. A integração por API segue estas regras:

- **Requisição:** só GET. Toda página tem de responder 200; qualquer outro status cancela a extração.
- **Resposta:** JSON com a lista na raiz, ou em `results`, ou em `data`. As chaves têm de ser exatamente os campos do modelo, com `null` quando não houver valor.
- **Paginação:** só pelo campo `next` com URL absoluta, no estilo DRF. O `next` precisa repetir os filtros.
- **Autenticação:** o token é pedido uma vez por modelo e não é renovado. No OAuth 2.0, só funciona `client_credentials`.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo) › Passo 2 — Cadastrar os provedores · [Visão geral]({{site.baseurl}}/documentacao/coletor/visao_geral) › Contexto na Plataforma Nilo Peçanha

### O painel diz que o Coletor não está configurado. E agora?

Essa mensagem aparece quando a instância nunca passou pelo setup inicial (ou quando o banco foi recriado com `coletor down --wipe`). Acesse o painel sem nenhum usuário cadastrado e a tela de configuração inicial aparece no lugar do login.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso).

### Quero estender o Coletor (novo tipo de provedor, novo banco). Onde está a documentação?

A documentação técnica de arquitetura e extensão do código não faz parte deste guia — está no [site de documentação do Coletor](https://pnp-ccv.github.io/coletor-pnp-microdados/), trilha "Técnica".

## 4. Operação do Coletor

### Qual é o caminho completo, do Coletor até a PNP?

São oito passos, e o painel do Coletor acompanha cada um:

1. Sincronizar com a PNP.
2. Cadastrar os provedores, que são as fontes dos dados.
3. Configurar a extração de cada modelo.
4. Extrair. O Coletor testa a qualidade automaticamente nesse passo.
5. Enviar à PNP.
6. Aguardar a validação da PNP.
7. Homologação pelo Gestor da Área, feita na PNP.
8. Aprovação do Reitor, feita na PNP.

Os passos 7 e 8 não têm botão no Coletor; ele só mostra o resultado.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo) · [Fluxo de negócio]({{site.baseurl}}/documentacao/coletor/fluxo_de_negocio)

### A instituição é obrigada a usar o Coletor?

Não. O Operador de Área Temática pode mandar os microdados direto na PNP, pela planilha (baixa o modelo, preenche e envia) ou pelo formulário. Esse envio passa pela mesma validação do contrato e depois segue para a homologação e a aprovação. Quem nomeia os operadores é o Gestor de Área Temática.

*Saiba Mais:* [Manual do usuário › Operador de Área Temática]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/operador-area-tematica) · [Manual do usuário › Enviar Planilha]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/enviar-planilha)

### Aparece "O ciclo de coleta está bloqueado (inativo ou fora do prazo)". O que faço?

Fora da janela principal e da janela de correção do ciclo, o Coletor recusa extrações e envios antes de qualquer tarefa entrar na fila. Um contrato sem ciclo de coleta associado também fica bloqueado. As datas vêm da PNP e chegam pela sincronização. Clique em "Sincronizar com a PNP" para trazer as datas atuais; a janela de testes foi estendida até 13/12/2026.

*Saiba Mais:* [Ciclo de coleta]({{site.baseurl}}/documentacao/coletor/ciclo_de_coleta) › Período de Correção: o que muda · [Sincronização com a PNP]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp) › Direção inversa

### O que o botão "Sincronizar com a PNP" faz, e quando uso?

Ele traz da PNP os ciclos e suas janelas, os contratos, os modelos e o que é obrigatório ou opcional. Traz também as tabelas de apoio (estruturas, áreas temáticas, subeixos e municípios) e os cadastros de matrículas e servidores. Use depois de instalar, depois de atualizar o Coletor e sempre que a PNP publicar mudanças nos contratos.

*Saiba Mais:* [Sincronização com a PNP]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp) › Direção inversa: o que "Sincronizar com a PNP" traz

### Onde está o modelo de planilha?

Há duas fontes: a [planilha de exemplo no Guia]({{site.baseurl}}/assets/files/template_fornecimento_dados.xlsx) e o modelo oferecido pelo Coletor ao cadastrar um provedor do tipo planilha. Quando as duas forem diferentes, vale a do Coletor, que acompanha o contrato em vigor. Cabe destacar que o modelo de planilha se comporta como uma referência de quais dados devem ser informados. Porém, esses dados serão analisados com base nas regras constantes no contrato.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo) › Passo 2 — Cadastrar os provedores

### Posso dividir a planilha em várias, uma por área?

Pode. Cada planilha, ou cada aba, é ligada ao seu modelo na Configuração de Extração. Ao separar as abas do modelo, copie junto a aba oculta `_listas`, que guarda as listas de valores; sem ela, os campos de lista dão erro. Mantenha as colunas opcionais, mesmo vazias.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo) › Passo 3 — Configurar a extração

### Usei um link do Google Sheets e o Coletor disse que o formato não é suportado

Use o link de exportação, não o de edição: `https://docs.google.com/spreadsheets/d/<ID>/export?format=xlsx`. O link `/edit` devolve uma página HTML. Também não use o link temporário do `googleusercontent.com`, que expira e faz a coleta quebrar dias depois. Antes de salvar, clique em "Testar extração" para ver as primeiras linhas.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo) › Passo 2 — Cadastrar os provedores; Passo 3 — Configurar a extração

### Os campos TRUE/FALSE estão dando erro

O Coletor aceita TRUE/FALSE, VERDADEIRO/FALSO, true/false e 1/0. Se ainda der erro, atualize o Coletor e sincronize.

### Onde acho os códigos de estrutura (campus), município, área CNPq e subeixo?

Depois de sincronizar, eles aparecem nas consultas do Coletor, na tela "Dados da PNP". Quem envia direto na PNP encontra os mesmos códigos em Microdados → Consultas. Nas planilhas vai o código, porque nada converte nome em código.

- **Estrutura:** código do campus.
- **Municípios atendidos:** lista de códigos IBGE, como `[2408102, 2403103]`, e não um texto separado por ponto e vírgula.
- **Subeixo:** se o código não existir, o teste do contrato reprova.
- **Área CNPq:** código inexistente gera só um aviso e não reprova.

*Saiba Mais:* [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial) › O que ela consegue conferir · [Ações de Extensão]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) › `referencia_pnp` — conferido na extração · [Manual do usuário › Consultas]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/consultas)

### Todo modelo é obrigatório? O que acontece se faltar um campo?

Há dois níveis de obrigatoriedade:

- **Modelo obrigatório:** o Coletor exige configuração e extração.
- **Modelo opcional:** só é cobrado se alguém configurá-lo. São opcionais, por exemplo, `programa` e `pessoas_atendidas_acoes_extensao` (Extensão), `acordos_parceria` e `dados_orcamentarios`. Um contrato que só tem modelos opcionais aparece como "Somente Modelos Opcionais", e isso é esperado.
- **Campo obrigatório vazio, coluna a mais ou tipo errado:** a validação de schema rejeita.
- **Regra de qualidade violada:** o arquivo é gravado, mas o contrato fica em "Qualidade Reprovada" e o envio fica bloqueado até a correção na origem.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo#modelos-opcionais-no-passo-3) › Nem todo modelo precisa ser configurado · [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados) · [Validação e qualidade]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade)

### Sou avisado quando um contrato muda?

As mudanças chegam pela sincronização. Quando um modelo ou uma configuração muda depois da última extração, o contrato aparece como "Reextração Necessária", e basta extrair de novo. Cada página de contrato no Guia tem um "Histórico de versões" que mostra o que mudou e se a mudança quebra envios antigos.

*Saiba Mais:* [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato) · [Ciclo de vida do contrato]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/ciclo_de_vida)

### O gestor entrou na PNP e não tem nada para homologar

A fila do gestor só mostra o que já foi enviado e aprovado na validação automática. Se ainda não houve envio, a fila fica vazia. Quem tem papéis em mais de uma área precisa escolher o papel em "Alterar Papel"; senão, a fila aparece vazia sem explicação. O papel volta ao padrão a cada login.

A mensagem "A conclusão de sua capacitação ainda não foi validada" se refere ao próximo ciclo e pode ser ignorada agora.

*Saiba Mais:* [Operação passo a passo]({{site.baseurl}}/documentacao/coletor/operacao_passo_a_passo#passos-7-e-8) › Passos 7 e 8 · [Manual do usuário › Fila de Homologação]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/fila-de-homologacao)

### A extração funcionou, mas o teste do contrato falhou. O que fazer?

O teste de qualidade roda **dentro** da extração, então um teste reprovado aparece como "Falha na Extração", não como um estado próprio — não há botão "Executar Teste". Abra o relatório em **Contratos → o contrato → resultados de teste** para identificar quais campos falharam (tipo, obrigatoriedade, domínio de valores). A partir daí, decida entre **corrigir os dados na fonte** (quando o contrato reflete a regra correta) ou **reportar à equipe da PNP** (quando a regra do YAML parece mais estrita do que o combinado).

*Saiba Mais:* [Validação e qualidade]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade).

### O teste do contrato reprovou por "validação referencial". O que isso quer dizer?

Que algum valor do dado aponta para uma entidade que **não existe no cadastro da Rede** — um código de campus, um município, uma área temática ou um CPF. O Coletor confere isso na extração, contra os cadastros que sincroniza da própria PNP: é a mesma conferência que a PNP faria depois do envio, antecipada para o dia da extração.

A extração conclui normalmente e o arquivo fica gravado; o que a reprovação bloqueia é o **envio**. Abra **Contratos → o contrato → Ver resultados de teste**: cada apontamento aparece como um card, com o campo, quantas linhas caíram e a tabela das linhas envolvidas — a linha inteira, não só o valor recusado, para dar para achar o registro na origem. A correção é sempre no **dado de origem**. Se o valor estiver certo e o cadastro local é que está velho, rode "Sincronizar com a PNP" e extraia de novo.

### A extração passou, mas o Registro de Extração trouxe uma "validação referencial" com violações. Está errado?

Não, e há duas leituras possíveis. A primeira: a extração **sempre** conclui — quem reprova é o teste do contrato, então o apontamento no Registro de Extração não é sinal de falha da extração, e sim o mesmo achado visto por outra tela.

A segunda: nem toda referência é declarada como impeditiva. O contrato marca cada uma como `erro` (reprova o teste e barra o envio) ou `aviso` (só registra). Um apontamento em amarelo é do segundo tipo — não reprovou nada. Ainda assim vale investigar na origem: se o apontamento estiver certo, é exatamente o que a PNP tende a rejeitar depois do envio.

*Saiba Mais:* [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### A PNP não recebeu os dados — onde olho primeiro?

Abra o registro mais recente em **Envios** (`/painel/sincronizacoes/`) e leia os detalhes — eles guardam a resposta completa devolvida pela API da PNP, com código HTTP e mensagem de erro. Em seguida, confira se a URL da PNP aponta para o ambiente correto (visível em **Configurações**, para administradores). Se a resposta for 401/403, a instância pode ter perdido a autenticação: reinicie a stack (`coletor down` seguido de `coletor up`) para reativá-la — os dados são preservados. O fluxo completo está em [Sincronização com a PNP]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

### Reenviei os dados e a rejeição continua. Por quê?

A PNP identifica cada dataset pelo **conteúdo** (checksum). Reextrair e reenviar um dado idêntico devolve o mesmo dataset com o status antigo — inclusive uma rejeição anterior. Para mudar o estado na PNP, o dado precisa efetivamente mudar na origem.

*Saiba Mais:* [Quando algo falha]({{site.baseurl}}/documentacao/coletor/quando_algo_falha).

### Um contrato (ou um modelo) sumiu do painel depois de sincronizar. O que houve?

Quase sempre é a PNP tendo **desabilitado** aquele modelo nesta versão do contrato (`meta.disabled: true` no YAML). Modelo desabilitado não é importado e, se já existia, sai de vista na sincronização seguinte; contrato que fica **sem nenhum modelo habilitado** desaparece inteiro pelo mesmo motivo. Não é erro nem falha de sincronização, e nada é apagado de fato: a remoção é lógica, e extrações, envios e arquivos já gerados continuam guardados — continuam listados nas telas de **Extrações** e **Envios**, que mostram o histórico por conta própria; o que sai de vista são as listagens de **Contratos** e **Modelos de Dados**. Se a PNP reabilitar o modelo mais adiante, ele volta "zerado": a Configuração de Extração anterior precisa ser refeita.

*Saiba Mais:* [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

### Um contrato aparece como "Somente Modelos Opcionais". Preciso fazer alguma coisa?

Não, a menos que a instituição queira coletar aquele dado. O badge significa que **todos** os modelos daquele contrato são [opcionais]({{site.baseurl}}/documentacao/coletor/glossario#modelo-opcional) e nenhum foi configurado — "não há nada a coletar". Esses contratos ficam fora do progresso do wizard, o que explica o painel marcar 8/8 (ou `1/1`) com contratos ainda "não coletados" na tela, e as ações em lote sumirem. Para coletar um deles, crie a Configuração de Extração do modelo: a partir daí ele passa a ser cobrado normalmente.

### Configurei um modelo opcional e agora o contrato voltou atrás. É bug?

Não. Modelo opcional só é invisível ao fluxo **enquanto ninguém o configura**. Assim que ganha uma Configuração de Extração, ele conta como qualquer modelo obrigatório: o contrato volta para "Aguardando Extração" e só fecha quando aquele modelo também for extraído, enviado, homologado e aprovado. Se a intenção era não coletá-lo, remova a configuração — o contrato sai do fluxo de novo.

### Excluí um Contrato de Dados por engano. Perdi tudo?

Não. A exclusão no Coletor é **lógica**: o registro permanece no banco, apenas marcado como excluído, e o histórico de extrações e envios é preservado para auditoria. A restauração exige intervenção técnica (não há botão no painel) — acione o suporte do Coletor. Se o ciclo ainda permitir, re-sincronizar com a PNP também recria contratos e modelos do ciclo vigente.

## 5. Usuários e perfis

### Quem faz o quê?

| Perfil | Onde atua | O que faz |
| --- | --- | --- |
| Administrador e operadores do Coletor (TI) | Coletor, na instituição | Instalam e mantêm o Coletor, cadastram provedores, extraem e enviam. O primeiro usuário é o administrador e cria os demais |
| Operador de Área Temática | PNP web | Envia os microdados da sua área pela planilha ou pelo formulário, sem usar o Coletor |
| Gestor de Área Temática | PNP web | Homologa ou rejeita, com justificativa, os dados da sua área. Também nomeia os operadores da área |
| Reitor | PNP web | Faz a aprovação final de todas as áreas; só pode aprovar |
| Pesquisador Institucional (PI) | PNP web | Cuida dos dados e das inconsistências de ensino, cadastra pessoas e atribui papéis |

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › Usuários adicionais · Manual do usuário: [Operador de Área Temática]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/operador-area-tematica), [Gestor de Área Temática]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/gestor-area-tematica), [Reitor]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/reitor), [Pesquisador Institucional]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/pesquisador-institucional)

### Os gestores cadastrados pela PNP não aparecem no Coletor. Está errado?

Não está. Os gestores usam a PNP web, não o Coletor. Quem opera o Coletor é criado pelo administrador local, na tela Usuários do menu Sistema. Contas comuns operam a coleta; contas de administrador também veem Tarefas Agendadas, Configurações e a gestão de usuários.

*Saiba Mais:* [Primeiro acesso]({{site.baseurl}}/documentacao/coletor/primeiro_acesso) › Usuários adicionais

### Queremos que outras pessoas enviem os dados da área, e não o gestor

O perfil para isso é o Operador de Área Temática, e quem o nomeia é o próprio Gestor da área, na PNP. O gestor continua responsável pela homologação. Se o envio for pelo Coletor, os operadores são usuários do Coletor, criados pelo administrador local.

*Saiba Mais:* [Manual do usuário › Gestor de Área Temática]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/gestor-area-tematica)

### O reitor precisa ser cadastrado? Onde ele aprova?

Não precisa; os reitores já vêm cadastrados pelo ciclo do CCV. Ele aprova na PNP web, em Aprovação de Microdados, e só recebe o que os gestores já homologaram, de todas as áreas juntas. Na homologação, entra com o CPF e a senha temporária; em produção, pelo gov.br.

*Saiba Mais:* [Manual do usuário › Reitor]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/reitor) · [Fluxo de negócio]({{site.baseurl}}/documentacao/coletor/fluxo_de_negocio) › Aprovação do Reitor

### Quero um perfil acima do de gestor na PNP

Acima do gestor fica o Pesquisador Institucional. Para recebê-lo, abra um chamado e anexe a portaria ou outro documento que comprove a designação. Para administrar o Coletor, não é preciso pedir nada à PNP; isso é resolvido pela TI da instituição.

*Saiba Mais:* [Manual do usuário › Pesquisador Institucional]({{site.baseurl}}/documentacao/manual-do-usuario/perfis/pesquisador-institucional)

## 6. Prazos, prévia e homologação

### Qual é o prazo? Vai ter prorrogação?

O ciclo de 2026 traz os dados do ano-base 2025. Envio, correção e homologação, incluindo a aprovação do reitor, acontecem na janela de 01/10 a 13/12/2026, sem prorrogação. Fora da janela, o Coletor e a PNP recusam extrações e envios. O envio por planilha vale até 23h59, horário de Recife, do último dia.

*Saiba Mais:* [Ciclo de coleta]({{site.baseurl}}/documentacao/coletor/ciclo_de_coleta) › Anatomia do ciclo; Período de Correção · [Manual do usuário › Enviar Planilha]({{site.baseurl}}/documentacao/manual-do-usuario/microdados/enviar-planilha) › O prazo

### Depois de homologado, ainda dá para corrigir?

Dá, enquanto o reitor não aprovar. Homologar não tranca o dado: a instituição corrige na origem, extrai e envia de novo, e a cadeia de aprovação recomeça. A aprovação do reitor é definitiva; depois dela, o Coletor bloqueia a reextração daquele modelo.

*Saiba Mais:* [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato#so-a-aprovacao-do-reitor-e-definitiva) › Só a Aprovação do Reitor é definitiva · [Fluxo de negócio]({{site.baseurl}}/documentacao/coletor/fluxo_de_negocio) › Homologação da Área

### Como funciona a prévia? Quem enviar depois de outubro fica sem ela?

A prévia sai todos os dias, de 01/11 a 13/12, com os dados de produção enviados até o dia anterior. Quem enviar depois de outubro continua tendo acesso. A prévia não depende de homologação, e a homologação (ambiente de testes) não tem prévia. Os indicadores de Sustentabilidade entram na prévia e na PNP pública.

### Onde estão o ofício, a nota técnica e as normas?

O Ofício Circular nº 99/2026/GAB/SETEC e a Nota Técnica nº 202/2026/CGPS/DDR/SETEC foram enviados às reitorias. O marco legal da PNP está no Guia. Dúvidas sobre o Sistec vão pelo Fale Conosco do MEC. Para localizar portarias em vigor, escreva para supervisao.cgps.ddr@mec.gov.br.

*Saiba Mais:* [Marco regulatório]({{site.baseurl}}/documentacao/pnp/marco_regulatorio) · [Referências]({{site.baseurl}}/documentacao/referencias/referencias)

### Os webinars foram gravados? Dá para marcar uma reunião com a equipe?

Os webinars sobre o Coletor não foram gravados, e o conteúdo está no [Manual de Operação do Coletor]({{site.baseurl}}/documentacao/coletor/manual_de_operacao). A reunião do FORTI em 04/09 foi gravada pelo próprio fórum. Para marcar uma reunião, abra um chamado com a pauta, as datas possíveis e os e-mails de quem vai participar.

## 7. Extensão

*Referência principal:* [contrato Ações de Extensão]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao). Cada modelo tem, na página, uma tabela de campos, as regras de qualidade e exemplos válidos e inválidos.

### Quais tabelas preciso enviar?

| Modelo | No fluxo | O que é |
| --- | --- | --- |
| `acoes_extensao` | Obrigatório | Uma linha por ação: projeto, curso, evento ou prestação de serviços |
| `pessoas_envolvidas_acoes_extensao` | Obrigatório | Equipe que executa: docente, TAE, estudante ou externo |
| `pessoas_atendidas_acoes_extensao` | Opcional | Público-alvo, com CPF e nome |
| `programa` | Opcional | Programas que agrupam as ações |

*Saiba Mais:* Ações de Extensão › [Modelos contidos]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao#modelos-contidos)

### Quais campos das ações são obrigatórios?

| Campo | Preenchimento | Observação |
| --- | --- | --- |
| `estrutura` | Obrigatório | Código do campus. Código inexistente reprova o teste |
| `area_tematica_cnpq` | Obrigatório | Código CNPq. Código inexistente gera só um aviso |
| `subeixo_tecnologico` | Obrigatório | Código do subeixo. Código inexistente reprova o teste |
| `parceria_institucional` | Obrigatório | Verdadeiro ou falso |
| `populacao_vulneravel` | Obrigatório | Verdadeiro ou falso |
| `instrumento_parceria` | Coluna opcional, mas cobrada por regra de qualidade | "Nenhum" quando não há parceria; Contrato, Convênio ou Acordo quando há |
| `tipo_vulnerabilidade` | Condicional | Lista obrigatória quando `populacao_vulneravel` é verdadeiro, e vazia quando é falso |
| `projeto_extensao_sustentavel` | Opcional | Só pode ser verdadeiro quando o tipo é "Projeto" |
| `municipios_atendidos` | Opcional | Lista de códigos IBGE, como `[2408102, 2403103]` |
| `produto`, `entidade_financiadora`, contrapartidas | Opcionais | Contrapartida externa maior que zero exige `entidade_financiadora` |

*Saiba Mais:* Ações de Extensão › [Modelo `acoes_extensao`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao#modelo-acoes_extensao) › Tabela de campos; Regras de qualidade

### Que regras de qualidade mais reprovam os dados enviados?

- A ação precisa ter ocorrido em pelo menos um dia de 2025: início até 31/12 e término, se houver, a partir de 01/01.
- O término não pode ser anterior ao início. Ação de um dia só é aceita; se o Coletor recusar, sincronize e extraia novamente.
- Ação "Finalizado" ou "Cancelado" precisa ter uma data de término.
- Uma pessoa não pode aparecer duas vezes na mesma ação, e o CPF deve ter 11 dígitos.
- Para pessoas envolvidas em ações de extensão, sejam alunos, docentes ou TAEs, é necessário informar a matrícula SISTEC para os alunos e a matrícula SIAPE para os servidores. ** O atributo matrícula é opcional apenas para os participantes externos. **

Violar uma regra não resulta em perda da extração: o contrato fica em "Qualidade Reprovada" e o envio fica bloqueado até a correção.

*Saiba Mais:* Ações de Extensão › Regras de qualidade (dos modelos [`acoes_extensao`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao#modelo-acoes_extensao) , [`pessoas_atendidas_acoes_extensao`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao#modelo-pessoas_atendidas_acoes_extensao) e [`pessoas_envolvidas_acoes_extensao`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao#modelo-pessoas_envolvidas_acoes_extensao)

### Como preencho as pessoas envolvidas?

- **`categoria`:** docente, TAE, estudante ou externo.
- **`matricula`:** SIAPE para docente e TAE; matrícula Sistec para estudante; vazia para externo. O par CPF + matrícula é conferido com os cadastros da PNP.
- **Situação:** "Ativo" não pode ter data de saída; "Inativo" precisa ter. O fim da ação não deixa ninguém inativo; "Inativo" é para quem saiu antes do fim.
- **Período:** a participação precisa ter durado pelo menos um dia em 2025.

*Saiba Mais:* Ações de Extensão › Modelo [`pessoas_envolvidas_acoes_extensao`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acoes_de_extensao#modelo-pessoas_envolvidas_acoes_extensao)`; `matricula` é roteada por `categoria`

### Qual a diferença entre pessoas envolvidas e pessoas atendidas?

Envolvidos são quem executa a ação. Atendidos são o público da ação, identificado por CPF e nome. Quem está na equipe não entra também como atendido na mesma ação.


Essa distinção deve ser observada no preenchimento, embora não seja verificada automaticamente pelas regras do contrato.

### Cursos online e programas com fomento externo entram?

Sim. Entram cursos presenciais e online, e todos os programas, com ou sem fomento externo, como o Mulheres Mil.

### Posso criar os IDs eu mesmo?

Pode. O `id_acao_extensao` é "fornecido pela instituição". Use uma sequência própria, sem repetir IDs.


## 8. Pesquisa e Inovação

### Produção com vários autores: repito o `id_producao`?

Sim. O modelo tem uma linha por autoria, e a chave é o par `id_producao` + `cpf`. O mesmo `id_producao` aparece em todas as linhas da produção, e o tipo, a classificação, o título e o ano precisam ser iguais em todas elas. Só docentes e TAEs entram, com matrícula SIAPE. O ano de publicação tem de ser 2025.

*Saiba Mais:* [Produção Intelectual]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/producao_intelectual) › Resumo do modelo; Tabela de campos; Regras de qualidade

### Em ativos de pesquisa, o que vai no campo "Estrutura"?

O código da estrutura a que o ativo está ligado, que o Coletor fornece. Quando os depósitos no INPI são feitos pela Agência de Inovação (NIT) da Reitoria, use a estrutura da Reitoria, e não a lotação dos pesquisadores. A exceção é quando o registro foi formalmente feito por outra unidade.

*Saiba Mais:* [Ativos de Pesquisa]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/ativos_pesquisa) › Tabela de campos

### Ativo com situação "Pedido em análise" dá erro de qualidade

Nesse caso, deixe a data de concessão e a validade vazias. As outras regras mais comuns:

- Situação "Ativo" exige data de concessão, e a concessão não pode ser anterior ao depósito.
- O depósito não pode ser posterior a 31/12/2025.
- Se o ativo foi transferido, a soma dos contratos de transferência, licenciamento e cessão precisa ser maior que zero; se não foi, essa soma precisa ser zero.
- Datas vão no formato AAAA-MM-DD.

*Saiba Mais:* [Ativos de Pesquisa]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/ativos_pesquisa) › Regras de qualidade; Exemplos inválidos

### O que entra em "Acordos de Parceria"?

Os instrumentos formais firmados com instituições externas, como acordos, convênios e contratos, com vigência, contrapartidas e estrutura. O modelo é opcional no fluxo. O número do acordo tem de ser único, e acordos formalizados depois de 31/12/2025 ficam para o próximo ciclo.

*Saiba Mais:* [Acordos de Parceria]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/acordos_de_parceria) › Resumo de negócio; Regras de qualidade

### A validação referencial reprovou pessoas que não estão na base. Posso incluí-las?

Não. O Coletor compara CPF e matrícula com os cadastros de servidores e de matrículas que a PNP envia na sincronização. Uma referência que não existe reprova o teste e bloqueia o envio. Retire dos modelos as pessoas que não constam na base do ano-base 2025.

*Saiba Mais:* [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial) › Os três modos; O que ela consegue conferir · [FAQ do Coletor]({{site.baseurl}}/documentacao/coletor/faq)

### Que matrícula do estudante devo informar?

A matrícula Sistec. O par CPF + matrícula precisa existir no cadastro de matrículas da PNP, que chega ao Coletor pela sincronização.

- Se tirar a matrícula direto do Sistec, use a coluna `CO_MATRICULA`.
- Se o estudante tiver mais de uma matrícula, use a do curso pelo qual ele participa do projeto.
- Estudante sem CPF fica fora do envio até o CPF ser regularizado. Não use CPF fictício.

*Saiba Mais:* [Projetos de Pesquisa]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) › Tabela de campos (`matricula`) · [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial) › `chave_composta` confere a tupla

### Existe ferramenta para tirar a produção intelectual em lote?

A PNP não oferece uma. Depende dos sistemas de cada instituição. O Coletor pode ler direto do sistema por API ou por banco de dados (seção 3); no SUAP, por exemplo, os dados do Lattes já vêm ligados aos servidores.

## 9. Orçamento

*Referência principal:* [contrato Orçamento]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/orcamento), versão 1.0.3 de 27/10/2026.

### Que dados orçamentários devo enviar?

A consulta completa de execução da instituição, com todos os Planos Internos. Não são só pesquisa e extensão; a separação por área é feita pela PNP. O Guia sugere uma consulta no Tesouro Gerencial com este filtro:

- **Item de informação:** 31 (DESPESAS LIQUIDADAS (CONTROLE EMPENHO)) e 44 (RESTOS A PAGAR NAO PROCESSADOS LIQUIDADOS).
- **Órgão UGE e Unidade Orçamentária:** os códigos da própria instituição.
- **Ano de lançamento:** 2025.
- **Métrica:** Movimento Líquido em R$.

O item 31 alimenta `liquidado_valor`, e o item 44 alimenta `rp_pago_valor`.

*Saiba Mais:* Orçamento › Resumo de negócio; [Uso do Tesouro Gerencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/orcamento#uso-do-tesouro-gerencial)

### Que erros de preenchimento mais reprovam?

| Campo | Regra |
| --- | --- |
| `programa_interno_cod` | Código completo do PI, com exatamente 11 caracteres e como texto (por exemplo, `M20RLP0100N`). "20" ou "21" sozinhos são reprovados |
| `ano` | Campo obrigatório desde a versão 1.0.2; tem de ser 2025, como número inteiro |
| `uo_cod` | Tem de ser o código da UO da própria instituição |
| `orgao_superior_cod`, `gnd_cod` | Vão como texto (`"26000"`, `"3"`), e não como número |
| `origem_despesa` | "Proposta do executivo", "Emenda" ou "-". Com "Emenda", o tipo e o número/ano da emenda são obrigatórios |
| `liquidado_valor`, `rp_pago_valor` | Obrigatórios e não podem ser negativos |
| Colunas a mais | São rejeitadas. Uma coluna `empenhado_valor`, por exemplo, reprova o envio |

*Saiba Mais:* Orçamento › [Tabela de campos]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/orcamento#modelo-dados_orcamentarios)

### Como ligo as colunas do Tesouro Gerencial aos campos da planilha?

| Campo | Coluna no Tesouro Gerencial | Exemplo |
| --- | --- | --- |
| `fonte_cod` | Fonte Recursos Detalhada | 1050000219 |
| `fonte_grupo_cod` | Grupo Fonte | 1 |
| `fonte_especificacao_cod` | Fonte Recursos ou Fonte Recursos Reduzida | 050 |


### A regra "o código UO deve ser da instituição" está reprovando, mesmo com o código certo

A regra compara com o código que a PNP devolve para a instituição. Se o Coletor ainda não tem esse código, o teste reprova. Abra Configurações e clique em Salvar. Se o campo Código continuar vazio, atualize o Coletor (`coletor update`), sincronize e salve as Configurações de novo.

*Saiba Mais:* Orçamento › [Regras de qualidade]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/orcamento#regras-de-qualidade) (Código da instituição)

### O contrato de Orçamento aparece como "Somente Modelos Opcionais". É erro?

Não. O modelo `dados_orcamentarios` é opcional no fluxo. Ele só passa a ser cobrado depois que alguém cadastra uma Configuração de Extração para ele.

*Saiba Mais:* Orçamento › [Modelos contidos]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/orcamento#modelos-contidos)

## 10. Sustentabilidade

*Referências principais:* [contrato Sustentabilidade]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sustentabilidade), [contrato Pessoal Terceirizado]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/pessoal_terceirizado) e [Indicadores de Sustentabilidade]({{site.baseurl}}/documentacao/usuarios-especializados/indicadores_de_sustentabilidade).

### Água e energia: soma do ano ou média mensal?

Soma do ano. `agua_consumo` e `energia_consumo` são a soma dos 12 meses, e `prod_energia_renovavel` é a produção anual. Os indicadores SCAG, SCEE e SGER dividem esses valores pela comunidade interna (CI). Use m³ para água e kWh para energia. O sistema não confere a unidade, então um valor em MWh entra mil vezes menor. Cada estrutura tem um registro só.

*Saiba Mais:* Sustentabilidade › [Modelo `agua_energia`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sustentabilidade#modelo-agua_energia) · Indicadores › SCAG; SCEE; SGER

### Como preencho instâncias de governança e canais de divulgação?

Os dois campos são listas de códigos, uma linha por estrutura, e cada código entra uma vez só. Três comissões e um núcleo, por exemplo, ficam `["COM", "NUC"]`. O valor de IG e de DIV é a quantidade de códigos diferentes. Use `NEN` quando não houver nenhum, sem combinar com outros códigos.

- **Instâncias:** COO, DEP, DIR, PRO, COM, NUC, GT, CAM, CON, CMT, OUT e NEN.
- **Canais:** PI (páginas na internet), RS (redes sociais), ER (eventos realizados), MD (materiais didáticos) e NEN. E-mail institucional não é canal.
- **Onde contar o canal:** uma página geral de sustentabilidade da instituição conta para a Reitoria (ou a Direção-Geral, no Cefet). Uma página de um campus conta só para aquele campus.

*Saiba Mais:* Sustentabilidade › Modelo [`governanca_gestao_sustentabilidade`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sustentabilidade#modelo-governanca_gestao_sustentabilidade) (legendas e regras) · Indicadores › SIGS; SIDS

### O que conta como "normativo" de compras sustentáveis?

Conta um ato normativo da própria instituição sobre critérios de sustentabilidade nas compras e contratações, como resolução, portaria ou instrução normativa. O indicador SICS vale 0 ou 1 e só se aplica às estruturas que fazem compras.

*Saiba Mais:* Indicadores › SICS · Sustentabilidade › Modelo [`compras_contratacoes`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sustentabilidade#modelo-compras_contratacoes) (`normativo_compras_sustentaveis`)

Seguir só a legislação federal não basta. Editais não contam, e o normativo vale apenas para a estrutura que o publicou.

### Como conto compras e contratações, gerais e sustentáveis?

- **Compras** são bens e materiais. **Contratações** são serviços, obras e todo o resto.
- **Sustentável** é a compra ou contratação efetivada no ano de referência com pelo menos um critério de sustentabilidade. O número de sustentáveis não pode passar do total; se passar, o teste reprova.
- **Efetivada** é a compra concluída em 2025. A referência pode ser a liquidação, e não a licitação, a assinatura ou o pagamento.
- **Registro de preços:** conta cada contratação feita a partir da ata.

*Saiba Mais:* Sustentabilidade › Modelo [`compras_contratacoes`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/sustentabilidade#modelo-compras_contratacoes) (tabela de campos e regras) · Indicadores › SPCS

### Quais terceirizados entram em `servidor_terceirizado`?

Os terceirizados que atuaram na estrutura, um por linha, com CPF, datas de ingresso e de saída e situação. "Ativo" pode ter data de saída futura, como o fim previsto do contrato. "Inativo" precisa ter data de saída até hoje. Eles entram na comunidade interna (CI) dos indicadores de água e energia.

*Saiba Mais:* [Pessoal Terceirizado]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/pessoal_terceirizado#modelo-servidor_terceirizado) › Tabela de campos; Regras de qualidade · Indicadores › SCAG (variável CI)

### Indicador SPRO: de onde vêm os dados e o que é um projeto "sustentável"?

O SPRO divide os projetos de ensino, pesquisa e extensão ligados à sustentabilidade pelo total de projetos da estrutura no ano. Os dados são os enviados pelo Coletor, nos campos de sustentabilidade de cada contrato. Na Extensão, só contam as ações do tipo "Projeto", que são também as únicas que podem ser marcadas como sustentáveis.


A ligação com um ODS, por si só, não basta: o projeto precisa trazer as dimensões ambiental, social e econômica no conteúdo, nos objetivos ou nos resultados.

## Veja também

- [Glossário do Coletor]({{site.baseurl}}/documentacao/coletor/glossario)
- [Quando algo falha]({{site.baseurl}}/documentacao/coletor/quando_algo_falha) — o roteiro completo de diagnóstico
