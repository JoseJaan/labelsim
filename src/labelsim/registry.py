"""Catalog of the measures and name resolution in the two variants.

Variant ``"literature"``: each name points to the published formula in ``literature.py``.
Names with the same formula, such as the seven of Gatto (2021) that equal b + c, point to
a single function. A name of Gatto (2021) with no formula checked against an available
source has no version in this variant, and requesting it raises
``MeasureUnavailableError``.

Variant ``"gatto2021"``: each of the 107 names points to its faithful transcription in
``gatto2021.py``, with the errors of the original code.

The accepted names are the measure identifier, the aliases in the ``aliases`` column of
``catalog/medidas.csv``, the original name of Gatto (2021), such as ``ochiai.e.1``, and
its form with underscores, such as ``ochiai_1``.
"""

import csv
from dataclasses import dataclass, field
from importlib import resources

from . import gatto2021, literature

LITERATURE = "literature"
GATTO2021 = "gatto2021"
VARIANTS = (LITERATURE, GATTO2021)


class MeasureUnavailableError(ValueError):
    """The measure exists in the catalog, but not in the requested variant."""


@dataclass(frozen=True)
class Measure:
    id: str
    name: str
    kind: str
    formula: str
    reference: str
    aliases: tuple
    note: str
    function: object = field(repr=False)


@dataclass(frozen=True)
class GattoEntry:
    gatto_name: str
    id: str
    canonical: str
    status: str
    formula: str
    note: str
    function: object = field(repr=False)


def _read_catalog(filename):
    path = resources.files("labelsim").joinpath("catalog", filename)
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _load_measures():
    measures = {}
    for row in _read_catalog("medidas.csv"):
        aliases = tuple(alias for alias in row["aliases"].split(";") if alias)
        measures[row["id"]] = Measure(
            id=row["id"], name=row["nome"], kind=row["tipo"], formula=row["formula"],
            reference=row["referencia"], aliases=aliases, note=row["nota"],
            function=literature.FUNCTIONS.get(row["id"]))
    return measures


def _load_gatto():
    entries = {}
    for row in _read_catalog("gatto2021.csv"):
        entries[row["nome_gatto"]] = GattoEntry(
            gatto_name=row["nome_gatto"], id=row["id"], canonical=row["canonica"],
            status=row["situacao"], formula=row["formula_gatto"], note=row["nota"],
            function=gatto2021.FUNCTIONS.get(row["nome_gatto"]))
    return entries


def _add_name(table, name, target):
    if table.get(name, target) != target:
        raise RuntimeError(f"o nome {name!r} aponta para {table[name]!r} e {target!r}")
    table[name] = target


def _literature_names(measures, gatto):
    names = {}
    for measure in measures.values():
        _add_name(names, measure.id, measure.id)
        for alias in measure.aliases:
            _add_name(names, alias, measure.id)
    for entry in gatto.values():
        _add_name(names, entry.gatto_name, entry.canonical)
        _add_name(names, entry.id, entry.canonical)
    return names


def _gatto_names(gatto):
    names = {}
    for entry in gatto.values():
        _add_name(names, entry.gatto_name, entry.gatto_name)
        _add_name(names, entry.id, entry.gatto_name)
    return names


MEASURES = _load_measures()
GATTO = _load_gatto()
_LITERATURE_NAMES = _literature_names(MEASURES, GATTO)
_GATTO_NAMES = _gatto_names(GATTO)


def _check_variant(variant):
    if variant not in VARIANTS:
        raise ValueError(f"variante desconhecida: {variant!r}; use uma de {VARIANTS}")


def _unknown(name):
    return KeyError(f"medida desconhecida: {name!r}; veja labelsim.list_measures()")


def resolve(name, variant=LITERATURE):
    """The function ``f(a, b, c, d, n)`` that the name designates in the requested variant."""
    _check_variant(variant)
    if variant == GATTO2021:
        if name in _GATTO_NAMES:
            return GATTO[_GATTO_NAMES[name]].function
        if name in _LITERATURE_NAMES:
            candidates = [entry.gatto_name for entry in GATTO.values()
                          if entry.canonical == _LITERATURE_NAMES[name]]
            raise MeasureUnavailableError(
                f"{name!r} não é um nome de Gatto (2021); os nomes com essa fórmula na "
                f"literatura são {candidates}")
        raise _unknown(name)

    if name not in _LITERATURE_NAMES:
        raise _unknown(name)
    canonical = _LITERATURE_NAMES[name]
    if not canonical:
        raise MeasureUnavailableError(
            f"{name!r} não tem fórmula conferida em fonte disponível; só existe a versão "
            f"de Gatto (2021), com variant='gatto2021'")
    return MEASURES[canonical].function


def list_measures(variant=LITERATURE, include_aliases=False):
    """The names available in the variant, in alphabetical order.

    Without aliases, the ``"literature"`` variant lists one entry per distinct formula and
    ``"gatto2021"`` the 107 original names.
    """
    _check_variant(variant)
    if variant == GATTO2021:
        names = _GATTO_NAMES if include_aliases else GATTO
        return sorted(names)
    if include_aliases:
        return sorted(name for name, target in _LITERATURE_NAMES.items() if target)
    return sorted(MEASURES)


def describe(name):
    """Everything the catalog knows about a name, in the two variants, as a dictionary."""
    if name not in _LITERATURE_NAMES and name not in _GATTO_NAMES:
        raise _unknown(name)
    info = {"name": name, "literature": None, "gatto2021": None}
    canonical = _LITERATURE_NAMES.get(name)
    if canonical:
        measure = MEASURES[canonical]
        info["literature"] = {
            "id": measure.id, "name": measure.name, "kind": measure.kind,
            "formula": measure.formula, "reference": measure.reference,
            "note": measure.note,
            "gatto_names": [entry.gatto_name for entry in GATTO.values()
                            if entry.canonical == canonical],
        }
    if name in _GATTO_NAMES:
        entry = GATTO[_GATTO_NAMES[name]]
        info["gatto2021"] = {
            "gatto_name": entry.gatto_name, "id": entry.id, "canonical": entry.canonical,
            "status": entry.status, "formula": entry.formula, "note": entry.note,
        }
    return info
