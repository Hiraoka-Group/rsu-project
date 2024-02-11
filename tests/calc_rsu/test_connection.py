from math import cos, radians, sin

import numpy as np
import pytest

from rsuanalyzer.calc_rsu.connection import rot_ca


def sin_deg(deg):
    return sin(radians(deg))
def cos_deg(deg):
    return cos(radians(deg))


@pytest.mark.parametrize(
    "con_type, delta_, expected",
    [
        ("FF", 120, [
            [-cos_deg(120), 0, -sin_deg(120)],
            [0, 1, 0],
            [sin_deg(120), 0, -cos_deg(120)]
        ]),
        ("FB", 120, [
            [-cos_deg(120), 0, sin_deg(120)],
            [0, -1, 0],
            [sin_deg(120), 0, cos_deg(120)]
        ]),
        ("BF", 120, [
            [-cos_deg(-120), 0, sin_deg(-120)],
            [0, -1, 0],
            [sin_deg(-120), 0, cos_deg(-120)]
        ]),
        ("BB", 120, [
            [-cos_deg(-120), 0, -sin_deg(-120)],
            [0, 1, 0],
            [sin_deg(-120), 0, -cos_deg(-120)]
        ]),
        ("FF", 90, [
            [0, 0, -1],
            [0, 1, 0],
            [1, 0, 0]
        ])
    ]
)
def test_calc_con_rot(con_type, delta_, expected):
    rot = rot_ca(con_type, delta_)
    assert np.allclose(rot.as_matrix(), expected)
