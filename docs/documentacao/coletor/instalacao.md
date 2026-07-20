---
layout: default
title: "Instalação"
toc: true
---

# Instalação

* TOC
{:toc}

> **Para quem é:** 🔌 integradores

Esta página cobre a instalação completa do Coletor em três etapas — instalar o Docker, instalar o executável `coletor` e subir a stack — além dos comandos de administração do dia a dia.

O conteúdo desta página incorpora e expande o [Manual do Usuário](https://github.com/PNP-CCV/coletor) publicado no repositório `PNP-CCV/coletor`, que é também a página onde os executáveis são distribuídos.

## 1. Instalar o Docker {#instalar-o-docker}

O Coletor precisa do **Docker Engine** e do plugin **Docker Compose**. Confirme antes os [requisitos técnicos](/documentacao/coletor/requisitos_tecnicos).

### Linux (servidor)

No Ubuntu, Debian e na maioria das distribuições, o caminho mais simples é o script oficial do Docker, que já inclui o plugin Compose:

```bash
curl -fsSL https://get.docker.com | sudo sh

# Usar o Docker (e o Coletor) sem sudo:
sudo usermod -aG docker $USER
# saia e entre na sessão de novo para valer
```

Garanta que o serviço do Docker inicia junto com a máquina:

```bash
sudo systemctl enable --now docker
```

### Windows

1. Baixe o **Docker Desktop** em [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
2. Execute o instalador e aceite ativar o **WSL 2** quando solicitado.
3. Reinicie o computador se for pedido.
4. Abra o Docker Desktop e espere o ícone indicar que está "rodando".

### macOS

1. Baixe o **Docker Desktop** em [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/), escolhendo a versão do seu chip (Apple Silicon ou Intel).
2. Abra o `.dmg` e arraste o Docker para a pasta *Aplicativos*.
3. Abra o Docker, conceda as permissões pedidas e espere ficar "rodando".

### Verificar a instalação

```bash
docker --version
docker compose version
docker run hello-world
```

Se os dois primeiros comandos mostram versão e o terceiro imprime *"Hello from Docker!"*, o Docker está pronto.

## 2. Instalar o executável `coletor`

O `coletor` é um **único arquivo executável** — não há instalador. Baixe a versão mais recente na página de releases:

🔗 **Download:** [github.com/PNP-CCV/coletor/releases/latest](https://github.com/PNP-CCV/coletor/releases/latest)

### Linux e macOS

```bash
# Baixe o executável da página de releases (exemplo: Linux x86-64)
curl -L -o coletor https://github.com/PNP-CCV/coletor/releases/latest/download/coletor

# Dê permissão de execução e mova para um diretório do PATH
chmod +x coletor
sudo mv coletor /usr/local/bin/

# Confirme que o sistema encontra o programa
coletor --help
```

### Windows

Coloque o `coletor.exe` numa pasta de sua preferência (por exemplo `C:\coletor\`) e execute a partir dela no PowerShell:

```powershell
cd C:\coletor
.\coletor.exe --help
```

Se `coletor --help` lista os comandos `up`, `down`, `status`, `logs` e `update`, a instalação está correta.

## 3. Subir a stack

```bash
coletor up
```

O comando liga todos os serviços descritos em [Requisitos técnicos](/documentacao/coletor/requisitos_tecnicos#o-que-a-instalacao-sobe). Quando termina, a aplicação está no ar em `http://<servidor>:8000/painel/` e o terminal pode ser fechado — os serviços continuam em segundo plano.

> ℹ️ **O primeiro `coletor up` baixa as imagens.** Na primeira execução o Coletor baixa os componentes da aplicação pela internet, o que pode levar alguns minutos. Nas execuções seguintes é quase instantâneo.

Para publicar o painel em outra porta do servidor:

```bash
coletor up --port 9090
```

A porta escolhida **fica salva**: os próximos `coletor up` e `coletor update` continuam usando a 9090 sem repetir a flag. Para voltar ao padrão, rode `coletor up --port 8000`.

## Comandos do dia a dia

| Comando | O que faz |
|---|---|
| `coletor up` | Liga todos os serviços |
| `coletor status` | Mostra quais serviços estão ligados e se estão saudáveis |
| `coletor logs` | Acompanha as mensagens de todos os serviços em tempo real |
| `coletor logs web` | Acompanha um serviço específico |
| `coletor update` | Baixa a versão mais nova dos componentes e reinicia a aplicação |
| `coletor down` | Desliga a aplicação, **preservando os dados** |
| `coletor down --wipe` | Desliga e **apaga o banco de dados** (pede confirmação) |
| `coletor --version` | Mostra a versão do executável |

Em `coletor logs`, `Ctrl + C` para de acompanhar sem desligar a aplicação.

### Atualização

`coletor update` baixa as imagens mais novas e reinicia a stack com elas. Antes de atualizar, o programa verifica se existe uma versão mais nova **do próprio executável**: se houver, ele avisa, mostra o link de download e **não atualiza a stack** — troque o `coletor` primeiro e rode `update` de novo. O mesmo aviso aparece (sem bloquear) nos demais comandos. A consulta acontece no máximo uma vez por dia e é ignorada sem internet.

### Desligar e apagar dados

`coletor down` preserva tudo: um `up` em seguida volta ao estado anterior. Já o `--wipe` remove o banco de dados de forma permanente.

> ⚠️ **`coletor down --wipe` apaga o banco de dados.** Não há como desfazer. O comando pede confirmação antes de apagar. Use apenas para recomeçar uma instalação do zero — e lembre que a instância ativada na PNP está vinculada ao hostname do servidor (ver [Primeiro acesso](/documentacao/coletor/primeiro_acesso#secret-casado-com-hostname)).

## Instalação sem a CLI

Equipes que preferem controlar o Compose diretamente podem subir a mesma stack sem o executável `coletor`: o arquivo de orquestração que ele embute está versionado em `cli/docker-compose.yml` no [repositório da aplicação](https://github.com/PNP-CCV/coletor-pnp-microdados), consumindo a imagem `ghcr.io/pnp-ccv/coletor`. Nesse caso a equipe assume o que a CLI faz sozinha — escolha da pasta de dados, injeção do `HOST_NAME` e do UID/GID do usuário, e atualização das imagens.

## Veja também

- [Primeiro acesso](/documentacao/coletor/primeiro_acesso) — o que fazer assim que o painel abrir
- [Requisitos técnicos](/documentacao/coletor/requisitos_tecnicos) — servidor, rede e credenciais necessárias
- [Manual do Usuário no repositório de releases](https://github.com/PNP-CCV/coletor) — versão resumida desta página
