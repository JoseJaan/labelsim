import numpy as np
import pytest
from scipy import sparse

import labelsim


def brute_force(Y):
    q = Y.shape[1]
    out = {key: np.zeros((q, q)) for key in "abcd"}
    for i in range(q):
        for j in range(q):
            x, y = Y[:, i], Y[:, j]
            out["a"][i, j] = np.sum((x == 1) & (y == 1))
            out["b"][i, j] = np.sum((x == 0) & (y == 1))
            out["c"][i, j] = np.sum((x == 1) & (y == 0))
            out["d"][i, j] = np.sum((x == 0) & (y == 0))
    return out


@pytest.fixture
def random_labels():
    rng = np.random.default_rng(1)
    return (rng.random((60, 7)) < 0.3).astype(int)


def test_orientation_follows_choi_table_1():
    # b counts i absent and j present; c counts i present and j absent.
    Y = np.array([[1, 0], [1, 1], [0, 1], [1, 0], [0, 0]])
    table = labelsim.contingency(Y)
    assert (table.a[0, 1], table.b[0, 1], table.c[0, 1], table.d[0, 1]) == (1, 1, 2, 1)


def test_matches_brute_force(random_labels):
    table = labelsim.contingency(random_labels)
    expected = brute_force(random_labels)
    for key in "abcd":
        np.testing.assert_array_equal(getattr(table, key), expected[key])
    np.testing.assert_array_equal(table.n, np.full((7, 7), 60.0))


def test_sparse_input_gives_the_same_table(random_labels):
    dense = labelsim.contingency(random_labels)
    for matrix in (sparse.csr_matrix(random_labels), sparse.csc_array(random_labels)):
        table = labelsim.contingency(matrix)
        for key in "abcd":
            np.testing.assert_array_equal(getattr(table, key), getattr(dense, key))


def test_invariants_hold(random_labels):
    table = labelsim.contingency(random_labels)
    assert labelsim.check_contingency(table, 60, positives=random_labels.sum(axis=0)) == []


def test_invariant_violations_are_reported(random_labels):
    table = labelsim.contingency(random_labels)
    broken = labelsim.Contingency(a=table.a, b=table.b + 1, c=table.c, d=table.d,
                                  labels=table.labels)
    problems = labelsim.check_contingency(broken, 60)
    assert "a + b + c + d difere do número de instâncias" in problems
    assert "b não é a transposta de c" in problems


def test_counts_are_float64_and_exact_beyond_32_bits():
    # With 20000 instances, the product of the four marginals exceeds 2^31.
    Y = np.zeros((20000, 2), dtype=np.int8)
    Y[:10000, 0] = 1
    Y[5000:15000, 1] = 1
    table = labelsim.contingency(Y)
    assert table.a.dtype == np.float64
    a, b, c, d = (getattr(table, key)[0, 1] for key in "abcd")
    assert (a + b) * (a + c) * (b + d) * (c + d) == 10000.0 ** 4


def test_labels_from_dataframe_and_argument(random_labels):
    pd = pytest.importorskip("pandas")
    names = [f"r{k}" for k in range(7)]
    assert labelsim.contingency(pd.DataFrame(random_labels, columns=names)).labels == tuple(names)
    assert labelsim.contingency(random_labels, labels=names).labels == tuple(names)
    assert labelsim.contingency(random_labels).labels == tuple(range(7))
    with pytest.raises(ValueError, match="nomes de rótulo"):
        labelsim.contingency(random_labels, labels=names[:3])


@pytest.mark.parametrize("bad", [np.array([[0, 2], [1, 0]]), np.array([[0.5, 1]]),
                                 np.array([[np.nan, 1]]), np.array([1, 0, 1])])
def test_rejects_non_binary_or_non_matrix(bad):
    with pytest.raises(ValueError):
        labelsim.contingency(bad)


def test_pairs_lists_upper_triangle(random_labels):
    pytest.importorskip("pandas")
    table = labelsim.contingency(random_labels, labels=list("ABCDEFG"))
    long = labelsim.pairs(table)
    assert len(long) == 21
    assert (long["i"] < long["j"]).all()
    row = long.iloc[0]
    assert (row["label_i"], row["label_j"]) == ("A", "B")
    assert row["b"] == table.b[0, 1]
