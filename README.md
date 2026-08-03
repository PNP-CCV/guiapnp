[![pages-build-deployment](https://github.com/Rede-DSBR/referencial/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Rede-DSBR/referencial/actions/workflows/pages/pages-build-deployment)

# Referencial

Conteúdo do referencial metodológico da Plataforma Nilo Peçanha e hospedagem como página web.

## Executando o site localmente

Este repositório contém um site Jekyll hospedado no GitHub Pages. Para testar localmente:

### Pré-requisitos

- Ruby (versão 3.0 ou superior)
- Bundler

### Instalação

1. **Configure o ambiente Ruby** para instalar gems no seu diretório home (evita necessidade de sudo):

```bash
# Adicione ao seu ~/.zshrc ou ~/.bashrc
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"

# Recarregue o terminal ou execute:
source ~/.zshrc  # ou source ~/.bashrc
```

2. **Instale o Bundler**:

```bash
gem install bundler
```

3. **Instale as dependências do Jekyll**:

```bash
cd docs
bundle install
```

### Executando o servidor local

Para executar o site localmente com o baseurl correto (como no GitHub Pages):

```bash
cd docs
bundle exec jekyll serve --baseurl "/guiapnp"
```

O site estará disponível em: **http://127.0.0.1:4000/guiapnp/**

Para testar sem o baseurl (simplifica navegação local):

```bash
bundle exec jekyll serve --baseurl ""
```

O site estará disponível em: **http://127.0.0.1:4000/**

### Parando o servidor

Pressione `Ctrl+C` no terminal onde o servidor está rodando.

## Links internos: sempre com `site.baseurl`

O site é publicado num subcaminho (`baseurl: "/guiapnp"` no `_config.yml`), então
**todo link ou imagem interna precisa carregar esse prefixo explicitamente**.

Em Markdown, use `{{ site.baseurl }}`:

```markdown
[Ciclo de coleta]({{ site.baseurl }}/documentacao/coletor/ciclo_de_coleta)
![Dashboard]({{ site.baseurl }}/assets/img/docs/coletor/02-dashboard.png)
```

Em HTML e nos templates (`_includes/`, `_layouts/`), use o filtro `relative_url`:

```liquid
<a href="{{ '/assets/files/Guia_PNP.pdf' | relative_url }}">Versão PDF</a>
```

Nunca escreva o caminho cru (`](/documentacao/...)`) nem o prefixo na mão
(`href="/guiapnp/..."`): o primeiro quebra em produção, o segundo quebra se o
`baseurl` mudar. Links externos, âncoras (`#secao`) e caminhos relativos ao
próprio diretório não precisam de nada disso.

> **Por que isso importa.** O repositório já teve um plugin
> (`docs/_plugins/relative_links.rb`) que injetava o prefixo no HTML gerado.
> O GitHub Pages **ignora plugins personalizados** — só executa uma lista fixa —,
> então o plugin funcionava no `jekyll serve` local e não em produção: os links
> das páginas quebravam, enquanto o menu continuava certo (os templates já usavam
> `relative_url`). O plugin foi removido justamente para que o build local
> reproduza o de produção. Se um link funciona no seu ambiente, funciona no ar.

### Conferindo antes do PR

O repositório tem um verificador em `scripts/verificar_links.py`, que é o mesmo
executado pelo CI (workflow **Verificar links internos**). Ele roda em duas
camadas:

```bash
# Rápido, não precisa do site construído: aponta arquivo e linha do fonte
python3 scripts/verificar_links.py --fonte

# Completo: confere links, âncoras e imagens no HTML gerado
cd docs && bundle exec jekyll build && cd ..
python3 scripts/verificar_links.py --site docs/_site
```

A primeira camada pega os dois padrões que já quebraram o site (caminho cru e
prefixo escrito à mão). A segunda pega o que só aparece depois do build: link
montado por template, âncora que deixou de existir, imagem renomeada.

O CI roda as duas em todo pull request que toque `docs/`, e também recusa a
recriação de `docs/_plugins/` — plugins personalizados fazem o build local
divergir do site publicado, que foi a origem do problema descrito acima.

## Estrutura do projeto

```
docs/
├── _config.yml           # Configuração do Jekyll
├── _data/                # Dados do site (menu, header)
├── _includes/            # Componentes reutilizáveis
├── _layouts/             # Layouts de páginas
├── assets/               # CSS, JS, imagens
├── documentacao/         # Conteúdo Markdown
└── Gemfile              # Dependências Ruby
```

## Fluxo editorial com Decap CMS

Esta configuracao permite que editores alterem conteudo via CMS com commits na branch `editoracao`, e que a publicacao em `deploy` aconteca apenas apos revisao.

### Como o fluxo funciona

1. O Decap CMS grava alteracoes na branch `editoracao`.
2. O workflow [`.github/workflows/editoracao-review-gate.yml`](.github/workflows/editoracao-review-gate.yml) garante a abertura de PR `editoracao -> deploy`.
3. Um terceiro revisa e aprova o PR.
4. Apos merge, a branch `deploy` e atualizada.

### Configuracao de seguranca recomendada no GitHub

Em `Settings > Branches`:

1. Proteger `deploy` com:
	1. `Require a pull request before merging`.
	2. `Require approvals` (minimo 1).
	3. Opcional: `Dismiss stale pull request approvals when new commits are pushed`.
2. Opcional: proteger `editoracao` para restringir quem pode editar.

### Teste local do CMS

Comandos em dois terminais:

Terminal 1 (site Jekyll):

```bash
cd docs
bundle exec jekyll serve --baseurl "/guiapnp"
```

Terminal 2 (proxy local do Decap):

```bash
npx decap-server
```

Abra:

- Site: `http://127.0.0.1:4000/guiapnp/`
- CMS: `http://127.0.0.1:4000/guiapnp/admin/`

Observacoes:

- O `local_backend: true` em [docs/admin/config.yml](docs/admin/config.yml) ativa o modo local para testes sem OAuth remoto.
- Em producao (GitHub Pages), o backend `github` exige um endpoint OAuth do Decap CMS para login com conta GitHub.

### Produção no GitHub Pages com login GitHub

Para o login funcionar no `/admin` publicado, configure um OAuth provider do Decap CMS (servico externo) e preencha em [docs/admin/config.yml](docs/admin/config.yml):

- `base_url`
- `auth_endpoint`

Sem isso, o editor funciona localmente, mas o login no ambiente publicado nao sera concluido.

## Licença

Todo o conteúdo deste site está publicado sob a licença MIT.

