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

Para conferir antes de abrir PR, gere o site e procure links sem o prefixo:

```bash
cd docs && bundle exec jekyll build
grep -rno 'href="/[^g][^"]*"' _site | grep -v '://' | head
```

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

## Licença

Todo o conteúdo deste site está publicado sob a licença MIT.

