import pandas as pd
import rsuanalyzer as ra


def main():
    rings = [
        # (name, theta, description)
        ("syn-T-1", "RLFFRLFFRLFF", 0, 
            "three membered ring in Pd6L4 (L=1)"),
        ("1,3-alt-S", "RRFFRRBBRRFFRRBB", 0, 
            "four membered ring in Pd6L4 (L=1)"),
        ("syn-T-1", "RLFFRLFFRLFF", 34, 
            "three membered ring in Pd9L6 (L=2)"),
        ("syn-S-2", "RRFBRLBBRRFBRLBB", 30, 
            "four membered ring in Pd9L6 (L=2)"),
        ("syn-S-1", "RRFFLLBBRRFFLLBB", 38, 
            "four membered ring in Pd12L8 (L=2)"),
    ]

    df = pd.DataFrame(columns=["name", "ring_id", "theta", "rsu", "description"])
    for name, ring_id, theta, description in rings:
        rsu = ra.calc_rsu(ring_id, theta)
        df.loc[len(df)] = [name, ring_id, theta, f"{rsu:.3f}", description]
    
    df.to_csv("script3.csv", index=False)


if __name__ == "__main__":
    main()
