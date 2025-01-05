import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from pathlib import Path

FOLDER_PATH = "/home/dishamodi0910/DEV/true-identify/Keystrokes/files";
result = []
def generateDataSet(filepath):
    global result
    with open(filepath, encoding='ISO-8859-1', errors='ignore') as file_content:
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
                result.append({"participant_id" : matches[0], "test_section_id" : matches[1], "key_used" : matches[-2], "press_time" : matches[-4], "release_time" : matches[-3]})


def processAllFilesInFolder():
    folder = Path(FOLDER_PATH)
    for file_path in folder.iterdir():
        if file_path.is_file():
            print(file_path)
            print("Processing file...")
            generateDataSet(file_path)
        else:
            print(file_path)
            print("Not a file, hence skipping")

processAllFilesInFolder()