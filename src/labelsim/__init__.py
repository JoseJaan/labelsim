"""Similarity measures between binary labels of multi-label data.

Gathers the 107 measures of Gatto (2021) on the contingency table (a, b, c, d), in two
variants: the published formulas (default) and the faithful transcription of the original
R code.

    >>> import numpy as np
    >>> import labelsim
    >>> Y = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 0]])
    >>> float(labelsim.similarity(Y, ["jaccard"])["jaccard"][0, 1])
    0.25
"""

from .api import from_contingency, similarity
from .contingency import Contingency, check_contingency, contingency, pairs
from .registry import MeasureUnavailableError, describe, list_measures, resolve

__version__ = "0.1.0"

__all__ = [
    "Contingency",
    "MeasureUnavailableError",
    "check_contingency",
    "contingency",
    "describe",
    "from_contingency",
    "list_measures",
    "pairs",
    "resolve",
    "similarity",
]
