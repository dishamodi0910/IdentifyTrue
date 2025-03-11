from asyncio import sleep
import asyncio
from flask import Flask, Response, request, render_template
from pynput import mouse
from pynput.mouse import Controller
from threading import Thread
import matplotlib.pyplot as plt
import matplotlib
from pymongo import MongoClient
from dotenv import dotenv_values
from flask_pymongo import PyMongo
import joblib
import sys
import os
from utils import blackListUA, processUA
from utils import readFromDB
from utils.prepareInput import prepare_keystroke_input, prepare_mouse_analysis_input
import pandas as pd
import numpy as np
import torch
from PIL import Image
from torchvision import models
from torchvision import transforms
import torch.nn as nn

utils_path = '/home/dishamodi0910/DEV/true-identify/utils'
sys.path.append(os.path.dirname(utils_path))

config = dotenv_values(".env")

keystroke_model = joblib.load("model/best_keystroke_model.joblib");

def findOutNumberOfSpacesInString(text):
    spaceCount = 0;
    for i in range(len(text)):
        if(text[i] == ' '):
            spaceCount = spaceCount + 1
    return spaceCount


#DEAL WITH MOUSE RELATED DATA
X = []
Y = []
def generate_separate_lists(mouse_readings):
    list1, list2 = zip(*mouse_readings)
    global X,Y
    #print(len(list1))
    #print(len(list2))
    X = list(list1)
    Y = list(list2)

def generate_graph(mouse_readings):
    generate_separate_lists(mouse_readings)
    #print(len(X))
    #print(len(Y))
    matplotlib.use('Agg') 
    plt.plot(X, Y, marker='o', linestyle='-', color='b')
    plt.xlabel('X-Axis (X)')
    plt.ylabel('Y-Axis (Y)')
    plt.title('Plot of Coordinates')
    plt.savefig('fig.png')


#DEAL WITH kEYSTROKE RELATED DATA
typingSpeed = 0
avgKeyStrokeLatency = 0
avgDiGraphDuration = 0
avgHoldTime = 0
avgInterReleaseLatency = 0
maxKeyStrokeLatency = 0
maxDiGraphDuration = 0
maxHoldTime = 0
maxInterReleaseLatency = 0
minKeyStrokeLatency = 0
minDiGraphDuration = 0
minHoldTime = 0
minInterReleaseLatency = 0

generate_keywise_times = []

def calculate_keystroke(events):
    global generate_keywise_times
    print("Generate keywise times : ", generate_keywise_times)
    for i in range(len(events)):
        event = events[i]
        if(event['type'] == 'Keydown'):
            for j in range(i+1, len(events)):
                if events[j]['key'] == event['key'] and events[j]['type'] == "Keyup" and events[j]['time'] > event['time']:
                    key = event['key']
                    key_press_time = event['time']
                    key_release_time = events[j]['time']
                    generate_keywise_times.append({"Key" : key, "keyPresssTime" : key_press_time, "keyReleaseTime" : key_release_time})
                    break
    print(f"The data generated : {generate_keywise_times}")

holdTimeAll = []
keyStrokeLatencyAll = []
digraphDurationAll = []
interReleaseLatencyAll = []
def generate_dynamics():
    global generate_keywise_times
    for i in range(len(generate_keywise_times)):
        characterWiseTime = generate_keywise_times[i]
        holdtime = characterWiseTime['keyReleaseTime'] - characterWiseTime['keyPresssTime']
        holdTimeAll.append(holdtime);
        if(i > 0):
            previous_char = generate_keywise_times[i-1]
            keystrokelatency = characterWiseTime['keyPresssTime'] - previous_char['keyPresssTime']
            keyStrokeLatencyAll.append(keystrokelatency)
            digraphduration = characterWiseTime['keyPresssTime'] - previous_char['keyReleaseTime']
            digraphDurationAll.append(digraphduration)
            intereleaselatency = characterWiseTime['keyReleaseTime'] - previous_char['keyReleaseTime']
            interReleaseLatencyAll.append(intereleaselatency)

    global holdTime, avgHoldTime, minHoldTime, maxHoldTime
    global keyStrokeLatency, avgKeyStrokeLatency, minKeyStrokeLatency, maxKeyStrokeLatency
    global digraphDuration, avgDiGraphDuration, minDiGraphDuration, maxDiGraphDuration
    global interReleaseLatency, avgInterReleaseLatency, minInterReleaseLatency, maxInterReleaseLatency

    if(holdTimeAll):
        avgHoldTime = sum(holdTimeAll)/len(holdTimeAll)
        minHoldTime = min(holdTimeAll)
        maxHoldTime = max(holdTimeAll)

    if(keyStrokeLatencyAll):
        avgKeyStrokeLatency = sum(keyStrokeLatencyAll)/len(keyStrokeLatencyAll)
        minKeyStrokeLatency = min(keyStrokeLatencyAll)
        maxKeyStrokeLatency = max(keyStrokeLatencyAll)

    if(digraphDurationAll):
        avgDiGraphDuration = sum(digraphDurationAll)/len(digraphDurationAll)
        minDiGraphDuration = min(digraphDurationAll)
        maxDiGraphDuration = max(digraphDurationAll)

    if(interReleaseLatencyAll):
        avgInterReleaseLatency = sum(interReleaseLatencyAll)/len(interReleaseLatencyAll)
        minInterReleaseLatency = min(interReleaseLatencyAll)
        maxInterReleaseLatency = max(interReleaseLatencyAll)

