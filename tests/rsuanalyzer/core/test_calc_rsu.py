import numpy as np
import pytest

from reprod.rsuanalyzer.core._global_vecs_rots import _calc_chain_end
from reprod.rsuanalyzer.core.calc_rsu import (
    _calc_chain_end_dist, _list_chains_derived_from_the_ring, calc_rsu)


def test_calc_chain_end_dist():
    dist = _calc_chain_end_dist("RRFFLL", 30, 120)
    expected_x = _calc_chain_end("RRFFLL", 30, 120)[0]
    expected = np.linalg.norm(expected_x)
    assert dist == expected


@pytest.mark.parametrize(
    "conf_id, theta, delta_, chains",
    [
        ("RRFF", 30, 120, ["RR"]),
        ("RRFFLLBB", 30, 120, ["RRFFLL", "LLBBRR"]),
        ("RRFBRRFB", 0, 87, ["RRFBRRFB", "RRFBRRFB"])
    ]
)
def test_calc_rsu(conf_id, theta, delta_, chains):
    rsu = calc_rsu(conf_id, theta, delta_)

    expected_sum_dist = sum(
            _calc_chain_end_dist(chain, theta, delta_) 
            for chain in chains)
    
    expected = expected_sum_dist / len(chains) ** 2
    
    assert rsu == expected


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFRLFF", ['RRFFRL', 'RLFFRR']),
        ("RRFFLLBBRLFB", ['RRFFLLBBRL', 'RLFBRRFFLL', 'LLBBRLFBRR'])
    ]
)
def test_list_chains_derived_from_the_ring(conf_id, expected):
    assert _list_chains_derived_from_the_ring(conf_id) == expected
