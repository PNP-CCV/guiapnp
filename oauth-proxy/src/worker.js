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

// Vale conferir antes de redirecionar. Sem isso, um GITHUB_CLIENT_ID esquecido no
// placeholder manda o editor para o GitHub, que responde com uma pagina de erro
// generica sem dizer qual parametro esta errado — e o rastro morre ali.
function configurado(valor) {
  return typeof valor === 'string' && valor.length > 0 && valor !== 'PREENCHER';
}

function iniciarLogin(url, env) {
  if (!configurado(env.GITHUB_CLIENT_ID)) {
    return paginaErro(
      'GITHUB_CLIENT_ID nao foi configurado neste Worker. Preencha o valor em ' +
        'oauth-proxy/wrangler.toml com o Client ID do OAuth App e rode ' +
        '`npx wrangler deploy` outra vez.'
    );
  }

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
  if (!configurado(env.GITHUB_CLIENT_SECRET)) {
    return paginaErro(
      'GITHUB_CLIENT_SECRET nao foi gravado neste Worker. Rode ' +
        '`npx wrangler secret put GITHUB_CLIENT_SECRET` e tente de novo.'
    );
  }

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
 * o popup anuncia "authorizing:github", o CMS responde com a mesma string, e so
 * entao o popup entrega o token. Se qualquer ponta do handshake falhar, o token
 * nunca chega e o CMS fica parado na tela de login.
 *
 * Esta pagina relata o que aconteceu em vez de ficar muda. O modo de falha comum
 * — o CMS rodando numa origem que nao esta em SITE_ORIGIN — e invisivel de outra
 * forma: o navegador simplesmente nao entrega a mensagem, sem erro no console.
 */
function paginaSucesso(token, siteOrigins) {
  const payload = JSON.stringify({ token, provider: 'github' }).replace(/</g, '\\u003c');
  const permitidas = JSON.stringify(
    String(siteOrigins || '')
      .split(',')
      .map(s => s.trim())
      .filter(Boolean)
  );

  const html = `<!doctype html>
<html lang="pt-br"><head><meta charset="utf-8"><title>Autenticando…</title>
<style>
  body { font: 15px/1.5 system-ui, sans-serif; margin: 2rem; max-width: 40rem; }
  code { background: #f0f0f0; padding: .1em .3em; border-radius: 3px; }
  .erro { color: #a00; }
  ul { padding-left: 1.2rem; }
</style></head>
<body>
<p id="estado">Entregando as credenciais ao CMS…</p>
<div id="diagnostico"></div>
<script>
  (function () {
    var PERMITIDAS = ${permitidas};
    var estado = document.getElementById('estado');
    var diagnostico = document.getElementById('diagnostico');
    var recebidas = [];
    var entregue = false;

    function falhar(titulo, itens) {
      estado.className = 'erro';
      estado.textContent = titulo;
      diagnostico.innerHTML = '<ul>' + itens.map(function (i) {
        return '<li>' + i + '</li>';
      }).join('') + '</ul>';
    }

    if (!window.opener) {
      falhar('Esta janela perdeu a referencia ao CMS que a abriu.', [
        'Abra o /admin e clique em "Login with GitHub" — nao acesse este endereco direto.',
        'Se voce chegou aqui pelo botao de login, algum bloqueador de popup pode ter interferido.'
      ]);
      return;
    }

    window.addEventListener('message', function aoReceber(e) {
      if (recebidas.indexOf(e.origin) === -1) recebidas.push(e.origin);
      if (PERMITIDAS.length && PERMITIDAS.indexOf(e.origin) === -1) return;
      entregue = true;
      window.opener.postMessage('authorization:github:success:${payload}', e.origin);
      window.removeEventListener('message', aoReceber, false);
      estado.textContent = 'Autenticacao concluida. Esta janela fecha sozinha.';
    }, false);

    // targetOrigin "*" aqui e seguro: a mensagem nao carrega segredo nenhum, e so
    // um "estou aqui". O token so sai depois, mirado na origem que respondeu.
    window.opener.postMessage('authorizing:github', '*');

    setTimeout(function () {
      if (entregue) return;
      falhar('O CMS nao respondeu ao handshake — o token nao foi entregue.', [
        'Origens aceitas por este Worker (<code>SITE_ORIGIN</code>): <code>' +
          (PERMITIDAS.join('</code>, <code>') || '(nenhuma)') + '</code>',
        'Origens que responderam: <code>' +
          (recebidas.join('</code>, <code>') || '(nenhuma)') + '</code>',
        'Se a origem do CMS nao estiver na primeira lista, acrescente-a a ' +
          '<code>SITE_ORIGIN</code> no <code>wrangler.toml</code> e rode <code>npx wrangler deploy</code>.',
        'Se nenhuma origem respondeu, o <code>base_url</code> do ' +
          '<code>docs/admin/config.yml</code> precisa ser exatamente <code>' +
          location.origin + '</code> — o CMS ignora o handshake vindo de outro endereco.'
      ]);
    }, 6000);
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
