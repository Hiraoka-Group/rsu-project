"""
Calculate the RSU for the syn-S-1 conformation with delta=87 for different
tilting angles (theta) and save the result to a CSV file.
"""

import os

import pandas as pd

from rsuanalyzer.rsu import calc_rsu

CONF_ID_OF_RING = "RR(FF)LL(BB)RR(FF)LL(BB)"
THETAS = range(0, 91, 1)
DELTA_ = 87

df = pd.DataFrame({
    "theta": THETAS,
    "rsu": [calc_rsu(CONF_ID_OF_RING, theta, DELTA_) for theta in THETAS]
    })

OUTPUT_FOLDER = "analysis/data/rsu_vs_theta/"
OUTPUT_FILENAME = "syn-S-1 (delta=87).csv"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

df.to_csv(OUTPUT_FOLDER + OUTPUT_FILENAME, index=False)
print(f"Saved to {OUTPUT_FOLDER + OUTPUT_FILENAME}")