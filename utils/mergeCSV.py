import numpy as np
import pandas as pd
def mergeCSVs():
    bot_data = pd.read_csv("keystroke_dataset/keystroke_data_processed_bot.csv")
    human_data = pd.read_csv("keystroke_dataset/keystroke_data_processed_human.csv")
    combined_data = pd.concat([bot_data, human_data])
    combined_data = combined_data.drop("_id", axis=1)
    combined_data.to_csv("keystroke_processed_data.csv", index=False)

mergeCSVs()