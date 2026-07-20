---
layout: default
title: "Perguntas frequentes"
---

# Perguntas frequentes

> **Para quem é:** 👔 gestores · 🔌 integradores

Perguntas reais que aparecem com frequência durante a operação do Coletor. Cada pergunta linka para a página onde o assunto é detalhado, quando aplicável.

### P: A extração funcionou, mas o teste do contrato falhou. O que fazer?

O teste de qualidade roda **dentro** da extração, então um teste reprovado aparece como "Falha na Extração", não como um estado próprio — não há botão "Executar Teste". Abra o relatório em **Contratos → o contrato → resultados de teste** para identificar quais campos falharam (tipo, obrigatoriedade, domínio de valores). A partir daí, decida entre **corrigir os dados na fonte** (quando o contrato reflete a regra correta) ou **reportar à equipe da PNP** (quando a regra do YAML parece mais estrita do que o combinado). Detalhes em [Validação e qualidade](/documentacao/usuarios-especializados/contratos/validacao_e_qualidade).

### P: A PNP não recebeu os dados — onde olho primeiro?

Abra o registro mais recente em **Envios** (`/painel/sincronizacoes/`) e leia os detalhes — eles guardam a resposta completa devolvida pela API da PNP, com código HTTP e mensagem de erro. Em seguida, confira se a URL da PNP aponta para o ambiente correto (visível em **Configurações**, para administradores). Se a resposta for 401/403, a instância pode ter perdido a autenticação: reinicie a stack (`coletor down` seguido de `coletor up`) para reativá-la — os dados são preservados. O fluxo completo está em [Sincronização com a PNP](/documentacao/usuarios-especializados/contratos/sincronizacao_pnp).

### P: Reenviei os dados e a rejeição continua. Por quê?

A PNP identifica cada dataset pelo **conteúdo** (checksum). Reextrair e reenviar um dado idêntico devolve o mesmo dataset com o status antigo — inclusive uma rejeição anterior. Para mudar o estado na PNP, o dado precisa efetivamente mudar na origem. Ver [Quando algo falha](/documentacao/coletor/quando_algo_falha).

### P: Quais bancos de dados são suportados como fonte?

Sete: **PostgreSQL, MySQL/MariaDB, SQL Server, SQLite, IBM Db2, MongoDB e CouchDB**. Além de bancos, o Coletor extrai de APIs HTTP, planilhas online (Google Docs, Dropbox, SharePoint) e upload de planilha (XLS/XLSX/ODS). Ver [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo).

### P: Posso disparar uma extração fora da janela do ciclo de coleta?

Não — fora da janela principal e da janela de correção, extração e envio são **bloqueados**: o sistema recusa a ação antes de qualquer tarefa entrar na fila, com a mensagem "Extração não permitida". Um contrato sem ciclo de coleta associado também conta como bloqueado. O comportamento de cada fase está descrito em [Ciclo de coleta](/documentacao/coletor/ciclo_de_coleta).

### P: Excluí um Contrato de Dados por engano. Perdi tudo?

Não. A exclusão no Coletor é **lógica**: o registro permanece no banco, apenas marcado como excluído, e o histórico de extrações e envios é preservado para auditoria. A restauração exige intervenção técnica (não há botão no painel) — acione o suporte do Coletor. Se o ciclo ainda permitir, re-sincronizar com a PNP também recria contratos e modelos do ciclo vigente.

### P: O painel diz que o Coletor não está configurado. E agora?

Essa mensagem aparece quando a instância nunca passou pelo setup inicial (ou quando o banco foi recriado com `coletor down --wipe`). Acesse o painel sem nenhum usuário cadastrado e a tela de configuração inicial aparece no lugar do login. Ver [Primeiro acesso](/documentacao/coletor/primeiro_acesso).

### P: Quero estender o Coletor (novo tipo de provedor, novo banco). Onde está a documentação?

A documentação técnica de arquitetura e extensão do código não faz parte deste guia — está no [site de documentação do Coletor](https://pnp-ccv.github.io/coletor-pnp-microdados/), trilha "Técnica".

### Veja também

- [Glossário do Coletor](/documentacao/coletor/glossario)
- [Quando algo falha](/documentacao/coletor/quando_algo_falha) — o roteiro completo de diagnóstico
