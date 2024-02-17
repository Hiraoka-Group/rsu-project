import rsuanalyzer as ra


def main():
    thetas = range(0, 91, 1)
    
    df1 = ra.create_rsu_vs_theta_df(
        "RRFFLLBBRRFFLLBB", delta_=103)  # syn-S-1, delta=103
    df2 = ra.create_rsu_vs_theta_df(
        "RRFFLRFBRRFFLLBB", delta_=103)  # syn-S-3, delta=103

    ra.plot_rsu_vs_theta(df1, df2, labels=[
        "syn-S-1 (delta=103)", "syn-S-3 (delta=103)"])


if __name__ == "__main__":
    main()
