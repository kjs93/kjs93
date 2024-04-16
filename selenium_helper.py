import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumConfig():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def close_driver(self):
        self.driver.quit()
    
    def find_element(self, by, element):
        return self.driver.find_element(by, element)

    def find_element_click(self, by, element):
        return self.driver.find_element(by, element).click()
    
    def send_text(self, by, element, contents):
        element = self.find_element(by, element)
        element.send_keys(contents)
    
    def navigate_and_search(self, departure, destination):
        self.driver.get('https://map.naver.com/p?c=15.00,0,0,0,dh')
        self.find_element_click(By.CSS_SELECTOR, '#header > nav > ul > li.sc-13bg05j.jmKA-Dw > button')
        time.sleep(3)
        depart_send_keys = '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/input'
        arrive_send_keys = '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/input'
        self.send_text(By.XPATH, depart_send_keys, departure)
        time.sleep(3)
        self.find_element_click(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[1]/ul/li[2]/div')
        time.sleep(3)
        self.send_text(By.XPATH, arrive_send_keys, destination)
        time.sleep(3)
        self.find_element_click(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/ul/li[2]/div')
        time.sleep(3)
        self.find_element_click(By.XPATH, '//*[@id="section_content"]/div/div[1]/div[2]/button[2]')
        time.sleep(5)
        time_taken = '//*[@id="tab_pubtrans_directions"]/ul/li[1]/div/div/div/em/span[1]'
        print(f" 소요시간 : {self.find_element(By.XPATH, time_taken).get_attribute('innerText')} 분")