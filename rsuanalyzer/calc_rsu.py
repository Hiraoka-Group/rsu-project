import numpy as np

from .calc_chain_end import calc_chain_end


def calc_chain_end_dist(
        conf_id: str, theta: float, delta_: float
        ) -> float:
    x, _ = calc_chain_end(conf_id, theta, delta_)
    return np.linalg.norm(x)


def calc_rsu(
        conf_id_of_ring: str, theta: float, delta_: float
        ) -> float:
    """
    Calculate the "Ring Strain per Unit" (RSU) for a ring.

    Args:
    - conf_id_of_ring (str): The conformation ID of the ring. 
      This should contain the same number of connection types as the 
      number of ligands in the ring. For example, for a 2-membered ring, 
      it would be "RR(FF)RL(FF)". Note that for a chain, the 
      conformation ID would contain n-1 connection types for a chain of 
      n ligands (e.g. "RR(FF)RL").
      With and without brackets are both acceptable.
    - theta (float): Tilting angles in ligands in degrees.
    - delta_ (float): N-Pd-N angles in degrees.

    Returns:
    - float: The calculated RSU. This is the average chain end distance 
      divided by the chain length.
    """
    conf_id_of_ring = conf_id_of_ring.replace("(", "").replace(")", "")
    chain_length = len(conf_id_of_ring) // 4
    conf_ids = ring_to_chains(conf_id_of_ring)

    ave_chain_end_dist = sum(
        calc_chain_end_dist(conf_id, theta, delta_) 
        for conf_id in conf_ids) / chain_length

    return ave_chain_end_dist / chain_length


def ring_to_chains(conf_id_of_ring: str) -> list[str]:
    """
    Convert the conformation ID of a ring to the conformation IDs of
    the chains.

    Args:
    - conf_id_of_ring (str): The conformation ID of the ring. 
      This should contain the same number of connection types as the 
      number of ligands in the ring. For example, for a 2-membered ring, 
      it would be "RR(FF)RL(FF)". With and without brackets are both
      acceptable.

    Returns:
    - list[str]: The conformation IDs of the chains.

    Examples:
    >>> ring_to_chains("RR(FF)RL(FF)")
    ['RRFFRL', 'RLFFRR']
    >>> ring_to_chains("RR(FF)RL(FF)RR(BF)")
    ['RRFFRLFFRR', 'RRBFRRFFRL', 'RLFFRRBFRR']
    """
    conf_id_of_ring = conf_id_of_ring.replace("(", "").replace(")", "")
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