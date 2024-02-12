"""Functions to calculate the minimum RSU for each theta."""

from typing import Iterable

import pandas as pd

from ..calc_rsu.rsu import calc_rsu


def calc_min_rsu_for_thetas(
        conf_ids: Iterable[str], thetas: Iterable[float], delta_: float
        ) -> pd.DataFrame:
    """Calculate the minimum RSU for each theta.

    Args:
        conf_ids (Iterable[str]): 
            The list of conformation IDs of rings, e.g. "RRFFLLBB".
        thetas (Iterable[float]): 
            The list of tilt angles of C-C bonds. (unit: degree) 
            0 <= theta <= 90.
        delta_ (float): 
            N-Pd-N angle. (unit: degree) 0 < delta_ <= 180.

    Returns:
        A pandas DataFrame containing the minimum RSU for each theta.
        The columns are "Theta", "Ring ID", and "RSU".
    """
    min_rsu_list = []
    for theta in thetas:
        min_rsu_list.append(
            _calc_min_rsu_for_specific_theta(conf_ids, theta, delta_))

    min_rsu_table = pd.DataFrame({
        "Theta": thetas,
        "Ring ID": [min_rsu[0] for min_rsu in min_rsu_list],
        "RSU": [min_rsu[1] for min_rsu in min_rsu_list]
    })

    return min_rsu_table


def _calc_min_rsu_for_specific_theta(
        ring_ids: Iterable[str], theta: float, delta_: float
        ) -> tuple[str, float]:
    """Calculate the minimum RSU for a specific theta.
    
    Args:
        ring_ids (Iterable[str]): 
            The list of conformation IDs of rings, e.g. "RRFFLLBB".
        theta (float): 
            The tilt angle of C-C bonds. (unit: degree) 
            0 <= theta <= 90.
        delta_ (float): 
            N-Pd-N angle. (unit: degree) 0 < delta_ <= 180.
        
    Returns:
        tuple[str, float]: 
            The conformation ID of the ring with the minimum RSU 
            and the minimum RSU.
    """
    
    rsu_list = [
        calc_rsu(ring_id, theta, delta_) for ring_id in ring_ids]
    min_rsu = min(rsu_list)
    min_rsu_idx = rsu_list.index(min_rsu)
    min_rsu_ring_id = ring_ids[min_rsu_idx]

    return min_rsu_ring_id, min_rsu
