"""Functions for visualizing the approximate positions of carbon atoms 
in a ligand.
"""

from math import cos, pi, sin
from typing import Literal

import numpy as np

from rsuanalyzer.calc_rsu.ligand import (_rot_ab1, _rot_ac, _x_ab_coord_a,
                                         _x_bc_coord_a)


def calc_c_positions_of_frags_in_lig(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float,
        hex_radius: float = .2, pd_n_dist: float = .16
        ) -> list[list[np.ndarray]]:
    """Calculate approximate positions of carbon atoms in a ligand.

    This function estimates the positions of carbon atoms within 
    a ligand molecule. The positions are represented in the local 
    coordinate system A. For details on the coordinate system A, 
    refer to the associated paper.

    Caution:
        This function is intended to provide an approximate 
        visualization of the ligand structure. It may not accurately 
        represent the precise positions of the atoms.

    Args:
        lig_type (Literal["RR", "RL", "LR", "LL"]): Type of ligand.
        theta (float): Tilt angle of C-C bonds in degrees. 
            Valid range is 0 <= theta <= 90.
        hex_radius (float, optional): Radius of the hexagon
            representing the two pyridine rings and the central
            benzene ring. Default is 0.2.
        pd_n_dist (float, optional): Distance between the
            Pd atom and the N atom in the pyridine ring. Default
            is 0.16.

    Returns:
        list[list[np.ndarray]]: A list of lists of numpy arrays.
        Each list corresponds to a fragment of the ligand molecule.
        The first three lists correspond to the first pyridine ring,
        the central benzene ring, and the second pyridine ring, 
        respectively. The fourth and fifth lists correspond to the 
        edges between the first and second pyridine rings and between 
        the second pyridine ring and the central benzene ring, 
        respectively.

    Example:
        This example demonstrates how to use the function to plot 
        the approximate positions of carbon atoms in a ligand:

        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        >>> frags = calc_c_positions_of_frags_in_lig("RR", 30)
        >>> for frag in frags:
        ...     xs = [vtx[0] for vtx in frag]
        ...     ys = [vtx[1] for vtx in frag]
        ...     zs = [vtx[2] for vtx in frag]
        ...     ax.plot(xs, ys, zs)
        >>> ax.set_xlim(-.2, 1.8)
        >>> ax.set_ylim(-1, 1)
        >>> ax.set_zlim(-1, 1)
        >>> ax.set_box_aspect([1, 1, 1])
        >>> plt.show()
    """
    # Make a prototype hexagon
    hex = []
    for i in range(7):
        phi = i * pi / 3
        hex.append(hex_radius * np.array([cos(phi), sin(phi), 0]))

    # Pyridine ring adjacent to the previous ligand
    first_hex = [
        np.array([(pd_n_dist + hex_radius), 0, 0]) + vtx for vtx in hex]

    # Central benzene ring
    second_hex = [
        _rot_ab1(lig_type, theta).apply(vtx)
        + _x_ab_coord_a(lig_type, theta) for vtx in hex]

    # Pyridine ring adjacent to the next ligand
    third_hex = [
        _rot_ac(lig_type, theta).apply(vtx)
        + _x_ab_coord_a(lig_type, theta)
        + _x_bc_coord_a(lig_type, theta) * (1 - pd_n_dist - hex_radius)
        for vtx in hex
        ]

    # Edge between the first and second hexagons
    edge_ab = [first_hex[0], second_hex[3]]

    # Edge between the second and third hexagons
    edge_bc = [second_hex[1 if lig_type in ("RR", "RL") else 5], third_hex[3]]

    return [first_hex, second_hex, third_hex, edge_ab, edge_bc]