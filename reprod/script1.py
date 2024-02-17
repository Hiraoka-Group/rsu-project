import pandas as pd
from focused_rings import NAME_TO_ID

import rsuanalyzer as ra


def main():
    df1 = ra.create_rsu_vs_theta_df(
        NAME_TO_ID["syn-S-1"], delta_=87)  # syn-S-1, delta=87
    df2 = ra.create_rsu_vs_theta_df(
        NAME_TO_ID["syn-S-1"], delta_=90)  # syn-S-1, delta=90

    df_con = pd.concat(
        [df1["theta"], df1["RSU"], df2["RSU"]], axis=1)
    df_con = df_con.set_axis(
        ["theta", "syn-S-1 (delta=87)", "syn-S-1 (delta=90)"],
        axis="columns", copy=False)

    ra.plot_rsu_vs_theta(df_con)


if __name__ == "__main__":
    main()
