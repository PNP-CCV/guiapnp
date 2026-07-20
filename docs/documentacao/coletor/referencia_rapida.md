---
layout: default
title: "Referência rápida"
toc: true
---

# Referência rápida

* TOC
{:toc}

> **Para quem é:** 🔌 integradores · 👔 gestores

Esta página condensa, em tabelas de consulta, o que o restante do manual explica em prosa: comandos, telas, status e o checklist do operador.

## Comandos do `coletor`

| Comando | O que faz |
|---|---|
| `coletor up` | Liga a stack (porta padrão 8000; `--port N` escolhe outra e fica salva) |
| `coletor down` | Desliga preservando os dados (`--wipe` apaga o banco, com confirmação) |
| `coletor status` | Saúde de cada serviço |
| `coletor logs [serviço]` | Logs em tempo real (`Ctrl + C` para sair sem desligar) |
| `coletor update` | Atualiza as imagens e reinicia a stack |
| `coletor --version` | Versão do executável |

## Pastas de dados

| Sistema | Pasta |
|---|---|
| Linux | `~/.local/share/coletor` |
| macOS | `~/Library/Application Support/coletor` |
| Windows | `%LocalAppData%\coletor` |

O banco Postgres fica no volume Docker `coletorpnp_db-data`.

## Telas do painel

| Menu | Tela | Serve para |
|---|---|---|
| — | Dashboard | Wizard de 8 passos, ações em lote ("Extrair todos", "Enviar todos") |
| Coleta | Contratos | Status de cada Contrato de Dados, envio à PNP, resultados de teste |
| Coleta | Modelos de Dados | Extração por modelo, prévia e download do Parquet, validação PNP |
| Coleta | Provedores | Cadastro das fontes (Provedores de Dados) |
| Coleta | Configurações de Extração | Liga modelo × provedor, com "Testar extração" |
| Consultas | Ciclos, Estruturas, Áreas Temáticas, Subeixos, Municípios, Matrículas, Servidores | Dados de referência importados da PNP |
| Histórico | Extrações | Toda tentativa de extração, com motivo do erro |
| Histórico | Envios | Toda sincronização com a resposta da PNP |
| Sistema | Tarefas Assíncronas | Estado dos jobs em background |
| Sistema | Tarefas Agendadas¹ | O que roda sozinho e quando |
| Sistema | Configurações¹ | Dados da instância junto à PNP |
| Sistema | Usuários¹ | Gestão de contas do painel |

¹ Visível apenas para administradores.

## Status do contrato, em uma linha cada

| Status | Ação do operador |
|---|---|
| Ciclo de Coleta inativo | Aguardar a janela do ciclo abrir |
| Sem Modelos / Modelos Não Configurados | Sincronizar com a PNP / criar a Configuração de Extração |
| Aguardando Extração | Disparar "Extrair Dados" |
| Falha na Extração | Ler o motivo no registro, corrigir, re-extrair |
| Reextração Necessária | Disparar nova extração |
| Pronto para Sincronizar | Enviar à PNP |
| Aguardando Validação PNP | Esperar (ou "Verificar agora") |
| Validação Rejeitada | Corrigir o dado na origem e re-extrair |
| Aguardando Homologação da Área | Ação humana na PNP — sem botão no Coletor |
| Aguardando Aprovação do Reitor | Ação humana na PNP — sem botão no Coletor |
| Sincronizado com Sucesso | Nada — estado terminal do ciclo |

A máquina de estados completa, com a tabela de transições, está em [Status do contrato](/documentacao/coletor/status_do_contrato).

## Checklist do operador

- URL de planilha é a de **export**, não a de edição nem link assinado temporário.
- **Testou** a extração antes de salvar a configuração.
- Códigos de estrutura/campus são **da sua instituição**.
- Falhou? Leia o bloco **Detalhes** do Registro de Extração antes de mexer em qualquer coisa.
- Lembre que reenvio com dado idêntico **não muda nada** na PNP.
- Travado no passo 7 ou 8? O problema não é técnico — falar com a área ou a reitoria.

## Veja também

- [Operação passo a passo](/documentacao/coletor/operacao_passo_a_passo) — o contexto de cada item acima
- [Quando algo falha](/documentacao/coletor/quando_algo_falha) — o roteiro de diagnóstico
- [Glossário do Coletor](/documentacao/coletor/glossario) — terminologia do Coletor usada neste manual
