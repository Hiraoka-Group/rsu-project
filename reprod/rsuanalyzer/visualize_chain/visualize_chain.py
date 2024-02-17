import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D

from ._utils import _limit_axis, _transpose_to_xyz
from .carbons import calc_carbon_positions
from .metals import calc_metal_positions


def visualize_chain(
        conf_id: str, theta: float, delta_: float = 87,
        show: bool = True
        ) -> tuple[Figure, Axes3D]:
    """Visualize the structure of a chain.

    You can either show the plot or get the figure and the axes object.
    The latter is useful when you want to customize the plot. 
    (See Example)

    Caution:
        This function is intended to provide an approximate visualization
        of the chain structure. It may not accurately represent the precise
        positions of the atoms.

    Args:
        conf_id (str):
            The conformation ID of the chain, e.g. "RLFFRLFFRL".
            Ring ID (e.g. "RLFFRLFFRLFF") is also acceptable, 
            but the last two characters will be ignored.
        theta (float):
            The tilt angle of the C-C bonds in degrees.
        delta_ (float, optional):
            The N-Pd-N angle in degrees. Default is 87.
        show (bool, optional):
            If True, the plot will be shown. Default is True.
            Set False if you just want to get the figure and the axes object.

    Returns:
        tuple[Figure, Axes3D]:
            A tuple of the figure and the 3D axes object.
    
    Example:
        Case 1:
            Plot the structure of a chain.
            
            >>> import rsuanalyzer as ra
            >>> ra.visualize_chain("RLFFRLFFRLFF", 34)
        
        Case 2:
            Get the figure and the axes object.
            This is useful when you want to customize the plot.

            >>> import matplotlib.pyplot as plt
            >>> import rsuanalyzer as ra
            >>> fig, ax = ra.visualize_chain("RLFFRLFFRLFF", 34, show=False)
            >>> ax.set_title("syn-T-1, theta=34, delta=87")
            >>> plt.show()
    """
    metal_positions = calc_metal_positions(conf_id, theta, delta_)
    frags_of_ligs = calc_carbon_positions(conf_id, theta, delta_)

    # Make a 3D plot
    fig, ax = plt.subplots(
        figsize=(6, 6), subplot_kw={'projection': '3d'})

    # Scatter the metal positions and label them
    for i, metal_pos in enumerate(metal_positions):
        ax.scatter(*metal_pos, c='orange', marker='o')
        ax.text(*metal_pos, f"{i+1}", color='orange')

    # Plot the ligands
    lig_colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#17becf']
    for lig, lig_colors in zip(frags_of_ligs, lig_colors):
        for frag in lig:
            ax.plot(*_transpose_to_xyz(frag), c=lig_colors)

    # View settings
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    _limit_axis(ax, 3)
    ax.view_init(20, -160, 0)  # (elevation, azimuth, rotate by z-axis)

    if show:
        # Show the plot
        plt.show()

    return fig, ax
