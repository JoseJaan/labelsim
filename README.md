# labelsim

Similarity measures between labels of multi-label data, computed on the contingency table
(a, b, c, d) of each pair of labels.

The library gathers the 107 measures of the
[MultiLabelSimilaritiesMeasures](https://github.com/cissagatto/MultiLabelSimilaritiesMeasures)
repository (Gatto, 2021) and the normalized mutual information (Strehl and Ghosh, 2002), in
two variants.

* `literature` (default) applies the formula as published. The 107 measures yield 64
  distinct formulas, because several names share the same formula, and the NMI completes
  the 65.
* `gatto2021` reproduces the original R code line by line, including where it diverges from
  the published formula. It is meant for comparison with results obtained with that code.

It is part of the undergraduate thesis *Estudo Sistemático de Medidas de Similaridade para
Correlações em Classificação Multirrótulo* (UFLA). The experiments of the thesis are in the
[Similarity-Measures](https://github.com/JoseJaan/Similarity-Measures) repository, in R.

## Installation

```bash
pip install -e .            # numpy and scipy
pip install -e ".[dev]"     # plus pandas, scikit-learn and pytest
```

Requires Python 3.10 or newer.

## Usage

```python
import numpy as np
import labelsim

# one row per instance, one column per label
Y = np.array([[1, 0, 1],
              [1, 1, 0],
              [0, 1, 1],
              [1, 0, 0]])

m = labelsim.similarity(Y, ["jaccard", "phi", "nmi"])
m["jaccard"]          # 3 x 3 matrix

# long format, one pair i < j per row (requires pandas)
labelsim.similarity(Y, ["jaccard", "phi"], output="long", labels=["x", "y", "z"])

# counts already computed
labelsim.from_contingency(a=10, b=5, c=3, d=982, measures=["yule_q", "sokal_michener"])

# a new formula, without touching the catalog
labelsim.similarity(Y, {"jaccard": "jaccard", "only_d": lambda a, b, c, d, n: d / n})

# the original code of Gatto (2021)
labelsim.similarity(Y, ["sorgenfrei.e"], variant="gatto2021")
```

`Y` may be a numpy array, a pandas DataFrame (the column names become the label names) or a
scipy sparse matrix. Values outside {0, 1} are rejected.

Without the `measures` argument, all measures of the variant are computed.
`labelsim.list_measures()` lists the names, and `labelsim.describe("ochiai.e.2")` shows what
the catalog records about a name in the two variants.

Divisions by zero and logarithms of zero yield `NaN` or infinity, with no warning and no
replacement by zero. A label that never occurs makes undefined, for example, the phi
correlation and the NMI of every pair it takes part in.

### scikit-learn

```python
from labelsim.sklearn import LabelSimilarity, make_metric

model = LabelSimilarity(measure="phi").fit(Y)
model.similarity_matrix_

from sklearn.metrics import pairwise_distances
pairwise_distances(Y.T, metric=make_metric("mean_manhattan"))
```

`LabelSimilarity` follows the scikit-learn estimator convention and works with `clone`,
`get_params` and `set_params`. `make_metric` returns the value of the measure as it is
defined; for `pairwise_distances`, use a distance-type measure.

## Table convention

For the pair (i, j), the library follows Table 1 of Choi, Cha and Tappert (2010).

| | j present | j absent |
| --- | --- | --- |
| **i present** | a | c |
| **i absent** | b | d |

Thus a + c counts the presences of i and a + b those of j, and each formula holds exactly as
printed in the source. The matrix returned by `similarity` uses, at position [i, j], the
table of the pair (i, j). Only three of the 65 formulas change when i and j swap places
(AMPLE, Tarantula and Peirce); for them, the opposite convention amounts to transposing the
matrix.

The Similarity-Measures repository and the text of the thesis use the opposite orientation,
with b for i present and j absent. This changes none of the measures used in the thesis,
which are symmetric in b and c.

## Accepted names

Each measure can be requested by its identifier (`ochiai_1`), by an alias (`ochiai`, used in
the Similarity-Measures repository), by the original name of Gatto (`ochiai.e.1`) or by the
form with underscores (`ochiai_1`). In the `literature` variant, names with the same formula
point to the same function. For example, `canberra.e`, `cityblock.e`, `hamming.e`,
`manhattan.e`, `minowski.e` and `square.euclidean.e` all yield b + c.

The full list, with the formula, reference and status of each name, is in
[docs/medidas.md](docs/medidas.md), generated from `src/labelsim/catalog/`.

## How the 107 measures were checked

Each name of Gatto (2021) was compared with the formula of Choi, Cha and Tappert (2010),
which gathers 76 measures, and with Table 4 of Kim, Kato and Zhang (2022). The `situacao`
column of `catalog/gatto2021.csv` records the result.

| Status | Names |
| --- | --- |
| Code equal to the published formula | 59 |
| R operator precedence changes the computation (`a/a+b` equals `1+b`) | 10 |
| One term replaced by another | 9 |
| Other divergence (missing root, discarded numerator) | 3 |
| Numerator equal to the denominator, always equals 1 | 2 |
| No formula checked against an available source | 24 |

The 24 names with no checked source (for example `cohen.e`, `scott.e`, `loevinger.e` and the
two versions of Sokal and Sneath IV) exist only in the `gatto2021` variant. Requesting them
in the `literature` variant raises `MeasureUnavailableError`. For Sokal and Sneath IV, eq. 49
of Choi, Cha and Tappert (2010) repeats the term d/(b+d), and the original source was not
consulted.

Some formulas of Choi, Cha and Tappert (2010) were kept as printed, even with unusual
consequences, and the catalog note records each case. In the cosine (eq. 31) the root
appears squared. In Cole (eq. 58), the radicand of the denominator is negative in most
tables, which leaves the measure undefined. Fager and McGowan appears in two forms, that of
eq. 47 of Choi and that of Kim, Kato and Zhang (2022).

## Tests

```bash
pytest
```

* The `gatto2021` variant is compared, on the 107 measures, with the original R code
  evaluated on 924 contingency tables, with a relative tolerance of 1e-12.
* The `literature` variant is compared with the 14 measures of `src/measures.R` in the
  Similarity-Measures repository, on the same grid and on the 171 pairs of the birds dataset.
* The tests also check algebraic identities between the measures (for example
  Dice = 2J/(1+J) and Hamann = 2SM - 1), the edge cases of identical, complementary, rare
  and empty labels, and the agreement with `scipy.spatial.distance`.

The reference values in `tests/fixtures/` are generated by
`experiments/08-python-fixtures.R` in the Similarity-Measures repository. The first line of
each file records the source commit. After changing the catalog, run
`python tools/tabela_medidas.py` to update `docs/medidas.md`.

## References

CHOI, S.-S.; CHA, S.-H.; TAPPERT, C. C. A survey of binary similarity and distance measures.
*Journal of Systemics, Cybernetics and Informatics*, v. 8, n. 1, p. 43-48, 2010.

GATTO, E. C. *MultiLabelSimilaritiesMeasures*. GitHub, 2021. Available at
<https://github.com/cissagatto/MultiLabelSimilaritiesMeasures>.

KIM, S.; KATO, I.; ZHANG, X. Comparative analysis of binary similarity measures for compound
identification in mass spectrometry-based metabolomics. *Metabolites*, v. 12, n. 8, 694, 2022.

STREHL, A.; GHOSH, J. Cluster ensembles: a knowledge reuse framework for combining multiple
partitions. *Journal of Machine Learning Research*, v. 3, p. 583-617, 2002.

## License

GPL-3.0, the same as the code of Gatto (2021), of which `gatto2021.py` is a transcription.
