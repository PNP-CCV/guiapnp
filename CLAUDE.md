# Guia PNP

Site Jekyll publicado no GitHub Pages em `/guiapnp`. O README é a referência;
os pontos abaixo são os que mais quebram o site.

- Branch de trabalho é a `deploy`: PRs vão contra ela, não contra a `main`.
- Links internos em `docs/documentacao/**.md` sempre como
  `{{site.baseurl}}/documentacao/...`, sem espaço dentro das chaves (ver
  "Links internos" no README). Nada de `docs/_plugins/`.
- Antes do PR: `python3 scripts/verificar_links.py --fonte`. O CI roda também a
  camada `--site` sobre o build.
- `docs/documentacao/manual-do-usuario/`, as figuras em
  `docs/assets/img/docs/manual-do-usuario/` e o item "Manual do Usuário" de
  `docs/_data/menu.yml` são **gerados** por `scripts/importar_manual_usuario.py`
  a partir de `doc/usuario` do pnp-ccv-frontend. Não edite à mão: corrija na
  fonte e reimporte (ver "Manual do usuário" no README).
