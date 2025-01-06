import os
import shutil
import re

SOURCE_DIR = '/home/dishamodi0910/DEV/true-identify/Keystroke_5'

def get_folder_name(file_number):
    start_range = (file_number // 1000) * 1000  
    end_range = start_range + 1000
    return f"keystroke_5_{file_number//1000}"

def organize_files():
    for file_name in os.listdir(SOURCE_DIR):
        if file_name.endswith('_keystrokes.txt'):
            match = re.match(r'(\d+)_keystrokes\.txt', file_name)
            if match:
                file_number = int(match.group(1))
                folder_name = get_folder_name(file_number)
                
                folder_path = os.path.join(SOURCE_DIR, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                file_path = os.path.join(SOURCE_DIR, file_name)
                new_file_path = os.path.join(folder_path, file_name)
                shutil.move(file_path, new_file_path)
                print(f"Moved: {file_name} to {folder_name}")

organize_files()
