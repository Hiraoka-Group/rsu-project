from typing import Iterable

import pandas as pd

from ..core.calc_rsu import calc_rsu


def create_small_rsu_ranking(
        ring_ids: Iterable[str], 
        theta: float, delta_: float = 87,
        top_num: int = 10) -> pd.DataFrame:
    """Make a rank table of RSU in ascending order.

    Args:
        ring_ids (Iterable[str]): 
            The Iterable of conformation IDs of rings, e.g. "RRFFLLBB".
        theta (float): 
            The tilt angle of C-C bonds. (unit: degree) 
            0 <= theta <= 90.
        delta_ (float, optional):
            N-Pd-N angle. (unit: degree) 0 < delta\_ <= 180. 
            Default is 87.
        top_num (int, optional): 
            The number of top-ranked rings. Default is 10.

    Returns:
        pd.DataFrame: 
            A pandas DataFrame containing the rank table of RSU.
            The columns are "Ring ID" and "RSU".
    
    Example:
        case 1:
            >>> import rsuanalyzer as ra
            >>> ra.create_small_rsu_ranking(
            ...     ["RRFFRRFF", "RRFFLLFF", "RRFFLLBB"], 30, 87)
            >>> # The result will be:
            >>> #        Ring ID       RSU
            >>> # Rank                    
            >>> # 1     RRFFLLFF  0.718436
            >>> # 2     RRFFLLBB  1.032532
            >>> # 3     RRFFRRFF  1.038581
        
        case 2:
            >>> import rsuanalyzer as ra
            >>> trimeric_rings = ra.enum_ring_ids(3)
            >>> ra.create_small_rsu_ranking(
            ...     trimeric_rings, 40, 87, 5)
            >>> # The result will be:
            >>> #            Ring ID       RSU
            >>> # Rank                        
            >>> # 1     RLFFRLFBLRBF  0.252823
            >>> # 2     RLFFRLFFRLFF  0.273040
            >>> # 3     RLFFRLFFLRFF  0.302913
            >>> # 4     RRFFRLFFLRFB  0.330514
            >>> # 5     RRFFLRFFLRFB  0.363424
    """
    ring_ids = list(ring_ids)

    rsu_list = [
        calc_rsu(ring_id, theta, delta_) for ring_id in ring_ids]

    rank_table = pd.DataFrame({
        "Ring ID": ring_ids,
        "RSU": rsu_list
    })

    rank_table = rank_table.sort_values("RSU", ascending=True)
    rank_table = rank_table.reset_index(drop=True)
    rank_table.index += 1
    rank_table.index.name = "Rank"

    return rank_table.head(top_num)
