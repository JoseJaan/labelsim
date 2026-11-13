"""Computes the measures from a label matrix or from counts already available."""

from collections.abc import Mapping

import numpy as np

from .contingency import contingency, pairs
from .registry import LITERATURE, list_measures, resolve

OUTPUTS = ("matrix", "long")


def _measure_functions(measures, variant):
    """Converts the ``measures`` argument into a dictionary output label -> function.

    Accepts ``None`` for every measure of the variant, a name, a list of names or a
    dictionary from label to name or to a function ``f(a, b, c, d, n)``. The dictionary
    is what allows testing a new formula without touching the catalog.
    """
    if measures is None:
        measures = list_measures(variant)
    if isinstance(measures, str) or callable(measures):
        measures = [measures]
    items = measures.items() if isinstance(measures, Mapping) else [(m, m) for m in measures]

    functions = {}
    for label, spec in items:
        if not isinstance(label, str):
            raise TypeError("uma medida dada como função precisa de nome; use um dicionário, "
                            "por exemplo {'minha': lambda a, b, c, d, n: a / n}")
        if label in functions:
            raise ValueError(f"medida repetida na chamada: {label!r}")
        functions[label] = spec if callable(spec) else resolve(spec, variant)
    return functions


def from_contingency(a, b, c, d, measures=None, *, variant=LITERATURE):
    """Applies the measures to counts already computed.

    ``a``, ``b``, ``c`` and ``d`` may be scalars or arrays of any compatible shape; n is
    recomputed as a + b + c + d. Returns a dictionary with one float64 array per measure,
    in the shape of the counts. Divisions by zero and logarithms of zero yield NaN or
    infinity, with no warning and no replacement by zero.
    """
    counts = np.broadcast_arrays(*(np.asarray(x, dtype=np.float64) for x in (a, b, c, d)))
    a, b, c, d = counts
    n = a + b + c + d
    functions = _measure_functions(measures, variant)
    with np.errstate(all="ignore"):
        return {label: np.asarray(fn(a, b, c, d, n), dtype=np.float64)
                for label, fn in functions.items()}


def similarity(Y, measures=None, *, variant=LITERATURE, output="matrix", labels=None):
    """Measures between all pairs of labels of a binary matrix.

    With ``output="matrix"``, returns a dictionary with one q x q matrix per measure, in
    which position [i, j] uses the table of the pair (i, j), diagonal included. With
    ``output="long"``, returns a pandas DataFrame with one pair i < j per row, the
    counts and one column per measure.
    """
    if output not in OUTPUTS:
        raise ValueError(f"saída desconhecida: {output!r}; use uma de {OUTPUTS}")
    table = contingency(Y, labels)
    if output == "matrix":
        return from_contingency(table.a, table.b, table.c, table.d, measures,
                                variant=variant)

    long = pairs(table)
    values = from_contingency(long["a"], long["b"], long["c"], long["d"], measures,
                              variant=variant)
    clashes = sorted(set(values) & set(long.columns))
    if clashes:
        raise ValueError(f"nome de medida igual a coluna da tabela: {clashes}")
    for label, column in values.items():
        long[label] = column
    return long
