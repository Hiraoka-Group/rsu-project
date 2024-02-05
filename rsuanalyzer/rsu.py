import numpy as np

from .chain import calc_chain_end_dist
from .conf_id import ring_to_chains


def calc_rsu(
        conf_id_of_ring: str, theta: float, delta_: float
        ) -> float:
    """
    Calculate the "Ring Strain per Unit" (RSU) for a ring.

    Args:
    - conf_id_of_ring (str): The conformation ID of the ring. 
      This should contain the same number of connection types as the 
      number of ligands in the ring. For example, for a 2-membered ring, 
      it would be "RRFFRLFF". Note that for a chain, the 
      conformation ID would contain n-1 connection types for a chain of 
      n ligands (e.g. "RRFFRL").
    - theta (float): Tilting angles in ligands in degrees.
    - delta_ (float): N-Pd-N angles in degrees.

    Returns:
    - float: The calculated RSU. This is the average chain end distance 
      divided by the chain length.
    """
    # Validate the input.
    if len(conf_id_of_ring) % 4 != 0:
        raise ValueError(
            "The length of the conformation ID of the ring should be a "
            "multiple of 4.")
    
    chain_length = len(conf_id_of_ring) // 4
    conf_ids = ring_to_chains(conf_id_of_ring)

    ave_chain_end_dist = sum(
        calc_chain_end_dist(conf_id, theta, delta_) 
        for conf_id in conf_ids) / chain_length

    return ave_chain_end_dist / chain_length


