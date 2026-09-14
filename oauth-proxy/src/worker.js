/**
 * Provedor OAuth do Decap CMS para o Guia PNP.
 *
 * O GitHub Pages serve arquivos estaticos, e a troca do `code` do OAuth pelo
 * `access_token` exige o client secret — que nao pode viver no navegador. Este
 * Worker existe so para essa troca: recebe o retorno do GitHub, chama a API com
 * o secret guardado no servidor e devolve o token ao CMS por postMessage.
 *
 * Duas rotas:
 *   GET /auth      -> redireciona para a tela de autorizacao do GitHub
 *   GET /callback  -> troca o code pelo token e entrega ao CMS
 *
 * Variaveis (wrangler.toml / wrangler secret):
 *   GITHUB_CLIENT_ID      publica, vem do OAuth App
 *   GITHUB_CLIENT_SECRET  secreta, nunca versionada
 *   SITE_ORIGIN           origem do site publicado, ex. https://pnp-ccv.github.io
 */

const GITHUB_AUTHORIZE = 'https://github.com/login/oauth/authorize';
const GITHUB_TOKEN = 'https://github.com/login/oauth/access_token';
const COOKIE_STATE = 'decap_oauth_state';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    switch (url.pathname) {
      case '/auth':
        return iniciarLogin(url, env);
      case '/callback':
        return concluirLogin(request, url, env);
      default:
        return new Response('Provedor OAuth do Decap CMS — Guia PNP.', {
          status: 200,
          headers: { 'content-type': 'text/plain; charset=utf-8' },
        });
    }
  },
};

function iniciarLogin(url, env) {
  // O `state` protege contra CSRF: e gerado aqui, guardado num cookie HttpOnly e
  // conferido no callback. Sem isso, um terceiro poderia induzir o navegador da
  // vitima a completar um login que ela nao iniciou.
  const state = crypto.randomUUID();

  const destino = new URL(GITHUB_AUTHORIZE);
  destino.searchParams.set('client_id', env.GITHUB_CLIENT_ID);
  destino.searchParams.set('redirect_uri', `${url.origin}/callback`);
  // `repo` e o escopo minimo que funciona: o CMS precisa ler e gravar conteudo,
  // e o repositorio e privado ou pode vir a ser. Em repositorio publico,
  // `public_repo` basta — troque aqui se for o caso.
  destino.searchParams.set('scope', 'repo,user');
  destino.searchParams.set('state', state);

  return new Response(null, {
    status: 302,
    headers: {
      Location: destino.toString(),
      'Set-Cookie': `${COOKIE_STATE}=${state}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=600`,
    },
  });
}

async function concluirLogin(request, url, env) {
  const code = url.searchParams.get('code');
  const state = url.searchParams.get('state');
  const esperado = lerCookie(request.headers.get('Cookie'), COOKIE_STATE);

  if (!code) return paginaErro('O GitHub nao devolveu o parametro `code`.');
  if (!state || state !== esperado) {
    return paginaErro('Parametro `state` ausente ou divergente — login recusado.');
  }

  const resposta = await fetch(GITHUB_TOKEN, {
    method: 'POST',
    headers: { 'content-type': 'application/json', accept: 'application/json' },
    body: JSON.stringify({
      client_id: env.GITHUB_CLIENT_ID,
      client_secret: env.GITHUB_CLIENT_SECRET,
      code,
      redirect_uri: `${url.origin}/callback`,
    }),
  });

  const dados = await resposta.json();
  if (!dados.access_token) {
    // A mensagem do GitHub entra aqui para nao obrigar a abrir o log do Worker.
    return paginaErro(`GitHub recusou a troca do code: ${dados.error_description || dados.error || 'motivo nao informado'}`);
  }

  return paginaSucesso(dados.access_token, env.SITE_ORIGIN);
}

function lerCookie(cabecalho, nome) {
  if (!cabecalho) return null;
  for (const parte of cabecalho.split(';')) {
    const [chave, ...resto] = parte.trim().split('=');
    if (chave === nome) return resto.join('=');
  }
  return null;
}

/**
 * O Decap abre este endereco num popup e espera um handshake por postMessage:
 * o popup anuncia "authorizing:github", o CMS responde, e so entao o popup
 * entrega o token. A resposta do CMS traz a origem real, usada para mirar a
 * segunda mensagem em vez de difundi-la com "*".
 */
function paginaSucesso(token, siteOrigin) {
  const payload = JSON.stringify({ token, provider: 'github' });
  const html = `<!doctype html>
<html lang="pt-br"><head><meta charset="utf-8"><title>Autenticando…</title></head>
<body>
<p>Autenticacao concluida. Pode fechar esta janela.</p>
<script>
  (function () {
    var permitida = ${JSON.stringify(siteOrigin || '')};
    function aoReceber(e) {
      if (permitida && e.origin !== permitida) return;
      window.opener.postMessage(
        'authorization:github:success:${payload.replace(/</g, '\\u003c')}',
        e.origin
      );
      window.removeEventListener('message', aoReceber, false);
    }
    window.addEventListener('message', aoReceber, false);
    window.opener.postMessage('authorizing:github', permitida || '*');
  })();
</script>
</body></html>`;
  return new Response(html, { headers: { 'content-type': 'text/html; charset=utf-8' } });
}

function paginaErro(mensagem) {
  const html = `<!doctype html>
<html lang="pt-br"><head><meta charset="utf-8"><title>Falha na autenticacao</title></head>
<body><h1>Falha na autenticacao</h1><p>${mensagem.replace(/</g, '&lt;')}</p></body></html>`;
  return new Response(html, { status: 400, headers: { 'content-type': 'text/html; charset=utf-8' } });
}
