from math import cos, radians, sin

import numpy as np

from rsuanalyzer.calc_lig_end import calc_lig_end


def cos_rad(deg):
    return cos(radians(deg))

def sin_rad(deg):    
    return sin(radians(deg))


# lig_conf_id = "RR", "RL", "LR" or "LL"
# angle = 0, 30, 90
# -> The following cases are tested:
# case 1: (lig_conf_id, angle) = ("RR", 0)
# case 2: (lig_conf_id, angle) = ("RR", 30)
# case 3: (lig_conf_id, angle) = ("RR", 90)
# case 4: (lig_conf_id, angle) = ("RL", 30)
# case 5: (lig_conf_id, angle) = ("LR", 30)
# case 6: (lig_conf_id, angle) = ("LL", 30)


def test_calc_lig_end_case1():
    LIG_CONF_ID = "RR"
    THETA = 0

    EXPECTED_P = np.array([1, 0, 0]) + \
        np.array([cos_rad(60), sin_rad(60), 0])
    EXPECTED_ROT = [
        [cos_rad(60), sin_rad(60), 0],
        [sin_rad(60), -cos_rad(60), 0],
        [0, 0, -1]]
    
    p, rot = calc_lig_end(LIG_CONF_ID, THETA)

    assert np.allclose(p, EXPECTED_P)
    assert np.allclose(rot.as_matrix(), EXPECTED_ROT)


def test_calc_lig_end_case2():
    LIG_CONF_ID = "RR"
    THETA = 30

    VEC_AB = np.array([1, 0, 0])
    ROT_AB1 = np.array([
        [1, 0, 0],
        [0, cos_rad(30), -sin_rad(30)],
        [0, sin_rad(30), cos_rad(30)]])
    ROT_B1B2 = np.array([
        [cos_rad(60), -sin_rad(60), 0],
        [sin_rad(60), cos_rad(60), 0],
        [0, 0, 1]])
    VEC_BC = ROT_AB1 @ ROT_B1B2 @ np.array([1, 0, 0])
    ROT_B2C1 = np.array([
        [1, 0, 0],
        [0, cos_rad(30), -sin_rad(30)],
        [0, sin_rad(30), cos_rad(30)]])
    ROT_C1C2 = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]])
    EXPECTED_P = VEC_AB + VEC_BC
    EXPECTED_ROT = ROT_AB1 @ ROT_B1B2 @ ROT_B2C1 @ ROT_C1C2

    p, rot = calc_lig_end(LIG_CONF_ID, THETA)
    
    assert np.allclose(p, EXPECTED_P)
    assert np.allclose(rot.as_matrix(), EXPECTED_ROT)


def test_calc_lig_end_case3():
    LIG_CONF_ID = "RR"
    THETA = 90

    EXPECTED_P = np.array([1, 0, 0]) + \
        np.array([cos_rad(60), 0, sin_rad(60)])
    ROT_AB1 = np.array([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]])
    ROT_B1B2 = np.array([
        [cos_rad(60), -sin_rad(60), 0],
        [sin_rad(60), cos_rad(60), 0],
        [0, 0, 1]])
    ROT_B2C1 = np.array([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]])
    ROT_C1C2 = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]])
    EXPECTED_ROT = ROT_AB1 @ ROT_B1B2 @ ROT_B2C1 @ ROT_C1C2
    
    p, rot = calc_lig_end(LIG_CONF_ID, THETA)

    assert np.allclose(p, EXPECTED_P)
    assert np.allclose(rot.as_matrix(), EXPECTED_ROT)


def test_calc_lig_end_case4():
    LIG_CONF_ID = "RL"
    THETA = 30

    VEC_AB = np.array([1, 0, 0])
    ROT_AB1 = np.array([
        [1, 0, 0],
        [0, cos_rad(30), -sin_rad(30)],
        [0, sin_rad(30), cos_rad(30)]])
    ROT_B1B2 = np.array([
        [cos_rad(60), -sin_rad(60), 0],
        [sin_rad(60), cos_rad(60), 0],
        [0, 0, 1]])
    ROT_B2C1 = np.array([
        [1, 0, 0],
        [0, cos_rad(-30), -sin_rad(-30)],
        [0, sin_rad(-30), cos_rad(-30)]])
    ROT_C1C2 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
    EXPECTED_P = VEC_AB + ROT_AB1 @ ROT_B1B2 @ np.array([1, 0, 0])
    EXPECTED_ROT = ROT_AB1 @ ROT_B1B2 @ ROT_B2C1 @ ROT_C1C2
    
    p, rot = calc_lig_end(LIG_CONF_ID, THETA)

    assert np.allclose(p, EXPECTED_P)
    assert np.allclose(rot.as_matrix(), EXPECTED_ROT)


def test_calc_lig_end_case5():
    LIG_CONF_ID = "LR"
    THETA = 30

    VEC_AB = np.array([1, 0, 0])
    ROT_AB1 = np.array([
        [1, 0, 0],
        [0, cos_rad(-30), -sin_rad(-30)],
        [0, sin_rad(-30), cos_rad(-30)]])
    ROT_B1B2 = np.array([
        [cos_rad(-60), -sin_rad(-60), 0],
        [sin_rad(-60), cos_rad(-60), 0],
        [0, 0, 1]])
    ROT_B2C1 = np.array([
        [1, 0, 0],
        [0, cos_rad(30), -sin_rad(30)],
        [0, sin_rad(30), cos_rad(30)]])
    ROT_C1C2 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
    EXPECTED_P = VEC_AB + ROT_AB1 @ ROT_B1B2 @ np.array([1, 0, 0])
    EXPECTED_ROT = ROT_AB1 @ ROT_B1B2 @ ROT_B2C1 @ ROT_C1C2
    
    p, rot = calc_lig_end(LIG_CONF_ID, THETA)

    assert np.allclose(p, EXPECTED_P)
    assert np.allclose(rot.as_matrix(), EXPECTED_ROT)


def test_calc_lig_end_case6():
    LIG_CONF_ID = "LL"
    THETA = 30

    VEC_AB = np.array([1, 0, 0])
    ROT_AB1 = np.array([
        [1, 0, 0],
        [0, cos_rad(-30), -sin_rad(-30)],
        [0, sin_rad(-30), cos_rad(-30)]])
    ROT_B1B2 = np.array([
        [cos_rad(-60), -sin_rad(-60), 0],
        [sin_rad(-60), cos_rad(-60), 0],
        [0, 0, 1]])
    ROT_B2C1 = np.array([
        [1, 0, 0],
        [0, cos_rad(-30), -sin_rad(-30)],
        [0, sin_rad(-30), cos_rad(-30)]])
    ROT_C1C2 = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]])
    EXPECTED_P = VEC_AB + ROT_AB1 @ ROT_B1B2 @ np.array([1, 0, 0])
    EXPECTED_ROT = ROT_AB1 @ ROT_B1B2 @ ROT_B2C1 @ ROT_C1C2
    
    p, rot = calc_lig_end(LIG_CONF_ID, THETA)

    assert np.allclose(p, EXPECTED_P)
    assert np.allclose(rot.as_matrix(), EXPECTED_ROT)