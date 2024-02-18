from itertools import product
from typing import Iterable

from ._id_duplicates import _enum_duplicate_ids


def enum_ring_ids(
        num_of_ligs: int, theta: float | None = None
        ) -> set[str]:
    """Enumerate all possible conformation IDs of rings.

    This function is used when you want to enumerate all possible
    conformation IDs of rings with the given number of ligands to
    create a rank table of RSU or to calculate the minimum RSU.
    (See examples below.)

    See also:
        The result of this function can be used in the following:

        - :func:`create_small_rsu_ranking \
            <rsuanalyzer.analyze_rsu.small_rsu_ranking.create_small_rsu_ranking>`
        - :func:`create_min_rsu_vs_theta_df \
            <rsuanalyzer.analyze_rsu.calc_min_rsu_vs_theta.create_min_rsu_vs_theta_df>`

        See the examples below for more details.

    Args:
        num_of_ligs (int): 
            The number of ligands in a ring.
        theta (float): 
            Tilting angle of the ligand in degree. Note that results 
            are same for 0 < theta < 90.

    Returns:
        set[str]: 
            The set of possible conformation IDs of rings with the 
            given number of ligands.

    Examples:
        Simple examples:
            >>> import rsuanalyzer as ra
            >>> ra.enum_conf_ids(1, 30)
            ['RRFF', 'RRFB', 'RRBF', 'RRBB', 'RLFF', ..., 'LLBB'] (16 items)
            >>> ra.enum_conf_ids(2, 30)
            ['RRFFRRFF', ... 'LLBBLLBB'] (256 items)

        Create a rank table of RSU:
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

        Calculate the minimum RSU:
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
    """
    conf_ids_with_dups = _enum_dup_included_ids(num_of_ligs)
    
    return _exclude_dups(conf_ids_with_dups, theta)


def _enum_dup_included_ids(num_of_ligs: int) -> set[str]:
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


def _exclude_dups(
        conf_ids_with_dups: Iterable[str], 
        theta: float | None = None
        ) -> set[str]:
    """Exclude duplicate conformation IDs of rings.

    Args:
        conf_ids_with_dups (Iterable[str]):
            The list of conformation IDs of rings possibly including 
            duplicates.
        theta (float): 
            Tilting angle of the ligand in degree. Results are same 
            for any 0 < theta < 90, and different for theta = 0 and 
            theta = 90.

    Returns:
        set[str]: The set of conformation IDs of rings without
        duplicates.
    """
    conf_ids_with_dups = set(conf_ids_with_dups)

    # Conformation IDs without duplicates.
    unique_ids = set()

    while conf_ids_with_dups:
        cur_id = conf_ids_with_dups.pop()
        dups_of_cur_id = _enum_duplicate_ids(cur_id, theta)

        # Choose the conformation ID with the maximum value
        # as the representative of the duplicates.
        # e.g. "RRFFLLBB", "LLBBRRFF", "LLFFRRBB", "RRBBLLFF" -> "RRFFLLBB"
        unique_ids.add(max(dups_of_cur_id))

        # Remove the duplicates from the list of conformation IDs
        # since they have no chance to be the representative.
        conf_ids_with_dups -= dups_of_cur_id

    return unique_ids
