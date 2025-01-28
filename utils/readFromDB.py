from dotenv import dotenv_values
from pymongo import MongoClient


maliciousIPList = []
maliciousReferrerList = []
maliciousUAList = []

def readFromDB():
    config = dotenv_values(".env")
    client = MongoClient(config.get("MONGO_URI"))
    db = client["botdetection"]
    maliciousIP = db["malicious-information"]
    maliciousReferrer = db["malicious-referrer"]
    maliciousUA = db["malicious-ua"]
    for document in maliciousIP.find():
        for key, value in document.items():
            if key.startswith("bad_ip_"):
                maliciousIPList.append(value)
    
    for document in maliciousReferrer.find():
        for key, value in document.items():
            if key.startswith("bad_referrer_"):
                maliciousReferrerList.append(value)


    for document in maliciousUA.find():
        for key, value in document.items():
            if key.startswith("bad_UA_"):
                maliciousUAList.append(value)


    return {
        "badIP" : maliciousIPList,
        "badReferrer" : maliciousReferrerList,
        "badUA" : maliciousUAList
    }
