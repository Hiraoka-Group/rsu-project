"""
Visualize the chain of a syn-S-1 with theta=38 and delta=87, 
which is the Pd4L4 structure in Pd12L8 cage measured by X-ray 
crystallography.
"""

import matplotlib.pyplot as plt

from chainvisualizer.chain import calc_carbon_positions, calc_metal_positions
from chainvisualizer.utils import limit_axis, transpose_to_xyz

CONF_ID = "RRFFLLBBRRFFLLBB"  # syn-S-1
THETA = 38  # by X-ray crystallography
DELTA = 87

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
ax.view_init(20, -160, 0)  # (elevation, azimuth, rotate by z-axis)

plt.show()