import numpy as np

from ._conf_id import _list_chains_derived_from_the_ring
from ._global_vecs_rots import _calc_chain_end


def calc_rsu(
        conf_id_of_ring: str, theta: float, delta_: float
        ) -> float:
    """Calculate the "Ring Strain per Unit" (RSU) for a ring.

    RSU is a measure of the strain of a ring. It is calculated as the
    [average distance]/[number of chains] where the average distance
    is the average of the distances between the ends of the chains
    derived from the ring by cutting at different points. 

    Consider the ring "RRFFLLBBRLFB". When cutting at different points,
    we get the following chains: "RRFFLLBBRL", "LLBBRLFBRR", and
    "RLFBRRFFLL". If we call the end distances of these chains
    d1, d2, and d3, the average of d1, d2, and d3 is (d1 + d2 + d3) / 3,
    therefore, the RSU of the ring is (d1 + d2 + d3) / 3 / 3. The last
    division by 3 is because the definition of RSU is the average
    distance *per unit*.

    Args:
        conf_id_of_ring (str): 
            Conformation ID of the ring. e.g., "RRFFLLBB".
        theta (float): 
            Tilting angle of the two C-C bonds in the ligand
            in degrees. 0 <= theta <= 90.
        delta_ (float): 
            N-Pd-N angle in degrees. 0 < delta\_ <= 180.

    Returns:
        float: The RSU for the ring.
    """
    # Validate the input.
    if len(conf_id_of_ring) % 4 != 0:
        raise ValueError(
            "The length of the conformation ID of the ring should " +
            "be a multiple of 4.")

    chain_length = len(conf_id_of_ring) // 4
    conf_ids = _list_chains_derived_from_the_ring(conf_id_of_ring)

    ave_chain_end_dist = sum(
        _calc_chain_end_dist(conf_id, theta, delta_)
        for conf_id in conf_ids) / chain_length

    return ave_chain_end_dist / chain_length


def _calc_chain_end_dist(
        conf_id: str, theta: float, delta_: float
        ) -> float:
    """Calculate the distance between the two ends of the chain.

    Args:
        conf_id (str): Conformation ID of the chain, e.g., "RRFFRL".
        theta (float): Tilting angle of the two C-C bonds in the ligand
            in degrees. 0 <= theta <= 90.
        delta_ (float): Angle in degrees. 0 < delta\_ <= 180.

    Returns:
        float: The distance between the two ends of the chain.
    """
    # x is the position vector of the end of the last ligand measured
    # from the global coordinate system.
    x, _ = _calc_chain_end(conf_id, theta, delta_)

    # Since the position of the other end is (0, 0, 0) in the global
    # coordinate system, the distance between the two ends is the
    # norm of x.
    return np.linalg.norm(x)
