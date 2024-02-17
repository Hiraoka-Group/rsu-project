import numpy as np

from reprod.rsuanalyzer.core._global_vecs_rots import (
    _calc_chain_end, _calc_global_lig_ends_in_chain)
from reprod.rsuanalyzer.core._local_vecs_rots import (_rot_ac, _rot_ca,
                                                      _x_ac_coord_a)


def test_calc_lig_ends_in_chain_of_monomer():
    lig_ends = _calc_global_lig_ends_in_chain("RR", 30, 120)
    assert len(lig_ends) == 1

    assert np.allclose(lig_ends[0][0], _x_ac_coord_a("RR", 30))
    assert np.allclose(
        lig_ends[0][1].as_matrix(), _rot_ac("RR", 30).as_matrix())


def test_calc_global_lig_ends_in_chain_of_dimer():
    lig_ends = _calc_global_lig_ends_in_chain("RRFFLL", 30, 120)
    assert len(lig_ends) == 2

    assert np.allclose(lig_ends[0][0], _x_ac_coord_a("RR", 30))
    assert np.allclose(
        lig_ends[0][1].as_matrix(), _rot_ac("RR", 30).as_matrix())
    
    expected_second_x = (
        _x_ac_coord_a("RR", 30) 
        + (_rot_ac("RR", 30) * _rot_ca("FF", 120)).apply(
            _x_ac_coord_a("LL", 30)))
    assert np.allclose(lig_ends[1][0], expected_second_x)

    expected_second_rot = (
        _rot_ac("RR", 30) * _rot_ca("FF", 120) * _rot_ac("LL", 30))
    assert np.allclose(
        lig_ends[1][1].as_matrix(), expected_second_rot.as_matrix())


def test__calc_chain_end_of_monmer():
    x, rot = _calc_chain_end("RR", 30, 120)
    expected_x = _x_ac_coord_a("RR", 30)
    expected_rot = _rot_ac("RR", 30)
    assert np.allclose(x, expected_x)
    assert np.allclose(rot.as_matrix(), expected_rot.as_matrix())


def test__calc_chain_end_of_dimer():
    expected = _calc_global_lig_ends_in_chain("RRFFLL", 30, 120)[-1]
    x, rot = _calc_chain_end("RRFFLL", 30, 120)
    assert np.allclose(x, expected[0])
    assert np.allclose(rot.as_matrix(), expected[1].as_matrix())
