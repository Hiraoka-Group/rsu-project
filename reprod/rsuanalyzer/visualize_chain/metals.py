import numpy as np

from ..core._global_vecs_rots import _calc_global_lig_ends_in_chain


def calc_metal_positions(
        conf_id: str, theta: float, delta_: float = 87
        ) -> list[np.ndarray]:
    """Calculate the positions of the metal atoms in a chain.

    Caution:
        This function is intended to provide an approximate 
        visualization of the chain structure. It may not accurately 
        represent the precise positions of the atoms.

    Note:
        You can use `rsuanalyzer.visualize_chain` to visualize chains
        more easily.

    Args:
        conf_id (str): 
            The conformation ID of the chain, e.g. "RLFFRLFFRL".
        theta (float): 
            The tilt angle of the C-C bonds in degrees.
        delta_ (float, optional): 
            The N-Pd-N angle in degrees. Default is 87.

    Returns:
        list[np.ndarray]: 
            A list of numpy arrays representing the
            positions of the metal atoms in the global coordinate system.

    Example:
        >>> import matplotlib.pyplot as plt
        >>> import rsuanalyzer as ra
        >>> fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        >>> metal_positions = ra.calc_metal_positions("RLFFRLFFRL", 34)
        >>> xs = [vtx[0] for vtx in metal_positions]
        >>> ys = [vtx[1] for vtx in metal_positions]
        >>> zs = [vtx[2] for vtx in metal_positions]
        >>> ax.scatter(xs, ys, zs)
        >>> ax.set_xlim(-.2, 1.8)
        >>> ax.set_ylim(-.25, 1.75)
        >>> ax.set_zlim(-1, 1)
        >>> ax.set_box_aspect([1, 1, 1])
        >>> plt.show()
    """
    # The first metal atom is at the origin of the global coordinate system.
    metal_positions = [np.array([0, 0, 0])]

    # global_lig_ends: [(x1, rot1), (x2, rot2), ...]
    #   x (np.ndarray): position of the end of the ligand in the 
    #       global coordinate system.
    #   rot (np.ndarray): rotation matrix from the global coordinate 
    #       system to the local coordinate system C.
    global_lig_ends = _calc_global_lig_ends_in_chain(
        conf_id, theta, delta_)
    for global_lig_end in global_lig_ends:
        global_x, _ = global_lig_end
        metal_positions.append(global_x)
    return metal_positions
