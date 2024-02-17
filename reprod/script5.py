import rsuanalyzer as ra


def main():
    df_syns2 = ra.create_rsu_vs_theta_df("RRFBRLBBRRFBRLBB")
    df_syns1 = ra.create_rsu_vs_theta_df("RRFFLLBBRRFFLLBB")
    df_synt1 = ra.create_rsu_vs_theta_df("RLFFRLFFRLFF")

    dimeric_rings = ra.enum_ring_ids(2)
    df_dimeric = ra.create_min_rsu_vs_theta_df(dimeric_rings)

    ra.plot_rsu_vs_theta(
        df_syns2, df_syns1, df_synt1, df_dimeric,
        labels=["syn-S-2", "syn-S-1", "syn-T-1", "min of dimeric rings"]
        )


if __name__ == "__main__":
    main()
