import numpy as np


def logTransform(data):
    data = data.copy()
    for col in ["Typing Speed", "Avg Hold Time", "Avg Keystroke Latency",
                "Max Digraph Duration", "Avg Inter-Release Latency", "Max Inter-Release Latency"]:
        if col in data.columns:
            min_val = data[col].min()
            if min_val <= 0:
                data[col] = np.log1p(data[col] - min_val + 1)
            else:
                data[col] = np.log1p(data[col])
    return data