from itertools import product

import pytest

from rsuanalyzer.enum_ids.enum_including_dups import \
    enum_conf_ids_including_dups

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
def test_enum_conf_ids_including_dups(num_of_ligs, expected):
    assert enum_conf_ids_including_dups(num_of_ligs) == expected