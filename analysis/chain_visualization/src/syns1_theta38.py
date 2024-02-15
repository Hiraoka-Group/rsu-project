"""
Visualize the chain of a syn-S-1 with theta=38 and delta=87.
Note that the depicted positions of C atoms provide a general 
representation rather than an exact depiction. In the context 
of the RSU analysis, only the positions of the metal atoms are crucial.
"""

import matplotlib.pyplot as plt

from regen_results.src.lib.utils import _limit_axis, _transpose_to_xyz
from rsuanalyzer.src.visualize_chain.chain import (calc_carbon_positions,
                                                   calc_metal_positions)


def main():
    NAME = "syn-S-1"
    CONF_ID = "RR(FF)LL(BB)RR(FF)LL(BB)"
    THETA = 38
    DELTA = 87

    conf_id_without_brackets = CONF_ID.replace("(", "").replace(")", "")
    metal_positions = calc_metal_positions(conf_id_without_brackets, THETA, DELTA)
    frags_of_ligs = calc_carbon_positions(conf_id_without_brackets, THETA, DELTA)

    # Make a 3D plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': '3d'})

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

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
