import pandas as pd

CSV_FILES_PATHS = [
    "/home/dishamodi0910/DEV/true-identify/keystroke_1.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_2.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_3.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_4.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_dataset_processed/keystroke_5.csv",
]

OUTPUT_FILE = "/home/dishamodi0910/DEV/true-identify/keystroke_data.csv"


def mergeCSVs_in_chunks():
    chunk_size = 10**6 

    with open(OUTPUT_FILE, 'w') as output_file:
        for idx, filename in enumerate(CSV_FILES_PATHS):
            chunk_iter = pd.read_csv(filename, chunksize=chunk_size)

            for chunk in chunk_iter:
                if idx == 0:  
                    chunk.to_csv(output_file, index=False, header=True)
                else:
                    chunk.to_csv(output_file, index=False, header=False)

mergeCSVs_in_chunks()