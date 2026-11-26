#!/usr/bin/env python3
"""Gera a planilha de exemplo de fornecimento de dados a partir dos contratos do Guia.

A fonte é o bloco YAML completo (o que tem ``dataContractSpecification`` e
``models``) publicado em cada página de
``docs/documentacao/usuarios-especializados/contratos/``. A saída é
``docs/assets/files/template_fornecimento_dados.xlsx``, refeita por inteiro:

- ``LEIA-ME``: orientações e um índice com uma linha por modelo (aba, contrato,
  título, obrigatoriedade, quantidade de campos, versão do contrato);
- ``Dicionario``: um campo por linha (tipo, obrigatório, chave, enum,
  referência, descrição);
- ``_listas`` (oculta): os valores de cada ``enum`` e o par TRUE/FALSE, que as
  listas suspensas das abas de modelo usam;
- uma aba por modelo, com cabeçalho colorido por papel (amarelo = chave
  primária, laranja = obrigatório, azul = opcional), comentário com o
  dicionário do campo, listas suspensas, formato de data e destaque vermelho
  em obrigatório vazio numa linha preenchida.

As linhas de exemplo (2 a 5 de cada aba) são lidas da planilha atual pelo nome
do campo e regravadas. Para corrigir um exemplo, edite a planilha e rode o
script de novo. Campo novo nasce sem exemplo, e campo removido do contrato
perde o seu. No fim, o script lista os exemplos que não respeitam o schema
(obrigatório vazio, valor fora do enum, tipo, tamanho, chave duplicada,
referência inexistente). Regras ``quality`` não são conferidas.

Antes de gravar, o script confere se cada página está coerente com o próprio
YAML: versão no cabeçalho, modelos, obrigatoriedade do modelo e, na tabela de
campos, a lista de campos, o tipo e a coluna Obrigatório. Se houver
divergência, ele para com erro e não grava nada, porque não dá para saber qual
dos dois lados está certo.

Uso:
    python3 scripts/gerar_planilha_contratos.py              # regrava a planilha
    python3 scripts/gerar_planilha_contratos.py --verificar  # só diz se está desatualizada

Dependências: ``pip install openpyxl pyyaml``.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import re
import sys
import tempfile
import warnings
from pathlib import Path

try:
    import yaml
    from openpyxl import Workbook, load_workbook
    from openpyxl.comments import Comment
    from openpyxl.formatting.rule import FormulaRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter as col
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError as e:  # pragma: no cover
    sys.exit(f"Dependência ausente ({e.name}). Instale com: pip install openpyxl pyyaml")

# A planilha atual traz validações numa extensão do Excel que o openpyxl não lê;
# ela é refeita do zero, então o aviso não interessa.
warnings.filterwarnings("ignore", message="Data Validation extension")

RAIZ = Path(__file__).resolve().parents[1]
CONTRATOS = RAIZ / "docs" / "documentacao" / "usuarios-especializados" / "contratos"
PLANILHA = RAIZ / "docs" / "assets" / "files" / "template_fornecimento_dados.xlsx"

# Páginas da pasta que trazem YAML de exemplo, não um contrato publicado.
IGNORAR = {"anatomia_yaml.md"}

ULTIMA_LINHA = 1001  # validações e formatação cobrem as linhas 2..1001
LINHAS_EXEMPLO = range(2, 6)

AZUL = "17365D"
F_TITULO = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
F_CAB = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
F_SUB = Font(name="Calibri", size=11, bold=True, color=AZUL)
F_TEXTO = Font(name="Calibri", size=11)
F_INDICE = Font(name="Calibri", size=12)
F_CAMPO = Font(name="Calibri", size=11, bold=True)
P_AZUL = PatternFill("solid", fgColor=AZUL)
P_CHAVE = PatternFill("solid", fgColor="FFF2CC")
P_OBRIG = PatternFill("solid", fgColor="FCE4D6")
P_OPC = PatternFill("solid", fgColor="DDEBF7")
P_EXEMPLO = PatternFill("solid", fgColor="E2F0D9")
P_ERRO = PatternFill("solid", fgColor="FFC7CE")
BORDA_CAB = Border(bottom=Side(style="thin", color="B7B7B7"))
FORMATO_DATA = "yyyy\\-mm\\-dd"

ORIENTACOES = [
    "• Preencha uma linha por registro, sem alterar os nomes das colunas.",
    "• Cabeçalhos em amarelo são chaves primárias; em laranja, campos obrigatórios; em azul, opcionais.",
    "• Datas devem usar o formato AAAA-MM-DD. Valores booleanos devem ser TRUE ou FALSE.",
    "• Campos array devem seguir o formato aceito pela integração da instituição; consulte o comentário da célula.",
    "• As listas suspensas refletem os valores enum declarados nos contratos.",
    "• Consulte a aba Dicionario para tipos, obrigatoriedade, referências e descrições completas.",
]
INDICE = ["Aba", "Contrato", "Modelo", "Título", "Modelo obrigatório",
          "Quantidade de campos", "Versão do contrato"]
LARGURAS_INDICE = [31, 28, 42, 45, 19, 20, 19]
DICIONARIO = ["Contrato", "Modelo", "Aba", "Campo", "Tipo", "Obrigatório",
              "Chave primária", "Enum", "Referência", "Descrição"]
LARGURAS_DICIONARIO = [28, 38, 31, 38, 18, 13, 15, 55, 45, 80]

RE_YAML = re.compile(r"^```yaml\n(.*?)^```", re.S | re.M)
RE_VERSAO = re.compile(r"\*\*Versão:\*\* `([^`]+)`")
RE_MODELO = re.compile(r"^## Modelo `([^`]+)`.*$", re.M)
RE_META_REQ = re.compile(r"meta\.required: (true|false)")
RE_TABELA = re.compile(r"^### Tabela de campos\s*\n((?:\|.*\n?)+)", re.M)


class Erro(Exception):
    pass


# ---------------------------------------------------------------- leitura

def sim_nao(v) -> str:
    return "sim" if v else "não"


def nome_aba(modelo: str) -> str:
    """Nome de aba do Excel (máx. 31): corta e sufixa com hash, como a planilha original."""
    if len(modelo) <= 31:
        return modelo
    return f"{modelo[:26]}_{hashlib.sha1(modelo.encode()).hexdigest()[:4]}"


def tipo(f: dict) -> str:
    if f.get("type") == "array":
        return f"array<{(f.get('items') or {}).get('type', '')}>"
    return f.get("type")


def valores_enum(f: dict) -> list | None:
    return f.get("enum") or (f.get("items") or {}).get("enum")


def texto_enum(f: dict) -> str | None:
    e = valores_enum(f)
    return " | ".join(str(v) for v in e) if e else None


def texto_ref(f: dict) -> str | None:
    partes = []
    if f.get("references"):
        partes.append(f["references"])
    rp = f.get("referencia_pnp")
    for r in (rp if isinstance(rp, list) else [rp] if rp else []):
        partes.append(f"PNP:{r['recurso']} ({r.get('tipo', '')})")
    return "; ".join(partes) or None


def tabela_campos(trecho: str) -> list[dict]:
    m = RE_TABELA.search(trecho)
    if not m:
        return []
    linhas = [l for l in m.group(1).splitlines() if l.startswith("|")]
    cab = [c.strip() for c in linhas[0].strip("|").split("|")]
    saida = []
    for l in linhas[2:]:
        celulas = [c.strip() for c in re.split(r"(?<!\\)\|", l.strip().strip("|"))]
        saida.append(dict(zip(cab, celulas)))
    return saida


def conferir_pagina(pagina: Path, texto: str, contrato: dict) -> list[str]:
    """Divergências entre o texto da página e o YAML que ela publica."""
    erros = []
    v = RE_VERSAO.search(texto)
    if v and v.group(1) != contrato["info"]["version"]:
        erros.append(f"cabeçalho diz versão {v.group(1)}, YAML diz {contrato['info']['version']}")

    partes = RE_MODELO.split(texto)
    secoes = dict(zip(partes[1::2], partes[2::2]))
    modelos = contrato["models"]
    if set(secoes) != set(modelos):
        erros.append(f"seções '## Modelo' {sorted(secoes)} ≠ modelos do YAML {sorted(modelos)}")

    for nome, sec in secoes.items():
        mv = modelos.get(nome)
        if mv is None:
            continue
        req = RE_META_REQ.search(sec)
        if req and (req.group(1) == "true") != bool(mv["meta"].get("required")):
            erros.append(f"{nome}: nota 'No fluxo do Coletor' diz meta.required: {req.group(1)}, "
                         f"YAML diz {str(bool(mv['meta'].get('required'))).lower()}")
        linhas = tabela_campos(sec)
        if not linhas:
            erros.append(f"{nome}: tabela de campos não encontrada")
            continue
        na_tabela = [l.get("Campo", "").strip("`") for l in linhas]
        if na_tabela != list(mv["fields"]):
            erros.append(f"{nome}: campos da tabela {na_tabela} ≠ campos do YAML {list(mv['fields'])}")
            continue
        for l, (campo, f) in zip(linhas, mv["fields"].items()):
            t = re.sub(r"`([^`]*)`\s*\(de `([^`]*)`\)", r"array<\2>", l.get("Tipo", "")).strip("`")
            if t != tipo(f):
                erros.append(f"{nome}.{campo}: tabela diz tipo {t}, YAML diz {tipo(f)}")
            if l.get("Obrigatório") != sim_nao(f.get("required")):
                erros.append(f"{nome}.{campo}: tabela diz obrigatório '{l.get('Obrigatório')}', "
                             f"YAML diz '{sim_nao(f.get('required'))}'")
    return [f"{pagina.name}: {e}" for e in erros]


def ler_contratos() -> list[dict]:
    contratos, erros, ids = [], [], {}
    for pagina in sorted(CONTRATOS.glob("*.md")):
        if pagina.name in IGNORAR:
            continue
        texto = pagina.read_text(encoding="utf-8")
        blocos = [b for b in RE_YAML.findall(texto)
                  if "dataContractSpecification" in b and "models:" in b]
        if not blocos:
            continue
        if len(blocos) > 1:
            erros.append(f"{pagina.name}: mais de um YAML de contrato completo")
            continue
        try:
            c = yaml.safe_load(blocos[0])
        except yaml.YAMLError as e:
            erros.append(f"{pagina.name}: YAML inválido: {e}")
            continue
        if c["id"] in ids:
            erros.append(f"{pagina.name}: contrato '{c['id']}' já publicado em {ids[c['id']]}")
        ids[c["id"]] = pagina.name
        erros += conferir_pagina(pagina, texto, c)
        contratos.append(c)
    if erros:
        raise Erro("Páginas incoerentes com o próprio YAML; corrija antes de gerar:\n  - "
                   + "\n  - ".join(erros))
    contratos.sort(key=lambda c: c["id"])
    return contratos


def ler_exemplos(planilha: Path) -> dict[str, list[dict]]:
    """{aba: [ {campo: valor}, ... ]} das linhas de exemplo da planilha atual."""
    if not planilha.exists():
        return {}
    wb = load_workbook(planilha)
    saida = {}
    for ws in wb.worksheets:
        if ws.title in ("LEIA-ME", "Dicionario", "_listas"):
            continue
        cab = [c.value for c in ws[1]]
        saida[ws.title] = [{h: ws.cell(r, j + 1).value for j, h in enumerate(cab) if h}
                           for r in LINHAS_EXEMPLO]
    return saida


def ler_larguras(planilha: Path) -> dict[tuple[str, str], float]:
    if not planilha.exists():
        return {}
    wb = load_workbook(planilha)
    saida = {}
    for ws in wb.worksheets:
        cab = [c.value for c in ws[1]]
        for d in ws.column_dimensions.values():
            if d.customWidth and d.min:
                for i in range(d.min, (d.max or d.min) + 1):
                    if i <= len(cab) and cab[i - 1]:
                        saida[(ws.title, cab[i - 1])] = d.width
    return saida


# ---------------------------------------------------------------- escrita

def comentario(f: dict) -> str:
    linhas = [f"Tipo: {f.get('type')}",
              f"Obrigatório: {sim_nao(f.get('required'))}",
              f"Chave primária: {sim_nao(f.get('primaryKey'))}"]
    if texto_enum(f):
        linhas.append(f"Valores permitidos: {texto_enum(f)}")
    lo, hi = f.get("minLength"), f.get("maxLength")
    if lo or hi:
        linhas.append(f"Tamanho: exatamente {lo} caracteres" if lo == hi
                      else f"Tamanho: de {lo or 0} a {hi or 'sem limite de'} caracteres")
    if texto_ref(f):
        linhas.append(f"Referência: {texto_ref(f)}")
    if f.get("description"):
        linhas.append(f"Descrição: {f['description']}")
    return "\n".join(linhas)


def intervalos(colunas: list[int]) -> list[tuple[int, int]]:
    saida: list[list[int]] = []
    for c in colunas:
        if saida and c == saida[-1][1] + 1:
            saida[-1][1] = c
        else:
            saida.append([c, c])
    return [tuple(i) for i in saida]


def montar(contratos: list[dict], exemplos: dict, larguras: dict) -> Workbook:
    modelos = [(c, m, mv) for c in contratos for m, mv in c["models"].items()]
    abas = [nome_aba(m) for _, m, _ in modelos]
    repetidas = {a for a in abas if abas.count(a) > 1}
    if repetidas:
        raise Erro(f"Modelos de contratos diferentes caem na mesma aba: {sorted(repetidas)}")

    wb = Workbook()
    leia = wb.active
    leia.title = "LEIA-ME"
    dic = wb.create_sheet("Dicionario")
    listas = wb.create_sheet("_listas")
    listas.sheet_state = "hidden"

    # _listas: coluna A booleana, depois uma coluna por enum escalar
    listas["A1"], listas["A2"], listas["A3"] = "boolean", "TRUE", "FALSE"
    faixa_lista = {}
    j = 2
    for c, m, mv in modelos:
        for campo, f in mv["fields"].items():
            if f.get("type") == "array" or not f.get("enum"):
                continue  # array aceita vários valores: lista suspensa não serve
            listas.cell(1, j, f"{c['id']}_{m}_{campo}")
            for i, v in enumerate(f["enum"]):
                listas.cell(2 + i, j, str(v))
            faixa_lista[(m, campo)] = f"_listas!${col(j)}$2:${col(j)}${1 + len(f['enum'])}"
            j += 1

    # LEIA-ME
    leia["A1"] = "Template consolidado para fornecimento de dados"
    leia["A1"].font, leia["A1"].fill = F_TITULO, P_AZUL
    leia.row_dimensions[1].height = 21
    leia["A2"] = "Orientações"
    leia["A2"].font = F_SUB
    for i, t in enumerate(ORIENTACOES):
        leia.cell(3 + i, 1, t).font = F_TEXTO
    for r in [1] + list(range(3, 3 + len(ORIENTACOES))):
        leia.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(INDICE))
    for i, h in enumerate(INDICE, start=1):
        cel = leia.cell(10, i, h)
        cel.font, cel.fill, cel.alignment = F_CAB, P_AZUL, Alignment(horizontal="center")
    for k, (c, m, mv) in enumerate(modelos):
        r = 11 + k
        valores = [nome_aba(m), c["id"], m, mv.get("title"), sim_nao(mv["meta"].get("required")),
                   len(mv["fields"]), c["info"]["version"]]
        for i, v in enumerate(valores, start=1):
            leia.cell(r, i, v).font = F_INDICE
        leia.row_dimensions[r].height = 15.75
    for i, w in enumerate(LARGURAS_INDICE, start=1):
        leia.column_dimensions[col(i)].width = w
    leia.freeze_panes = "A11"

    # Dicionario
    for i, h in enumerate(DICIONARIO, start=1):
        cel = dic.cell(1, i, h)
        cel.font, cel.fill = F_CAB, P_AZUL
        cel.alignment = Alignment(horizontal="center", vertical="center")
    r = 2
    for c, m, mv in modelos:
        for campo, f in mv["fields"].items():
            valores = [c["id"], m, nome_aba(m), campo, tipo(f), sim_nao(f.get("required")),
                       sim_nao(f.get("primaryKey")), texto_enum(f), texto_ref(f), f.get("description")]
            for i, v in enumerate(valores, start=1):
                cel = dic.cell(r, i, v)
                cel.font, cel.alignment = F_TEXTO, Alignment(wrap_text=True, vertical="top")
            r += 1
    for i, w in enumerate(LARGURAS_DICIONARIO, start=1):
        dic.column_dimensions[col(i)].width = w
    dic.auto_filter.ref = f"A1:{col(len(DICIONARIO))}1"
    dic.freeze_panes = "A2"

    # Uma aba por modelo
    for c, m, mv in modelos:
        aba = nome_aba(m)
        ws = wb.create_sheet(aba)
        campos = list(mv["fields"].items())
        ultima = col(len(campos))
        linhas_ex = exemplos.get(aba) or [{} for _ in LINHAS_EXEMPLO]
        obrigatorias = []
        for j, (campo, f) in enumerate(campos, start=1):
            cab = ws.cell(1, j, campo)
            cab.font = F_CAMPO
            cab.fill = P_CHAVE if f.get("primaryKey") else P_OBRIG if f.get("required") else P_OPC
            cab.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
            cab.border = BORDA_CAB
            nota = Comment(comentario(f), "Coletor PNP")
            nota.width, nota.height = 144, 79
            cab.comment = nota
            if f.get("required"):
                obrigatorias.append(j)
            ws.column_dimensions[col(j)].width = larguras.get((aba, campo), max(10, len(campo) + 4))

            data = f.get("type") == "date"
            for r, linha in zip(LINHAS_EXEMPLO, linhas_ex):
                cel = ws.cell(r, j, linha.get(campo))
                cel.fill = P_EXEMPLO
                if data:
                    cel.number_format = FORMATO_DATA
            if data:
                for r in range(LINHAS_EXEMPLO.stop, ULTIMA_LINHA + 1):
                    ws.cell(r, j).number_format = FORMATO_DATA

            faixa = f"{col(j)}2:{col(j)}{ULTIMA_LINHA}"
            opcional = not f.get("required")
            if f.get("type") == "boolean":
                dv = DataValidation(type="list", formula1="_listas!$A$2:$A$3", allow_blank=opcional,
                                    showErrorMessage=True, errorTitle="Valor booleano inválido",
                                    error="Selecione TRUE ou FALSE.", showInputMessage=True,
                                    promptTitle=campo[:32], prompt="Selecione TRUE ou FALSE.")
            elif (m, campo) in faixa_lista:
                dv = DataValidation(type="list", formula1=faixa_lista[(m, campo)], allow_blank=opcional,
                                    showErrorMessage=True, errorTitle="Valor fora da lista",
                                    error="Selecione um valor previsto no contrato.")
            else:
                dv = None
            if dv:
                dv.add(faixa)
                ws.add_data_validation(dv)

        ws.row_dimensions[1].height = 45
        for a, b in intervalos(obrigatorias):
            ws.conditional_formatting.add(
                f"{col(a)}2:{col(b)}{ULTIMA_LINHA}",
                FormulaRule(formula=[f'AND(COUNTA($A2:${ultima}2)>0,{col(a)}2="")'], fill=P_ERRO))
        ws.auto_filter.ref = f"A1:{ultima}{ULTIMA_LINHA}"
        ws.freeze_panes = "A2"

    wb.active = 0
    return wb


# ---------------------------------------------------------------- conferências

TIPOS = {
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "bigint": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "double": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "date": lambda v: isinstance(v, (datetime.date, datetime.datetime)),
    "string": lambda v: isinstance(v, str),
    "array": lambda v: isinstance(v, str),  # na planilha o array vai como texto "a; b"
}


def conferir_exemplos(contratos: list[dict], exemplos: dict) -> list[str]:
    avisos = []
    for c in contratos:
        dados = {m: exemplos.get(nome_aba(m)) or [] for m in c["models"]}
        for m, mv in c["models"].items():
            aba = nome_aba(m)
            chave = [n for n, f in mv["fields"].items() if f.get("primaryKey")]
            vistas = {}
            for r, linha in zip(LINHAS_EXEMPLO, dados[m]):
                if not any(linha.get(n) not in (None, "") for n in mv["fields"]):
                    avisos.append(f"{aba} linha {r}: sem exemplo")
                    continue
                k = tuple(linha.get(n) for n in chave)
                if chave and k in vistas:
                    avisos.append(f"{aba} linha {r}: chave {k} repete a linha {vistas[k]}")
                vistas.setdefault(k, r)
                for n, f in mv["fields"].items():
                    v, onde = linha.get(n), f"{aba} linha {r}, {n}"
                    if v in (None, ""):
                        if f.get("required"):
                            avisos.append(f"{onde}: obrigatório vazio")
                        continue
                    if not TIPOS.get(f.get("type"), lambda _: True)(v):
                        avisos.append(f"{onde}: {v!r} não é {f.get('type')}")
                    e = valores_enum(f)
                    itens = [x.strip() for x in str(v).split(";")] if f.get("type") == "array" else [str(v)]
                    if e and any(x not in map(str, e) for x in itens):
                        avisos.append(f"{onde}: {v!r} fora dos valores permitidos")
                    lo, hi = f.get("minLength"), f.get("maxLength")
                    if (lo and len(str(v)) < lo) or (hi and len(str(v)) > hi):
                        avisos.append(f"{onde}: {v!r} fora do tamanho ({lo}..{hi})")
                    ref = f.get("references")
                    if ref:
                        rm, rf = ref.split(".")
                        if rm in dados and v not in [x.get(rf) for x in dados[rm]]:
                            avisos.append(f"{onde}: {v!r} não existe em {ref}")
    return avisos


def conteudo(planilha: Path) -> dict:
    """Valores e comentários de todas as células, para comparar versões.

    Listas suspensas e formatação saem dos mesmos dados (enum, tipo,
    obrigatório), que aparecem no Dicionario e nos comentários; comparar o
    texto basta para saber se o contrato mudou.
    """
    wb = load_workbook(planilha)
    saida = {}
    for ws in wb.worksheets:
        celulas = [(c.coordinate, c.value, c.comment.text if c.comment else None)
                   for linha in ws.iter_rows() for c in linha if c.value is not None]
        saida[ws.title] = (ws.sheet_state, celulas)
    return saida


# ---------------------------------------------------------------- principal

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--verificar", action="store_true",
                    help="não grava; sai com código 1 se a planilha estiver desatualizada")
    ap.add_argument("--saida", type=Path, default=PLANILHA,
                    help=f"arquivo a gravar (padrão: {PLANILHA.relative_to(RAIZ)})")
    args = ap.parse_args()

    try:
        contratos = ler_contratos()
        exemplos = ler_exemplos(PLANILHA)
        wb = montar(contratos, exemplos, ler_larguras(PLANILHA))
    except Erro as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2

    if args.verificar:
        if not PLANILHA.exists():
            print(f"{PLANILHA.relative_to(RAIZ)} não existe.")
            return 1
        with tempfile.TemporaryDirectory() as tmp:
            novo = Path(tmp) / "nova.xlsx"
            wb.save(novo)
            igual = conteudo(novo) == conteudo(PLANILHA)
        print("Planilha em dia com os contratos." if igual else
              "Planilha desatualizada: rode python3 scripts/gerar_planilha_contratos.py")
        return 0 if igual else 1

    wb.save(args.saida)
    n = sum(len(c["models"]) for c in contratos)
    print(f"Gravado {args.saida.relative_to(RAIZ) if args.saida.is_relative_to(RAIZ) else args.saida}: "
          f"{len(contratos)} contratos, {n} modelos.")
    for c in contratos:
        print(f"  {c['id']} {c['info']['version']}")

    avisos = conferir_exemplos(contratos, exemplos)
    if avisos:
        print(f"\nAVISO: {len(avisos)} problema(s) nas linhas de exemplo. Corrija na planilha "
              "e rode de novo:")
        for a in avisos:
            print(f"  - {a}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
