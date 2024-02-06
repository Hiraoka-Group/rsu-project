"""
Calculate the RSU for the syn-T-1 conformation with delta=90 for different
tilting angles (theta) and save the result to a CSV file.
"""

import os

import pandas as pd

from rsuanalyzer.core.rsu import calc_rsu

CONF_ID_OF_RING = "RLFFRLFFRLFF"
THETAS = range(0, 91, 1)
DELTA_ = 90

df = pd.DataFrame({
    "theta": THETAS,
    "rsu": [calc_rsu(CONF_ID_OF_RING, theta, DELTA_) for theta in THETAS]
    })

OUTPUT_FOLDER = "analysis/rsu_vs_theta_for_specific_ring/output/"
OUTPUT_FILENAME = "syn-T-1 (delta=90).csv"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

df.to_csv(OUTPUT_FOLDER + OUTPUT_FILENAME, index=False)
print(f"Saved to {OUTPUT_FOLDER + OUTPUT_FILENAME}")