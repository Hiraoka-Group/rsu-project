"""Make a rank table of RSU in ascending order."""

from typing import Iterable

import pandas as pd

from ..calc_rsu.rsu import calc_rsu


def make_rank_table(
        ring_ids: Iterable[str], theta: float, delta_: float,
        top_num: int = 10) -> pd.DataFrame:
    """Make a rank table of RSU in ascending order.

    Args:
        ring_ids (Iterable[str]): 
            The Iterable of conformation IDs of rings, e.g. "RRFFLLBB".
        theta (float): 
            The tilt angle of C-C bonds. (unit: degree) 
            0 <= theta <= 90.
        delta_ (float): 
            N-Pd-N angle. (unit: degree) 0 < delta_ <= 180.
        top_num (int, optional): 
            The number of top-ranked rings. Default is 10.

    Returns:
        pd.DataFrame: 
            A pandas DataFrame containing the rank table of RSU.
            The columns are "Ring ID" and "RSU".
    """
    rsu_list = [
        calc_rsu(ring_id, theta, delta_) for ring_id in ring_ids]

    rank_table = pd.DataFrame({
        "Ring ID": ring_ids,
        "RSU": rsu_list
    })

    rank_table = rank_table.sort_values("RSU", ascending=True)

    return rank_table.head(top_num)
