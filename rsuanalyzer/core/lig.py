from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R


def calc_lig_end(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> tuple[np.ndarray, R]:
    """
    Calculate x_ac and rot_ac2 of the ligand.

    x_ac is the vector from point A to point C measured from
    coordinate system A. rot_ac2 is the rotation from coordinate 
    system A to C2. 

    For the definitions of the coordinate systems and the points,
    together with the lig_type and theta, please refer to the paper.
    
    Args:
    - lig_type (Literal["RR", "RL", "LR", "LL"]): Combination of two 
    letters, which represent the rotation directions of the two C-C
    bonds between the pyridine rings and the central benzene ring.
    - theta (float): Dihedral angle between the two pyridine rings 
    and the central benzene ring in degrees. Same value is used for
    both rotations. 0 <= theta <= 90.

    Returns:
    - x_ac (np.ndarray): Vector from point A to point C measured from
    coordinate system A
    - rot_ac2 (R): Rotation from coordinate system A to C2.
    """
    # Validate the input.
    if lig_type not in ("RR", "RL", "LR", "LL"):
        raise ValueError(f"Invalid lig_type: {lig_type}")
    if not 0 <= theta <= 90:
        raise ValueError(f"Invalid theta: {theta}")

    (x_ab_in_coord_a, x_bc_in_coord_a, 
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2) = calc_vecs_rots_in_lig(
        lig_type, theta)
    
    x_ac_in_coord_a = x_ab_in_coord_a + x_bc_in_coord_a
    rot_ac = rot_ab1 * rot_b1b2 * rot_b2c1 * rot_c1c2

    return x_ac_in_coord_a, rot_ac


def calc_vecs_rots_in_lig(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> tuple[np.ndarray, np.ndarray, R, R, R, R]:
    """
    Calculate the vectors and rotations in the ligand.

    For the definitions of the coordinate systems and the points,
    together with the lig_type and theta, please refer to the paper.

    Args:
    - lig_type (Literal["RR", "RL", "LR", "LL"]): Combination of two
    letters, which represent the rotation directions of the two C-C
    bonds between the pyridine rings and the central benzene ring.
    - theta (float): Dihedral angle between the two pyridine rings
    and the central benzene ring in degrees. Same value is used for
    both rotations. 0 <= theta <= 90.
    
    Returns:
    - tuple[np.ndarray, np.ndarray, R, R, R, R]: Vectors and
    rotations in the ligand.

    The returned values are as follows:
    - x_ab_in_coord_a (np.ndarray): Vector from point A to point B
    measured from coordinate system A.
    - x_bc_in_coord_a (np.ndarray): Vector from point B to point C
    measured from coordinate system A.
    - rot_ab1 (R): Rotation from coordinate system A to B1.
    - rot_b1b2 (R): Rotation from B1 to B2.
    - rot_b2c1 (R): Rotation from B2 to C1.
    - rot_c1c2 (R): Rotation from C1 to C2.
    """
    # j and k represent the rotation directions.
    # Each of them is either 1 or -1.
    # e.g. RR -> j = 1, k = 1, RL -> j = 1, k = -1, etc.
    j, k = lig_type_to_signs(lig_type)
    
    x_ab_in_coord_a = np.array([1, 0, 0])
    rot_ab1 = R.from_euler('x', j * theta, degrees=True)
    rot_b1b2 = R.from_euler('z', j * 60, degrees=True)
    rot_b2c1 = R.from_euler('x', k * theta, degrees=True)
    x_bc_in_coord_a = (rot_ab1 * rot_b1b2).apply([1, 0, 0])

    if lig_type in ("RR", "LL"):
        # By definition, the z-axis of coordinates C2 protrudes towards
        # the "Front" face of the pyridine ring.
        # Therefore, the rotation from C1 to C2 should be 180 degrees
        # around the x-axis, if the lig_type is "RR" or "LL".
        rot_c1c2 = R.from_euler('x', 180, degrees=True)
    else:
        rot_c1c2 = R.from_euler('x', 0, degrees=True)
    
    return (x_ab_in_coord_a, x_bc_in_coord_a,
        rot_ab1, rot_b1b2, rot_b2c1, rot_c1c2)
    

def lig_type_to_signs(
        lig_type: Literal["RR", "RL", "LR", "LL"]) -> tuple[int, int]:
    """
    Convert the conformation ID to the signs of the rotation directions.

    Each of the two letters in the conformation ID is converted to
    either 1 or -1: "R" -> 1, "L" -> -1.

    Args:
    - lig_type (Literal["RR", "RL", "LR", "LL"]): Combination of two
    letters, which represent the rotation directions of the two C-C
    bonds between the pyridine rings and the central benzene ring.

    For the definitions of the rotation directions, please refer to the
    paper.

    Returns:
    - tuple[int, int]: Signs of the rotation directions.

    The returned values are as follows:
    - j (int): Sign of the rotation direction of the first C-C bond.
    - k (int): Sign of the rotation direction of the second C-C bond.

    Examples:
    >>> lig_type_to_signs("RR")
    (1, 1)
    >>> lig_type_to_signs("RL")
    (1, -1)
    >>> lig_type_to_signs("LR")
    (-1, 1)
    >>> lig_type_to_signs("LL")
    (-1, -1)
    """
    if lig_type == "RR":
        return 1, 1
    elif lig_type == "RL":
        return 1, -1
    elif lig_type == "LR":
        return -1, 1
    elif lig_type == "LL":
        return -1, -1
    else:
        raise ValueError(f"Invalid lig_type: {lig_type}")