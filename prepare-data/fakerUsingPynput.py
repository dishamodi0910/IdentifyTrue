import time
import pandas as pd
from pynput.keyboard import Controller
import random


keyboard = Controller()
keypress_data = []
collection = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

def generateRandomText():
    lengthCollection = len(collection)
    lenUserName = random.randint(5,10)
    username = ""
    for i in range(0,lenUserName):
        username = username + (collection[random.randint(0,lengthCollection-1)])
    return username



def simulate_typing(username, password):
    full_text = username + " " + password
    start_time = time.time()
    
    for char in full_text:
        press_time = (time.time() - start_time) * 1000  #Converted to MS
        keyboard.press(char)
        keyboard.release(char)
        release_time = (time.time() - start_time) * 1000    #Converted to MS
        
        keypress_data.append({
            'key_used': char,
            'press_time': press_time,
            'release_time': release_time
        })

        time.sleep(random.uniform(0.5,1.0))


def process_group(group):
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
        "Typing Speed": float(typing_speed),
        "No of Backspaces": int(backspace_count),
        "Avg Hold Time": float(avg_hold_time),
        "Max Hold Time": float(max_hold_time),
        "Min Hold Time": float(min_hold_time),
        "Avg Keystroke Latency": float(avg_keystroke_latency),
        "Max Keystroke Latency": float(max_keystroke_latency),
        "Min Keystroke Latency": float(min_keystroke_latency),
        "Avg Digraph Duration": float(avg_digraph_duration),
        "Max Digraph Duration": float(max_digraph_duration),
        "Min Digraph Duration": float(min_digraph_duration),
        "Avg Inter-Release Latency": float(avg_inter_release_latency),
        "Max Inter-Release Latency": float(max_inter_release_latency),
        "Min Inter-Release Latency": float(min_inter_release_latency),
        "output_label": 0  
    }

allFakeData = []
def fakeDataUsingPynput():
    for i in range(500):
        username = generateRandomText()
        password = generateRandomText()
        simulate_typing(username,password)
        df = pd.DataFrame(keypress_data)
        functionResult = process_group(df)
        allFakeData.append(functionResult)

fakeDataUsingPynput()
df = pd.DataFrame(allFakeData)
df.to_csv("keystroke-data-pynput-bot-4.csv", index=False)