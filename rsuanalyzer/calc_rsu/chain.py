import numpy as np
from scipy.spatial.transform import Rotation as R

from .conf_id_to_lig_and_con_types import conf_id_to_lig_and_con_types
from .connection import calc_con_rot
from .ligand import rot_ac, x_ac_coord_a


def calc_chain_end_dist(
        conf_id: str, theta: float, delta_: float
        ) -> float:
    x, _ = calc_lig_ends_in_chain(conf_id, theta, delta_)[-1]
    return np.linalg.norm(x)


def calc_lig_ends_in_chain(
        conf_id: str, theta: float, delta_: float
        ) -> list[tuple[np.ndarray, R]]:
    """
    Calculate the positions and rotations of the ends of the ligands 
    in the chain.

    Args:
    - conf_id (str): Conformation ID of the chain, e.g., "RRFFRL".
    - theta (float): Tilting angle of the two C-C bonds in the ligand 
    in degrees. 0 <= theta <= 90.
    - delta_ (float): Angle in degrees. 0 < delta_ <= 180.

    Returns:
    - list[tuple[np.ndarray, R]]: Positions and rotations of the ends 
    of the ligands.
    """
    lig_ends = []
    lig_types, con_types = conf_id_to_lig_and_con_types(conf_id)

    # Position vector of the end of the most recent ligand measured 
    # from the global coordinate system.
    x_of_prev_lig_end: np.ndarray
    # Rotation matrix from the global coordinate system to the local
    # coordinate system of the most recent ligand.
    rot_of_prev_lig_end: R

    # Calculate x and rot for the first ligand.
    local_d_x_of_first_lig = x_ac_coord_a(lig_types[0], theta)
    local_d_rot_of_first_lig = rot_ac(lig_types[0], theta)
    
    lig_ends.append((local_d_x_of_first_lig, local_d_rot_of_first_lig))
    
    # Initialize x and rot with the values for the first ligand.
    # Note that we define the global coordinate system to be the
    # same as the local coordinate system of the first ligand.
    x_of_prev_lig_end = local_d_x_of_first_lig
    rot_of_prev_lig_end = local_d_rot_of_first_lig

    for lig_type, con_type in zip(lig_types[1:], con_types):
        con_rot = calc_con_rot(con_type, delta_)
        local_d_x = x_ac_coord_a(lig_type, theta)
        local_d_rot = rot_ac(lig_type, theta)
        
        # Calculate x and rot for the current ligand.
        x_of_cur_lig_end = x_of_prev_lig_end \
            + (rot_of_prev_lig_end * con_rot).apply(local_d_x)
        rot_of_cur_lig_end = rot_of_prev_lig_end * con_rot * local_d_rot

        lig_ends.append((x_of_cur_lig_end, rot_of_cur_lig_end))

        # Update x and rot for the next iteration.
        x_of_prev_lig_end = x_of_cur_lig_end
        rot_of_prev_lig_end = rot_of_cur_lig_end
    
    return lig_ends
