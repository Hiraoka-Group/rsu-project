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


def ring_to_chains(conf_id_of_ring: str) -> list[str]:
    """
    Convert the conformation ID of a ring to the conformation IDs of
    the chains.

    Args:
    - conf_id_of_ring (str): The conformation ID of the ring. 
      This should contain the same number of connection types as the 
      number of ligands in the ring. For example, for a 2-membered ring, 
      it would be "RRFFRLFF".

    Returns:
    - list[str]: The conformation IDs of the chains.

    Examples:
    >>> ring_to_chains("RRFFRLFF")
    ['RRFFRL', 'RLFFRR']
    >>> ring_to_chains("RRFFRLFFRRBF")
    ['RRFFRLFFRR', 'RRBFRRFFRL', 'RLFFRRBFRR']
    """
    # Validate the input.
    if len(conf_id_of_ring) % 4 != 0:
        raise ValueError(
            "The length of the conformation ID of the ring should be a "
            "multiple of 4.")
    
    chain_length = len(conf_id_of_ring) // 4
    chains = []
    for _ in range(chain_length):
        conf_id = conf_id_of_ring[:-2]
        conf_id_of_ring = conf_id_of_ring[-4:] + conf_id_of_ring[:-4]
        chains.append(conf_id)
    return chains


if __name__ == "__main__":
    import doctest
    doctest.testmod()