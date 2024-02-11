import pytest

from rsuanalyzer.calc_rsu.chain import calc_chain_end_dist
from rsuanalyzer.calc_rsu.rsu import calc_rsu


@pytest.mark.parametrize(
    "conf_id, theta, delta_, chains",
    [
        ("RRFF", 30, 120, ["RR"]),
        ("RRFFLLBB", 30, 120, ["RRFFLL", "LLBBRR"]),
    ]
)
def test_calc_rsu(conf_id, theta, delta_, chains):
    rsu = calc_rsu(conf_id, theta, delta_)

    expected_sum_dist = sum(
            calc_chain_end_dist(chain, theta, delta_) 
            for chain in chains)
    
    expected = expected_sum_dist / len(chains) ** 2
    
    assert rsu == expected