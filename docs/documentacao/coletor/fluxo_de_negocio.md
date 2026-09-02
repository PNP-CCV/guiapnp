---
layout: default
title: "Fluxo de negócio"
toc: true
---

# Fluxo de negócio

* TOC
{:toc}

> **Para quem é:** 👔 gestores · 🔌 integradores

Esta página percorre o fluxo de ponta a ponta — do cadastro do **[Provedor de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#provedor-de-dados)** até a **[Aprovação do Reitor]({{ site.baseurl }}/documentacao/coletor/glossario#aprovacao-do-reitor)** na PNP — em linguagem de negócio. Antes de ler, recomenda-se passar pela [Visão geral]({{ site.baseurl }}/documentacao/coletor/visao_geral) para entender o papel do sistema na cadeia de coleta.

## Visão macro do fluxo

```text
NO COLETOR (instituição)
  Provedor de Dados → Configuração de Extração → Modelo de Dados → Contrato de Dados
  Modelo de Dados → Extração → Teste do Contrato → Sincronização com a PNP
                                                            │
NA PNP (MEC)                                                ▼
  Validação estrutural → Homologação da Área → Aprovação do Reitor
```

> ℹ️ **As três últimas etapas não acontecem no Coletor.** Validação, homologação e aprovação são feitas **na PNP**. O Coletor não tem botão para nenhuma delas: ele apenas **consulta** o resultado e reflete no status do contrato. Se a coleta travou nessas etapas, o caminho é falar com o gestor da área ou com a reitoria — não mexer no sistema.

## Cada etapa em 2-3 linhas

### Provedor de Dados

O Provedor de Dados representa uma fonte concreta de microdados — uma API, um banco relacional, uma planilha online ou uma planilha enviada por upload. O cadastro guarda as credenciais e o endereço de acesso.

### Configuração de Extração

A **[Configuração de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#configuracao-de-extracao)** liga um Provedor a um Modelo, dizendo *como* aquele dado é obtido daquela fonte: endpoint da API, query SQL, nome da aba da planilha. É a unidade que o operador edita com mais frequência.

### Modelo de Dados

O **[Modelo de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-de-dados)** é uma tabela lógica única dentro de um contrato — por exemplo, `acoes_extensao` ou `projetos_de_pesquisa`. Cada modelo tem um schema próprio (colunas, tipos, restrições) e uma ou mais Configurações de Extração apontando para os Provedores que o alimentam.

O contrato também diz **se cada modelo é cobrado**: modelos [obrigatórios]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-obrigatorio) sempre seguram o fluxo; modelos [opcionais]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-opcional) só passam a segurar depois que alguém configura a extração deles; e modelos [desabilitados]({{ site.baseurl }}/documentacao/coletor/glossario#modelo-desabilitado) pela PNP nem chegam a ser importados. Quem decide é a PNP, no YAML do contrato — a instituição não altera isso no painel. Detalhes em [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#modelos-obrigatorios-opcionais-e-desabilitados).

### Contrato de Dados

O **[Contrato de Dados]({{ site.baseurl }}/documentacao/coletor/glossario#contrato-de-dados)** agrupa um conjunto coerente de Modelos relacionados, com schema, regras de qualidade e metadados de governança expressos em um arquivo YAML. Cada contrato pertence a um **[Ciclo de Coleta]({{ site.baseurl }}/documentacao/coletor/glossario#ciclo-de-coleta)** e tem uma versão.

> ℹ️ **Nem todo contrato do catálogo chega ao painel.** Se a PNP desabilitou **todos** os modelos de um contrato nesta versão, o contrato não é criado no Coletor — e, se já existia, sai de vista na sincronização seguinte. Não é erro nem falha de sincronização: é o contrato dizendo que não há o que coletar. A remoção é lógica, o histórico continua guardado.

### Extração

A extração lê os dados do Provedor segundo a Configuração de Extração, normaliza colunas e tipos para o schema do contrato, e grava um arquivo **[Parquet]({{ site.baseurl }}/documentacao/coletor/glossario#parquet)** local. Cada execução, bem-sucedida ou não, gera um **[Registro de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-extracao)** com motivo do erro e detalhes técnicos.

### Teste do Contrato

Os testes de qualidade rodam **dentro da extração**: a ferramenta de validação lê os Parquets gerados, confere schema e executa as regras de qualidade descritas no YAML. O resultado fica registrado no contrato e habilita ou bloqueia a próxima etapa.

### Sincronização com a PNP

Com o teste aprovado, a sincronização envia cada Parquet à API da **[PNP]({{ site.baseurl }}/documentacao/coletor/glossario#pnp)** mantida pelo **[MEC]({{ site.baseurl }}/documentacao/coletor/glossario#mec)**. Cada tentativa é registrada em um Registro de Sincronização, com status HTTP, resposta da API e timestamps, garantindo a rastreabilidade do que foi efetivamente entregue.

Enviar não encerra o fluxo: o contrato entra em "Aguardando Validação PNP" e o Coletor passa a acompanhar o que acontece do outro lado, gravando cada mudança em um **[Registro de Validação de Modelo]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-validacao-de-modelo)**.

### Validação estrutural (na PNP)

A PNP confere o parquet recebido por conta própria. Além do schema, roda uma **validação referencial**: campos que apontam para entidades da Rede — campus, área temática, município — precisam existir de fato no cadastro dela. Um dado pode passar no contrato e ainda assim ser rejeitado aqui, por exemplo com o código de campus de outra instituição.

O Coletor passou a **antecipar essa mesma conferência na extração**, usando os cadastros que ele já sincroniza da PNP. De fábrica ela só *aponta* a divergência, sem bloquear — mas o erro aparece no dia da extração, não dias depois. Ver [Validação referencial]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_referencial).

### Homologação da Área (na PNP)

O **Gestor de Área Temática** revisa o que a sua área enviou e decide. Cada área responde pelos seus dados — Extensão homologa Extensão, Pesquisa homologa Pesquisa. Neste nível existe rejeição: a área pode devolver o dataset com uma justificativa, que volta ao Coletor para a instituição corrigir e reenviar.

Homologar **não tranca** o modelo. Se a área homologou um dado que depois se revelou errado, a instituição corrige na origem e re-extrai: a validação anterior fica obsoleta e o envio volta a ser oferecido, reiniciando a cadeia. Ver [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato#so-a-aprovacao-do-reitor-e-definitiva).

### Aprovação do Reitor (na PNP)

Só chega ao Reitor o que a área já homologou. A decisão é institucional, cobre todas as áreas de uma vez, e é **terminal**: aqui só existe aprovar. Depois do aceite, o Coletor reflete o estado final e passa a **bloquear a reextração** daquele modelo — substituir dado já aceito exige um novo [Ciclo de Coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta).

## Onde isso acontece na interface

| Etapa | Onde | Tela |
|---|---|---|
| Importar contratos e modelos | Coletor | Botão "Sincronizar com a PNP" no Dashboard |
| Cadastrar Provedor | Coletor | "Provedores" |
| Configurar extração | Coletor | "Configurações de Extração" (com "Testar extração") |
| Disparar extração | Coletor | "Extrair Dados" em "Modelos de Dados" ou "Contratos" |
| Ver o resultado dos testes | Coletor | "Ver resultados de teste" no contrato |
| Enviar à PNP | Coletor | "Enviar" no contrato, ou "Sincronizar todos" |
| Consultar a validação | Coletor | "Verificar agora" no modelo |
| **Homologar (área)** | **PNP** | "Fila de Homologação" |
| **Aprovar (Reitor)** | **PNP** | "Aprovação de Microdados" |

> ⚠️ **Na PNP, confira o papel ativo.** A Fila de Homologação mostra apenas a área do **papel ativo** de quem está logado. Quem acumula vínculos em várias áreas precisa trocar em "Alterar Papel" — caso contrário a fila aparece vazia, sem indicar o motivo. O Reitor não passa por isso: o escopo dele é institucional e ele vê tudo de uma vez.

## Quando uma etapa falha

**Provedor inacessível.** A extração registra falha imediatamente: credenciais inválidas, endpoint indisponível, banco recusando conexão ou planilha movida de lugar. O contrato fica com status "Falha na Extração", o motivo do erro vai para o Registro de Extração e a operação correta é corrigir a Configuração ou o Provedor e re-extrair.

**Validação de schema.** A fonte respondeu, mas as colunas não batem com o contrato (faltam colunas obrigatórias, sobram colunas, tipos divergentes). A extração rejeita o conjunto de dados antes de gerar Parquet, e o motivo descreve a divergência. A correção pode estar tanto na Configuração de Extração (ex.: query incompleta) quanto no schema do contrato.

**Teste de qualidade.** O Parquet foi gerado, mas as regras declarativas do contrato (unicidade, intervalo de valores, completude) reprovaram. Como o teste roda **dentro** da extração, o contrato vai para **"Falha na Extração"** — não existe um estado "Testes com Falha". Exige investigação do dado de origem antes de uma nova extração. Para detalhes da máquina de estados, veja [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato); para casos típicos, consulte as [Perguntas frequentes]({{ site.baseurl }}/documentacao/coletor/faq).

**Validação rejeitada pela PNP.** O envio foi aceito, mas a PNP reprovou o parquet — tipicamente na validação referencial (um campus, área ou município que não existe no cadastro da Rede). O contrato vai para "Validação Rejeitada" e o motivo fica no Registro de Validação. A correção é no **dado de origem**, não na configuração.

**Rejeição pela área.** O Gestor de Área Temática devolveu o dataset com uma justificativa. Diferente das falhas anteriores, aqui não há defeito técnico: é uma discordância sobre o conteúdo. A justificativa fica registrada e orienta a correção.

> ⚠️ **Reenviar dado idêntico não reseta a validação.** A PNP identifica cada dataset pelo **conteúdo** (checksum). Reextrair e reenviar um dado que não mudou faz a PNP devolver o **mesmo dataset, com o status anterior** — inclusive uma rejeição antiga. O sintoma é "reenviei e continua rejeitado". Para mudar o estado, o dado precisa mudar de verdade.

## Veja também

- [Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta)
- [Status do contrato]({{ site.baseurl }}/documentacao/coletor/status_do_contrato)
- [Operação passo a passo]({{ site.baseurl }}/documentacao/coletor/operacao_passo_a_passo) — o mesmo fluxo, com as telas reais
