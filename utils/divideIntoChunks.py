from dotenv import dotenv_values
from pymongo import MongoClient

bad_UA = ["list"]
def divideIntoChunks():
    dict = {}
    listVal = []
    dictKeyName = ""
    for i in range(len(bad_UA)):
        if i%1000 == 0:
            dict[dictKeyName] = listVal
            listVal = []
            value = i//1000
            dictKeyName = "bad_UA_" + str(value)
            listVal.append(bad_UA[i])
        else:
            listVal.append(bad_UA[i])
    dict[dictKeyName] = listVal
    return dict

dict = divideIntoChunks()
dict.pop("")
print(dict)
config = dotenv_values(".env")
client = MongoClient(config.get("MONGO_URI"))

db = client["botdetection"]
collection = db["malicious-ua"]

for key, value in dict.items():
    # print(f"Key: {key}, Value: {value}")
    collection.insert_one({key : value})

