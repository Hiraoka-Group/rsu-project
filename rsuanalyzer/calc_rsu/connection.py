"""Functions to calculate the rotation for connection on metal"""

from typing import Literal

from scipy.spatial.transform import Rotation as R


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
