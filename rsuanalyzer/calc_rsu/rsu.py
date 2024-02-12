"""Calculate the "Ring Strain per Unit" (RSU) for a ring."""

from .chain import calc_chain_end_dist


def calc_rsu(
        conf_id_of_ring: str, theta: float, delta_: float
        ) -> float:
    """Calculate the "Ring Strain per Unit" (RSU) for a ring.
    
    RSU is a measure of the strain of a ring. It is calculated as the
    [average distance]/[number of chains] where the average distance
    is the average of the distances between the ends of the chains
    derived from the ring by cutting at different points. For more
    details, see the associated paper.

    Args:
        conf_id_of_ring (str): 
            Conformation ID of the ring. e.g., "RRFFLLBB".
        theta (float): 
            Tilting angle of the two C-C bonds in the ligand
            in degrees. 0 <= theta <= 90.
        delta_ (float): 
            Angle in degrees. 0 < delta\_ <= 180.
        
    Returns:
        float: The RSU for the ring.
    """
    # Validate the input.
    if len(conf_id_of_ring) % 4 != 0:
        raise ValueError(
            "The length of the conformation ID of the ring should " + 
            "be a multiple of 4.")
    
    chain_length = len(conf_id_of_ring) // 4
    conf_ids = _ring_id_to_chain_ids(conf_id_of_ring)

    ave_chain_end_dist = sum(
        calc_chain_end_dist(conf_id, theta, delta_) 
        for conf_id in conf_ids) / chain_length

    return ave_chain_end_dist / chain_length


def _ring_id_to_chain_ids(conf_id_of_ring: str) -> list[str]:
    """Return the list of conformation IDs of chains derived from the
    ring by cutting at different points.
    
    Args:
        conf_id_of_ring (str): 
            Conformation ID of the ring. e.g., "RRFFLLBB".

    Returns:
        list[str]: The list of conformation IDs of chains.
    
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
