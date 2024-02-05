from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R

from .calc_lig_end import calc_lig_end


def calc_chain_end(
        conf_id: str, theta: float, delta_: float
        ) -> tuple[np.ndarray, R]:
    conf_id = conf_id.replace("(", "").replace(")", "")

    lig_types, con_types = conf_id_to_lig_types_and_con_types(conf_id)
    x, rot = calc_lig_end(lig_types.popleft(), theta)

    while lig_types:
        x, rot = calc_next_lig_end(
            lig_types.popleft(), theta, delta_, con_types.popleft(), x, rot)
    return x, rot


def calc_next_lig_end(
        lig_type: Literal["RR", "RL", "LR", "LL"],
        theta: float, delta_: float, 
        con_type: Literal["FF", "FB", "BF", "BB"] | None = None,
        prev_x: np.ndarray | None = None, 
        prev_rot: R | None = None,
        ) -> tuple[np.ndarray, R]:
    """
    Calculate the position and rotation of the next ligand in the chain.
    
    Args:
    - lig_type (Literal["RR", "RL", "LR", "LL"]): Type of the ligand.
    - theta (float): Tilting angle of the two C-C bonds in the ligand in
        degrees. 0 <= theta <= 90.
    - delta_ (float): Angle in degrees. 0 < delta_ <= 180.
    - con_type (Literal["FF", "FB", "BF", "BB"] | None): Connection type of 
      the ligand. If the ligand is the first one in the chain, con_type must
      be None.
    - prev_x (np.ndarray | None): Position of the previous ligand. If con_type
      is provided, prev_x must be provided.
    - prev_rot (R | None): Rotation of the previous ligand. If con_type is
      provided, prev_rot must be provided.

    Returns:
    - tuple[np.ndarray, R]: Position and rotation of the next ligand.
    """
    # Validate the input.
    if lig_type not in ("RR", "RL", "LR", "LL"):
        raise ValueError(f"Invalid lig_type: {lig_type}")
    if not 0 <= theta <= 90:
        raise ValueError(f"Invalid theta: {theta}")
    if not 0 < delta_ <= 180:
        raise ValueError(f"Invalid delta_: {delta_}")
    if con_type is not None and (prev_x is None or prev_rot is None):
        raise ValueError("x and rot must be provided if con_type is provided.")

    local_dx, local_drot = calc_lig_end(lig_type, theta)

    # If the ligand is the first one in the chain:
    if con_type is None:
        return local_dx, local_drot
    
    # If the ligand is not the first one in the chain:
    con_rot = calc_con_rot(con_type, delta_)
    x = prev_x + (prev_rot * con_rot).apply(local_dx)
    rot = prev_rot * con_rot * local_drot
    return x, rot


def conf_id_to_lig_types_and_con_types(
        conf_id: str) -> tuple[list[str], list[str]]:
    """
    Convert the conformation ID to the ligand types and connection types.

    Args:
    - conf_id (str): Conformation ID of the chain.
    
    Returns:
    - tuple[list[str], list[str]]: Ligand types and connection types.
    """
    conf_id = conf_id.replace("(", "").replace(")", "")
    lig_types = [conf_id[i:i+2] for i in range(0, len(conf_id), 4)]
    con_types = [conf_id[i:i+2] for i in range(2, len(conf_id), 4)]
    return lig_types, con_types


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