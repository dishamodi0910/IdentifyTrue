import threading
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from pathlib import Path

FOLDER_PATHS = [ 
                    "/home/dishamodi0910/DEV/true-identify/Keystroke_0/keystroke_0_0",
                    "/home/dishamodi0910/DEV/true-identify/Keystroke_0/keystroke_0_1",
               ];

def generateDataSet(folderPath, result_list):
    folder_data = []
    folder = Path(folderPath)
    for file_path in folder.iterdir():
        if file_path.is_file():
            print(file_path)
            print("Processing file...")
            with open(file_path, encoding='ISO-8859-1', errors='ignore') as file_content:
                for line in file_content:
                    #print(f"Raw line: {repr(line)}")  
                    matches = line.split("\t")
                    print(line)
                    if(matches[0] and matches[1] and matches[-2] and matches[-3] and matches[-4]):
                        # print(matches[0])
                        # print(matches[1])
                        # print(matches[-2])
                        # print(matches[-3])
                        # print(matches[-4])
                        # print(matches)  
                        folder_data.append({"participant_id" : matches[0], "test_section_id" : matches[1], "key_used" : matches[-2], "press_time" : matches[-4], "release_time" : matches[-3]})
        else:
            print(file_path)
            print("Not a file, hence skipping")
    result_list.append(folder_data)


def processAllFilesInFolder(folders):
    threads = []
    result_list = []

    for folder in folders:
        thread = threading.Thread(target=generateDataSet, args=(folder, result_list))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_data = [item for sublist in result_list for item in sublist]
    df = pd.DataFrame(all_data)
    return df


df = processAllFilesInFolder(FOLDER_PATHS)
print(df.head())