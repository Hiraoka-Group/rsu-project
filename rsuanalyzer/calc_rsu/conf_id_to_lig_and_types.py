def conf_id_to_lig_types(conf_id: str) -> list[str]:
    """
    Extract the ligand types from the conformation ID.

    Args:
    - conf_id (str): Conformation ID of the chain or ring.
    
    Returns:
    - list[str]: Ligand types.
    """
    return [conf_id[i:i+2] for i in range(0, len(conf_id), 4)]


def conf_id_to_con_types(conf_id: str) -> list[str]:
    """
    Extract the connection types from the conformation ID.

    Args:
    - conf_id (str): Conformation ID of the chain or ring.
    
    Returns:
    - list[str]: Connection types.
    """
    return [conf_id[i:i+2] for i in range(2, len(conf_id), 4)]
