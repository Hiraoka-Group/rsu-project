from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R


def calc_lig_end(
        conf_id: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> tuple[np.ndarray, R]:
    """
    Calculate x_ac and rot_ac2 of the ligand.
    x_ac is the position vector of point C2 measured from coordinate 
    system A.
    rot_ac2 is the rotation from coordinate system A to C2.

    Args:
    - conf_id (Literal["RR", "RL", "LR", "LL"]): Conformation ID of 
    the ligand.
    - theta (float): Angle in degrees.

    Returns:
    - x_ac (np.ndarray): Position vector of point C2 measured from 
    coordinate system A.
    - rot_ac2 (R): Rotation from coordinate system A to C2.
    """
    # Validate the input.
    if conf_id not in ("RR", "RL", "LR", "LL"):
        raise ValueError(f"Invalid conf_id: {conf_id}")
    if not 0 <= theta <= 90:
        raise ValueError(f"Invalid theta: {theta}")

    # j and k represent the rotation directions.
    j, k = conf_id_to_signs(conf_id)
    
    x_ab = np.array([1, 0, 0])
    rot_ab1 = R.from_euler('x', j * theta, degrees=True)
    rot_b1b2 = R.from_euler('z', j * 60, degrees=True)
    rot_b2c1 = R.from_euler('x', k * theta, degrees=True)

    if conf_id in ("RR", "LL"):
        # If conf_id is RR or LL, rotate 180 degrees around x-axis
        # in order that the z-axis of coordinates C2 protrudes towards 
        # the "Front" face.
        rot_c1c2 = R.from_euler('x', 180, degrees=True)
    else:
        rot_c1c2 = R.from_euler('x', 0, degrees=True)
    
    x_ac = x_ab + (rot_ab1 * rot_b1b2).apply([1, 0, 0])
    rot_ac = rot_ab1 * rot_b1b2 * rot_b2c1 * rot_c1c2

    return x_ac, rot_ac


def conf_id_to_signs(
        conf_id: Literal["RR", "RL", "LR", "LL"]) -> tuple[int, int]:
    """
    Convert the conformation ID to the signs of the rotation directions.

    Args:
    - conf_id (Literal["RR", "RL", "LR", "LL"]): Conformation ID of the ligand.

    Returns:
    - tuple[int, int]: Signs of the rotation directions.
    """
    if conf_id == "RR":
        return 1, 1
    elif conf_id == "RL":
        return 1, -1
    elif conf_id == "LR":
        return -1, 1
    elif conf_id == "LL":
        return -1, -1
    else:
        raise ValueError(f"Invalid conf_id: {conf_id}")