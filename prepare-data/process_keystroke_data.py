import numpy as np
import pandas as pd
from joblib import Parallel, delayed 

data = pd.read_csv("/content/drive/MyDrive/keystroke_data.csv")
print("Data reading completed")

#Convert columns of press time and release time to numeric, coerce errors and drop the invalid rows
data['press_time'] = pd.to_numeric(data['press_time'], errors='coerce')
data['release_time'] = pd.to_numeric(data['release_time'], errors='coerce')
data = data.dropna(subset=['press_time', 'release_time'])
data['key_used'] = data['key_used'].astype(str)

df_grouped = data.groupby("participant_id")


def process_group(participant_id, group):
    print("Processing...")
    start_time = group['press_time'].iloc[0]
    finish_time = group['release_time'].iloc[-1]
    typing_speed = (finish_time - start_time) / len(group)

    backspace_count = (group['key_used'] == "BKSP").sum()

    group['hold_time'] = group['release_time'] - group['press_time']
    avg_hold_time = group['hold_time'].mean()
    max_hold_time = group['hold_time'].max()
    min_hold_time = group['hold_time'].min()

    group['keystroke_latency'] = group['press_time'].diff()
    avg_keystroke_latency = group['keystroke_latency'].mean()
    max_keystroke_latency = group['keystroke_latency'].max()
    min_keystroke_latency = group['keystroke_latency'].min()

    group['digraph_duration'] = group['press_time'] - group['release_time'].shift()
    avg_digraph_duration = group['digraph_duration'].mean()
    max_digraph_duration = group['digraph_duration'].max()
    min_digraph_duration = group['digraph_duration'].min()

    group['inter_release_latency'] = group['release_time'].diff()
    avg_inter_release_latency = group['inter_release_latency'].mean()
    max_inter_release_latency = group['inter_release_latency'].max()
    min_inter_release_latency = group['inter_release_latency'].min()

    return {
        "Typing Speed": typing_speed,
        "No of Backspaces": backspace_count,
        "Avg Hold Time": avg_hold_time,
        "Max Hold Time": max_hold_time,
        "Min Hold Time": min_hold_time,
        "Avg Keystroke Latency": avg_keystroke_latency,
        "Max Keystroke Latency": max_keystroke_latency,
        "Min Keystroke Latency": min_keystroke_latency,
        "Avg Digraph Duration": avg_digraph_duration,
        "Max Digraph Duration": max_digraph_duration,
        "Min Digraph Duration": min_digraph_duration,
        "Avg Inter-Release Latency": avg_inter_release_latency,
        "Max Inter-Release Latency": max_inter_release_latency,
        "Min Inter-Release Latency": min_inter_release_latency,
        "output_label": 1  
    }


results = Parallel(n_jobs=-1)(delayed(process_group)(pid, grp) for pid, grp in df_grouped)
humans_data_df = pd.DataFrame(results)
print(humans_data_df.head())
print("Size of humans_data_df:", len(humans_data_df))
humans_data_df.to_csv("keystroke_data_processed_human.csv", index=False)

