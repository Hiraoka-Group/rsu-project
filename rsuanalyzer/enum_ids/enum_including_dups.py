"""Functions for enumerating conformation IDs of rings including duplicates."""

from itertools import product


def enum_conf_ids_including_dups(num_of_ligs: int) -> set[str]:
    """Enumerate all possible conformation IDs of rings.

    Note: 
        this function includes duplicate conformation IDs, i.e.,
        conformation IDs that represent the same ring structure, e.g. 
        "RRFFLLBB" and "LLBBRRFF", or "RRFFRRFF" and "LLFFLLFF".

    Args:
        num_of_ligs (int): 
            The number of ligands in a ring.

    Returns:
        set[str]: 
            The set of possible conformation IDs of rings with the 
            given number of ligands.

    Examples:
        >>> enum_conf_ids_including_dups(1)
        ['RRFF', 'RRFB', 'RRBF', 'RRBB', 'RLFF', ..., 'LLBB'] (16 items)
        >>> enum_conf_ids_including_dups(2)
        ['RRFFRRFF', ... 'LLBBLLBB'] (256 items)
    """
    LIG_TYPES = ["RR", "RL", "LR", "LL"]
    CON_TYPES = ["FF", "FB", "BF", "BB"]

    # All combinations of ligand types and connection types.
    # ["RRFF", "RRFB", "RRBF", "RRBB", "RLFF", ... "LLBB"] (16 items)
    LIG_CON_TYPES = [
        lig_type + con_type
        for lig_type, con_type in product(LIG_TYPES, CON_TYPES)]

    # All combinations of lig_con_types for the given number 
    # of ligands.
    return {
        "".join(con_lig_type) for con_lig_type
        in product(LIG_CON_TYPES, repeat=num_of_ligs)}
