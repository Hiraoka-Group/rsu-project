import pandas as pd

from ..core.rsu import calc_rsu


def make_rank_table(
        ring_ids: list[str], theta: float, delta_: float,
        top_num: int = 10) -> pd.DataFrame:
    """
    Make a rank table of ring structures.

    Args:
    - ring_ids (list[str]): The list of conformation IDs of rings.
    - theta (float): Tilting angle of the ligand in degree.
    - delta_ (float): N-Pd-N angle of the ligand in degree.
    - top_num (int): The number of top ring structures to be shown.

    Returns:
    - pd.DataFrame: The rank table of ring structures.
    """
    rsu_list = [calc_rsu(ring_id, theta, delta_) for ring_id in ring_ids]

    rank_table = pd.DataFrame({
        "Ring ID": ring_ids,
        "RSU": rsu_list
    })

    rank_table = rank_table.sort_values("RSU", ascending=True)

    return rank_table.head(top_num)
    