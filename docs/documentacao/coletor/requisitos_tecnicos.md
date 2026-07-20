---
layout: default
title: "Requisitos técnicos"
toc: true
---

# Requisitos técnicos

* TOC
{:toc}

> **Para quem é:** 🔌 integradores

Esta página lista o que a instituição precisa providenciar **antes** de instalar o Coletor: servidor, software de base, liberações de rede e as credenciais fornecidas pela PNP.

## O que a instalação sobe {#o-que-a-instalacao-sobe}

O Coletor não é um único programa: é uma *stack* de contêineres Docker orquestrada pelo executável `coletor`. Conhecer os serviços ajuda a dimensionar o servidor e a conversar com a equipe de infraestrutura:

| Serviço | Imagem | Papel |
|---|---|---|
| `web` | `ghcr.io/pnp-ccv/coletor` | Aplicação que serve o painel na porta 8000 |
| `db` | `postgres:16-alpine` | Banco de dados da aplicação |
| `redis` | `redis` | Fila de mensagens das tarefas em background |
| `celery-worker` | `ghcr.io/pnp-ccv/coletor` | Executa as extrações, testes e envios em background |
| `celery-beat` | `ghcr.io/pnp-ccv/coletor` | Agenda as tarefas recorrentes |
| `datacontract-api` | `datacontract/cli` | Valida os arquivos Parquet contra o Contrato de Dados |

Apenas o serviço `web` é publicado para fora do servidor (porta 8000 por padrão). Os demais conversam entre si na rede interna do Docker.

## Servidor {#servidor}

- **Sistema operacional:** Linux é o alvo de produção. A imagem da aplicação é publicada **somente para `linux/amd64`** (x86-64) — inclusive porque o driver IBM Db2 usado em produção só existe para essa arquitetura. Windows e macOS (via Docker Desktop) funcionam para avaliação e testes, não para a instância definitiva.
- **Hostname estável:** o secret fornecido pela PNP é **vinculado ao hostname** da máquina no primeiro registro (detalhes em [Primeiro acesso](/documentacao/coletor/primeiro_acesso#secret-casado-com-hostname)). Escolha o servidor definitivo antes de ativar a instância — trocar de máquina depois exige contato com a equipe da PNP.
- **Dimensionamento de referência** (a stack completa, para uma instituição):

| Recurso | Mínimo | Recomendado |
|---|---|---|
| vCPUs | 2 | 4 |
| Memória RAM | 4 GB | 8 GB |
| Disco | 20 GB livres | 50 GB livres (SSD) |

A extração carrega cada conjunto de dados em memória antes de gravar o arquivo Parquet — instituições com modelos muito volumosos devem folgar a RAM. O disco guarda as imagens Docker, o banco Postgres e os Parquets extraídos.

## Software

O único pré-requisito de software é o **Docker**:

- **Docker Engine** com o plugin **Docker Compose v2** (o comando `docker compose`, sem hífen). No Linux, o script oficial de instalação já inclui os dois.
- No Windows e macOS, o **Docker Desktop** já traz Engine e Compose.

Nada além disso: o executável `coletor` é um binário único, sem dependências, e a aplicação roda inteiramente dentro dos contêineres — não é preciso instalar Python, PostgreSQL ou Redis no servidor.

## Rede

Liberações de **saída** (o servidor precisa alcançar):

| Destino | Para quê |
|---|---|
| URL da API da PNP (HTTPS) | Ativação da instância, importação de contratos, envio dos Parquets e consulta da validação |
| `ghcr.io` (HTTPS) | Download das imagens da aplicação (`docker pull`) |
| `github.com` e domínios de release do GitHub (HTTPS) | Download do executável `coletor` e checagem de novas versões |
| Fontes de dados da instituição | APIs, bancos de dados, planilhas online ou compartilhamentos SMB de onde os microdados serão extraídos |

Liberações de **entrada**:

| Porta | Para quê |
|---|---|
| `8000/tcp` (ou a porta escolhida com `coletor up --port`) | Acesso dos operadores ao painel via navegador |

O acesso às fontes de dados merece atenção: se o banco acadêmico está em outra rede ou atrás de firewall, a liberação é do **servidor do Coletor** para a fonte — o dado é extraído pelo servidor, não pela máquina do operador.

## Credenciais junto à PNP {#credenciais-junto-a-pnp}

Antes do primeiro acesso, tenha em mãos, fornecidos pela equipe da PNP à sua instituição:

- a **URL da API** da PNP; e
- o **secret** de integração da instituição.

Sem esses dois valores a instância não ativa — o setup inicial valida a integração com a PNP na hora e não conclui sem ela.

## Usuário de operação

No Linux, crie (ou use) um usuário comum, **sem `sudo`**, e adicione-o ao grupo `docker`:

```bash
sudo usermod -aG docker $USER
# saia e entre na sessão de novo para valer
```

> ⚠️ **Não rode o `coletor` com sudo.** O Coletor guarda os dados na pasta do usuário que o executa. Rodar com `sudo` cria os dados no perfil do root e confunde as execuções seguintes. O grupo `docker` existe exatamente para dispensar o `sudo`.

## Onde os dados ficam

O executável `coletor` gerencia uma pasta de dados por usuário — é dela que a stack sobe e onde os Parquets extraídos ficam (`storage/`):

| Sistema | Pasta de dados |
|---|---|
| Linux | `~/.local/share/coletor` |
| macOS | `~/Library/Application Support/coletor` |
| Windows | `%LocalAppData%\coletor` |

O banco Postgres vive no volume Docker nomeado `coletorpnp_db-data`. Um plano de backup da instância cobre, portanto, dois alvos: a pasta de dados acima e um dump periódico do banco (ou o volume em si).

## Veja também

- [Instalação](/documentacao/coletor/instalacao) — o próximo passo do roteiro
- [Primeiro acesso](/documentacao/coletor/primeiro_acesso) — onde a URL e o secret da PNP são usados
