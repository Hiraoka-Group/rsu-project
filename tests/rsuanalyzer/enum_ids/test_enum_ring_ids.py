from itertools import product

import pytest

from reprod.rsuanalyzer.enum_ring_ids.enum_ring_ids import (
    _enum_dup_included_ids, _exclude_dups, enum_ring_ids)

LIG_CON_PAIRS = {
    "RRFF", "RRFB", "RRBF", "RRBB",
    "RLFF", "RLFB", "RLBF", "RLBB",
    "LRFF", "LRFB", "LRBF", "LRBB",
    "LLFF", "LLFB", "LLBF", "LLBB",
    }


@pytest.mark.parametrize(
    "num_of_ligs, expected",
    [
        (1, LIG_CON_PAIRS),
        (2, {
            lig_con1 + lig_con2 for lig_con1, lig_con2 
            in product(LIG_CON_PAIRS, repeat=2)}),
        (3, {
            lig_con1 + lig_con2 + lig_con3 for lig_con1, lig_con2, lig_con3
            in product(LIG_CON_PAIRS, repeat=3)}),
    ]
)
def test__enum_dup_included_ids(num_of_ligs, expected):
    assert _enum_dup_included_ids(num_of_ligs) == expected
