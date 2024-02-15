import os

from rsuanalyzer.src.analyze_rsu.make_rank_table import make_rank_table


def main():
    NUM_LIGS = 4
    THETA = 38
    DELTA = 87
    TOPNUM = 10

    OUTPUT_FOLDER = "analysis/rank_for_specific_num_ligs_and_theta/output"


    input_path = f"analysis/enum_ring_groups/output/groups (num_ligs={NUM_LIGS}).txt"

    with open(input_path, "r") as f:
        groups = f.read().splitlines()

    rank_table = make_rank_table(groups, THETA, DELTA, TOPNUM)

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    filename = f"rank (num={NUM_LIGS}, theta={THETA}, delta={DELTA}).csv"
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    rank_table.to_csv(output_path, index=False)
    print(f"Saved the rank table to '{output_path}'")


if __name__ == "__main__":
    main()
