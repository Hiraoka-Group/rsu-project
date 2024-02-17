import rsuanalyzer as ra


def main():
    df1 = ra.create_rsu_vs_theta_df(
        "RRFBRLBBRRFBRLBB", delta_=87)  # syn-S-2, delta=87
    df2 = ra.create_rsu_vs_theta_df(
        "RRFBRLBBRRFBRLBB", delta_=90)  # syn-S-2, delta=90
    df3 = ra.create_rsu_vs_theta_df(
        "RLFFRLFFRLFF", delta_=87)  # syn-T-1, delta=87
    df4 = ra.create_rsu_vs_theta_df(
        "RLFFRLFFRLFF", delta_=90)  # syn-T-1, delta=90

    ra.plot_rsu_vs_theta(df1, df2, df3, df4, labels=[
        "syn-S-2 (delta=87)", "syn-S-2 (delta=90)",
        "syn-T-1 (delta=87)", "syn-T-1 (delta=90)"])


if __name__ == "__main__":
    main()
