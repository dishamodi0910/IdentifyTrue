from asyncio import sleep
import asyncio
import os
from flask import Flask, Response, request, render_template
from pynput import mouse
from pynput.mouse import Controller
from threading import Thread
import matplotlib.pyplot as plt
import matplotlib


X = []
Y = []
def generate_separate_lists(mouse_readings):
    list1, list2 = zip(*mouse_readings)
    global X,Y
    print(len(list1))
    print(len(list2))
    X = list(list1)
    Y = list(list2)

def generate_graph(mouse_readings):
    generate_separate_lists(mouse_readings)
    print(len(X))
    print(len(Y))
    matplotlib.use('Agg') 
    plt.plot(X, Y, marker='o', linestyle='-', color='b')
    plt.xlabel('X-Axis (X)')
    plt.ylabel('Y-Axis (Y)')
    plt.title('Plot of Coordinates')
    plt.savefig('fig.png')



stop_tracking = False
mouse_readings = []


def track_behaviour(mouse):
    global stop_tracking, mouse_readings
    while not stop_tracking:
        mouse_readings.append(mouse.position)


def create_app(test_config=None):
    app = Flask(__name__)

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
        mouse = Controller()

        tracking_thread = Thread(target=track_behaviour, args=(mouse,))
        tracking_thread.daemon = True  
        tracking_thread.start()

        print("We are here");
        return render_template('login.html');

    @app.route('/home', methods=['POST'])
    def form_submitted():
        stop_tracking = True
        username = request.form.get('username');
        password = request.form.get('password');
        typingData = request.form.get('typingData');
        keypressData = request.form.get('keypressData');
        backSpaceCount = request.form.get('backSpaceCount');
        hiddenFieldUsed = request.form.get('hiddenFieldUsed');

        print(f'MouseReadingsList Size: {len(mouse_readings)}');
        generate_graph(mouse_readings)
        print(f'Username : {username}');
        print(f'Password : {password}');
        print(f'typingData : {typingData}');
        print(f'keypressData : {keypressData}');
        print(f'FOrm Data : {request.form}');
        print(f'backSpaceCount : {backSpaceCount}');
        print(f'hiddenFieldUsed : {hiddenFieldUsed}');
        return 'Tracking stopped.'

    return app

