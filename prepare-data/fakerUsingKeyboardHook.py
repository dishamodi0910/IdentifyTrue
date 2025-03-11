import time
import pandas as pd
from pynput import keyboard
import random

keypress_data = []
collection = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

def generate_random_text():
    return ''.join(random.choice(collection) for _ in range(random.randint(5, 10)))

def on_key_press(key):
    try:
        press_time = time.time() * 1000
        key_char = key.char if hasattr(key, 'char') else str(key)
        keypress_data.append({
            'key_used': key_char,
            'press_time': press_time,
            'release_time': None
        })
    except AttributeError:
        pass

def on_key_release(key):
    release_time = time.time() * 1000
    key_char = key.char if hasattr(key, 'char') else str(key)
    for entry in keypress_data:
        if entry['key_used'] == key_char and entry['release_time'] is None:
            entry['release_time'] = release_time
            break

def simulate_typing(username, password):
    full_text = username + " " + password
    controller = keyboard.Controller()
    
    for char in full_text:
        controller.type(char)
        time.sleep(random.uniform(0.5, 1))

def process_group(group):
    group.dropna(inplace=True)
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


all_fake_data = []

def fake_data_using_pynput():
    for _ in range(100):
        username = generate_random_text()
        password = generate_random_text()

        global keypress_data
        keypress_data = []

        with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
            simulate_typing(username, password) 
            listener.stop()

        df = pd.DataFrame(keypress_data).dropna()
        if not df.empty:
            function_result = process_group(df)
            all_fake_data.append(function_result)

fake_data_using_pynput()
df = pd.DataFrame(all_fake_data)
df.to_csv("keystroke-data-pynput-5.csv", index=False)