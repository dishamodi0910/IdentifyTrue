import pandas as pd
import random

collection = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

username_password = []

def generateBotUserNamePassword():
    for i in range(0,10):
        lengthCollection = len(collection)
        lenUserName = random.randint(1,10)
        lenPassword = random.randint(1,10)
        username = ""
        password = ""
        for i in range(0,lenUserName):
            username = username + (collection[random.randint(0,lengthCollection-1)])
        for i in range(0,lenPassword):
            password = password + (collection[random.randint(0,lengthCollection-1)])
        username_password.append({"username" : username, "password" : password});
    print("Username_Password List is : ",username_password)
    data = pd.DataFrame(username_password)
    data.to_csv("data/dummyBotUsernamePass.csv",index=False)
    
generateBotUserNamePassword()

