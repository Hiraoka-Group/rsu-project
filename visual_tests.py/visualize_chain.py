import matplotlib.pyplot as plt
import numpy as np

from chainvisualizer.chain import calc_carbon_positions, calc_metal_positions
from rsuanalyzer.chain import calc_chain_end


def visualize_chain(conf_id: str, theta: float, delta_: float):
    x_a0 = [0, 0, 0]
    x_c2n, _ = calc_chain_end(conf_id, theta, delta_)

    metal_atom_positions = calc_metal_positions(conf_id, theta, delta_)
    carbon_pos_of_frags_of_all_ligs = calc_carbon_positions(conf_id, theta, delta_)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot([x_a0[0], x_c2n[0]], [x_a0[1], x_c2n[1]], [x_a0[2], x_c2n[2]], 'r')
    
    colors = ['b', 'g', 'y', 'm', 'c']
    
    for i, metal_atom_position in enumerate(metal_atom_positions):
        ax.text(metal_atom_position[0], metal_atom_position[1], metal_atom_position[2], i+1, color='orange')
        ax.scatter(metal_atom_position[0], metal_atom_position[1], metal_atom_position[2], c='orange', marker='o')
    
    for i, carbon_pos_of_frags in enumerate(carbon_pos_of_frags_of_all_ligs):
        for carbon_pos_list in carbon_pos_of_frags:
            carbon_pos_array = np.array(carbon_pos_list)
            ax.plot(carbon_pos_array[:, 0], carbon_pos_array[:, 1], carbon_pos_array[:, 2], c=colors[i % len(colors)])
                
    
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
    visualize_chain("RRFFRL", 30, 90)