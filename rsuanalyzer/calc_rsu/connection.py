from typing import Literal

from scipy.spatial.transform import Rotation as R


def calc_con_rot(
        con_type: Literal["FF", "FB", "BF", "BB"], delta_: float
        ) -> R:
    """
    Calculate the rotation from the coordinate system of the previous 
    ligand to the coordinate system of the next ligand.
    
    Args:
    - con_type (Literal["FF", "FB", "BF", "BB"]): Connection type of 
    the ligand.
    - delta_ (float): Angle in degrees. 0 < delta_ <= 180.
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
