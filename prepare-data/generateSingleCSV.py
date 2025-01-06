import pandas as pd
import os

CSV_DIRECTORY = '/home/dishamodi0910/DEV/true-identify/keystroke_dataset_processed';
CSV_FILES_PATHS = [
    "/home/dishamodi0910/DEV/true-identify/keystroke_1.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_2.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_3.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_4.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_dataset_processed/keystroke_5.csv",
]


def mergeCSVs():
    dfs = []
    for filename in CSV_FILES_PATHS:
        if filename.endswith('.csv'):
            # file_path = os.path.join(CSV_DIRECTORY, filename)
            df = pd.read_csv(filename)
            dfs.append(df)


    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv('/home/dishamodi0910/DEV/true-identify/keystroke_data.csv', index=False)

mergeCSVs()