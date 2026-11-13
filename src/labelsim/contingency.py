"""2x2 contingency table of all pairs of labels.

For the pair (i, j), it follows Table 1 of Choi, Cha and Tappert (2010)
    a  i present and j present
    b  i absent and j present
    c  i present and j absent
    d  i absent and j absent

With this orientation, a + c counts the presences of i and a + b those of j, and the
catalog formulas hold exactly as printed in the source. The matrices b and c are
transposes of each other, so swapping the convention amounts to swapping i and j.
"""

from dataclasses import dataclass

import numpy as np
from scipy import sparse


@dataclass(frozen=True)
class Contingency:
    """The four counts of each pair of labels, as q x q float64 matrices.

    Double precision is deliberate. The product of the four marginals, which appears in
    the denominator of several measures, exceeds the 32-bit integer limit with about
    twenty thousand instances, and in float64 the computation is exact up to 2^53.
    """

    a: np.ndarray
    b: np.ndarray
    c: np.ndarray
    d: np.ndarray
    labels: tuple

    @property
    def n(self):
        return self.a + self.b + self.c + self.d

    @property
    def n_labels(self):
        return self.a.shape[0]


def _label_names(labels, n_labels):
    names = tuple(range(n_labels)) if labels is None else tuple(labels)
    if len(names) != n_labels:
        raise ValueError(f"{len(names)} nomes de rótulo para {n_labels} colunas")
    return names


def _as_binary_matrix(Y):
    if sparse.issparse(Y):
        Y = sparse.csr_array(Y, dtype=np.float64)
        values = Y.data
    else:
        Y = np.asarray(Y, dtype=np.float64)
        values = Y
    if Y.ndim != 2:
        raise ValueError("Y precisa ser uma matriz instâncias x rótulos")
    if not np.all((values == 0) | (values == 1)):
        raise ValueError("Y precisa ser binária, só com 0 e 1")
    return Y


def contingency(Y, labels=None):
    """Computes a, b, c and d for all pairs of labels of a binary matrix.

    ``Y`` has one row per instance and one column per label, dense (numpy array or
    DataFrame) or sparse (scipy). The label names come from ``labels``, from the columns
    of a DataFrame or, when both are missing, from the column position.

    Only the co-occurrence matrix a = YᵀY is computed by a product; b, c and d are derived
    from it and from the presence counts, without building the complement 1 - Y, which
    would be dense for a sparse matrix.
    """
    if labels is None and hasattr(Y, "columns"):
        labels = list(Y.columns)
    Y = _as_binary_matrix(Y)
    names = _label_names(labels, Y.shape[1])
    n_instances = Y.shape[0]

    a = Y.T @ Y
    a = a.toarray() if sparse.issparse(a) else np.asarray(a)
    a = a.astype(np.float64, copy=False)
    present = np.diag(a).copy()

    b = present[np.newaxis, :] - a
    c = present[:, np.newaxis] - a
    d = n_instances - a - b - c

    table = Contingency(a=a, b=b, c=c, d=d, labels=names)
    problems = check_contingency(table, n_instances)
    if problems:
        raise RuntimeError("tabela de contingência inconsistente: " + "; ".join(problems))
    return table


def check_contingency(table, n_instances, positives=None, tolerance=1e-9):
    """Lists the inconsistencies of a table, empty when everything is correct.

    These are the same checks as ``validate_contingency`` in the Similarity-Measures
    repository, plus the one for negative counts.
    """
    checks = {
        "a + b + c + d difere do número de instâncias":
            np.any(np.abs(table.n - n_instances) > tolerance),
        "há contagem negativa":
            any(np.any(m < -tolerance) for m in (table.a, table.b, table.c, table.d)),
        "a não é simétrica": np.any(np.abs(table.a - table.a.T) > tolerance),
        "d não é simétrica": np.any(np.abs(table.d - table.d.T) > tolerance),
        "b não é a transposta de c": np.any(np.abs(table.b - table.c.T) > tolerance),
        "a diagonal de a difere da contagem de presenças de cada rótulo":
            positives is not None
            and np.any(np.abs(np.diag(table.a) - np.asarray(positives)) > tolerance),
    }
    return [message for message, failed in checks.items() if failed]


def pairs(table):
    """The pairs i < j in long format, one per row, as a pandas DataFrame.

    The diagonal is left out, as in ``contingency_pairs`` of the Similarity-Measures
    repository.
    """
    import pandas as pd

    i, j = np.triu_indices(table.n_labels, k=1)
    return pd.DataFrame({
        "i": i,
        "j": j,
        "label_i": [table.labels[k] for k in i],
        "label_j": [table.labels[k] for k in j],
        "a": table.a[i, j],
        "b": table.b[i, j],
        "c": table.c[i, j],
        "d": table.d[i, j],
        "n": table.n[i, j],
    })
