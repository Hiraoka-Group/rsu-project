from functools import cache
from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R


@cache
def _x_ab_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    """Calculate the vector AB in the coordinate system A.

    For the definitions of the points and the coordinate systems, 
    see the associated paper.
    """
    return np.array([1, 0, 0])


@cache
def _x_bc_coord_a(
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


@cache
def _x_ac_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    """Calculate the vector AC in the coordinate system A.

    For the definitions of the points and the coordinate systems, 
    see the associated paper.
    """
    return _x_ab_coord_a(lig_type, theta) + _x_bc_coord_a(
        lig_type, theta)


@cache
def _rot_ab1(
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


@cache
def _rot_ac(
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


@cache
def _rot_ca(
        con_type: Literal["FF", "FB", "BF", "BB"], delta_: float
        ) -> R:
    """Calculate the rotation for connection on metal.

    Rotation from the coordinate system C of the current ligand to the
    coordinate system A of the next ligand is calculated. For more
    detailed definitions, see the associated paper.

    Args:
        con_type (Literal["FF", "FB", "BF", "BB"]): Connection type.
        delta_ (float): N-M-N angle in degrees. 0 < delta\_ <= 180.

    Returns:
        R: The rotation from the coordinate system C of the current
        ligand to the coordinate system A of the next ligand.
    """
    if not 0 < delta_ <= 180:
        raise ValueError(f"Invalid delta_: {delta_}")

    if con_type == "FF":
        return R.from_euler("Y", delta_ + 180, degrees=True)
    elif con_type == "FB":
        return R.from_euler("YZ", [delta_, 180], degrees=True)
    elif con_type == "BF":
        return R.from_euler("YZ", [-delta_, 180], degrees=True)
    elif con_type == "BB":
        return R.from_euler("Y", -delta_ + 180, degrees=True)
    else:
        raise ValueError(f"Invalid con_type: {con_type}")
