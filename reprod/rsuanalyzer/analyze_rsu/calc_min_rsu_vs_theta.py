from typing import Iterable

import pandas as pd
from matplotlib import pyplot as plt

from ..core.calc_rsu import calc_rsu


def create_min_rsu_vs_theta_df(
        ring_ids: Iterable[str], 
        thetas: Iterable[float] = range(0, 91, 1), 
        delta_: float = 87) -> pd.DataFrame:
    """Calculate the minimum RSU in the given rings for each theta.

    Args:
        ring_ids (Iterable[str]): 
            The list of conformation IDs of rings, 
            e.g. ``["RRFFRRFF", "RLFFRLFF", "RRFFLLBB"]``.

            Hint:
                You can get the list of all conformation IDs of rings
                by using the function :func:`enum_ring_ids 
                <rsuanalyzer.enum_ring_ids.enum_ring_ids.enum_ring_ids>`.
            
        thetas (Iterable[float], optional): 
            The list of tilt angles of C-C bonds. (unit: degree) 
            0 <= theta <= 90. Default is ``range(0, 91, 1)``.
        delta_ (float, optional): 
            N-Pd-N angle. (unit: degree) 0 < delta\_ <= 180. 
            Default is 87.
    
    Returns:
        pd.DataFrame:
            A pandas DataFrame containing the minimum RSU for each theta.
            The columns are "theta", "Ring ID", and "RSU".
    
    Example:
        Case 1:
            >>> import rsuanalyzer as ra
            >>> ra.create_min_rsu_vs_theta_df(
            ...     ["RRFFRRFF", "RLFFRLBB", "RRFBRRFB"], range(0, 91, 10))
            >>> # The result will be:
            >>> #    theta   Ring ID       RSU
            >>> # 0      0  RRFBRRFB  1.032532
            >>> # 1     10  RLFFRLBB  1.032532
            >>> # 2     20  RLFFRLBB  1.032532
            >>> # 3     30  RLFFRLBB  1.032532
            >>> # 4     40  RRFFRRFF  0.914018
            >>> # 5     50  RRFFRRFF  0.783468
            >>> # 6     60  RRFFRRFF  0.652789
            >>> # 7     70  RRFFRRFF  0.532255
            >>> # 8     80  RRFFRRFF  0.440357
            >>> # 9     90  RRFFRRFF  0.404339
        
        Case 2: Using the function :func:`enum_ring_ids \
                <rsuanalyzer.enum_ring_ids.enum_ring_ids.enum_ring_ids>`.
            >>> import rsuanalyzer as ra
            >>> trimeric_rings = ra.enum_ring_ids(2)
            >>> ra.create_min_rsu_vs_theta_df(trimeric_rings)
            >>> #     theta   Ring ID       RSU
            >>> # 0       0  RLFFRLFF  1.032532
            >>> # 1       1  RLFFRLFF  1.021568
            >>> # 2       2  RLFFRLFF  1.010608
            >>> # 3       3  RLFFRLFF  0.999655
            >>> # 4       4  RRFFLLFF  0.988711
            >>> # ..    ...       ...       ...
            >>> # 86     86  RRFFLLFF  0.405869
            >>> # 87     87  RRFFLLFF  0.405200
            >>> # 88     88  RLFFRLFF  0.404722
            >>> # 89     89  RLFFRLFF  0.404435
            >>> # 90     90  RRFFRRFF  0.404339
            >>> # 
            >>> # [91 rows x 3 columns]

    See Also:
        You can plot the result using the function
        :func:`plot_rsu_vs_theta \
        <rsuanalyzer.analyze_rsu.plot_rsu_vs_theta.plot_rsu_vs_theta>`
    """
    min_rsu_list = [
        _calc_min_rsu_for_specific_theta(ring_ids, theta, delta_)
        for theta in thetas]
    
    min_rsu_table = pd.DataFrame({
        "theta": thetas,
        "Ring ID": [ring_id for ring_id, _ in min_rsu_list],
        "RSU": [rsu for _, rsu in min_rsu_list]
    })

    return min_rsu_table


def _calc_min_rsu_for_specific_theta(
        ring_ids: Iterable[str], theta: float, delta_: float
        ) -> tuple[str, float]:
    """Calculate the minimum RSU in the given rings.

    Args:
        ring_ids (Iterable[str]): 
            The list of conformation IDs of rings, 
            e.g. ["RRFFRRFF", "RLFFRLFF", "RRFFLLBB"].
        theta (float): 
            The tilt angle of C-C bonds. (unit: degree) 
            0 <= theta <= 90.
        delta_ (float): 
            N-Pd-N angle. (unit: degree) 0 < delta\_ <= 180.

    Returns:
        tuple[str, float]: 
            The conformation ID of the ring with the minimum RSU
            and the minimum RSU.
    """
    ring_ids = sorted(list(ring_ids), reverse=True)

    rsu_list = [
        calc_rsu(ring_id, theta, delta_) for ring_id in ring_ids]
    min_rsu = min(rsu_list)
    min_rsu_idx = rsu_list.index(min_rsu)
    min_rsu_ring_id = ring_ids[min_rsu_idx]

    return min_rsu_ring_id, min_rsu
