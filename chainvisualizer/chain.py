
import numpy as np

from rsuanalyzer.calc_rsu.chain import calc_con_rot, calc_lig_ends_in_chain
from rsuanalyzer.calc_rsu.conf_id_to_lig_and_con_types import \
    conf_id_to_lig_and_con_types

from .lig import calc_c_positions_of_frags_in_lig


def calc_metal_positions(
        conf_id: str, theta: float, delta_: float
        ) -> list[np.ndarray]:
    metal_positions = [np.array([0, 0, 0])]
    lig_ends = calc_lig_ends_in_chain(conf_id, theta, delta_)
    for lig_end in lig_ends:
        x, rot = lig_end
        metal_positions.append(x)
    return metal_positions


def calc_carbon_positions(conf_id: str, theta: float, delta_: float):
    lig_types, con_types = conf_id_to_lig_and_con_types(conf_id)

    lig_ends = calc_lig_ends_in_chain(conf_id, theta, delta_)
    carbon_positions_of_all_ligs = [calc_c_positions_of_frags_in_lig(lig_types[0], theta)]

    for lig_type, con_type, prev_lig_end in zip(lig_types[1:], con_types, lig_ends[:-1]):
        x_of_prev_lig_end, rot_of_prev_lig_end = prev_lig_end
        con_rot = calc_con_rot(con_type, delta_)
        local_carbon_positions = calc_c_positions_of_frags_in_lig(lig_type, theta)
        carbon_positions = [
            x_of_prev_lig_end \
                + (rot_of_prev_lig_end * con_rot).apply(carbon_position) 
            for carbon_position in local_carbon_positions]

        carbon_positions_of_all_ligs.append(carbon_positions)
        
    return carbon_positions_of_all_ligs
    