
## 📌 Overview

We know that Bots can perform harmful activities such as fake signups, credential stuffing, content scraping, and denial-of-service attacks, leading to data breaches, system overload, and loss of user
trust. 
Detecting such advanced, human-like bots remains a persistent and complex challenge for web platforms.
CAPTCHAs were introduced to solve this issue, but with AI advancements, systems were capable of cracking CAPTCHAs. 

Hence, there was a strong need for an adaptive, behavior-based detection system that differentiates
bots from humans based on real-time user interaction patterns.

--- 

## 📌 Goal
To develop an intelligent, behavior-based bot detection system that accurately distinguishes between human and automated interactions.

---

## 📌 Technical Aspects
The system implements a multi-modal behavioral analysis pipeline to distinguish between human users and bots using real-time behavioral data:
- Keystroke Dynamics: Analyzes typing patterns, including key hold time, latency, and flight time.
- Mouse Trajectories: Captures cursor movement paths, velocity, acceleration, and click frequency to identify human-like vs bot-like behavior.

**1. Machine Learning Models**
- Decision Tree Classifier is used for classifying user behavior based on keystroke dynamics.
- Convolutional Neural Network (Pretrained & Custom) is trained on mouse trajectory heatmaps for bot detection.
- Joblib and scikit-learn are used for training and saving ML models.
- Keras Tuner is utilized for hyperparameter optimization in deep learning pipelines.

**2. Web Integration with Flask**
- A full-stack Flask web application handles user interactions, feature capture, and bot classification.
- Includes REST endpoints for submitting behavioral data and receiving predictions.
- Uses Flask-PyMongo for seamless integration with MongoDB.

**3. Database & Storage**
- MongoDB stores user behavioral data, prediction results, and logs for analysis.
- Implements user sessions, IP tracking, and result caching via Python-based middleware.

**4. Data Processing & Visualization**
- Uses pandas, numpy, and dask for efficient data manipulation.
- Matplotlib, Seaborn, and tqdm are used for creating performance and behavior graphs.
- Torchvision aids in image transformation for CNN input.

---


## 📌 Tech Stacks
-  Python
-  Flask
-  PyTorch
-  MongoDB 

---


## 📌 Dataset Information
 - Keystroke Dynamics Dataset: <a href="https://huggingface.co/datasets/dishamodi/Keystroke_Processed">Custom Generated Dataset</a>
 - Mouse Trajectories Dataset: <a href="https://huggingface.co/datasets/dishamodi/Keystroke_Processed">Custom Generated Dataset</a>

---

## 📌 Snapshots

![image](https://github.com/user-attachments/assets/ee5cfadc-9be3-4684-9a4b-7352ce50f8d9)

![image](https://github.com/user-attachments/assets/4168bb53-467d-486b-b03a-0b3beeb4c589)

![image](https://github.com/user-attachments/assets/4768b425-35bc-4b4d-a942-01b77b116412)

![image](https://github.com/user-attachments/assets/6e14c420-e23c-4237-8964-8a12aed98535)

![image](https://github.com/user-attachments/assets/db5bde0f-b82f-4e71-9790-03642dfcbf42)

---


## 📌 Demo Video



https://github.com/user-attachments/assets/c22f67bb-087f-49af-ba1e-b696ea9d1945



---
