"""This module is for visually testing the chainvisualizer.lig module.

Just run this module to check if the ligand fragments are being visualized correctly."""

import matplotlib.pyplot as plt

from rsuanalyzer.src.visualize_chain.ligand import \
    calc_c_positions_of_frags_in_lig


def main():
    LIG_TYPE = "LL"
    THETA = 0

    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    frags = calc_c_positions_of_frags_in_lig(LIG_TYPE, THETA)
    for frag in frags:
        xs = [vtx[0] for vtx in frag]
        ys = [vtx[1] for vtx in frag]
        zs = [vtx[2] for vtx in frag]
        ax.plot(xs, ys, zs)

    ax.set_title(f"ligand type: {LIG_TYPE}, theta: {THETA}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(-.2, 1.8)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_box_aspect([1, 1, 1])

    ax.view_init(20, -160, 0)
    plt.show()


if __name__ == "__main__":
    main()
