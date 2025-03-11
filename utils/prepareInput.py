import torch
import torchvision.transforms as transforms
import pandas as pd
from utils import yeoJohnsonTransform
from utils.logTransformData import logTransform

def prepare_keystroke_input(data): 
   features = [
        "Typing Speed", "No of Backspaces",
        "Avg Hold Time", "Max Hold Time", "Min Hold Time",
        "Avg Keystroke Latency", "Max Keystroke Latency", "Min Keystroke Latency",
        "Avg Digraph Duration", "Max Digraph Duration", "Min Digraph Duration",
        "Avg Inter-Release Latency", "Max Inter-Release Latency", "Min Inter-Release Latency"
    ]
   input_data = pd.DataFrame([data], columns=features)
   input_data = logTransform(input_data)
   input_data = yeoJohnsonTransform(input_data)

   return data


def prepare_mouse_analysis_input(image):
   transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
   
   input_tensor = transform(image).unsqueeze(0)   # Add batch dimension
   return input_tensor