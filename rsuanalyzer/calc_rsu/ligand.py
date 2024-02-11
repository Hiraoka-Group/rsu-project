"""Functions to calculate vectors and rotations for the ligand.

Model ligand has points A, B, and C, and the coordinate systems A, B1, 
B2, and C. For more detailed definitions, see the associated paper.
"""

from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R


def x_ac_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    """Calculate the vector AC in the coordinate system A.
    
    For the definitions of the points and the coordinate systems, 
    see the associated paper.
    """
    return x_ab_coord_a(lig_type, theta) + x_bc_coord_a(
        lig_type, theta)


def x_ab_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    """Calculate the vector AB in the coordinate system A.

    For the definitions of the points and the coordinate systems, 
    see the associated paper.
    """
    return np.array([1, 0, 0])


def x_bc_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    """Calculate the vector BC in the coordinate system A.

    For the definitions of the points and the coordinate systems,
    see the associated paper.
    """
    if lig_type in ("RR", "RL"):
        return R.from_euler(
            "XZ", [theta, 60], degrees=True).apply([1, 0, 0])
    elif lig_type in ("LR", "LL"):
        return R.from_euler(
            "XZ", [-theta, -60], degrees=True).apply([1, 0, 0])
    else:
        raise ValueError(f"Invalid lig_type: {lig_type}")


def rot_ab1(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> R:
    """Calculate the rotation from the coordinate system A to B1.

    For the definitions of the points and the coordinate systems,
    see the associated paper.
    """
    if lig_type in ("RR", "RL"):
        return R.from_euler("X", theta, degrees=True)
    elif lig_type in ("LR", "LL"):
        return R.from_euler("X", -theta, degrees=True)
    else:
        raise ValueError(f"Invalid lig_type: {lig_type}")


def rot_ac(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> R:
    """Calculate the rotation from the coordinate system A to C.

    For the definitions of the points and the coordinate systems,
    see the associated paper.
    """
    if lig_type == "RR":
        # Last rotation of 180 degrees is for ensuring that the
        # z-axis of the coordinate system C protrudes from the
        # "Front" side of the pyridine ring.
        return R.from_euler(
            "XZX", [theta, 60, theta + 180], degrees=True)
    elif lig_type == "RL":
        return R.from_euler("XZX", [theta, 60, -theta], degrees=True)
    elif lig_type == "LR":
        return R.from_euler("XZX", [-theta, -60, theta], degrees=True)
    elif lig_type == "LL":
        # Last rotation of 180 degrees is for ensuring that the
        # z-axis of the coordinate system C protrudes from the
        # "Front" side of the pyridine ring.
        return R.from_euler(
            "XZX", [-theta, -60, -theta + 180], degrees=True)
    else:
        raise ValueError(f"Invalid lig_type: {lig_type}")
