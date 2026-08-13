---
layout: default
title: "Validação e qualidade"
toc: true
---
# Validação e qualidade

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Esta página descreve as duas camadas de validação que rodam sobre os dados de um **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** no Coletor — schema (durante a extração) e qualidade (testes do contrato) — e como ler o relatório de testes.

## Duas camadas de validação

| Camada | Quando roda | O que valida |
|---|---|---|
| **Schema (extração)** | Assim que a fonte devolve os dados, antes de gravar o **[Parquet]({{ site.baseurl }}/documentacao/coletor/glossario#parquet)** | Colunas obrigatórias presentes; tipos básicos (string, integer, double, boolean, date, array); **rejeita colunas extras** sempre |
| **Qualidade (teste do contrato)** | Automaticamente, ao fim de uma extração bem-sucedida | Regras **[SodaCL]({{ site.baseurl }}/documentacao/coletor/glossario#sodacl)** declaradas no bloco `quality:` do YAML |

A primeira camada é **bloqueante**: se a extração rejeitar, nenhum Parquet é gravado e o **[Registro de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-extracao)** entra com status de falha.

A segunda **não é disparada pelo operador** — não existe botão "Executar Testes" no painel. Ela roda sozinha ao final da extração, e só quando *todos* os modelos cobrados do contrato foram extraídos com sucesso (não faz sentido testar um contrato incompleto). Modelos **opcionais** sem Configuração de Extração não entram nessa conta: a extração em lote os pula de propósito, porque tentar extrair um modelo sem provedor derrubaria a tarefa inteira e o teste de qualidade nem chegaria a rodar. Como consequência, um teste de qualidade reprovado aparece no fluxo como **"Falha na Extração"**, e não como um estado próprio.

> ℹ️ **Bloco `quality` ausente em todos os contratos hoje.** Nenhum dos onze contratos da PNP populou o bloco [`quality`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-quality). Logo, o teste verifica hoje apenas a estrutura básica: que o Parquet exista, seja legível e não esteja corrompido. Quando os checks SodaCL forem adicionados, a validação ganha conteúdo de domínio (chave única, valores em enum, frescor temporal, etc.).

## Como o teste roda

Ao final de uma extração bem-sucedida, o Coletor envia o schema do contrato ao serviço de validação (`datacontract-cli`, que roda como um componente da própria stack) e indica onde estão os Parquets recém-gerados. O serviço carrega os arquivos, executa os checks e devolve um relatório, que fica registrado junto ao contrato.

O teste passa só se **nenhum** check falhou — avisos (`warn`) são tolerados. Uma falha de comunicação com o serviço de validação também conta como teste falho, com a mensagem de erro registrada.

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
4. Algum modelo **que conta no fluxo** sem Configuração de Extração → "Modelos Não Configurados".
5. Algum modelo nunca extraído → "Aguardando Extração".
6. Modelo ou configuração alterados depois da última extração → "Reextração Necessária".
7. Última extração com falha → "Falha na Extração" — inclui o caso de o **teste de qualidade** ter reprovado, já que ele roda dentro da extração.
8. Conforme o estado das validações na PNP → "Aguardando Validação PNP", "Validação Rejeitada", "Aguardando Homologação da Área" ou "Aguardando Aprovação do Reitor".
9. Aprovado pelo Reitor → "Sincronizado com Sucesso" — terminal.
10. Caso contrário → "Pronto para Sincronizar".

> ℹ️ **"Modelo que conta no fluxo" a partir do passo 4.** Um modelo **opcional** (`meta.required: false`) só entra nas condições 4 em diante depois de ganhar uma Configuração de Extração; enquanto não ganha, é como se não estivesse ali para efeito de status. Modelo **desabilitado** (`meta.disabled: true`) sequer é importado. Ver [Bloco `meta`]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml#bloco-meta).

A máquina de estados tem hoje **12 códigos de status e 13 rótulos** — dois rótulos compartilham o mesmo código ("Sem Modelos" e "Modelos Não Configurados"), e "Reextração Necessária" cobre dois sub-casos. A tabela completa de estados e transições está em [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato).

## Veja também

- [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato)
- [Anatomia do YAML do Contrato]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Quando algo falha]({{ site.baseurl }}/documentacao/coletor/quando_algo_falha) — o roteiro de diagnóstico do operador
