#!/usr/bin/env python3
"""Importa o manual do usuário final do pnp-ccv-frontend (VitePress) para o Guia.

A fonte de verdade é ``doc/usuario`` no repositório do frontend: lá as figuras
nascem de specs Playwright (``pnpm docs:shots``) e não são versionadas. Este
script converte as páginas para o Jekyll do Guia e copia só as figuras citadas.
Rodar de novo sobrescreve ``docs/documentacao/manual-do-usuario`` por inteiro,
então correções devem ser feitas na fonte, não aqui.

O que muda na conversão:
- front matter Jekyll (layout, title tirado do H1, toc);
- links ``.md`` relativos viram ``{{site.baseurl}}/documentacao/...``;
- figuras ``../images/...`` viram ``{{site.baseurl}}/assets/img/docs/...``;
- âncoras citadas ganham ``{#id}`` explícito no título, porque o slug do
  VitePress tira acentos e o do kramdown não garante o mesmo id;
- containers ``::: danger|warning Título`` viram blockquote.

Uso:
    python3 scripts/importar_manual_usuario.py /caminho/para/pnp-ccv-frontend
"""

from __future__ import annotations

import json
import posixpath
import re
import shutil
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PASTA = "manual-do-usuario"
DESTINO = RAIZ / "docs" / "documentacao" / PASTA
DESTINO_IMG = RAIZ / "docs" / "assets" / "img" / "docs" / PASTA
URL_DOC = "{{site.baseurl}}/documentacao/" + PASTA
URL_IMG = "{{site.baseurl}}/assets/img/docs/" + PASTA

IGNORAR = {"CONTRIBUINDO.md"}
RE_LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")
RE_TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*$")

# O index.md da fonte abre com um aviso para desenvolvedores (pnpm, Docker,
# CONTRIBUINDO.md) que não faz sentido no Guia.
RE_AVISO_DEV = re.compile(r"\n> A forma boa de ler este manual.*?\n(?=\n)", re.S)


def slug(texto: str) -> str:
    """Mesmo slug do VitePress: sem acento, minúsculo, separado por hífen."""
    s = unicodedata.normalize("NFKD", texto)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def url_pagina(rel: str) -> str:
    rel = rel[: -len(".md")]
    if rel == "index":
        return URL_DOC + "/"
    return URL_DOC + "/" + rel.removesuffix("/index")


def converter_containers(texto: str) -> str:
    saida, dentro = [], False
    for linha in texto.split("\n"):
        m = re.match(r"^:::\s*(\w+)\s*(.*)$", linha)
        if m and not dentro:
            dentro = True
            saida.append(f"> **⚠️ {m.group(2) or m.group(1).capitalize()}**")
            saida.append(">")
        elif linha.strip() == ":::" and dentro:
            dentro = False
        elif dentro:
            saida.append(f"> {linha}" if linha.strip() else ">")
        else:
            saida.append(linha)
    assert not dentro, "container ::: sem fechamento"
    return "\n".join(saida)


def main(frontend: Path) -> None:
    fonte = frontend / "doc" / "usuario"
    paginas = sorted(
        p.relative_to(fonte).as_posix()
        for p in fonte.rglob("*.md")
        if ".vitepress" not in p.parts and p.name not in IGNORAR
    )
    textos = {rel: (fonte / rel).read_text(encoding="utf-8") for rel in paginas}
    textos["index.md"], n = RE_AVISO_DEV.subn("", textos["index.md"])
    assert n == 1, "aviso de desenvolvedor do index.md mudou na fonte"

    # 1ª passada: reescreve links e coleta âncoras e figuras citadas.
    ancoras: dict[str, set[str]] = {rel: set() for rel in paginas}
    figuras: set[str] = set()

    def reescrever(rel: str):
        base = posixpath.dirname(rel)

        def troca(m: re.Match) -> str:
            bang, rotulo, alvo = m.groups()
            if re.match(r"^[a-z]+:", alvo):
                return m.group(0)
            caminho, _, ancora = alvo.partition("#")
            destino = posixpath.normpath(posixpath.join(base, caminho)) if caminho else rel
            if ancora:
                assert destino in ancoras, f"{rel}: âncora para página inexistente {alvo}"
                ancoras[destino].add(ancora)
            if not caminho:
                return m.group(0)
            if bang:
                assert destino.startswith("images/"), f"{rel}: figura fora de images/ {alvo}"
                figuras.add(destino)
                return f"![{rotulo}]({URL_IMG}/{destino.removeprefix('images/')})"
            assert destino in textos, f"{rel}: link para página inexistente {alvo}"
            url = url_pagina(destino) + (f"#{ancora}" if ancora else "")
            return f"[{rotulo}]({url})"

        return troca

    convertidos = {rel: RE_LINK.sub(reescrever(rel), t) for rel, t in textos.items()}

    if DESTINO.exists():
        shutil.rmtree(DESTINO)
    if DESTINO_IMG.exists():
        shutil.rmtree(DESTINO_IMG)

    # 2ª passada: âncoras explícitas, containers, front matter.
    for rel, texto in convertidos.items():
        faltando = set(ancoras[rel])
        linhas, titulo, em_codigo = [], None, False
        for linha in texto.split("\n"):
            if linha.startswith("```"):
                em_codigo = not em_codigo
            m = None if em_codigo else RE_TITULO.match(linha)
            if m:
                if titulo is None and m.group(1) == "#":
                    titulo = m.group(2)
                s = slug(m.group(2))
                if s in faltando:
                    faltando.discard(s)
                    linha = f"{linha} {{#{s}}}"
            linhas.append(linha)
        assert not faltando, f"{rel}: âncoras sem título correspondente {faltando}"
        assert titulo, f"{rel}: sem H1"
        corpo = converter_containers("\n".join(linhas))
        cabecalho = f"---\nlayout: default\ntitle: {json.dumps(titulo, ensure_ascii=False)}\ntoc: true\n---\n"
        alvo = DESTINO / rel
        alvo.parent.mkdir(parents=True, exist_ok=True)
        alvo.write_text(cabecalho + corpo, encoding="utf-8")

    for fig in sorted(figuras):
        origem = fonte / fig
        assert origem.is_file(), f"figura citada não existe na fonte: {fig} (rode pnpm docs:shots)"
        alvo = DESTINO_IMG / fig.removeprefix("images/")
        alvo.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origem, alvo)

    print(f"{len(convertidos)} páginas e {len(figuras)} figuras em {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]).resolve())
