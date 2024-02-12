import numpy as np
import pytest

from rsuanalyzer.calc_rsu.chain import (calc_chain_end_dist,
                                        calc_global_lig_ends_in_chain)
from rsuanalyzer.calc_rsu.connection import rot_ca
from rsuanalyzer.calc_rsu.ligand import rot_ac, x_ac_coord_a


def test_calc_global_lig_ends_in_chain_of_dimer():
    lig_ends = calc_global_lig_ends_in_chain("RRFFLL", 30, 120)
    assert len(lig_ends) == 2

    assert np.allclose(lig_ends[0][0], x_ac_coord_a("RR", 30))
    assert np.allclose(
        lig_ends[0][1].as_matrix(), rot_ac("RR", 30).as_matrix())
    
    expected_second_x = (
        x_ac_coord_a("RR", 30) 
        + (rot_ac("RR", 30) * rot_ca("FF", 120)).apply(
            x_ac_coord_a("LL", 30)))
    assert np.allclose(lig_ends[1][0], expected_second_x)

    expected_second_rot = (
        rot_ac("RR", 30) * rot_ca("FF", 120) * rot_ac("LL", 30))
    assert np.allclose(
        lig_ends[1][1].as_matrix(), expected_second_rot.as_matrix())


def test_calc_lig_ends_in_chain_of_monomer():
    lig_ends = calc_global_lig_ends_in_chain("RR", 30, 120)
    assert len(lig_ends) == 1

    assert np.allclose(lig_ends[0][0], x_ac_coord_a("RR", 30))
    assert np.allclose(
        lig_ends[0][1].as_matrix(), rot_ac("RR", 30).as_matrix())


@pytest.mark.parametrize(
    "conf_id, theta, delta_", [
        ("RRFFLL", 30, 120),
        ("RR", 30, 120)
    ]
)
def test_calc_chain_end_dist(conf_id, theta, delta_):
    dist = calc_chain_end_dist(conf_id, theta, delta_)
    expected = np.linalg.norm(calc_global_lig_ends_in_chain(conf_id, theta, delta_)[-1][0])
    assert np.isclose(dist, expected)
