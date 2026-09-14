# Provedor OAuth do Decap CMS

O `/admin` do Guia PNP roda no GitHub Pages, que serve apenas arquivos
estaticos. O login com conta GitHub, porem, termina numa troca do `code` pelo
`access_token` que exige o *client secret* — e segredo nao pode ir para o
navegador. Este Worker existe so para essa etapa.

Sem ele, o `/admin` publicado abre mas o login nunca conclui. Localmente nada
disso e necessario: o `local_backend: true` usa o `decap-server`.

## Deploy

```bash
cd oauth-proxy
npx wrangler login
# preencha GITHUB_CLIENT_ID no wrangler.toml antes deste passo
npx wrangler secret put GITHUB_CLIENT_SECRET
npx wrangler deploy
```

O deploy imprime a URL publica (`https://guiapnp-cms-oauth.<conta>.workers.dev`).
Ela alimenta dois lugares:

1. A *Authorization callback URL* do OAuth App: `<url>/callback`
2. O `base_url` em [`../docs/admin/config.yml`](../docs/admin/config.yml)

## Conferindo

```bash
curl -i "https://<sua-url>/auth"
```

Deve responder `302` com `Location:` para `github.com/login/oauth/authorize` e um
`Set-Cookie` com o `state`. Se responder 302 sem `client_id` na URL de destino, o
`GITHUB_CLIENT_ID` nao foi preenchido.

## Por que nao usar um provedor de terceiros pronto

Existem instancias publicas desse mesmo servico. Usa-las significa entregar a um
terceiro o token de escrita no repositorio de todos os editores. Sao 100 linhas
de codigo — vale manter as proprias.
