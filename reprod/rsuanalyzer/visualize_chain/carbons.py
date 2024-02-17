import numpy as np

from ..core._conf_id import _id_to_con_types, _id_to_lig_types
from ..core._global_vecs_rots import _calc_global_lig_ends_in_chain
from ..core._local_vecs_rots import _rot_ca
from ._ligand import _calc_c_positions_of_frags_in_lig


def calc_carbon_positions(
        conf_id: str, theta: float, delta_: float = 87
        ) -> list[list[list[np.ndarray]]]:
    """Calculate the positions of the carbon atoms in the ligands of a chain.

    This function is intended to be used for visualizing chains with
    matplotlib 3D plots. The calculated positions of the carbon atoms
    are represented in the global coordinate system.

    Note:
        You can use `rsuanalyzer.visualize_chain` to visualize chains
        more easily.

    Caution:
        This function is intended to provide an approximate visualization 
        of the ligand structure. It may not accurately represent the 
        precise positions of the atoms.

    Args:
        conf_id (str): The conformation ID of the chain, e.g. "RRFFLL".
        theta (float): The tilt angle of the C-C bonds in degrees.
        delta_ (float, optional): The N-Pd-N angle in degrees. Default is 87.

    Returns:
        list[list[list[np.ndarray]]]: 
            A list of lists of lists of numpy arrays.
            Each list corresponds to a ligand in the chain. Each inner list 
            corresponds to a fragment of the ligand molecule. The numpy arrays 
            in the innermost lists represent the positions of the carbon atoms 
            in the global coordinate system.

    Example:
        >>> import matplotlib.pyplot as plt
        >>> import rsuanalyzer as ra
        >>> fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        >>> c_positions_of_ligs = ra.calc_carbon_positions("RLFFRLFFRL", 34)
        >>> for lig in c_positions_of_ligs:
        ...     for frag in lig:
        ...         xs = [vtx[0] for vtx in frag]
        ...         ys = [vtx[1] for vtx in frag]
        ...         zs = [vtx[2] for vtx in frag]
        ...         ax.plot(xs, ys, zs)
        >>> ax.set_xlim(-.2, 1.8)
        >>> ax.set_ylim(-.25, 1.75)
        >>> ax.set_zlim(-1, 1)
        >>> ax.set_box_aspect([1, 1, 1])
        >>> plt.show()
    """
    lig_types = _id_to_lig_types(conf_id)  # "RRFFLL" -> ["RR", "LL"]
    con_types = _id_to_con_types(conf_id)  # "RRFFLL" -> ["FF"]

    # global_lig_ends: [(x1, rot1), (x2, rot2), ...]
    #   x (np.ndarray): position of the end of the ligand in the 
    #       global coordinate system.
    #   rot (np.ndarray): rotation matrix from the global coordinate 
    #       system to the local coordinate system C.
    global_lig_ends = _calc_global_lig_ends_in_chain(conf_id, theta, delta_)

    # local_c_positions_of_ligs: [[[np.ndarray, ...], ...], ...]
    #   (list)  > (list) > (list)    > (np.ndarray)
    #   ligands > ligand > fragments > carbon atom positions
    # 
    # Initialize with the carbon positions of the first ligand, since
    # the local coordinate system A of the first ligand is the same as
    # the global coordinate system.
    global_c_positions_of_ligs = [
        _calc_c_positions_of_frags_in_lig(lig_types[0], theta)]

    # Convert the carbon positions of from the local coordinate system 
    # to the global coordinate system.
    for lig_type, con_type, prev_lig_end in zip(
            lig_types[1:], con_types, global_lig_ends[:-1]):
        x_of_prev_lig_end, rot_of_prev_lig_end = prev_lig_end
        rot_ca_ = _rot_ca(con_type, delta_)
        local_carbon_positions = _calc_c_positions_of_frags_in_lig(
            lig_type, theta)

        # Convert the local carbon positions to the global coordinate 
        # system.
        global_carbon_positions = [
            x_of_prev_lig_end
                + (rot_of_prev_lig_end * rot_ca_).apply(carbon_position)
            for carbon_position in local_carbon_positions]

        global_c_positions_of_ligs.append(global_carbon_positions)

    return global_c_positions_of_ligs
