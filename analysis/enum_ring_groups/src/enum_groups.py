import os

from rsuanalyzer.ranker.enum_groups import (enum_all_rings,
                                            enum_groups_from_rings)

OUTPUT_FOLDER = "analysis/enum_ring_groups/output"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

for num_of_ligs in range(1, 5):
    rings = enum_all_rings(num_of_ligs)
    groups = enum_groups_from_rings(rings)

    filename = f"groups (num_ligs={num_of_ligs}).txt"
    
    with open(f"{OUTPUT_FOLDER}/{filename}", "w") as f:
        f.write("\n".join(groups))
    print(f"Saved '{filename}' to {OUTPUT_FOLDER}.")