import numpy as np
import pytest

import labelsim

Y = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 0], [0, 0, 1]])


def test_documented_example():
    Y = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 0]])
    assert float(labelsim.similarity(Y, ["jaccard"])["jaccard"][0, 1]) == 0.25


def test_matrix_and_long_outputs_agree():
    pytest.importorskip("pandas")
    matrices = labelsim.similarity(Y, ["jaccard", "phi"])
    long = labelsim.similarity(Y, ["jaccard", "phi"], output="long", labels=list("xyz"))
    for _, row in long.iterrows():
        assert row["jaccard"] == matrices["jaccard"][row["i"], row["j"]]
        assert row["phi"] == matrices["phi"][row["i"], row["j"]]
    assert list(long["label_i"]) == ["x", "x", "y"]


def test_matrix_of_an_asymmetric_measure_is_the_transpose_under_swap():
    m = labelsim.similarity(Y, ["peirce"])["peirce"]
    table = labelsim.contingency(Y)
    swapped = labelsim.from_contingency(table.a, table.c, table.b, table.d, ["peirce"])
    np.testing.assert_allclose(swapped["peirce"], m.T, equal_nan=True)


def test_default_runs_every_measure_of_the_variant():
    assert len(labelsim.similarity(Y)) == len(labelsim.list_measures())
    assert len(labelsim.similarity(Y, variant="gatto2021")) == 107


def test_measure_specifications():
    single = labelsim.similarity(Y, "jaccard")
    custom = labelsim.similarity(Y, {"j": "jaccard", "so_d": lambda a, b, c, d, n: d / n})
    np.testing.assert_array_equal(custom["j"], single["jaccard"])
    np.testing.assert_allclose(custom["so_d"], labelsim.contingency(Y).d / 5)


def test_aliases_give_the_same_values():
    names = ["jaccard", "tanimoto", "tanimoto.e", "jaccard.e"]
    result = labelsim.similarity(Y, names)
    for name in names[1:]:
        np.testing.assert_array_equal(result[name], result["jaccard"])


def test_variants_differ_where_gatto_has_an_error():
    literature = labelsim.similarity(Y, ["sorgenfrei.e"])["sorgenfrei.e"]
    original = labelsim.similarity(Y, ["sorgenfrei.e"], variant="gatto2021")["sorgenfrei.e"]
    assert not np.allclose(literature, original, equal_nan=True)


def test_errors():
    with pytest.raises(ValueError, match="repetida"):
        labelsim.similarity(Y, ["jaccard", "jaccard"])
    with pytest.raises(KeyError, match="desconhecida"):
        labelsim.similarity(Y, ["nao_existe"])
    with pytest.raises(labelsim.MeasureUnavailableError, match="gatto2021"):
        labelsim.similarity(Y, ["cohen"])
    with pytest.raises(labelsim.MeasureUnavailableError, match="hamming.e"):
        labelsim.similarity(Y, ["minkowski"], variant="gatto2021")
    with pytest.raises(ValueError, match="variante"):
        labelsim.similarity(Y, ["jaccard"], variant="outra")
    with pytest.raises(ValueError, match="saída"):
        labelsim.similarity(Y, ["jaccard"], output="tabela")
    with pytest.raises(TypeError, match="nome"):
        labelsim.similarity(Y, [lambda a, b, c, d, n: a])


def test_pending_measures_still_run_in_gatto_variant():
    result = labelsim.similarity(Y, ["cohen"], variant="gatto2021")
    assert result["cohen"].shape == (3, 3)


def test_from_contingency_broadcasts_and_keeps_undefined_values():
    result = labelsim.from_contingency(0, [0, 1], [0, 1], 5, ["jaccard", "gilbert_wells"])
    assert result["jaccard"].shape == (2,)
    assert np.isnan(result["jaccard"][0])
    assert result["jaccard"][1] == 0
    assert np.isneginf(result["gilbert_wells"][1])


def test_list_measures():
    assert len(labelsim.list_measures()) == 65
    assert len(labelsim.list_measures("gatto2021")) == 107
    with_aliases = labelsim.list_measures(include_aliases=True)
    assert "tanimoto.e" in with_aliases and "russel_rao" in with_aliases
    assert "cohen" not in with_aliases


def test_describe():
    info = labelsim.describe("ochiai.e.2")
    assert info["literature"]["id"] == "ochiai_2"
    assert info["gatto2021"]["status"] == "termo_trocado"
    assert "sokal.sneath.e.5b" in info["literature"]["gatto_names"]
    assert labelsim.describe("cohen")["literature"] is None
    assert labelsim.describe("phi")["gatto2021"] is None


def test_sklearn_estimator():
    pytest.importorskip("sklearn")
    from sklearn.base import clone

    from labelsim.sklearn import LabelSimilarity

    model = LabelSimilarity(measure="phi").fit(Y)
    np.testing.assert_array_equal(model.similarity_matrix_,
                                  labelsim.similarity(Y, ["phi"])["phi"])
    assert model.labels_ == (0, 1, 2)
    copy = clone(model)
    assert copy.get_params() == {"measure": "phi", "variant": "literature"}
    assert not hasattr(copy, "similarity_matrix_")


def test_sklearn_metric():
    pytest.importorskip("sklearn")
    from sklearn.metrics import pairwise_distances

    from labelsim.sklearn import make_metric

    distances = pairwise_distances(Y.T, metric=make_metric("mean_manhattan"))
    np.testing.assert_allclose(distances,
                               labelsim.similarity(Y, ["mean_manhattan"])["mean_manhattan"])
