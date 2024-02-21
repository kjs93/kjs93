import requests
from selenium import webdriver

driver=webdriver.Chrome()

response=requests.get('https://news.naver.com')
print(response.text)
print(response.status_code)