from typing import Iterable

import pandas as pd

from ..calc_rsu.rsu import calc_rsu


def calc_min_rsu_for_thetas(
        ring_ids: Iterable[str], thetas: Iterable[float], delta_: float
        ) -> pd.DataFrame:
    
    min_rsu_list = []
    for theta in thetas:
        min_rsu_list.append(
            _calc_min_rsu_for_specific_theta(ring_ids, theta, delta_))

    min_rsu_table = pd.DataFrame({
        "Theta": thetas,
        "Ring ID": [min_rsu[0] for min_rsu in min_rsu_list],
        "RSU": [min_rsu[1] for min_rsu in min_rsu_list]
    })

    return min_rsu_table


def _calc_min_rsu_for_specific_theta(
        ring_ids: Iterable[str], theta: float, delta_: float
        ) -> tuple[str, float]:
    
    rsu_list = [
        calc_rsu(ring_id, theta, delta_) for ring_id in ring_ids]
    min_rsu = min(rsu_list)
    min_rsu_idx = rsu_list.index(min_rsu)
    min_rsu_ring_id = ring_ids[min_rsu_idx]

    return min_rsu_ring_id, min_rsu
