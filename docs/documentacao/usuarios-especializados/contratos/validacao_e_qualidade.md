---
layout: default
title: "Validação e qualidade"
toc: true
---
# Validação e qualidade

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página descreve as camadas de validação que rodam sobre os dados de um **[Contrato de Dados]({{site.baseurl}}/documentacao/coletor/glossario#contrato-de-dados)** no Coletor — schema e referências (durante a extração) e qualidade (testes do contrato) — e como ler o relatório de testes.

## As camadas de validação

| Camada | Quando roda | O que valida |
|---|---|---|
| **Schema (extração)** | Assim que a fonte devolve os dados, antes de gravar o **[Parquet]({{site.baseurl}}/documentacao/coletor/glossario#parquet)** | Colunas obrigatórias presentes; tipos básicos (string, integer, double, boolean, date, array); **rejeita colunas extras** sempre |
| **Referencial (extração)** | Depois de consolidar os dados do modelo, antes de gravar o Parquet | Se os códigos de campus, município, área e subeixo — e os CPFs — existem nos cadastros da Rede sincronizados localmente. Ver [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial) |
| **Qualidade (teste do contrato)** | Automaticamente, ao fim de uma extração bem-sucedida | Regras **[SodaCL]({{site.baseurl}}/documentacao/coletor/glossario#sodacl)** declaradas no bloco `quality:` do YAML |

A primeira camada é **bloqueante**: se a extração rejeitar, nenhum Parquet é gravado e o **[Registro de Extração]({{site.baseurl}}/documentacao/coletor/glossario#registro-de-extracao)** entra com status de falha.

A camada referencial confere e **anota**, sem derrubar a extração: o apontamento é somado às regras de qualidade no teste do contrato, e é lá que uma referência declarada como `severidade: erro` reprova e barra o envio (`severidade: aviso` vira alerta e não reprova). O ganho de juntar as duas coisas num resultado só é o operador ver de uma vez tudo o que precisa corrigir, em vez de descobrir um problema por extração. Quem regula a rigidez é o próprio contrato, campo a campo — a variável de ambiente que muda o modo é alavanca de emergência da CCV. Os três modos e a gramática `referencia_pnp` estão em [Validação referencial]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/validacao_referencial).

A segunda **não é disparada pelo operador** — não existe botão "Executar Testes" no painel. Ela roda sozinha ao final da extração, e só quando *todos* os modelos cobrados do contrato foram extraídos com sucesso (não faz sentido testar um contrato incompleto). Modelos **opcionais** sem Configuração de Extração não entram nessa conta: a extração em lote os pula de propósito, porque tentar extrair um modelo sem provedor derrubaria a tarefa inteira e o teste de qualidade nem chegaria a rodar. Um teste reprovado deixa o contrato em **"Qualidade Reprovada"**: os dados foram extraídos e o Parquet continua gravado, mas o envio à PNP fica bloqueado até a linha ser corrigida na origem e o contrato ser reextraído.

> ℹ️ **O bloco `quality` chega pelo schema sincronizado da PNP.** As regras de qualidade não estão nos arquivos que o Coletor traz de fábrica: elas vêm no YAML que a sincronização baixa, então um contrato pode estar verificando dezenas de regras que nenhum arquivo local mostra — Ações de Extensão, por exemplo, traz dez. Para ver o que um contrato de fato verifica, olhe **Ver resultados de teste** no painel.

### Tokens nas regras de qualidade

Uma regra `quality` pode usar dois tokens, que o Coletor substitui no texto do contrato antes de rodar o teste:

- **`#ANO_REFERENCIA#`** — o **ano-base** da coleta, `ciclo.ano - 1` (o ciclo de 2026 coleta o que aconteceu em 2025). Contrato que usa o token sem ciclo de coleta associado falha com erro explícito.
- **`#CODIGO_INSTITUICAO#`** — o código da instituição na PNP (IFRN é `26435`), obtido quando a instância é ativada. Se o código ainda não foi obtido, porque a instância não foi reativada depois da atualização, o teste do contrato reprova com erro explícito. Para resolver, salve as **Configurações** da instância: isso a reativa e busca o código na PNP.

```sql
SELECT COUNT(*) FROM dados_orcamentarios
WHERE ano <> #ANO_REFERENCIA# OR uo_cod <> '#CODIGO_INSTITUICAO#'
```

> ⚠️ **Não confunda com os tokens da extração.** `#ANO_CORRENTE#`, `#DATA_REFERENCIA#` e os demais tokens das consultas de extração são outro conjunto, resolvido em outro momento. Um token de extração escrito numa regra `quality` **não** é substituído, e vice-versa.

## Como o teste roda

Ao final de uma extração bem-sucedida, o próprio Coletor monta o schema do contrato e roda o motor do `datacontract` no seu processo, apontando para os Parquets recém-gerados. O motor carrega os arquivos, executa os checks e devolve um relatório, que fica registrado junto ao contrato.

O teste passa só se **nenhum** check falhou — avisos (`warn`) são tolerados. Um erro do próprio motor (YAML que ele recusa, por exemplo) também conta como teste falho, com a mensagem registrada.

> ℹ️ **O schema enviado ao teste é o YAML inteiro.** Ele inclui os modelos opcionais que ninguém configurou — eles ficam de fora do *status*, dos *contadores* e da *extração em lote*, mas continuam aparecendo no schema submetido ao serviço de validação. Se o relatório mencionar um modelo que a instituição não coleta, é isso.

## Visualização do relatório

A tela **Contratos → o contrato → resultados de teste** apresenta o último relatório: status geral, contagens de checks aprovados/reprovados, lista de checks com filtro por modelo e mensagem de erro detalhada quando houver.

## Como ler um relatório SodaCL

Quando o bloco `quality` for populado, cada check no relatório tem mais ou menos esta forma:

```json
{
  "name": "duplicate_count(id_acao_extensao) = 0",
  "result": "passed",
  "model": "acoes_extensao",
  "field": "id_acao_extensao",
  "diagnostics": {"value": 0}
}
```

Campos relevantes:

- `result` — `passed`, `failed`, `warn` ou `error`. `warn` indica observação não-bloqueante; `error` indica que o check não pôde sequer rodar.
- `model` / `table` — qual modelo/tabela do contrato.
- `field` — coluna alvo (opcional, depende do tipo de check).
- `diagnostics` — payload com contagens e linhas falhas (quando o check as declara).

## Tipos de check SodaCL típicos

Estes são os formatos mais comuns para os contratos da PNP — sintaxe completa em [docs.soda.io](https://docs.soda.io/soda-cl/soda-cl-overview.html):

- `row_count > 0` — rejeita arquivos vazios.
- `duplicate_count(<col>) = 0` — chave única.
- `missing_count(<col>) = 0` — coluna não pode ter nulos.
- `freshness(<timestamp_col>) < 30d` — dado precisa ser recente.
- `failed rows query: <SQL>` — consulta customizada para regras complexas.

## Como o resultado move o status do contrato

O status do contrato é calculado em tempo real, avaliando as condições nesta ordem — a primeira que casa define o badge:

1. **Ciclo bloqueado** (inativo ou fora do prazo) → "Ciclo de Coleta inativo". Tem prioridade sobre tudo.
2. Sem modelos → "Sem Modelos".
3. Só modelos **opcionais** (`meta.required: false`) e nenhum deles configurado → "Somente Modelos Opcionais" — não há nada a coletar, e o contrato fica fora do progresso do assistente.
4. **Todos** os modelos que contam no fluxo já aprovados pelo Reitor → "Sincronizado com Sucesso" — terminal. É checado antes de olhar extração e teste, para um contrato já aprovado não voltar a "Falha" por causa de um registro posterior.
5. Algum modelo **que conta no fluxo** sem Configuração de Extração → "Modelos Não Configurados".
6. Algum modelo nunca extraído → "Aguardando Extração".
7. Modelo ou configuração alterados depois da última extração → "Reextração Necessária".
8. Última extração de algum modelo com falha → "Falha na Extração" — falha real de extração (schema, fonte de dados, conexão); **não** é onde uma regra de qualidade aparece.
9. Todos os modelos extraídos com sucesso → olha o último teste do contrato:
   - sem teste, ou teste anterior à última extração → "Reextração Necessária";
   - teste reprovado → "Qualidade Reprovada" — mesmo código de "Falha na Extração", rótulo diferente: os dados foram extraídos, só o envio está bloqueado.
10. Teste aprovado → conforme o estado das validações na PNP: "Aguardando Validação PNP", "Validação Rejeitada", "Aguardando Homologação da Área" ou "Aguardando Aprovação do Reitor"; sem nenhuma sincronização ainda → "Pronto para Sincronizar".

> ℹ️ **"Modelo que conta no fluxo" a partir do passo 4.** Um modelo **opcional** (`meta.required: false`) só entra nas condições 4 em diante depois de ganhar uma Configuração de Extração; enquanto não ganha, é como se não estivesse ali para efeito de status. Modelo **desabilitado** (`meta.disabled: true`) sequer é importado. Ver [Bloco `meta`]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta).

A máquina de estados tem hoje **12 códigos de status e 14 rótulos** — dois códigos têm dois rótulos cada ("Sem Modelos"/"Modelos Não Configurados" e "Falha na Extração"/"Qualidade Reprovada"), e "Reextração Necessária" cobre dois sub-casos. A tabela completa de estados e transições está em [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato).

## Veja também

- [Status do contrato]({{site.baseurl}}/documentacao/coletor/status_do_contrato)
- [Anatomia do YAML do Contrato]({{site.baseurl}}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Quando algo falha]({{site.baseurl}}/documentacao/coletor/quando_algo_falha) — o roteiro de diagnóstico do operador
