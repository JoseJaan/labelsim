"""The literature variant reproduces the 14 measures of src/measures.R in the TCC repository.

All 14 are symmetric in b and c, so the difference in orientation between the convention
here (Choi, Cha and Tappert, 2010) and that of src/contingency.R changes no value.
"""

import pytest

import labelsim

from conftest import assert_same, numeric

R_REGISTRY = ["jaccard", "dice", "sokal_sneath_1", "ochiai", "simpson", "kulczynski2",
              "russel_rao", "sokal_michener", "rogers_tanimoto", "sokal_sneath_v", "hamann",
              "yule_q", "phi", "nmi"]

TCC_MEASURES = ["jaccard", "ochiai", "russel_rao", "sokal_michener", "phi", "yule_q", "nmi"]


def test_tcc_measures_are_in_the_r_registry():
    assert set(TCC_MEASURES) <= set(R_REGISTRY)


@pytest.mark.parametrize("fixture_name", ["registry_grid", "registry_birds"])
@pytest.mark.parametrize("measure", R_REGISTRY)
def test_same_value_as_r(measure, fixture_name, request):
    table = request.getfixturevalue(fixture_name)
    counts = [numeric(table[column]) for column in "abcd"]
    values = labelsim.from_contingency(*counts, [measure])[measure]
    assert_same(values, numeric(table[measure]), f"{measure} em {fixture_name}")


def test_birds_has_every_pair_once(registry_birds):
    pairs = list(zip(registry_birds["i"], registry_birds["j"]))
    assert len(pairs) == len(set(pairs)) == 19 * 18 // 2
