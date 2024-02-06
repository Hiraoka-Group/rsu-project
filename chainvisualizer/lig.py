from math import cos, pi, sin

import numpy as np

from rsuanalyzer.core.lig import calc_inner_vecs_and_rots


def calc_carbon_positions_of_fragments_of_lig(
        lig_type: str, theta: float) -> list[list[np.ndarray]]:
    (x_ab_in_coord_a, x_bc_in_coord_a, rot_ab1, rot_b1b2, rot_b2c1, 
        rot_c1c2) = calc_inner_vecs_and_rots(lig_type, theta)
    
    PD_N_DIST = .16
    RADIUS = .2
    HEXAGON = [
        RADIUS * np.array([cos(2 * pi * i / 6), sin(2 * pi * i / 6), 0])
        for i in range(7)
        ]

    vec_of_pd_to_cent_of_first_hex = (PD_N_DIST + RADIUS) * np.array([1, 0, 0])
    first_hex = [
        vec_of_pd_to_cent_of_first_hex + vtx for vtx in HEXAGON]
    
    second_hex = []
    for vtx in HEXAGON:
        vtx_in_coord_b1 = vtx
        vtx_in_coord_a = x_ab_in_coord_a + rot_ab1.apply(vtx_in_coord_b1)
        second_hex.append(vtx_in_coord_a)

    pd_to_third_hex_in_coord_c1 = (PD_N_DIST + RADIUS) * np.array([-1, 0, 0])
    third_hex = []
    rot_ac1 = rot_ab1 * rot_b1b2 * rot_b2c1
    for vtx in HEXAGON:
        vtx_in_coord_c1 = vtx + pd_to_third_hex_in_coord_c1
        vtx_in_coord_a = x_ab_in_coord_a + x_bc_in_coord_a + rot_ac1.apply(vtx_in_coord_c1)
        third_hex.append(vtx_in_coord_a)
    
    edge_ab = [np.array([PD_N_DIST + 2 * RADIUS, 0, 0]), x_ab_in_coord_a - np.array([RADIUS, 0, 0])]
    edge_bc = [second_hex[1 if lig_type in ("RR", "RL") else 5], third_hex[3]]

    return [first_hex, second_hex, third_hex, edge_ab, edge_bc]