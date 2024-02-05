from dataclasses import dataclass

from rsuanalyzer.rsu import calc_rsu


@dataclass
class Structure:
    name: str
    conf_id: str
    theta: float
    delta_: float

structures = [
    Structure("syn_T_1_theta_0", "RL(FF)RL(FF)RL(FF)", 0, 87),
    Structure("alt_S_theta_0", "RR(FF)RR(BB)RR(FF)RR(BB)", 0, 87),
    Structure("syn_T_1_theta_34", "RL(FF)RL(FF)RL(FF)", 34, 87),
    Structure("syn_S_2_theta_30", "RR(FB)RL(BB)RR(FB)RL(BB)", 30, 87),
    Structure("syn_S_1_theta_38", "RR(FF)LL(BB)RR(FF)LL(BB)", 38, 87),
]

for structure in structures:
    result = calc_rsu(structure.conf_id, structure.theta, structure.delta_)
    print(f"{structure.name}: RSU = {result:.3f}")