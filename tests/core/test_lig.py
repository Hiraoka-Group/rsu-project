from math import cos, radians, sin

import numpy as np
import pytest
from scipy.spatial.transform import Rotation as R

from rsuanalyzer.core.lig import (calc_lig_end, calc_vecs_rots_in_lig,
                                  lig_type_to_signs)


def cos_deg(deg):
    return cos(radians(deg))

def sin_deg(deg):
    return sin(radians(deg))


@pytest.mark.parametrize(
    "lig_type, expected_signs", 
    [
        ("RR", (1, 1)),
        ("RL", (1, -1)),
        ("LR", (-1, 1)),
        ("LL", (-1, -1))
    ]
)
def test_lig_type_to_signs(lig_type, expected_signs):
    assert lig_type_to_signs(lig_type) == expected_signs


# =============================================================
# Test calc_vecs_rots_in_lig
# =============================================================
# lig_type = "RR", "RL", "LR" or "LL"
# theta = 0, 30, 90
#
# -> The following cases are tested:
# case 1: (lig_type, theta) = ("RR", 0)
# case 2: (lig_type, theta) = ("RR", 30)
# case 3: (lig_type, theta) = ("RR", 90)
# case 4: (lig_type, theta) = ("RL", 30)
# case 5: (lig_type, theta) = ("LR", 30)
# case 6: (lig_type, theta) = ("LL", 30)


@pytest.mark.calc_vecs_rots_in_lig
def test_calc_vecs_rots_in_lig_RR_theta_0():
    (
        x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2
        ) = calc_vecs_rots_in_lig("RR", 0)

    assert np.allclose(x_ab_in_coord_a, np.array([1, 0, 0]))
    assert np.allclose(
        x_bc_in_coord_a, 
        R.from_euler("z", 60, degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot_ab1.as_matrix(), 
        R.from_euler("x", 0, degrees=True).as_matrix())
    assert np.allclose(
        rot_b1b2.as_matrix(), 
        R.from_euler("z", 60, degrees=True).as_matrix())
    assert np.allclose(
        rot_b2c1.as_matrix(), 
        R.from_euler("x", 0, degrees=True).as_matrix())
    assert np.allclose(
        rot_c1c2.as_matrix(), 
        R.from_euler("x", 180, degrees=True).as_matrix())


@pytest.mark.calc_vecs_rots_in_lig
def test_calc_vecs_rots_in_lig_RR_theta_90():
    (
        x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2
        ) = calc_vecs_rots_in_lig("RR", 90)

    assert np.allclose(x_ab_in_coord_a, np.array([1, 0, 0]))
    assert np.allclose(
        x_bc_in_coord_a, 
        R.from_euler("y", -60, degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot_ab1.as_matrix(), 
        R.from_euler("x", 90, degrees=True).as_matrix())
    assert np.allclose(
        rot_b1b2.as_matrix(), 
        R.from_euler("z", 60, degrees=True).as_matrix())
    assert np.allclose(
        rot_b2c1.as_matrix(), 
        R.from_euler("x", 90, degrees=True).as_matrix())
    assert np.allclose(
        rot_c1c2.as_matrix(), 
        R.from_euler("x", 180, degrees=True).as_matrix())


@pytest.mark.calc_vecs_rots_in_lig
def test_calc_vecs_rots_in_lig_RR_theta_30():
    (
        x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2
        ) = calc_vecs_rots_in_lig("RR", 30)

    assert np.allclose(x_ab_in_coord_a, np.array([1, 0, 0]))
    assert np.allclose(
        x_bc_in_coord_a, 
        R.from_euler("zx", [60, 30], degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot_ab1.as_matrix(), 
        R.from_euler("x", 30, degrees=True).as_matrix())
    assert np.allclose(
        rot_b1b2.as_matrix(), 
        R.from_euler("z", 60, degrees=True).as_matrix())
    assert np.allclose(
        rot_b2c1.as_matrix(), 
        R.from_euler("x", 30, degrees=True).as_matrix())
    assert np.allclose(
        rot_c1c2.as_matrix(), 
        R.from_euler("x", 180, degrees=True).as_matrix())


@pytest.mark.calc_vecs_rots_in_lig
def test_calc_vecs_rots_in_lig_RL_theta_30():
    (
        x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2
        ) = calc_vecs_rots_in_lig("RL", 30)

    assert np.allclose(x_ab_in_coord_a, np.array([1, 0, 0]))
    assert np.allclose(
        x_bc_in_coord_a, 
        R.from_euler("zx", [60, 30], degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot_ab1.as_matrix(), 
        R.from_euler("x", 30, degrees=True).as_matrix())
    assert np.allclose(
        rot_b1b2.as_matrix(), 
        R.from_euler("z", 60, degrees=True).as_matrix())
    assert np.allclose(
        rot_b2c1.as_matrix(), 
        R.from_euler("x", -30, degrees=True).as_matrix())
    assert np.allclose(
        rot_c1c2.as_matrix(), 
        R.from_euler("x", 0, degrees=True).as_matrix())


@pytest.mark.calc_vecs_rots_in_lig
def test_calc_vecs_rots_in_lig_LR_theta_30():
    (
        x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2
        ) = calc_vecs_rots_in_lig("LR", 30)

    assert np.allclose(x_ab_in_coord_a, np.array([1, 0, 0]))
    assert np.allclose(
        x_bc_in_coord_a, 
        R.from_euler("zx", [-60, -30], degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot_ab1.as_matrix(), 
        R.from_euler("x", -30, degrees=True).as_matrix())
    assert np.allclose(
        rot_b1b2.as_matrix(), 
        R.from_euler("z", -60, degrees=True).as_matrix())
    assert np.allclose(
        rot_b2c1.as_matrix(), 
        R.from_euler("x", 30, degrees=True).as_matrix())
    assert np.allclose(
        rot_c1c2.as_matrix(), 
        R.from_euler("x", 0, degrees=True).as_matrix())


@pytest.mark.calc_vecs_rots_in_lig
def test_calc_vecs_rots_in_lig_LL_theta_30():
    (
        x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2
        ) = calc_vecs_rots_in_lig("LL", 30)

    assert np.allclose(x_ab_in_coord_a, np.array([1, 0, 0]))
    assert np.allclose(
        x_bc_in_coord_a, 
        R.from_euler("zx", [-60, -30], degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot_ab1.as_matrix(), 
        R.from_euler("x", -30, degrees=True).as_matrix())
    assert np.allclose(
        rot_b1b2.as_matrix(), 
        R.from_euler("z", -60, degrees=True).as_matrix())
    assert np.allclose(
        rot_b2c1.as_matrix(), 
        R.from_euler("x", -30, degrees=True).as_matrix())
    assert np.allclose(
        rot_c1c2.as_matrix(), 
        R.from_euler("x", 180, degrees=True).as_matrix())


@pytest.mark.calc_lig_end
def test_calc_lig_end_RR_theta_0():
    x, rot = calc_lig_end("RR", 0)

    assert np.allclose(
        x, 
        np.array([1, 0, 0]) \
        + R.from_euler("z", 60, degrees=True).apply([1, 0, 0]))
    assert np.allclose(
        rot.as_matrix(), 
        R.from_euler("ZX", [60, 180], degrees=True).as_matrix())