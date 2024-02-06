from itertools import product

from .conf_group import conf_id_to_group_id


def enum_all_rings(num_of_ligs: int) -> list[str]:
    LIG_TYPES = ["RR", "RL", "LR", "LL"]
    CON_TYPES = ["FF", "FB", "BF", "BB"]

    LIG_CON_TYPES = [lig_type + con_type for lig_type, con_type in product(LIG_TYPES, CON_TYPES)]
    
    return ["".join(con_lig_type) for con_lig_type in product(LIG_CON_TYPES, repeat=num_of_ligs)]


def enum_groups_from_rings(rings: list[str]) -> set[str]:
    return {conf_id_to_group_id(ring) for ring in rings}