from itertools import product
from typing import Iterable

from ..core._conf_id import _id_to_con_types, _id_to_lig_types


def _enum_duplicate_ids(
        ring_id: str, theta: float | None = None
        ) -> set[str]:
    """Return the set of conformation IDs that are duplicates of the
    input conformation ID.

    "Duplicates" means conformation IDs that represent the same ring
    structure. 

    Args:
        ring_id (str): Conformation ID of the ring.
        theta (float): Tilting angle of the ligand in degree. Note that
            results are same for 0 < theta < 90.

    Returns:
        set[str]: The set of conformation IDs that are duplicates of the
            input conformation ID. The set includes the input conformation ID.

    Note:
        The results include the input conformation ID.

    Details:
        There are five types of duplicates, and they and their combinations
        are considered in this function. The types are as follows:

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
            at any one or more positions preserving connection types.
            (e.g. "RRFFRRFB", "RRFFRLFB", "RRFFLRFB", "RRFFLLFB", 
            "RLFFRRFB", "RLFFRLFB", ...)

    Caution:
        the types 4 and 5 are only for theta = 0 and theta = 90, 
        respectively.

    For more details, see the docstrings of the functions that
    implement each type of duplicates.
    """
    # Original conformation ID and its duplicates.
    orig_and_dups = {ring_id}

    # In the following, we consider the five types of duplicates.
    # By checking the duplicates of the duplicates, we can cover all
    # the possible combinations of the types of duplicates.

    # Type 1: Different Cut Points.
    orig_and_dups.update(_different_cut_points(ring_id))

    # Type 2: Reverse Order.
    for cur_id in orig_and_dups.copy():
        orig_and_dups.add(_rev_order(cur_id))

    # Type 3: Enantiomers.
    for cur_id in orig_and_dups.copy():
        orig_and_dups.add(_enantiomer(cur_id))

    if theta == 0:
        for cur_id in orig_and_dups.copy():
            # Type 4: Lig-Con Set Reverse.
            orig_and_dups.update(_lig_con_set_revs(cur_id))

    if theta == 90:
        # Type 5: All Possible R-L Reversals.
        for cur_id in orig_and_dups.copy():
            orig_and_dups.update(_all_possible_rl_revs(cur_id))

    return orig_and_dups


# Type 1: Different Cut Points.
def _different_cut_points(conf_id: str) -> set[str]:
    """Return the set of conformation IDs that are derived from the
    same ring as the input conformation ID, by cutting at different
    points.

    Example:
    >>> _different_cut_points("RRFFLLBB")
    {"RRFFLLBB", "LLBBRRFF"}
    """
    return {
        conf_id[i*4:] + conf_id[:i*4]
        for i in range(len(conf_id) // 4)}


# Type 2: Reverse Order.
def _rev_order(conf_id: str) -> str:
    """Return the conformation ID gained by reading the ligand types
    and connection types in the opposite direction along the ring.

    Since the conformation ID should start with ligand type, not
    connection type, the result is not simply the reverse of the input
    conformation ID.

    Example:
    >>> _rev_order("RRFFLLBB")
    "LLFFRRBB"
    """
    tail = conf_id[-2:]  # "RRFFLLBB" -> "BB"
    body = conf_id[:-2]  # "RRFFLLBB" -> "RRFFLL"
    return body[-1::-1] + tail[-1::-1]  # "LLFFRR" + "BB" -> "LLFFRRBB"


# Type 3: Enantiomers.
def _enantiomer(conf_id: str) -> str:
    """Return the enantiomer of the input conformation ID.

    The enantiomer is the conformation ID that is same to the input
    conformation ID when all the letters of ligand types are replaced
    with the opposite letters, i.e., R -> L and L -> R.

    Example:
    >>> _enantiomer("RRFFLLBB")
    "LLFFRRBB"
    """
    return conf_id.translate(str.maketrans("RL", "LR"))


# Type 4: Lig-Con Set Reverse (Only for theta = 0)
# e.g. "RRFF"="RLBF", "RRBB"="RLFB", "RRFF"="LRFB".
def _lig_con_set_revs(conf_id: str) -> set[str]:
    """Return the set of conformation IDs that are gained by replacing
    one or more pairs of "R" or "L" and "F" or "B", with the reversed
    ones.

    Example:
    >>> _lig_con_set_revs("RRFF")
    {"RRFF", "RLBF", "LRFB", "LLBB"}
    """
    dups = set()

    # In order to make the first letter and the last letter adjacent, 
    # we rotate the input conformation ID by one letter.
    rotated_input_id = conf_id[1:] + conf_id[0]  # "RRFF" -> "RFFR"

    # Split the rotated conformation ID into pairs of two letters: 
    # ligand type and connection type, or reversed ones.
    # "RFFR" -> ["RF", "FR"]
    input_lig_con_pairs = [
        rotated_input_id[i:i+2] for i
        in range(0, len(rotated_input_id), 2)]

    # Enumerate all the possible combinations of whether the pairs of
    # ligand type and connection type are reversed or not.
    # In the example of ["RF", "FR"], the combinations are
    # [True, True], [True, False], [False, True], and [False, False].
    # For example, [True, False] means the first pair "RF" is reversed
    # to "LB", and the second pair "FR" is not reversed, thus the
    # new_id_2 is "LBFR".
    for bools_of_rev in product(
            [True, False], repeat=len(input_lig_con_pairs)):
        dup_lig_con_pairs = []
        for input_lig_con_pair, bool_of_rev in zip(
                input_lig_con_pairs, bools_of_rev):
            if bool_of_rev:
                # "R" -> "L", "L" -> "R", "F" -> "B", "B" -> "F"
                dup_lig_con_pairs.append(
                    input_lig_con_pair.translate(
                        str.maketrans("RLFB", "LRBF")))
            else:
                dup_lig_con_pairs.append(input_lig_con_pair)
        rotated_dup_id = "".join(dup_lig_con_pairs)

        # Rotate the conformation ID back to the original order.
        dups.add(rotated_dup_id[-1] + rotated_dup_id[:-1])

    return dups


# Type 5: All possible R-L reversals. (Only for theta = 90)
def _all_possible_rl_revs(conf_id: str) -> set[str]:
    """Return the set of conformation IDs that are gained by
    substituting "R" with "L" and vice versa, at any one or more
    positions preserving connection types.

    Example:
    >>> _all_possible_rl_revs("RRFF")
    {"RRFF", "RLFF", "LRFF", "LLFF"}
    >>> _all_possible_rl_revs("RRFFLLBB")
    {"RRFFRRBB", "RRFFRLBB", "RRFFLRBB", "RRFFLLBB", ... "LLFFLLBB"} (16 items)
    """
    ids = set()

    lig_tyes = _id_to_lig_types(conf_id)
    con_types = _id_to_con_types(conf_id)

    for cur_lig_types in product(
        ["RR", "RL", "LR", "LL"], repeat=len(lig_tyes)):
        new_lig_con_types = []
        for lig_type, con_type in zip(cur_lig_types, con_types):
            new_lig_con_types.append(lig_type + con_type)
        new_id = "".join(new_lig_con_types)
        ids.add(new_id)
    return ids
