import numpy as np
import pandas as pd

data = pd.read_csv("/content/drive/MyDrive/IdentifyTrueDataset/keystroke_data.csv")

print(data.head(1000))

df_grouped = data.groupby("participant_id")
print(df_grouped.head(5))

humans_data = []
for participant_id, group in df_grouped:
    backspace_count = 0
    typingSpeed = 0
    avgKeyStrokeLatency = 0
    avgDiGraphDuration = 0
    avgHoldTime = 0
    avgInterReleaseLatency = 0
    maxKeyStrokeLatency = 0
    maxDiGraphDuration = 0
    maxHoldTime = 0
    maxInterReleaseLatency = 0
    minKeyStrokeLatency = 0
    minDiGraphDuration = 0
    minHoldTime = 0
    minInterReleaseLatency = 0

    holdTimeAll = []
    keyStrokeLatencyAll = []
    digraphDurationAll = []
    interReleaseLatencyAll = []

    len_group = 0
    # print("Group is : ", group)

    start_time = 0
    finish_time = 0

    for idx, row in enumerate(group.itertuples()):
        len_group = len(group)
        # print(f"Index is: {idx}")
        if(row.key_used == "BKSP"):
          backspace_count = backspace_count + 1
        holdTime = row.release_time - row.press_time
        holdTimeAll.append(holdTime)

        if idx == 0:
          start_time = row.press_time

        if idx == len_group - 1:
          finish_time = row.release_time

        if idx > 0:
            prev_row = group.iloc[idx - 1]
            keyStrokeLatency = row.press_time - prev_row.press_time
            keyStrokeLatencyAll.append(keyStrokeLatency)

        if idx > 0:
            prev_row = group.iloc[idx - 1]
            digraphDuration = row.press_time - prev_row.release_time
            digraphDurationAll.append(digraphDuration)

        if idx > 0:
            prev_row = group.iloc[idx - 1]
            interReleaseLatency = row.release_time - prev_row.release_time
            interReleaseLatencyAll.append(interReleaseLatency)

    typingSpeed = (finish_time - start_time)/(len_group)

    if len(holdTimeAll) > 0:
        avgHoldTime = sum(holdTimeAll) / len(holdTimeAll)
        maxHoldTime = max(holdTimeAll)
        minHoldTime = min(holdTimeAll)

    if len(keyStrokeLatencyAll) > 0:
        avgKeyStrokeLatency = sum(keyStrokeLatencyAll) / len(keyStrokeLatencyAll)
        maxKeyStrokeLatency = max(keyStrokeLatencyAll)
        minKeyStrokeLatency = min(keyStrokeLatencyAll)

    if len(digraphDurationAll) > 0:
        avgDiGraphDuration = sum(digraphDurationAll) / len(digraphDurationAll)
        maxDiGraphDuration = max(digraphDurationAll)
        minDiGraphDuration = min(digraphDurationAll)

    if len(interReleaseLatencyAll) > 0:
        avgInterReleaseLatency = sum(interReleaseLatencyAll) / len(interReleaseLatencyAll)
        maxInterReleaseLatency = max(interReleaseLatencyAll)
        minInterReleaseLatency = min(interReleaseLatencyAll)

    # print(f"Start Time: {start_time}, Finish Time: {finish_time}")
    # print(f"Length of group: {len_group}")
    # print(f"Deno : ", {len_group})
    # print(f"NUmer : ", {finish_time - start_time})
    # print(f"Participant ID: {participant_id}")
    # print(f"Typing Speed: {typingSpeed}")
    # print(f"Avg Keystroke Latency: {avgKeyStrokeLatency}")
    # print(f"Avg Digraph Duration: {avgDiGraphDuration}")
    # print(f"Avg Hold Time: {avgHoldTime}")
    # print(f"Avg Inter-Release Latency: {avgInterReleaseLatency}")
    # print(f"Max Keystroke Latency: {maxKeyStrokeLatency}")
    # print(f"Max Digraph Duration: {maxDiGraphDuration}")
    # print(f"Max Hold Time: {maxHoldTime}")
    # print(f"Max Inter-Release Latency: {maxInterReleaseLatency}")
    # print(f"Min Keystroke Latency: {minKeyStrokeLatency}")
    # print(f"Min Digraph Duration: {minDiGraphDuration}")
    # print(f"Min Hold Time: {minHoldTime}")
    # print(f"Min Inter-Release Latency: {minInterReleaseLatency}")
    # print(f"No of backspaces pressed : {backspace_count}")

    humans_data.append({
        "Typing Speed" : typingSpeed,
        "No of backspaces" : backspace_count,
        "Avg Hold Time" : avgHoldTime,
        "Avg Keystroke Latency" : avgKeyStrokeLatency,
        "Avg Digraph Duration" : avgDiGraphDuration,
        "Avg Inter-Release Latency" : avgInterReleaseLatency,
        "Max Hold Time" : maxHoldTime,
        "Max Keystroke Latency" : maxKeyStrokeLatency,
        "Max Digraph Duration" : maxDiGraphDuration,
        "Max Inter-Release Latency" : maxInterReleaseLatency,
        "Min Hold Time" : minHoldTime,
        "Min Keystroke Latency" : minKeyStrokeLatency,
        "Min Digraph Duration" : minDiGraphDuration,
        "Min Inter-Release Latency" : minInterReleaseLatency,
        "output_label" : 1
    })


humans_data_df = pd.DataFrame(humans_data, ignore_index=True)
print(humans_data_df.head())
print("Size of humans_data is : ",len(humans_data_df))