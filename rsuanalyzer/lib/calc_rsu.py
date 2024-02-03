def calc_chain_end_dist(
        conf_id: str, theta: float, phi: float, delta_: float
        ) -> float:
    ...


def calc_chain_length(conf_id: str) -> int:
    ...


def calc_rsu(
        conf_id: str, theta: float, phi: float, delta_: float
        ) -> float:
    chain_length = calc_chain_length(conf_id)
    chain_end_dist = calc_chain_end_dist()
    return chain_end_dist / chain_length