def calculateTypingSpeed(username, password):
    global generate_keywise_times
    global typingSpeed
    totalCharsTyped = 0
    #Typing Speed will be total time taken/Total characters written
    # spacesUsername = findOutNumberOfSpacesInString(username)
    # spacesPassword = findOutNumberOfSpacesInString(password)
    # if(spacesUsername > 0):
    #     wordsInUserName = len(username.split(' '))
    #     totalWordsTyped = totalWordsTyped + wordsInUserName + spacesUsername
    # else:
    #     totalWordsTyped = totalWordsTyped + 1


    # if(spacesPassword > 0):
    #     wordsInPassword = len(password.split(' '))
    #     totalWordsTyped = totalWordsTyped + wordsInPassword + spacesPassword
    # else:
    #     totalWordsTyped = totalWordsTyped + 1
    totalCharsTyped = len(username) + len(password);
    totalTimeTaken = (generate_keywise_times[len(generate_keywise_times) - 1]['keyReleaseTime'] - generate_keywise_times[0]['keyPresssTime'])*1.0;
    typingSpeed = (totalTimeTaken)/totalCharsTyped;
    return typingSpeed


stop_tracking = False
mouse_readings = []


def track_behaviour(mouse):
    global stop_tracking, mouse_readings
    while not stop_tracking:
        mouse_readings.append(mouse.position)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["MONGO_URI"] = config.get("MONGO_URI")
    print("Mongo URI is : ", config.get("MONGO_URI"))
    mongo = PyMongo(app)
    @app.route('/hello')
    def hello():
        return render_template('hello.html')

    @app.route('/login', methods=['GET'])
    def process_request():
        print("Method type : ",request.method);
        print("Referrer String : ",request.referrer);
        print("Headers info" ,dict(request.headers.items()));
        print("User Agent String",request.headers.get('User-Agent'))
        print("Remote Address",request.remote_addr);
        userAgentString = str(request.headers.get('User-Agent'))
        print(userAgentString)
        userAgentProcessed = processUA.processUserAgentString(userAgentString)

        dbCollectionValues = readFromDB.readFromDB()
        UAIdentifier = userAgentProcessed.get("parsedLegacyToken")


        maliciousReferrerList = dbCollectionValues.get("badReferrer")
        isMaliciousReferrer = request.referrer in maliciousReferrerList

        maliciousIPList = dbCollectionValues.get("badIP")
        isMaliciousIP = request.remote_addr in maliciousIPList

        maliciousUAList = dbCollectionValues.get("badUA")
        isMaliciousUA = UAIdentifier in maliciousUAList

        print("Is Malicious IP : ", isMaliciousIP)
        print("Is Malicious Referrer : ", isMaliciousReferrer)
        print("Is Malicious UA : ", isMaliciousUA)


        requestedPath = request.path
        print("Requested Path is : ", requestedPath)

        if(requestedPath.endswith("robots.txt")):
            blackListUA.blackListUA(UAIdentifier)
    
        mouse = Controller()

        tracking_thread = Thread(target=track_behaviour, args=(mouse,))
        tracking_thread.daemon = True  
        tracking_thread.start()

        return render_template('login.html');

    @app.route('/home', methods=['POST'])
    def form_submitted():
        stop_tracking = True
        data = request.get_json()
        username = data['username'];
        password = data['password'];
        typingData = data['typingData'];
        keypressData = data['keypressData'];
        backSpaceCount = data['backSpaceCount'];
        hiddenFieldUsed = data['hiddenFieldUsed'];
        # innerHeight = data['innerHeight']
        # outerHeight = data['outerHeight']
        # innerWidth  = data['innerWidth']
        # outerWidth = data['outerWidth']
        print(f'MouseReadingsList Size: {len(mouse_readings)}');

        generate_graph(mouse_readings)
        
        print(f'Username : {username}');
        print(f'Password : {password}');
        #print(f'typingData : {typingData}');
        print(f'keypressData : {keypressData}');
        
        generate_keywise_times = calculate_keystroke(keypressData);
        generate_dynamics()
        print(f"Hold time : {holdTimeAll}")
        print(f"Average Hold time : {avgHoldTime}")
        print(f"Max Hold time : {maxHoldTime}")
        print(f"Min Hold time : {minHoldTime}")
        print(f"KeyStroke Latencies : {keyStrokeLatencyAll}")
        print(f"Average Keystroke Latency: {avgKeyStrokeLatency} ms")
        print(f"Max Keystroke Latency: {maxKeyStrokeLatency} ms")
        print(f"Min Keystroke Latency: {minKeyStrokeLatency} ms")
        print(f"Digraph Duration{digraphDurationAll}")
        print(f"Average Digraph Duration: {avgDiGraphDuration} ms")
        print(f"Max Digraph Duration: {maxDiGraphDuration} ms")
        print(f"Min Digraph Duration: {minDiGraphDuration} ms")
        print(f"InterRelease Latency : {interReleaseLatencyAll}")
        print(f"Average Inter-Release Latency: {avgInterReleaseLatency} ms")
        print(f"Max Inter-Release Latency: {maxInterReleaseLatency} ms")
        print(f"Min Inter-Release Latency: {minInterReleaseLatency} ms")
        print(f'backSpaceCount : {backSpaceCount}');
        print(f'hiddenFieldUsed : {hiddenFieldUsed}');
        calculateTypingSpeed(username, password)
        print(f"Typing Speed is : {typingSpeed}");
        # print(f"OuterWidth : {outerWidth}")
        # print(f"InnerWidth : {innerWidth}")
        # print(f"OuterHeight : {outerHeight}")
        # print(f"InnerHeight : {innerHeight}")
          
        # keystroke_data = {
        #     "username": username,
        #     "password": password,
        #     "keypress_data": keypressData,
        #     "Typing Speed" : typingSpeed,
        #     "No of Backspaces" : backSpaceCount,
        #     "typing_metrics": {
        #         "hold_time": {
        #             "all": holdTimeAll,
        #             "average": avgHoldTime,
        #             "min": minHoldTime,
        #             "max": maxHoldTime,
        #         },
        #         "keystroke_latency": {
        #             "all": keyStrokeLatencyAll,
        #             "average": avgKeyStrokeLatency,
        #             "min": minKeyStrokeLatency,
        #             "max": maxKeyStrokeLatency,
        #         },
        #         "digraph_duration": {
        #             "all": digraphDurationAll,
        #             "average": avgDiGraphDuration,
        #             "min": minDiGraphDuration,
        #             "max": maxDiGraphDuration,
        #         },
        #         "inter_release_latency": {
        #             "all": interReleaseLatencyAll,
        #             "average": avgInterReleaseLatency,
        #             "min": minInterReleaseLatency,
        #             "max": maxInterReleaseLatency,
        #         },
        #     },
        #     "hidden_field_used": hiddenFieldUsed,
        #     "inner_dimensions": {"width": innerWidth, "height": innerHeight},
        #     "outer_dimensions": {"width": outerWidth, "height": outerHeight},
        # }


        keystroke_data = np.array([typingSpeed, backSpaceCount, avgHoldTime, maxHoldTime, minHoldTime, avgKeyStrokeLatency, maxKeyStrokeLatency, minKeyStrokeLatency, avgDiGraphDuration, maxDiGraphDuration, minDiGraphDuration, avgInterReleaseLatency, maxInterReleaseLatency, minInterReleaseLatency])
        
        # dimensions_honeypot_info = {
        #     "innerWidth"  :  innerWidth,
        #     "innerHeight" : innerHeight,
        #     "outerWidth" : outerWidth,
        #     "outerHeight" : outerHeight,
        #     "hidden_field_used" : hiddenFieldUsed,
        #     "output_label" : 0
        # }

        # try:
        #     mongo.db.keystrokedata.insert_one(keystroke_data)
            # mongo.db.keystrokes_bot.insert_one(keystrokes_data_small)
        #     mongo.db.dimensions_bot.insert_one(dimensions_honeypot_info)
        #     print("Keystroke data saved to MongoDB.")
        # except Exception as e:
        #     print(f"Error inserting into MongoDB: {e}")
        #     return "Error saving to db"

        request_response = -1
        mouse_analysis_response = -1
        keystroke_analysis_response = -1


        if (hiddenFieldUsed || isMaliciousIP || isMaliciousReferrer || isMaliciousUA)
        {
            request_response = 0
            mouse_analysis_response = 0
            keystroke_analysis_response = 0
        }
        else
        {
        
        }
        
        input_keystrokes_formatted = prepare_keystroke_input(keystroke_data)
        print("Input formatted strokes : ", input_keystrokes_formatted)
        input_keystrokes_formatted = input_keystrokes_formatted.reshape(1,-1);
        print("Input keystroke reshaped : ", input_keystrokes_formatted);
        predicted_keystroke_result = keystroke_model.predict(input_keystrokes_formatted)
         # print("Predicted Keystroke Result : ", predicted_keystroke_result)

        mouse_prediction_result = -1

        img_path = "fig.png"
        image = Image.open(img_path)
        image = image.convert("RGB")

        model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
        num_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(num_features, 2)  
        model.load_state_dict(torch.load('model\mouse_trajectory_model.pth', map_location=torch.device('cpu')))
        model.eval()  

        input_image = prepare_mouse_analysis_input(image)
        with torch.no_grad():
            output = model(input_image)
            _, predicted = torch.max(output, 1)

            predicted = predicted.numpy()
            mouse_prediction_result = predicted[0]
                # print("Mouse Prediction Result : ", mouse_prediction_result)

        result = {
            'mouse_prediction_result' : "Bot" if mouse_prediction_result == 1 else "Human",
            'keystroke_prediction_result' : "Bot" if predicted_keystroke_result == 0 else "Human"
        }
        print(result)
        return render_template('result.html', result=result)

    return app

