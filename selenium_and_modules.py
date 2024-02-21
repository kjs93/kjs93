# 내용 유지할 것
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://comento.kr/?index"
latest_version = requests.get(
    "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
).text
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version=latest_version).install())
)
driver.set_window_position(-200, 1080)
driver.maximize_window()

driver.get(url)
driver.implicitly_wait(10)

console_error = driver.get_log("browser")
response = requests.get(url, verify=False)

if len(console_error) >= 1:
    for a in range(len(console_error)):
        print(
            "CONSOLE_ERROR : "
            + console_error[a]["level"]
            + " >>> "
            + console_error[a]["message"]
            + "\n"
            "NETWORK_STATUS : " + str(response.status_code) + "\n"
        )
