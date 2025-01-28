from pymongo import MongoClient
from dotenv import dotenv_values

def blackListUA(userAgentStr):
    config = dotenv_values(".env")
    client = MongoClient(config.get("MONGO_URI"))
    db = client["botdetection"]
    maliciousUA = db["malicious-ua"]

    last_doc = maliciousUA.find_one(sort=[("_id", -1)])

    if last_doc:
        current_key = list(last_doc.keys())[-1] 
        key_prefix, current_number = current_key.split("_")
        current_number = int(current_number)
    else:
        current_key = "bad_UA_0"
        current_number = 0

    if last_doc and len(last_doc.get(current_key, [])) < 1000:
        maliciousUA.update_one(
            {"_id": last_doc["_id"]},
            {"$push": {current_key: userAgentStr}}
        )
        print(f"User agent '{userAgentStr}' added to '{current_key}'.")
    else:
        new_key = f"{key_prefix}_{current_number + 1}"
        maliciousUA.insert_one({new_key: [userAgentStr]})
        print(f"User agent '{userAgentStr}' added to new document with key '{new_key}'.")
