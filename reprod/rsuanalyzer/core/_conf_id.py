def _id_to_lig_types(conf_id: str) -> list[str]:
    """
    Extract the ligand types from the conformation ID.

    Args:
        conf_id (str): Conformation ID of chain or ring.

    Returns:
        list[str]: Ligand types.

    Examples:
        >>> conf_id_to_lig_types("RRFFLL")  # chain
        ["RR", "LL"]
        >>> conf_id_to_lig_types("RRFFLLBB")  # ring
        ["RR", "LL"]
    """
    return [conf_id[i:i+2] for i in range(0, len(conf_id), 4)]


def _id_to_con_types(conf_id: str) -> list[str]:
    """
    Extract the connection types from the conformation ID.

    Args:
        conf_id (str): Conformation ID of chain or ring.

    Returns:
        list[str]: Connection types.

    Examples:
        >>> conf_id_to_lig_types("RRFFLL")  # chain
        ["FF"]
        >>> conf_id_to_lig_types("RRFFLLBB")  # ring
        ["FF", "BB"]
    """
    return [conf_id[i:i+2] for i in range(2, len(conf_id), 4)]


def _list_chains_derived_from_the_ring(ring_id: str) -> list[str]:
    """Return the list of conformation IDs of chains derived from the
    ring by cutting at different points.

    These are the chains that are used to calculate the RSU of the ring.

    Consider the ring "RRFFLLBBRLFB". When cutting at different points,
    we get the following chains: "RRFFLLBBRL", "LLBBRLFBRR", and 
    "RLFBRRFFLL". If we call the end distances of these chains
    d1, d2, and d3, the average of d1, d2, and d3 is (d1 + d2 + d3) / 3,
    therefore, the RSU of the ring is (d1 + d2 + d3) / 3 / 3. The last
    division by 3 is because the definition of RSU is the average
    distance *per unit*.

    Args:
        ring_id (str): 
            Conformation ID of the ring. e.g., "RRFFLLBBRLFB".

    Returns:
        list[str]: 
            The list of conformation IDs of chains derived from
            the ring by cutting at different points.

    Examples:
        >>> ring_to_chains("RRFFRLFF")
        ['RRFFRL', 'RLFFRR']
        >>> ring_to_chains("RRFFLLBBRLFB")
        ['RRFFLLBBRL', 'RLFBRRFFLL', 'LLBBRLFBRR']
    """
    # Validate the input.
    if len(ring_id) % 4 != 0:
        raise ValueError(
            "The length of the conformation ID of the ring should be a "
            "multiple of 4.")

    chain_length = len(ring_id) // 4
    chains = []
    for _ in range(chain_length):
        conf_id = ring_id[:-2]
        ring_id = ring_id[-4:] + ring_id[:-4]
        chains.append(conf_id)
    return sorted(chains, reverse=True)
