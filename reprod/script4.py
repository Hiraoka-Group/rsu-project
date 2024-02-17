import pandas as pd
from focused_rings import NAME_TO_ID

import rsuanalyzer as ra


def main():
    rings = [
        # (name, delta, description)
        (
            "syn-S-1", 103, 
            "four membered ring in Pd12L8 (L=2), but with a delta in Zn12L8"),
        (
            "syn-S-3", 103, 
            "four membered ring in Zn12L8"),
    ]

    thetas = range(0, 91, 1)
    df = pd.DataFrame({"theta": thetas})
    for name, delta, description in rings:
        ring_id = NAME_TO_ID[name]
        df_ = ra.create_rsu_vs_theta_df(ring_id, delta_=delta, thetas=thetas)
        df = pd.concat([df, df_["RSU"]], axis=1)
        df = df.rename(columns={"RSU": f"{name} (delta={delta})"})

    ra.plot_rsu_vs_theta(df)        
        


if __name__ == "__main__":
    main()
