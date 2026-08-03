---
layout: default
title: "Perguntas frequentes"
---

# Perguntas frequentes

> **Para quem é:** 👔 gestores · 🔌 integradores

Perguntas reais que aparecem com frequência durante a operação do Coletor. Cada pergunta linka para a página onde o assunto é detalhado, quando aplicável.

### P: A extração funcionou, mas o teste do contrato falhou. O que fazer?

O teste de qualidade roda **dentro** da extração, então um teste reprovado aparece como "Falha na Extração", não como um estado próprio — não há botão "Executar Teste". Abra o relatório em **Contratos → o contrato → resultados de teste** para identificar quais campos falharam (tipo, obrigatoriedade, domínio de valores). A partir daí, decida entre **corrigir os dados na fonte** (quando o contrato reflete a regra correta) ou **reportar à equipe da PNP** (quando a regra do YAML parece mais estrita do que o combinado). Detalhes em [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade).

### P: A PNP não recebeu os dados — onde olho primeiro?

Abra o registro mais recente em **Envios** (`/painel/sincronizacoes/`) e leia os detalhes — eles guardam a resposta completa devolvida pela API da PNP, com código HTTP e mensagem de erro. Em seguida, confira se a URL da PNP aponta para o ambiente correto (visível em **Configurações**, para administradores). Se a resposta for 401/403, a instância pode ter perdido a autenticação: reinicie a stack (`coletor down` seguido de `coletor up`) para reativá-la — os dados são preservados. O fluxo completo está em [Sincronização com a PNP]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

### P: Reenviei os dados e a rejeição continua. Por quê?

A PNP identifica cada dataset pelo **conteúdo** (checksum). Reextrair e reenviar um dado idêntico devolve o mesmo dataset com o status antigo — inclusive uma rejeição anterior. Para mudar o estado na PNP, o dado precisa efetivamente mudar na origem. Ver [Quando algo falha]({{ site.baseurl }}/documentacao/coletor/quando_algo_falha).

### P: Quais bancos de dados são suportados como fonte?

Sete: **PostgreSQL, MySQL/MariaDB, SQL Server, SQLite, IBM Db2, MongoDB e CouchDB**. Além de bancos, o Coletor extrai de APIs HTTP, planilhas online (Google Docs, Dropbox, SharePoint) e upload de planilha (XLS/XLSX/ODS). Ver [Operação passo a passo]({{ site.baseurl }}/documentacao/coletor/operacao_passo_a_passo).

### P: Posso disparar uma extração fora da janela do ciclo de coleta?

Não — fora da janela principal e da janela de correção, extração e envio são **bloqueados**: o sistema recusa a ação antes de qualquer tarefa entrar na fila, com a mensagem "Extração não permitida". Um contrato sem ciclo de coleta associado também conta como bloqueado. O comportamento de cada fase está descrito em [Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta).

### P: Um contrato (ou um modelo) sumiu do painel depois de sincronizar. O que houve?

Quase sempre é a PNP tendo **desabilitado** aquele modelo nesta versão do contrato (`meta.disabled: true` no YAML). Modelo desabilitado não é importado e, se já existia, sai de vista na sincronização seguinte; contrato que fica **sem nenhum modelo habilitado** desaparece inteiro pelo mesmo motivo. Não é erro nem falha de sincronização, e nada é apagado de fato: a remoção é lógica, e extrações, envios e arquivos já gerados continuam guardados — continuam listados nas telas de **Extrações** e **Envios**, que mostram o histórico por conta própria; o que sai de vista são as listagens de **Contratos** e **Modelos de Dados**. Se a PNP reabilitar o modelo mais adiante, ele volta "zerado": a Configuração de Extração anterior precisa ser refeita. Ver [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

### P: Um contrato aparece como "Somente Modelos Opcionais". Preciso fazer alguma coisa?

Não, a menos que a instituição queira coletar aquele dado. O badge significa que **todos** os modelos daquele contrato são [opcionais]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-opcional) e nenhum foi configurado — "não há nada a coletar". Esses contratos ficam fora do progresso do wizard, o que explica o painel marcar 8/8 (ou `1/1`) com contratos ainda "não coletados" na tela, e as ações em lote sumirem. Para coletar um deles, crie a Configuração de Extração do modelo: a partir daí ele passa a ser cobrado normalmente.

### P: Configurei um modelo opcional e agora o contrato voltou atrás. É bug?

Não. Modelo opcional só é invisível ao fluxo **enquanto ninguém o configura**. Assim que ganha uma Configuração de Extração, ele conta como qualquer modelo obrigatório: o contrato volta para "Aguardando Extração" e só fecha quando aquele modelo também for extraído, enviado, homologado e aprovado. Se a intenção era não coletá-lo, remova a configuração — o contrato sai do fluxo de novo.

### P: Atualizei o Coletor. Preciso fazer algo para as marcações de modelo valerem?

Sim: rode **"Sincronizar com a PNP"** uma vez. Logo após a atualização, todos os modelos existentes continuam tratados como obrigatórios (o comportamento antigo); as marcações `meta.required` e `meta.disabled` do contrato só entram em vigor na primeira sincronização depois da atualização.

### P: Excluí um Contrato de Dados por engano. Perdi tudo?

Não. A exclusão no Coletor é **lógica**: o registro permanece no banco, apenas marcado como excluído, e o histórico de extrações e envios é preservado para auditoria. A restauração exige intervenção técnica (não há botão no painel) — acione o suporte do Coletor. Se o ciclo ainda permitir, re-sincronizar com a PNP também recria contratos e modelos do ciclo vigente.

### P: O painel diz que o Coletor não está configurado. E agora?

Essa mensagem aparece quando a instância nunca passou pelo setup inicial (ou quando o banco foi recriado com `coletor down --wipe`). Acesse o painel sem nenhum usuário cadastrado e a tela de configuração inicial aparece no lugar do login. Ver [Primeiro acesso]({{ site.baseurl }}/documentacao/coletor/primeiro_acesso).

### P: Quero estender o Coletor (novo tipo de provedor, novo banco). Onde está a documentação?

A documentação técnica de arquitetura e extensão do código não faz parte deste guia — está no [site de documentação do Coletor](https://pnp-ccv.github.io/coletor-pnp-microdados/), trilha "Técnica".

### Veja também

- [Glossário do Coletor]({{ site.baseurl }}/documentacao/coletor/glossario)
- [Quando algo falha]({{ site.baseurl }}/documentacao/coletor/quando_algo_falha) — o roteiro completo de diagnóstico
