"""Functions for calculating the distance between the ends of chains."""

import numpy as np
from scipy.spatial.transform import Rotation as R

from .conf_id_to_lig_con_types import (_conf_id_to_con_types,
                                       _conf_id_to_lig_types)
from .connection import _rot_ca
from .ligand import _rot_ac, _x_ac_coord_a


def calc_chain_end_dist(
        conf_id: str, theta: float, delta_: float
        ) -> float:
    """Calculate the distance between the two ends of the chain.

    Args:
        conf_id (str): Conformation ID of the chain, e.g., "RRFFRL".
        theta (float): Tilting angle of the two C-C bonds in the ligand
            in degrees. 0 <= theta <= 90.
        delta_ (float): Angle in degrees. 0 < delta\_ <= 180.

    Returns:
        float: The distance between the two ends of the chain.
    """
    # x is the position vector of the end of the last ligand measured
    # from the global coordinate system.
    x, _ = calc_global_lig_ends_in_chain(conf_id, theta, delta_)[-1]

    # Since the position of the other end is (0, 0, 0) in the global
    # coordinate system, the distance between the two ends is the
    # norm of x.
    return np.linalg.norm(x)


def calc_global_lig_ends_in_chain(
        conf_id: str, theta: float, delta_: float
        ) -> list[tuple[np.ndarray, R]]:
    """Calculate the positions and rotations of the ends of the ligands
    in the chain measured from the global coordinate system.

    Args:
        conf_id (str): Conformation ID of the chain, e.g., "RRFFRL".
        theta (float): Tilting angle of the two C-C bonds in the ligand
            in degrees. 0 <= theta <= 90.
        delta_ (float): Angle in degrees. 0 < delta\_ <= 180.

    Returns:
        list[tuple[np.ndarray, R]]: 
            The list of tuples, each of which contains the position
            and the rotation of the end of a ligand measured from the
            global coordinate system.
    """
    lig_ends = []
    lig_types = _conf_id_to_lig_types(conf_id)
    con_types = _conf_id_to_con_types(conf_id)

    # Position vector of the end of the most recent ligand measured 
    # from the global coordinate system.
    x_of_prev_lig_end: np.ndarray
    # Rotation matrix from the global coordinate system to the local
    # coordinate system of the most recent ligand.
    rot_of_prev_lig_end: R

    # Calculate x and rot for the first ligand.
    local_d_x_of_first_lig = _x_ac_coord_a(lig_types[0], theta)
    local_d_rot_of_first_lig = _rot_ac(lig_types[0], theta)
    
    lig_ends.append((local_d_x_of_first_lig, local_d_rot_of_first_lig))
    
    # Initialize x and rot with the values for the first ligand.
    # Note that we define the global coordinate system to be the
    # same as the local coordinate system of the first ligand.
    x_of_prev_lig_end = local_d_x_of_first_lig
    rot_of_prev_lig_end = local_d_rot_of_first_lig

    for lig_type, con_type in zip(lig_types[1:], con_types):
        con_rot = _rot_ca(con_type, delta_)
        local_d_x = _x_ac_coord_a(lig_type, theta)
        local_d_rot = _rot_ac(lig_type, theta)
        
        # Calculate x and rot for the current ligand.
        x_of_cur_lig_end = x_of_prev_lig_end \
            + (rot_of_prev_lig_end * con_rot).apply(local_d_x)
        rot_of_cur_lig_end = rot_of_prev_lig_end * con_rot * local_d_rot

        lig_ends.append((x_of_cur_lig_end, rot_of_cur_lig_end))

        # Update x and rot for the next iteration.
        x_of_prev_lig_end = x_of_cur_lig_end
        rot_of_prev_lig_end = rot_of_cur_lig_end
    
    return lig_ends
