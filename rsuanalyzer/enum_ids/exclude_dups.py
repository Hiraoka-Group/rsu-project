from itertools import product
from typing import Iterable

from rsuanalyzer.calc_rsu.conf_id_to_lig_and_con_types import \
    conf_id_to_lig_and_con_types


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
        dup_ids = _id_to_dup_ids(ring, theta)

        # Choose the conformation ID with the maximum value
        # as the representative of the duplicates.
        unique_ids.add(max(dup_ids))

        # Remove the duplicates from the list of conformation IDs
        # since they are already included in the representative.
        conf_ids -= dup_ids

    return unique_ids


def _id_to_dup_ids(conf_id: str, theta: float) -> set[str]:
    """
    Convert a conformation ID to a set of conformation IDs that are
    duplicates of the input conformation ID.

    "Duplicates" means conformation IDs that represent the same ring
    structure.

    There are 5 types of duplicates, and the Type 4 and 5 are
    only for theta = 0 and theta = 90, respectively.

    1. Different Cut Points 
        IDs derived from the same ring by cutting at different points. 
        (e.g. "RRFFLLBBRRFB", "LLBBRRFBRRFF" and "RRFBRRFFLLBB")
    2. Reverse Order 
        IDs derived by reading the ligand types and connection types 
        in the opposite direction along the ring. Note that IDs should
        start with ligand type, not connection type.
        (e.g. "RRFFLLFB", "LLFFRRBF")
    3. Enantiomer 
        IDs being same to each other when all the letters of ligand 
        types are replaced with the opposite letters, i.e., R -> L and
        L -> R.
        (e.g. "RRFFLLFB" and "LLFFRRFB")
    4. Lig-Con Set Reverse (Only for theta = 0)
        IDs gained by replacing one or more pairs of "R" or "L" and 
        "F" or "B", with the reversed ones, e.g. "RF" -> "FR", "FR" 
        -> "RF", "RB" -> "BR", ...
        (e.g. "RRFFLLFB", "RLBFLLFB", "RRFFLRBB", "LRFFLLFF", 
        "RLBFLRBB", ...)
    5. All Possible R-L Reversals (Only for theta = 90)
        IDs gained by substituting "R" with "L" and vice versa, 
        at any one or more positions.
        (e.g. "RRFFRRFB", "RRFFRLFB", "RRFFLRFB", "RRFFLLFB", 
        "RLFFRRFB", "RLFFRLFB", ...)

    Args:
    - conf_id (str): Conformation ID of the ring.
    - theta (float): Tilting angle of the ligand in degree. Note that
    results are same for 0 < theta < 90.

    Returns:
    - set[str]: The set of conformation IDs that are duplicates of the
    input conformation ID.
    """
    ids = {conf_id}
    # Type 1: Different cut points.
    ids.update(_different_cut_points(conf_id))

    # Type 2: Reversed conformation IDs.
    for cur_id in ids.copy():
        ids.add(_order_reversed(cur_id))

    # Type 3: Enantiomers.
    for cur_id in ids.copy():
        ids.add(_enantiomer(cur_id))

    if theta == 0:
        for cur_id in ids.copy():
            # Type 4: lig-con set reverse.
            ids.update(_lig_con_set_revs(cur_id))

    if theta == 90:
        # Type 5: R-L rev.
        for cur_id in ids.copy():
            ids.update(_rl_revs(cur_id))

    return ids


# Type 1: Different cut points.
# e.g. "RRFFLLBB" and "LLBBRRFF"
def _different_cut_points(conf_id: str) -> list[str]:
    return [
        conf_id[i*4:] + conf_id[:i*4]
        for i in range(len(conf_id) // 4)]


# Type 2: Reversed conformation IDs.
# e.g. "RRFFLLBB" and "LLFFRRBB"
def _order_reversed(conf_id: str) -> str:
    tail = conf_id[-2:]  # "RRFFLLBB" -> "BB"
    body = conf_id[:-2]  # "RRFFLLBB" -> "RRFFLL"
    return body[-1::-1] + tail[-1::-1]  # "LLFFRR" + "BB" -> "LLFFRRBB"


# Type 3: Enantiomers.
# e.g. "RRFFLLBB" and "LLFFRRBB"
def _enantiomer(conf_id: str) -> str:
    return conf_id.translate(str.maketrans("RL", "LR"))  # "RRFFLLBB" -> "LLBBRRFF"


# Type 4: lig-con set reverse. (Only for theta = 0)
# If theta = 0, structures remain the same when 
# adjacent ligand type and connection type is both reversed.
# e.g. "RRFF"="RLBF", "RRBB"="RLFB", "RRFF"="LRFB".
def _lig_con_set_revs(conf_id: str) -> set[str]:
    ids = set()
    cur_id_2 = conf_id[1:] + conf_id[0]  # "RRFF" -> "RFFR"

    # "RFFR" -> ["RF", "FR"]
    lig_con_sets = [
        cur_id_2[i:i+2] for i in range(0, len(cur_id_2), 2)]

    # Enumerate all the possible combinations of if the ligand type and
    # the connection type are reversed.
    for rev_list in product([True, False], repeat=len(lig_con_sets)):
        new_lig_con_set_list = []
        for lig_con_set, rev in zip(lig_con_sets, rev_list):
            if rev:
                new_lig_con_set_list.append(
                    lig_con_set.translate(
                        str.maketrans("RLFB", "LRBF")))
            else:
                new_lig_con_set_list.append(lig_con_set)
        new_id_2 = "".join(new_lig_con_set_list)
        ids.add(new_id_2[-1] + new_id_2[:-1])

    return ids


# Type 5: All possible R-L reversals. (Only for theta = 90)
# e.g. "RRFFRRFB" and "RRFFRLFB"
def _rl_revs(conf_id: str) -> set[str]:
    ids = set()

    lig_tyes, con_types = conf_id_to_lig_and_con_types(conf_id)

    for cur_lig_types in product(["RR", "RL", "LR", "LL"], repeat=len(lig_tyes)):
        new_lig_con_types = []
        for lig_type, con_type in zip(cur_lig_types, con_types):
            new_lig_con_types.append(lig_type + con_type)
        new_id = "".join(new_lig_con_types)
        ids.add(new_id)
    return ids