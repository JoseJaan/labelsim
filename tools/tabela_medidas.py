"""Generates docs/medidas.md from the catalogs.

Usage:
    python tools/tabela_medidas.py
"""

from collections import Counter
from pathlib import Path

from labelsim.registry import GATTO, MEASURES

OUTPUT = Path(__file__).resolve().parents[1] / "docs" / "medidas.md"

STATUS_TEXT = {
    "correta": "Igual à fórmula publicada.",
    "erro_precedencia": "A precedência de operadores do R muda a conta.",
    "termo_trocado": "Um termo da fórmula foi trocado por outro.",
    "formula_divergente": "A expressão difere da publicada de outra forma.",
    "constante": "Numerador e denominador iguais; vale 1 ou NaN.",
    "fonte_pendente": "Sem fórmula conferida em fonte disponível; só existe a variante gatto2021.",
}


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def render():
    lines = [
        "# Medidas do labelsim",
        "",
        "Gerado por `tools/tabela_medidas.py` a partir de `src/labelsim/catalog/`. Não edite à mão.",
        "",
        "Convenção da tabela para o par (i, j), como na Tabela 1 de Choi, Cha e Tappert (2010).",
        "",
        "| | j presente | j ausente |",
        "| --- | --- | --- |",
        "| **i presente** | a | c |",
        "| **i ausente** | b | d |",
        "",
        "## Variante literature",
        "",
        f"{len(MEASURES)} fórmulas distintas. A coluna de nomes de Gatto (2021) lista os nomes "
        "do código original que, nesta variante, dão a fórmula da linha.",
        "",
        "| id | Medida | Tipo | Fórmula | Referência | Apelidos | Nomes de Gatto (2021) |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for measure in sorted(MEASURES.values(), key=lambda m: m.id):
        gatto_names = sorted(e.gatto_name for e in GATTO.values() if e.canonical == measure.id)
        lines.append("| " + " | ".join(cell(x) for x in (
            f"`{measure.id}`", measure.name, measure.kind, f"`{measure.formula}`",
            measure.reference, ", ".join(f"`{a}`" for a in measure.aliases),
            ", ".join(f"`{g}`" for g in gatto_names))) + " |")

    counts = Counter(entry.status for entry in GATTO.values())
    lines += [
        "",
        "## Variante gatto2021",
        "",
        f"Os {len(GATTO)} nomes de `getNamesListFunctions()`, transcritos do código R original "
        "com a mesma precedência de operadores.",
        "",
        "| Situação | Nomes | Significado |",
        "| --- | --- | --- |",
    ]
    for status, text in STATUS_TEXT.items():
        lines.append(f"| `{status}` | {counts.get(status, 0)} | {text} |")
    lines += [
        "",
        "| Nome original | id | Situação | Fórmula no código | Fórmula da literatura | Nota |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for entry in sorted(GATTO.values(), key=lambda e: e.gatto_name):
        target = f"`{entry.canonical}`" if entry.canonical else ""
        lines.append("| " + " | ".join(cell(x) for x in (
            f"`{entry.gatto_name}`", f"`{entry.id}`", entry.status, f"`{entry.formula}`",
            target, entry.note)) + " |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    OUTPUT.write_text(render(), encoding="utf-8", newline="\n")
    print(f"gravado: {OUTPUT}")
