"""Literature formulas: catalog consistency, identities, edge cases and scipy."""

import numpy as np
import pytest
from scipy.spatial import distance

import labelsim
from labelsim import gatto2021, literature
from labelsim.registry import GATTO, MEASURES

from conftest import assert_same

STATUSES = {"correta", "erro_precedencia", "termo_trocado", "formula_divergente",
            "constante", "fonte_pendente"}


def values(counts, *names, variant="literature"):
    result = labelsim.from_contingency(*counts, list(names), variant=variant)
    return [result[name] for name in names]


# Catalog


def test_every_literature_function_has_a_catalog_row():
    assert set(literature.FUNCTIONS) == set(MEASURES)
    assert all(measure.function is not None for measure in MEASURES.values())


def test_every_gatto_function_has_a_catalog_row():
    assert len(GATTO) == 107
    assert set(gatto2021.FUNCTIONS) == set(GATTO)


def test_gatto_rows_point_to_existing_measures():
    for entry in GATTO.values():
        assert entry.status in STATUSES, entry.gatto_name
        if entry.status == "fonte_pendente":
            assert entry.canonical == "", entry.gatto_name
        else:
            assert entry.canonical in MEASURES, entry.gatto_name
        assert entry.id == entry.gatto_name.replace(".e.", "_").removesuffix(".e") \
            .replace(".", "_"), entry.gatto_name


def test_every_divergence_is_explained():
    for entry in GATTO.values():
        if entry.status != "correta":
            assert entry.note, entry.gatto_name


def test_every_measure_has_a_reference():
    for measure in MEASURES.values():
        assert measure.reference, measure.id
        assert measure.kind in ("similaridade", "distancia"), measure.id


def test_every_choi_measure_is_covered():
    # The 76 equations of Choi, Cha and Tappert (2010), except 49 (Sokal and Sneath IV),
    # which stays pending because the source repeats the term d/(b+d).
    cited = set()
    for measure in MEASURES.values():
        if "Choi2010" in measure.reference:
            part = measure.reference.split("Choi2010, ")[1].split(";")[0]
            cited |= {int(token.strip(" eq.,")) for token in part.replace(" e ", ",")
                      .split(",") if token.strip(" eq.")}
    assert cited == set(range(1, 77)) - {49}


# The gatto2021 variant matches the literature exactly where the catalog says so.


def comparable(x, y):
    return ~(np.isnan(x) & np.isnan(y))


@pytest.mark.parametrize("name", sorted(n for n, e in GATTO.items() if e.status == "correta"))
def test_correct_gatto_functions_match_the_literature(name, grid_counts):
    (gatto,) = values(grid_counts, name, variant="gatto2021")
    (published,) = values(grid_counts, GATTO[name].canonical)
    assert_same(gatto, published, name)


@pytest.mark.parametrize("name", sorted(n for n, e in GATTO.items()
                                        if e.status not in ("correta", "fonte_pendente")))
def test_divergent_gatto_functions_differ_from_the_literature(name, grid_counts):
    (gatto,) = values(grid_counts, name, variant="gatto2021")
    (published,) = values(grid_counts, GATTO[name].canonical)
    mask = comparable(gatto, published)
    assert not np.allclose(gatto[mask], published[mask], equal_nan=True), name


def test_constant_gatto_functions_are_one_or_undefined(grid_counts):
    for name in ("yule.e.1", "yule.e.3", "dibby.e"):
        (gatto,) = values(grid_counts, name, variant="gatto2021")
        assert set(np.unique(gatto[~np.isnan(gatto)])) == {1.0}, name


# Algebraic identities, the same as Part B of 05-check-measures.R and others that follow
# directly from the formulas.


def test_algebraic_identities(grid_counts):
    a, b, c, d = grid_counts
    n = a + b + c + d
    (j, dice, ss1, sm, rt, rr, hamann, k2, ochiai, phi, ss5, chi2, pearson_2, yq, yqd,
     bc_dist, johnson, cosine, sorgenfrei, chord, hellinger) = values(
        grid_counts, "jaccard", "dice", "sokal_sneath_1", "sokal_michener",
        "rogers_tanimoto", "russell_rao", "hamann", "kulczynski_2", "ochiai_1", "phi",
        "ochiai_2", "pearson_1", "pearson_2", "yule_q", "yule_q_distance", "bray_curtis",
        "johnson", "cosine", "sorgenfrei", "chord", "hellinger")
    with np.errstate(all="ignore"):
        assert_same(dice, 2 * j / (1 + j), "Dice = 2J/(1+J)")
        assert_same(ss1, j / (2 - j), "SS-I = J/(2-J)")
        assert_same(rt, sm / (2 - sm), "RT = SM/(2-SM)")
        assert_same(hamann, 2 * sm - 1, "Hamann = 2SM-1")
        assert_same(sm, rr + d / n, "SM = RR + d/n")
        assert_same(ss5 - phi, b * c / np.sqrt((a + b) * (a + c) * (b + d) * (c + d)),
                    "SS-V - Phi = bc/sqrt(...)")
        assert_same(chi2, n * phi ** 2, "Pearson I = n phi^2")
        assert_same(pearson_2 ** 2, chi2 / (n + chi2), "Pearson II^2")
        assert_same(yqd, 1 - yq, "D Yule Q = 1 - Q")
        assert_same(bc_dist, 1 - dice, "Bray-Curtis = 1 - Dice")
        assert_same(johnson, 2 * k2, "Johnson = 2 Kulczynski II")
        assert_same(sorgenfrei, a * cosine, "Sorgenfrei = a cosseno")
        assert_same(chord ** 2, 2 * (1 - ochiai), "Corda^2 = 2(1 - Ochiai)")
        assert_same(hellinger ** 2, 4 * (1 - ochiai), "Hellinger^2 = 4(1 - Ochiai)")
    mask = comparable(k2, ochiai)
    assert np.all(k2[mask] >= ochiai[mask] - 1e-12), "Kulczynski II >= Ochiai"


