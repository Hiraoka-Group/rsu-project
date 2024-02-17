import rsuanalyzer as ra


def main():
    df1 = ra.create_rsu_vs_theta_df(
        "RRFFLLBBRRFFLLBB", delta_=87)  # syn-S-1, delta=87
    df2 = ra.create_rsu_vs_theta_df(
        "RRFFLLBBRRFFLLBB", delta_=90)  # syn-S-1, delta=90

    ra.plot_rsu_vs_theta(
        df1, df2, labels=["syn-S-1 (delta=87)", "syn-S-1 (delta=90)"])


if __name__ == "__main__":
    main()
