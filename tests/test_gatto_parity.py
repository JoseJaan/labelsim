"""The gatto2021 variant reproduces the original R code on the 924 tables of the grid."""

import pytest

import labelsim
from labelsim.registry import GATTO

from conftest import assert_same, numeric


def test_fixture_covers_all_107_names(gatto_grid):
    names = [column for column in gatto_grid if column not in ("a", "b", "c", "d", "n")]
    assert len(names) == 107
    assert set(names) == set(GATTO)


@pytest.mark.parametrize("name", sorted(GATTO))
def test_same_value_as_r(name, gatto_grid, grid_counts):
    values = labelsim.from_contingency(*grid_counts, [name], variant="gatto2021")[name]
    assert_same(values, numeric(gatto_grid[name]), name)
