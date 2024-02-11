import os

from rsuanalyzer.analyze_rsu.min_rsu import calc_min_rsu_for_thetas

NUM_LIGS = 2
THETA_STEP = 10
THETAS = list(range(0, 91, THETA_STEP))
DELTA = 87

OUTPUT_FOLDER = "analysis/min_rsu_for_specific_num_ligs/output"

input_path = f"analysis/enum_ring_groups/output/groups (num_ligs={NUM_LIGS}).txt"

with open(input_path, "r") as f:
    groups = f.read().splitlines()

min_rsu_table = calc_min_rsu_for_thetas(groups, THETAS, DELTA)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

filename = f"min_rsu (num={NUM_LIGS}, theta_step={THETA_STEP}, delta={DELTA}).csv"
output_path = os.path.join(OUTPUT_FOLDER, filename)
min_rsu_table.to_csv(output_path, index=False)
print(f"Saved the min RSU table to '{output_path}'")
