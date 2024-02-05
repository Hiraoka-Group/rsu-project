import matplotlib.pyplot as plt
import numpy as np

from chainvisualizer.chain import calc_carbon_positions, calc_metal_positions
from rsuanalyzer.chain import calc_chain_end
from rsuanalyzer.conf_id import conf_id_to_lig_and_con_types


def visualize_chain(conf_id: str, theta: float, delta_: float, show_lig_type: bool = True):
    ORIGIN = [0, 0, 0]
    lig_types, con_types = conf_id_to_lig_and_con_types(conf_id)

    x_of_chain_end, _ = calc_chain_end(conf_id, theta, delta_)
    dist = np.linalg.norm(x_of_chain_end)

    metal_positions = calc_metal_positions(conf_id, theta, delta_)
    frags_of_ligs = calc_carbon_positions(conf_id, theta, delta_)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Draw the line from the origin to the chain end.
    ax.plot(
        *([ORIGIN[i], x_of_chain_end[i]] for i in range(3)),
        c='#666', linestyle='dashed', linewidth=0.5, marker='o', 
        markersize=3)
    
    mid_point = [(ORIGIN[i] + x_of_chain_end[i]) / 2 for i in range(3)]
    ax.text(
        *mid_point, f"dist: {dist:.2f}", color='#444', ha='center', 
        va='center')
    
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#17becf']
    
    for i, metal_atom_position in enumerate(metal_positions):
        offset = 0.1
        ax.text(metal_atom_position[0] + offset, metal_atom_position[1] + offset, metal_atom_position[2] + offset, i+1, color='orange')
        ax.scatter(metal_atom_position[0], metal_atom_position[1], metal_atom_position[2], c='orange', marker='o')
    
    for i, (frags, lig_type) in enumerate(zip(frags_of_ligs, lig_types)):
        for j, carbon_positions in enumerate(frags):
            carbon_pos_array = np.array(carbon_positions)

            color = colors[i % len(colors)]
            ax.plot(carbon_pos_array[:, 0], carbon_pos_array[:, 1], carbon_pos_array[:, 2], c=color)
            
            if show_lig_type:
                if j == 3:
                    text_pos = [(carbon_pos_array[0, k] + carbon_pos_array[-1, k]) / 2 for k in range(3)]
                    ax.text(*text_pos, lig_type[0], color=color, ha='center', va='center')
                elif j == 4:
                    text_pos = [(carbon_pos_array[0, k] + carbon_pos_array[-1, k]) / 2 for k in range(3)]
                    ax.text(*text_pos, lig_type[1], color=color, ha='center', va='center')
    
    # Set the aspect ratio of the plot axes
    ax.set_box_aspect([1, 1, 1])
    
    # Adjust axis limits if width is less than 3 for all axes
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    z_min, z_max = ax.get_zlim()
    if x_max - x_min < 3 and y_max - y_min < 3 and z_max - z_min < 3:
        ax.set_xlim(x_min - (3 - (x_max - x_min)) / 2, x_max + (3 - (x_max - x_min)) / 2)
        ax.set_ylim(y_min - (3 - (y_max - y_min)) / 2, y_max + (3 - (y_max - y_min)) / 2)
        ax.set_zlim(z_min - (3 - (z_max - z_min)) / 2, z_max + (3 - (z_max - z_min)) / 2)
    
    plt.show()


if __name__ == "__main__":
    visualize_chain("RRFFRLBFLL", 30, 90)