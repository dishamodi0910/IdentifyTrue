import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import multiprocessing
import time

CSV_FILE_PATH = "data/dummyBotUsernamePass.csv";
FLASK_APP_URL = "http://127.0.0.1:5000/login";
BATCH_SIZE = 1000



def process_batch(batch):
    driver = webdriver.Firefox()
    for _,row in batch.iterrows():
        username, password = row["username"], row["password"]
        try:
            driver.get(FLASK_APP_URL)
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = driver.find_element(By.NAME, "password")

            username_field.clear()  
            username_field.send_keys(username)
            password_field.clear()
            password_field.send_keys(password)

            login_button = driver.find_element(By.NAME, "loginBtn")
            login_button.click()

        except Exception as e:
            print(f"Exception occurred : {e}")
            raise e
    driver.quit()

def processCSV():
    credentials = pd.read_csv(CSV_FILE_PATH)
    # processes = []

    # for chunk in credentials:
    #     process = multiprocessing.Process(target=process_batch, args=(chunk,))
    #     processes.append(process)
    #     process.start()
    
    # for process in processes:
    #     process.join()
    process_batch(credentials)

processCSV()
