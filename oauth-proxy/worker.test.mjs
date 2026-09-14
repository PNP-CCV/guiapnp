/**
 * Testes do Worker de OAuth. Rode com `npm test` dentro de oauth-proxy/.
 *
 * Nao precisa de rede nem de credencial: a chamada ao GitHub e simulada. Cobre o
 * que quebra na pratica — credencial esquecida no placeholder, `state` divergente
 * e a pagina de handshake, cujo JS so falharia em producao, dentro do popup.
 */
import worker from './src/worker.js';

const env = {
  GITHUB_CLIENT_ID: 'Iv1.abc123',
  GITHUB_CLIENT_SECRET: 'segredo',
  SITE_ORIGIN: 'https://pnp-ccv.github.io,http://127.0.0.1:4000',
};
const base = 'https://guiapnp-cms-oauth.exemplo.workers.dev';
let falhas = 0;
const ok = (c, m) => { console.log((c ? '  ok   ' : '  FALHA') + '  ' + m); if (!c) falhas++; };

// 1. guarda do client id
let r = await worker.fetch(new Request(base + '/auth'), { ...env, GITHUB_CLIENT_ID: 'PREENCHER' });
ok(r.status === 400, 'client_id nao preenchido -> 400 (era 302 silencioso antes)');

// 2. redirect normal
r = await worker.fetch(new Request(base + '/auth'), env);
const loc = new URL(r.headers.get('location'));
ok(r.status === 302, '/auth -> 302');
ok(loc.searchParams.get('client_id') === 'Iv1.abc123', 'client_id vai na URL');
const state = loc.searchParams.get('state');
ok(!!state, 'state gerado');
ok(/HttpOnly/.test(r.headers.get('set-cookie')), 'cookie do state e HttpOnly');

// 3. callback com state divergente
r = await worker.fetch(new Request(base + '/callback?code=x&state=OUTRO', {
  headers: { Cookie: 'decap_oauth_state=' + state },
}), env);
ok(r.status === 400, 'state divergente -> recusado (CSRF)');

// 4. callback feliz, com o GitHub simulado
const fetchReal = globalThis.fetch;
globalThis.fetch = async () => new Response(JSON.stringify({ access_token: 'gho_TOKEN123' }));
r = await worker.fetch(new Request(base + '/callback?code=x&state=' + state, {
  headers: { Cookie: 'decap_oauth_state=' + state },
}), env);
globalThis.fetch = fetchReal;
const html = await r.text();
ok(r.status === 200, 'callback valido -> 200');
ok(html.includes('authorization:github:success:'), 'mensagem do protocolo presente');
ok(html.includes('gho_TOKEN123'), 'token embutido');
ok(html.includes('"https://pnp-ccv.github.io"'), 'origem permitida embutida');
ok(html.includes('http://127.0.0.1:4000'), 'segunda origem tambem');

// 5. o JS inline compila?
const inline = html.match(/<script>([\s\S]*?)<\/script>/)[1];
try { new Function(inline); ok(true, 'JS da pagina compila'); }
catch (e) { ok(false, 'JS da pagina NAO compila: ' + e.message); }

console.log(falhas ? `\n${falhas} falha(s)` : '\nTodos os testes passaram');
process.exit(falhas ? 1 : 0);
