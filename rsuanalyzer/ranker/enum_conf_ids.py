from itertools import product
from typing import Iterable

from .conf_group import id_to_dup_ids


def enum_conf_ids_including_dups(num_of_ligs: int) -> list[str]:
    """
    Enumerate all possible conformation IDs of rings.

    Note that this function includes duplicate conformation IDs, i.e.,
    conformation IDs that represent the same ring structure.

    Args:
    - num_of_ligs (int): The number of ligands in a ring.

    Returns:
    - list[str]: The list of conformation IDs of rings.

    Examples:
    >>> enum_conf_ids_including_dups(1)
    ['RRFF', 'RRFB', 'RRBF', 'RRBB', 'RLFF', ... 'LLBB'] (16 items)
    >>> enum_conf_ids_including_dups(2)
    ['RRFFRRFF', ... 'LLBBLLBB'] (256 items)
    """
    LIG_TYPES = ["RR", "RL", "LR", "LL"]
    CON_TYPES = ["FF", "FB", "BF", "BB"]

    # All combinations of ligand types and connection types.
    # ["RRFF", "RRFB", "RRBF", "RRBB", "RLFF", ... "LLBB"]
    LIG_CON_TYPES = [
        lig_type + con_type 
        for lig_type, con_type in product(LIG_TYPES, CON_TYPES)]
    
    # All combinations of lig_con_types for the given number 
    # of ligands.
    return [
        "".join(con_lig_type) for con_lig_type 
        in product(LIG_CON_TYPES, repeat=num_of_ligs)]


def exclude_duplicates(
        conf_ids: Iterable[str], theta: float) -> set[str]:
    """
    Exclude duplicate conformation IDs of rings.

    Args:
    - conf_ids (Iterable[str]): The list of conformation IDs of rings 
    including duplicates.
    - theta (float): Tilting angle of the ligand in degree. (Results 
    are same for 0 < theta < 90.)

    Returns:
    - set[str]: The set of unique conformation IDs of rings.
    """
    conf_ids = set(conf_ids)

    # Store conformation IDs that are not duplicates.
    unique_ids = set()

    while conf_ids:
        ring = conf_ids.pop()
        dup_ids = id_to_dup_ids(ring, theta)

        # Choose the conformation ID with the maximum value
        # as the representative of the duplicates.
        unique_ids.add(max(dup_ids))

        # Remove the duplicates from the list of conformation IDs
        # since they are already included in the representative.
        conf_ids -= dup_ids
    
    return unique_ids