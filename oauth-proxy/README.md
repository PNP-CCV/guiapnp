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

## Testes

```bash
cd oauth-proxy && npm test
```

Nao precisa de rede nem credencial. Cobre credencial esquecida no placeholder,
`state` divergente e a compilacao do JS da pagina de handshake — que, sem teste,
so falharia em producao dentro do popup.

## Conferindo o deploy

```bash
curl -i "https://<sua-url>/auth"
```

Deve responder `302` com `Location:` para `github.com/login/oauth/authorize`, com
`client_id` preenchido, e um `Set-Cookie` com o `state`. Se vier `400`, a mensagem
diz qual variavel falta.

### "TLS connect error" logo apos o primeiro deploy

O certificado curinga de `*.<subdominio>.workers.dev` e emitido depois que o
subdominio e criado, e leva alguns minutos. Ate la o handshake TLS falha com
`ssl/tls alert handshake failure`. Nao ha o que corrigir — espere e repita. Para
confirmar que e isso:

```bash
openssl s_client -connect <host>:443 -servername <host> </dev/null 2>/dev/null \
  | openssl x509 -noout -dates
```

Se `notBefore` for posterior ao momento do seu teste, era a emissao do certificado.

### O login conclui mas o CMS nao abre

O popup entrega o token por `postMessage`, e o navegador so entrega a mensagem a
uma origem que o Worker autorize. Se a origem do `/admin` nao estiver em
`SITE_ORIGIN`, a mensagem e descartada **sem erro no console** — o popup fica
aberto e o CMS parado na tela de login. A propria pagina do popup detecta isso
apos 6 segundos e mostra as origens envolvidas.

A outra causa e o `base_url` do `docs/admin/config.yml` nao bater exatamente com a
origem do Worker: o CMS ignora o handshake vindo de qualquer outro endereco. Sem
barra no fim, com `https://`.

## Por que nao usar um provedor de terceiros pronto

Existem instancias publicas desse mesmo servico. Usa-las significa entregar a um
terceiro o token de escrita no repositorio de todos os editores. Sao 100 linhas
de codigo — vale manter as proprias.