# Edge cases from instrucao.txt


def pair(x, y, *names):
    Y = np.column_stack([x, y])
    result = labelsim.similarity(Y, list(names))
    return {name: result[name][0, 1] for name in names}


TCC = ("jaccard", "ochiai", "russell_rao", "sokal_michener", "phi", "yule_q", "nmi")


def test_identical_labels():
    x = [1, 0, 1, 1, 0, 0]
    got = pair(x, x, *TCC, "hamming", "dice")
    assert got == pytest.approx({"jaccard": 1, "ochiai": 1, "russell_rao": 0.5,
                                 "sokal_michener": 1, "phi": 1, "yule_q": 1, "nmi": 1,
                                 "hamming": 0, "dice": 1})


def test_complementary_labels():
    x = np.array([1, 0, 1, 1, 0, 0])
    got = pair(x, 1 - x, *TCC, "hamming")
    assert got == pytest.approx({"jaccard": 0, "ochiai": 0, "russell_rao": 0,
                                 "sokal_michener": 0, "phi": -1, "yule_q": -1, "nmi": 1,
                                 "hamming": 6})


def test_never_together():
    got = pair([1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], *TCC)
    assert got["jaccard"] == got["ochiai"] == got["russell_rao"] == 0
    assert got["yule_q"] == -1
    assert got["phi"] < 0


def test_very_rare_label_and_empty_label():
    rare = pair([0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], *TCC)
    assert all(np.isfinite(value) for value in rare.values())
    empty = pair([0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0], *TCC)
    assert np.isnan(empty["phi"]) and np.isnan(empty["nmi"])
    assert empty["jaccard"] == 0 and empty["sokal_michener"] == 0.5


# scipy.spatial.distance, for boolean vectors


SCIPY = [
    ("jaccard", lambda s: 1 - s),
    ("dice", lambda s: 1 - s),
    ("rogerstanimoto", lambda s: 1 - s),
    ("russellrao", lambda s: 1 - s),
    ("sokalsneath", lambda s: 1 - s),
    ("hamming", lambda s: s),
    ("yule", lambda s: s),
    ("cosine", lambda s: 1 - s),
]
OURS = {"jaccard": "jaccard", "dice": "dice", "rogerstanimoto": "rogers_tanimoto",
        "russellrao": "russell_rao", "sokalsneath": "sokal_sneath_1",
        "hamming": "mean_manhattan", "yule": "yule_q_distance", "cosine": "ochiai_1"}


@pytest.mark.parametrize("scipy_name,to_distance", SCIPY)
def test_matches_scipy(scipy_name, to_distance):
    rng = np.random.default_rng(7)
    for _ in range(50):
        u, v = rng.random((2, 40)) < 0.4
        value = pair(u.astype(int), v.astype(int), OURS[scipy_name])[OURS[scipy_name]]
        # scipy's cosine needs numeric vectors; with booleans, the inner product
        # becomes logical.
        if scipy_name == "cosine":
            u, v = u.astype(float), v.astype(float)
        reference = getattr(distance, scipy_name)(u, v)
        assert to_distance(value) == pytest.approx(reference, rel=1e-12, abs=1e-12)


# Symmetry in b and c


def test_only_known_measures_depend_on_the_order_of_the_pair(grid_counts):
    a, b, c, d = grid_counts
    asymmetric = set()
    for name in MEASURES:
        (forward,) = values((a, b, c, d), name)
        (backward,) = values((a, c, b, d), name)
        mask = comparable(forward, backward)
        if not np.allclose(forward[mask], backward[mask], rtol=1e-12, equal_nan=True):
            asymmetric.add(name)
    assert asymmetric == {"ample", "tarantula", "peirce"}
