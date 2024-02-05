from math import cos, radians, sin

import numpy as np

from rsuanalyzer.chain import calc_chain_end, calc_con_rot


def sin_deg(deg):
    return sin(radians(deg))
def cos_deg(deg):
    return cos(radians(deg))


# Test the function calc_con_rot.
# case 1: (con_type, delta_) = ("FF", 120)
# case 2: (con_type, delta_) = ("FB", 120)
# case 3: (con_type, delta_) = ("BF", 120)
# case 4: (con_type, delta_) = ("BB", 120)
# case 5: (con_type, delta_) = ("FF", 90)

def test_calc_con_rot_case_1():
    rot = calc_con_rot("FF", 120)
    EXPECTED = [
        [-cos_deg(120), 0, -sin_deg(120)],
        [0, 1, 0],
        [sin_deg(120), 0, -cos_deg(120)]
    ]
    assert np.allclose(rot.as_matrix(), EXPECTED)


def test_calc_con_rot_case_2():
    rot = calc_con_rot("FB", 120)
    EXPECTED = [
        [-cos_deg(120), 0, sin_deg(120)],
        [0, -1, 0],
        [sin_deg(120), 0, cos_deg(120)]
    ]
    assert np.allclose(rot.as_matrix(), EXPECTED)


def test_calc_con_rot_case_3():
    rot = calc_con_rot("BF", 120)
    EXPECTED = [
        [-cos_deg(-120), 0, sin_deg(-120)],
        [0, -1, 0],
        [sin_deg(-120), 0, cos_deg(-120)]
    ]
    assert np.allclose(rot.as_matrix(), EXPECTED)


def test_calc_con_rot_case_4():
    rot = calc_con_rot("BB", 120)
    EXPECTED = [
        [-cos_deg(-120), 0, -sin_deg(-120)],
        [0, 1, 0],
        [sin_deg(-120), 0, -cos_deg(-120)]
    ]
    assert np.allclose(rot.as_matrix(), EXPECTED)


def test_calc_con_rot_case_5():
    rot = calc_con_rot("FF", 90)
    EXPECTED = [
        [0, 0, -1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    assert np.allclose(rot.as_matrix(), EXPECTED)



# Test the function calc_chain_end.
# case 1: (conf_id, theta, delta_) = ("RR(FF)RL", 30, 90)

def test_calc_chain_end_case_1():
    x, rot = calc_chain_end("RRFFRL", 30, 90)
    EXPECTED_X = [1.2, 1.3, -1.2]
    assert np.allclose(x, EXPECTED_X, atol=1e-1)