import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager


flask_app_url = "http://127.0.0.1:5000/login";
credentials = [
    {"username" : "user1", "password" : "pass1"},
    {"username" : "user2", "password" : "pass2"},
    {"username" : "user3", "password" : "pass3"},
    {"username" : "user4", "password" : "pass4"}
]

# options = Options()
# options.add_argument("--headless")  
# options.binary_location = "chromedriver-linux64/chromedriver"
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# print(f"Driver is : {driver}")

#Binary Location needed.

for cred in credentials:
    print(f"Current cred is : {cred}")
    try:
        driver.get(flask_app_url)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = driver.find_element(By.NAME, "password")

        username_field.clear()
        username_field.send_keys(cred["username"])
        password_field.clear()
        password_field.send_keys(cred["password"])

        login_button = driver.find_element(By.NAME, "loginBtn")
        login_button.click()

    except Exception as e:
        print(f"Exception occurred : {e}")
        raise e
    
driver.quit()
