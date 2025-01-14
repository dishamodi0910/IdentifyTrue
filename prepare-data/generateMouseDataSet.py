from utils.generateFolderList import findSubFolders
from pathlib import Path
import matplotlib.pyplot as plt
import uuid
import os
import matplotlib

FOLDER_PATH_MOUSE_RAW_DATASET = "/home/dishamodi0910/DEV/true-identify/mouse_dataset_raw";
def generateGraph(coordinatesX, coordinatesY, isHuman):
    matplotlib.use('Agg')
    plt.plot(coordinatesX, coordinatesY, marker='o', label='Linear Growth')

    if not os.path.exists("mouse_dataset"):
        os.makedirs("mouse_dataset")
    generated_uuid = uuid.uuid4()
    if isHuman == 1:
        file_name = f"mouse_dataset/human/human_{generated_uuid}.png"
    else:
        file_name = f"mouse_dataset/bot/bot_{generated_uuid}.png"

    plt.savefig(file_name)
    plt.close()  

    print(f"Graph saved as: {file_name}")



def folderPathContainsHumanOrBot(folderPath):
    if(folderPath.find("bot")!=-1):
        return 0;
    else:
        return 1;



def processSubFolder(folderPath):
    isHuman = folderPathContainsHumanOrBot(folderPath)
    coordinatesX = []
    coordinatesY = []
    resolutionX = 0
    resolutionY = 0
    folder = Path(folderPath)
    for file in folder.iterdir():
        print(file)
        print("File processed")
        if file.is_file():
            with open(file, encoding='ISO-8859-1', errors='ignore') as file_content:
                
                for line in file_content:  
                    values = line.split(",")
                    resolutionX = values[-2].split(":")[-1]
                    resolutionY = values[-1]
                    break
                
                for line in file_content:
                    coordinates = line.split(",")
                    coordinatesX.append((float(coordinates[-2]))*1.0/float(resolutionX))
                    coordinatesY.append((float(coordinates[-1]))*1.0/float(resolutionY))

        
            # print(coordinatesX)
            # print(coordinatesY)
            print("Processed file : ", file)
            generateGraph(coordinatesX, coordinatesY, isHuman)


def generateMouseDataset():
    subFolderList = findSubFolders(FOLDER_PATH_MOUSE_RAW_DATASET)
    for folderName in subFolderList:
        print(folderName)
        processSubFolder(folderName)
    pass


generateMouseDataset()
