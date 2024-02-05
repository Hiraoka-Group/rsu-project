import matplotlib.pyplot as plt
import numpy as np

from chainvisualizer.chain import calc_carbon_positions, calc_metal_positions
from chainvisualizer.utils import limit_axis, transpose_to_xyz
from rsuanalyzer.chain import calc_chain_end
from rsuanalyzer.conf_id import conf_id_to_lig_and_con_types

CONF_ID = "RRFFRLBFLL"
THETA = 30
DELTA = 90

metal_positions = calc_metal_positions(CONF_ID, THETA, DELTA)
frags_of_ligs = calc_carbon_positions(CONF_ID, THETA, DELTA)

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
        ax.plot(*transpose_to_xyz(frag), c=lig_colors)

# View settings
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
limit_axis(ax, 3)

plt.show()