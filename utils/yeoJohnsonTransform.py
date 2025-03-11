import numpy as np
import pandas as pd
from scipy.stats import yeojohnson


def yeoJohnsonTransform(data):
    data = data.copy()
    for col in ["Avg Digraph Duration", "Min Hold Time"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
            data[col].replace([np.inf, -np.inf], np.nan, inplace=True)

            if data[col].isna().sum() == len(data[col]):
                print(f"Skipping column {col}, all values are NaN after cleanup")
                continue
            data[col].fillna(data[col].median(), inplace=True)
            data[col], _ = yeojohnson(data[col])
    return data