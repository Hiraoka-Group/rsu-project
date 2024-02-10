import os

from rsuanalyzer.ranker.enum_conf_ids import (enum_conf_ids_including_dups,
                                              exclude_duplicates)

THETA = 30
OUTPUT_FOLDER = "analysis/enum_ring_groups/output"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

for num_of_ligs in range(1, 5):
    rings = enum_conf_ids_including_dups(num_of_ligs)
    groups = exclude_duplicates(rings, THETA)

    filename = f"groups (num_ligs={num_of_ligs}).txt"
    
    with open(f"{OUTPUT_FOLDER}/{filename}", "w") as f:
        f.write("\n".join(sorted(groups)))
    print(f"Saved '{filename}' to {OUTPUT_FOLDER}.")