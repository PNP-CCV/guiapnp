#!/usr/bin/env python3
"""Verifica os links internos do Guia PNP.

O site é publicado num subcaminho (``baseurl: "/guiapnp"``), então todo link
interno precisa carregar esse prefixo. Em Markdown isso se escreve com
``{{ site.baseurl }}``; em HTML e nos templates, com o filtro ``relative_url``.

Este script roda em duas camadas, porque elas pegam coisas diferentes:

1. **Fonte** (``--fonte``) — procura, nos arquivos versionados, os dois padrões
   que já quebraram o site: o caminho cru (``](/documentacao/...)``) e o
   prefixo escrito à mão (``/guiapnp/...``). Dá mensagem por arquivo e linha,
   e não precisa do site construído.

2. **Site gerado** (``--site DIR``) — percorre o HTML e confere que cada link,
   âncora e imagem interna resolve de fato. Pega o que a camada de fonte não
   vê: link montado por template, âncora que deixou de existir, imagem
   renomeada.

Histórico: o repositório teve um plugin (``docs/_plugins/relative_links.rb``)
que injetava o prefixo no HTML. O GitHub Pages ignora plugins personalizados,
então ele funcionava no build local e não em produção — os links das páginas
quebravam no ar enquanto o menu, que usa ``relative_url``, continuava certo.
O plugin foi removido; este script existe para que a regressão não passe
despercebida de novo.

Uso:
    python3 scripts/verificar_links.py --fonte
    python3 scripts/verificar_links.py --site docs/_site
    python3 scripts/verificar_links.py --fonte --site docs/_site

Sai com código 1 se encontrar qualquer problema.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
CONFIG = DOCS / "_config.yml"

# Links markdown com caminho absoluto cru: ](/algo  -- sem o {{ site.baseurl }}.
RE_MD_CRU = re.compile(r"\]\((/(?!/)[^)]*)\)")
# Prefixo do baseurl escrito a mao, em qualquer arquivo versionado.
RE_HARDCODE = re.compile(r'["\'(](/guiapnp/)')

RE_HREF = re.compile(r'href="([^"]*)"')
RE_SRC = re.compile(r'src="([^"]*)"')
RE_ID = re.compile(r'id="([^"]+)"')

# Prefixos que nao sao link interno e nao passam pela checagem.
EXTERNOS = ("http://", "https://", "mailto:", "tel:", "data:", "//", "javascript:", "#")

# Extensoes varridas na camada de fonte.
FONTES = {".md", ".html", ".markdown"}
# Diretorios ignorados (saida de build, dependencias, cache).
IGNORADOS = {"_site", ".jekyll-cache", ".sass-cache", "vendor", ".git", ".bundle"}


def ler_baseurl() -> str:
    """Lê o baseurl do _config.yml sem exigir PyYAML."""
    if not CONFIG.is_file():
        return ""
    for linha in CONFIG.read_text(encoding="utf-8").splitlines():
        if linha.strip().startswith("baseurl:"):
            valor = linha.split(":", 1)[1].strip()
            valor = valor.split("#", 1)[0].strip()
            return valor.strip("\"'").rstrip("/")
    return ""


def arquivos_de_fonte():
    for caminho in DOCS.rglob("*"):
        if not caminho.is_file() or caminho.suffix not in FONTES:
            continue
        if any(parte in IGNORADOS for parte in caminho.parts):
            continue
        yield caminho


def checar_fonte(baseurl: str) -> list[str]:
    """Procura caminho cru e prefixo escrito à mão nos arquivos versionados."""
    problemas = []
    for caminho in arquivos_de_fonte():
        rel = caminho.relative_to(RAIZ)
        for n, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), 1):
            for destino in RE_MD_CRU.findall(linha):
                # Caminho ja prefixado pelo Liquid nao cai aqui: o texto antes
                # do "/" seria "{{ site.baseurl }}", nao "](" .
                if destino.startswith(baseurl + "/") and baseurl:
                    problemas.append(
                        f"{rel}:{n}: prefixo '{baseurl}' escrito à mão em '{destino}' "
                        f"— use {{{{ site.baseurl }}}}{destino[len(baseurl):]}"
                    )
                else:
                    problemas.append(
                        f"{rel}:{n}: link interno sem prefixo: '{destino}' "
                        f"— use ]({{{{ site.baseurl }}}}{destino})"
                    )
            if baseurl:
                for _ in RE_HARDCODE.findall(linha):
                    if "site.baseurl" in linha or "relative_url" in linha:
                        continue
                    problemas.append(
                        f"{rel}:{n}: prefixo '{baseurl}' escrito à mão "
                        f"— use o filtro relative_url ou {{{{ site.baseurl }}}}"
                    )
    return problemas


def checar_site(site: Path, baseurl: str) -> list[str]:
    """Confere links, âncoras e imagens no HTML gerado."""
    problemas = []
    paginas = [p for p in site.rglob("*.html")]
    if not paginas:
        return [f"nenhuma página .html encontrada em {site} — o build rodou?"]

    cache_ids: dict[Path, set[str]] = {}

    def ids_de(p: Path) -> set[str]:
        if p not in cache_ids:
            cache_ids[p] = set(RE_ID.findall(p.read_text(encoding="utf-8", errors="replace")))
        return cache_ids[p]

    def resolver(destino: str, origem: Path):
        if destino.startswith("/"):
            p = destino.lstrip("/")
            if baseurl and p.startswith(baseurl.lstrip("/")):
                p = p[len(baseurl.lstrip("/")):].lstrip("/")
            base = site
        else:
            base = origem.parent
            p = destino
        alvo = Path(os.path.normpath(base / p))
        for cand in (alvo, alvo.with_name(alvo.name + ".html"), alvo / "index.html"):
            if cand.is_file():
                return cand
        return None

    for pagina in paginas:
        rel = pagina.relative_to(site)
        html = pagina.read_text(encoding="utf-8", errors="replace")

        for bruto in RE_HREF.findall(html):
            href = bruto.strip()
            if not href or href.startswith(EXTERNOS):
                continue
            alvo, _, ancora = href.partition("#")
            alvo = alvo.strip()
            if alvo in ("", "/", baseurl, baseurl + "/"):
                continue
            if alvo.startswith("/") and baseurl and not alvo.startswith(baseurl + "/"):
                problemas.append(
                    f"{rel}: link sem o prefixo '{baseurl}': {href} "
                    f"(quebra em produção — veja o README)"
                )
                continue
            destino = resolver(alvo, pagina)
            if destino is None:
                problemas.append(f"{rel}: link aponta para página inexistente: {href}")
            elif ancora and ancora not in ids_de(destino):
                problemas.append(f"{rel}: âncora inexistente no destino: {href}")

        for bruto in RE_SRC.findall(html):
            src = bruto.strip()
            if not src or src.startswith(EXTERNOS):
                continue
            if src.startswith("/") and baseurl and not src.startswith(baseurl + "/"):
                problemas.append(f"{rel}: imagem/script sem o prefixo '{baseurl}': {src}")
                continue
            if src.startswith("/") and resolver(src, pagina) is None:
                problemas.append(f"{rel}: arquivo referenciado não existe: {src}")

    return problemas


def main() -> int:
    ap = argparse.ArgumentParser(description="Verifica os links internos do Guia PNP.")
    ap.add_argument("--fonte", action="store_true", help="checa os arquivos versionados")
    ap.add_argument("--site", metavar="DIR", help="checa o site gerado neste diretório")
    args = ap.parse_args()

    if not args.fonte and not args.site:
        args.fonte = True  # padrão: a checagem que não exige build

    baseurl = ler_baseurl()
    print(f"baseurl configurado: '{baseurl or '(vazio)'}'")

    problemas: list[str] = []
    if args.fonte:
        achados = checar_fonte(baseurl)
        print(f"\n[fonte] arquivos versionados — {len(achados)} problema(s)")
        problemas += achados
    if args.site:
        site = Path(args.site)
        if not site.is_dir():
            print(f"\nERRO: diretório não encontrado: {site}", file=sys.stderr)
            return 1
        achados = checar_site(site, baseurl)
        print(f"[site]  {site} — {len(achados)} problema(s)")
        problemas += achados

    if problemas:
        print("\nProblemas encontrados:\n")
        for p in problemas:
            print(f"  {p}")
        print(
            f"\n{len(problemas)} problema(s). Links internos precisam de "
            "{{ site.baseurl }} (Markdown) ou do filtro relative_url (HTML/templates).\n"
            "Detalhes na seção 'Links internos' do README."
        )
        return 1

    print("\nOK: nenhum link interno quebrado ou sem prefixo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
