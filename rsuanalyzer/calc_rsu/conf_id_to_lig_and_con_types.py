def conf_id_to_lig_and_con_types(
        conf_id: str) -> tuple[list[str], list[str]]:
    """
    Convert the conformation ID to the ligand types and connection types.

    Args:
    - conf_id (str): Conformation ID of the chain or ring.
    
    Returns:
    - tuple[list[str], list[str]]: Ligand types and connection types.
    """
    lig_types = [conf_id[i:i+2] for i in range(0, len(conf_id), 4)]
    con_types = [conf_id[i:i+2] for i in range(2, len(conf_id), 4)]
    return lig_types, con_types
