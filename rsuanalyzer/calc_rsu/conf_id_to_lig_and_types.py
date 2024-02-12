"""Functions to extract ligand types and connection types from a 
conformation ID."""

def conf_id_to_lig_types(conf_id: str) -> list[str]:
    """
    Extract the ligand types from the conformation ID.

    Args:
        conf_id (str): Conformation ID of the chain or ring.
    
    Returns:
        list[str]: Ligand types.

    Examples:
        >>> conf_id_to_lig_types("RRFFLL")  # chain
        ["RR", "LL"]
        >>> conf_id_to_lig_types("RRFFLLBB")  # ring
        ["RR", "LL"]
    """
    return [conf_id[i:i+2] for i in range(0, len(conf_id), 4)]


def conf_id_to_con_types(conf_id: str) -> list[str]:
    """
    Extract the connection types from the conformation ID.

    Args:
        conf_id (str): Conformation ID of the chain or ring.
    
    Returns:
        list[str]: Connection types.

    Examples:
        >>> conf_id_to_lig_types("RRFFLL")  # chain
        ["FF"]
        >>> conf_id_to_lig_types("RRFFLLBB")  # ring
        ["FF", "BB"]
    """
    return [conf_id[i:i+2] for i in range(2, len(conf_id), 4)]
