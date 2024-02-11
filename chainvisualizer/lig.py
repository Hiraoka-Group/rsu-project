from math import cos, pi, sin

import numpy as np

from rsuanalyzer.calc_rsu.ligand import (rot_ab1, rot_ac, x_ab_coord_a,
                                         x_bc_coord_a)


def calc_c_positions_of_frags_in_lig(
        lig_type: str, theta: float, hex_radius: float = .2,
        pd_n_dist: float = .16
        ) -> list[list[np.ndarray]]:
    
    hex = []
    for i in range(7):
        phi = i * pi / 3
        hex.append(hex_radius * np.array([cos(phi), sin(phi), 0]))

    first_hex = [
        np.array([(pd_n_dist + hex_radius), 0, 0]) + vtx for vtx in hex]
    
    second_hex = [
        rot_ab1(lig_type, theta).apply(vtx)
        + x_ab_coord_a(lig_type, theta) for vtx in hex]
    
    third_hex = [
        rot_ac(lig_type, theta).apply(vtx) 
        + x_ab_coord_a(lig_type, theta) 
        + x_bc_coord_a(lig_type, theta) * (1 - pd_n_dist - hex_radius)
        for vtx in hex
        ]
    
    edge_ab = [first_hex[0], second_hex[3]]
    edge_bc = [second_hex[1 if lig_type in ("RR", "RL") else 5], third_hex[3]]

    return [first_hex, second_hex, third_hex, edge_ab, edge_bc]