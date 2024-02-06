def are_conf_ids_in_same_group(conf_id1: str, conf_id2: str) -> bool:
    return conf_id_to_group_id(conf_id1) == conf_id_to_group_id(conf_id2)


def conf_id_to_group_id(conf_id: str) -> str:
    return max(conf_id_to_ids_in_same_group(conf_id))


def conf_id_to_ids_in_same_group(conf_id: str) -> set[str]:
    """
    Convert a conformation ID to a set of conformation IDs in the same group. 
    
    There can be multiple conformation IDs for the same
    ring structure. We define the conformation IDs that are equivalent
    to each other as "in the same group".

    Four patterns and their combinations are considered.
    Pattern 1: Different cut points. 
    e.g. "RRFFLLBB" and "LLBBRRFF"
    Pattern 2: Reversed conformation IDs.
    e.g. "RRFFLLBB" and "LLFFRRBB"
    Pattern 3: Enantiomers.
    e.g. "RRFFLLBB" and "LLFFRRBB"

    Args:
    - conf_id (str): The conformation ID.

    Returns:
    - set[str]: The conformation IDs in the same group.

    Examples:
    >>> conf_id_to_ids_in_same_group("RRFFLLBB")
    {"RRFFLLBB", "LLBBRRFF", "LLFFRRBB", "RRBBLLFF"}
    >>> conf_id_to_ids_in_same_group("RLFBRRFF")
    {"RLFBRRFF", "RRFFRLFB", "RRBFLRFF", "LRFFRRBF", 
     "LRFBLLFF", "LLFFLRFB", "LLBFRLFF", "RLFFLLBF"}
    """

    num_of_ligs = len(conf_id) // 4
    ids = {conf_id}

    # Pattern 1
    # e.g. "RRFFLLBB" and "LLBBRRFF"
    for i in range(1, num_of_ligs):
        ids.add(conf_id[i*4:] + conf_id[:i*4])

    # Pattern 2
    # e.g. "RRFFLLBB" and "LLFFRRBB"
    for cur_id in ids.copy():
        rev = cur_id[-1::-1]  # "RRFFLLBB" -> "BBLLFFRR"
        ids.add(rev[2:] + rev[:2])  # "BBLLFFRR" -> "LLFFRRBB"

    # Pattern 3
    # e.g. "RRFFLLBB" and "LLFFRRBB"
    for cur_id in ids.copy():
        enant = cur_id.translate(str.maketrans("RL", "LR"))  # "RRFFLLBB" -> "LLBBRRFF"
        ids.add(enant)

    return ids