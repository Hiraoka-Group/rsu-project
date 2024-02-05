import os
from dataclasses import dataclass

from rsuanalyzer.rsu import calc_rsu


@dataclass
class Structure:
    name: str
    conf_id: str
    theta: float
    delta_: float

structures = [
    Structure("syn-T-1", "RL(FF)RL(FF)RL(FF)", 0, 87),
    Structure("1,3-alt-S", "RR(FF)RR(BB)RR(FF)RR(BB)", 0, 87),
    Structure("syn-T-1", "RL(FF)RL(FF)RL(FF)", 34, 87),
    Structure("syn-S-2", "RR(FB)RL(BB)RR(FB)RL(BB)", 30, 87),
    Structure("syn-S-1", "RR(FF)LL(BB)RR(FF)LL(BB)", 38, 87),
    ]

OUTPUT_DIR = "analysis/rsu_analysis/rsu_of_specific_rings/output/"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


for structure in structures:
    conf_id_without_brackets = \
        structure.conf_id.replace("(", "").replace(")", "")
    rsu = calc_rsu(
        conf_id_without_brackets, structure.theta, structure.delta_)
        
    filename = f"{structure.name} (theta={structure.theta}, "\
        f"delta={structure.delta_}).txt"
    
    report_text = "# INPUT\n"\
        f"Name            : {structure.name}\n"\
        f"Conformation ID : {structure.conf_id}\n"\
        f"Theta /deg.     : {structure.theta}\n"\
        f"Delta /deg.     : {structure.delta_}\n"\
        "\n"\
        "# OUTPUT\n"\
        f"Calculated RSU  : {rsu}"\
    
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(report_text)
    print(f"Saved to '{filename}'")