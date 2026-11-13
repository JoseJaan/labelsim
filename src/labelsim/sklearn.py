"""Integration with scikit-learn, which is an optional dependency.

``LabelSimilarity`` follows the scikit-learn estimator convention (parameters in the
constructor, ``fit`` returning the object itself and learned attributes with a trailing
underscore), so it works with ``clone``, ``get_params`` and ``set_params``.
``make_metric`` builds a function of two binary vectors for
``sklearn.metrics.pairwise_distances``.
"""

import numpy as np
from sklearn.base import BaseEstimator

from .api import from_contingency
from .contingency import contingency
from .registry import LITERATURE

_OUTPUT = "measure"


class LabelSimilarity(BaseEstimator):
    """Similarity matrix between the labels of Y for one measure.

    ``measure`` is a catalog name or a function ``f(a, b, c, d, n)``. After ``fit``,
    ``similarity_matrix_`` (q x q), ``contingency_`` and ``labels_`` are available.
    """

    def __init__(self, measure="jaccard", variant=LITERATURE):
        self.measure = measure
        self.variant = variant

    def fit(self, Y, y=None):
        table = contingency(Y)
        values = from_contingency(table.a, table.b, table.c, table.d,
                                  {_OUTPUT: self.measure}, variant=self.variant)
        self.contingency_ = table
        self.labels_ = table.labels
        self.similarity_matrix_ = values[_OUTPUT]
        return self


def make_metric(measure, variant=LITERATURE):
    """Function ``f(u, v)`` that applies the measure to two binary vectors.

    ``u`` plays the role of label i and ``v`` of label j. The value is returned as the
    measure defines it: for ``pairwise_distances``, which expects a distance, use a
    distance-type measure or convert the similarity beforehand.
    """
    def metric(u, v):
        u = np.asarray(u, dtype=np.float64)
        v = np.asarray(v, dtype=np.float64)
        a = np.sum(u * v)
        b = np.sum((1 - u) * v)
        c = np.sum(u * (1 - v))
        d = u.size - a - b - c
        return float(from_contingency(a, b, c, d, {_OUTPUT: measure}, variant=variant)[_OUTPUT])
    return metric
