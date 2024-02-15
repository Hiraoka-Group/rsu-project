from math import cos, radians, sin

import numpy as np
import pytest
from scipy.spatial.transform import Rotation as R

from rsuanalyzer.src.calc_rsu._ligand import (_rot_ab1, _rot_ac, _x_ab_coord_a,
                                              _x_ac_coord_a, _x_bc_coord_a)


def cos_deg(deg):
    return cos(radians(deg))

def sin_deg(deg):
    return sin(radians(deg))


@pytest.mark.parametrize(
    "lig_type, theta, expected_rot_ab1",
    [
        ("RR", 30, R.from_euler("x", 30, degrees=True)),
        ("RL", 30, R.from_euler("x", 30, degrees=True)),
        ("LR", 30, R.from_euler("x", -30, degrees=True)),
        ("LL", 30, R.from_euler("x", -30, degrees=True))
    ]
)
def test_rot_ab1(lig_type, theta, expected_rot_ab1: R):
    assert np.allclose(_rot_ab1(lig_type, theta).as_matrix(), expected_rot_ab1.as_matrix())


@pytest.mark.parametrize(
    "lig_type, theta, expected_rot_ac",
    [
        ("RR", 30, R.from_euler("XZX", [30, 60, 30 + 180], degrees=True)),
        ("RL", 30, R.from_euler("XZX", [30, 60, -30], degrees=True)),
        ("LR", 30, R.from_euler("XZX", [-30, -60, 30], degrees=True)),
        ("LL", 30, R.from_euler("XZX", [-30, -60, -30 + 180], degrees=True))
    ]
)
def test_rot_ac(lig_type, theta, expected_rot_ac: R):
    assert np.allclose(_rot_ac(lig_type, theta).as_matrix(), expected_rot_ac.as_matrix())


def test_x_ab_coord_a():
    assert np.allclose(_x_ab_coord_a("RR", 30), np.array([1, 0, 0]))


@pytest.mark.parametrize(
    "lig_type, theta, expected_x_bc_coord_a",
    [
        ("RR", 30, R.from_euler("XZ", [30, 60], degrees=True).apply([1, 0, 0])),
        ("RL", 30, R.from_euler("XZ", [30, 60], degrees=True).apply([1, 0, 0])),
        ("LR", 30, R.from_euler("XZ", [-30, -60], degrees=True).apply([1, 0, 0])),
        ("LL", 30, R.from_euler("XZ", [-30, -60], degrees=True).apply([1, 0, 0]))
    ]
)
def test_x_bc_coord_a(lig_type, theta, expected_x_bc_coord_a):
    assert np.allclose(_x_bc_coord_a(lig_type, theta), expected_x_bc_coord_a)


def test_x_ac_coord_a():
    assert np.allclose(_x_ac_coord_a("RR", 30), _x_ab_coord_a("RR", 30) + _x_bc_coord_a("RR", 30))