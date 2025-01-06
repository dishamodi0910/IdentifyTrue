from pathlib import Path

parent_dir = Path('/path/to/your/folder')

def findSubFolders(folder_path):
    subfolder_list = []
    parent_dir = Path(folder_path)
    subfolders = [f for f in parent_dir.iterdir() if f.is_dir()]
    print("Subfolders:")
    for subfolder in subfolders:
        subfolder_list.append(str(subfolder))
        
    print(subfolder_list)
    return subfolder_list