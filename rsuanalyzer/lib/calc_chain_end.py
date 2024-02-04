from collections import deque
from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R

from .calc_lig_end import calc_lig_end


def calc_chain_end(
        conf_id: str, theta: float, delta_: float
        ) -> tuple[np.ndarray, R]:
    conf_id = conf_id.replace("(", "").replace(")", "")
    lig_types = deque([conf_id[i:i+2] for i in range(0, len(conf_id), 4)])
    con_types = deque([conf_id[i:i+2] for i in range(2, len(conf_id), 4)])
    x, rot = calc_lig_end(lig_types.popleft(), theta)

    while lig_types:
        local_dx, local_drot = calc_lig_end(lig_types.popleft(), theta)
        con_rot = calc_con_rot(con_types.popleft(), delta_)
        x = x + (rot * con_rot).apply(local_dx)
        rot = rot * con_rot * local_drot

    return x, rot 


def calc_con_rot(
        con_type: Literal["FF", "FB", "BF", "BB"], delta_: float
        ) -> R:
    """
    Calculate the rotation from the coordinate system of the previous ligand
    to the coordinate system of the next ligand.
    
    Args:
    - con_type (Literal["FF", "FB", "BF", "BB"]): Connection type of the ligand.
    - delta_ (float): Angle in degrees. 0 < delta_ <= 180.
    """
    if con_type not in ("FF", "FB", "BF", "BB"):
        raise ValueError(f"Invalid con_type: {con_type}")
    if not 0 < delta_ <= 180:
        raise ValueError(f"Invalid delta_: {delta_}")
    
    l, m = con_type_to_signs(con_type)
    rot1 = R.from_euler('y', l * delta_, degrees=True)
    if con_type in ("FF", "BB"):
        rot2 = R.from_euler('y', 180, degrees=True)
    else:
        rot2 = R.from_euler('z', 180, degrees=True)
    return rot1 * rot2


def con_type_to_signs(
        con_type: Literal["FF", "FB", "BF", "BB"]) -> tuple[int, int]:
    """
    Convert the connection type to the signs of the rotation directions.

    Args:
    - con_type (Literal["FF", "FB", "BF", "BB"]): Connection type of the ligand.
    """
    if con_type == "FF":
        return 1, 1
    elif con_type == "FB":
        return 1, -1
    elif con_type == "BF":
        return -1, 1
    elif con_type == "BB":
        return -1, -1
    else:
        raise ValueError(f"Invalid con_type: {con_type}")