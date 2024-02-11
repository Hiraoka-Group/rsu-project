from typing import Literal

import numpy as np
from scipy.spatial.transform import Rotation as R


def x_ac_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    return x_ab_coord_a(lig_type, theta) + x_bc_coord_a(
        lig_type, theta)


def x_ab_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
    return np.array([1, 0, 0])


def x_bc_coord_a(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> np.ndarray:
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
    if lig_type in ("RR", "RL"):
        return R.from_euler("X", theta, degrees=True)
    elif lig_type in ("LR", "LL"):
        return R.from_euler("X", -theta, degrees=True)
    else:
        raise ValueError(f"Invalid lig_type: {lig_type}")


def rot_ac(
        lig_type: Literal["RR", "RL", "LR", "LL"], theta: float
        ) -> R:
    if lig_type == "RR":
        return R.from_euler(
            "XZX", [theta, 60, theta + 180], degrees=True)
    elif lig_type == "RL":
        return R.from_euler("XZX", [theta, 60, -theta], degrees=True)
    elif lig_type == "LR":
        return R.from_euler("XZX", [-theta, -60, theta], degrees=True)
    elif lig_type == "LL":
        return R.from_euler(
            "XZX", [-theta, -60, -theta + 180], degrees=True)
    else:
        raise ValueError(f"Invalid lig_type: {lig_type}")
