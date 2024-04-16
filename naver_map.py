import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumConfig():
    driver = webdriver.Chrome()

    def Selenium_Close(self):
        self.driver.quit()
    
    def driver_find_element(self, by, element):
        return self.driver.find_element(by, element)

    def driver_find_element_click(self, by, element):
        return self.driver.find_element(by, element).click()
    
    def driver_send_text(self, by, element, contents):
        element = self.driver_find_element(by, element)
        element.send_keys(contents)
        
    
if __name__=='__main__':
    test=SeleniumConfig()
    test.driver.get('https://map.naver.com/p?c=15.00,0,0,0,dh')
    test.driver_find_element_click(By.CSS_SELECTOR, '#header > nav > ul > li.sc-13bg05j.jmKA-Dw > button')
    time.sleep(3)
    depart_send_keys= '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/input'
    arrive_send_keys= '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/input'
    test.driver_send_text(By.XPATH, depart_send_keys,'청량리역')
    time.sleep(3)
    test.driver_find_element_click(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[1]/ul/li[2]/div')
    time.sleep(3)
    test.driver_send_text(By.XPATH, arrive_send_keys, '남부터미널')
    time.sleep(3)
    test.driver_find_element_click(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/ul/li[2]/div')
    time.sleep(3)
    test.driver_find_element_click(By.XPATH, '//*[@id="section_content"]/div/div[1]/div[2]/button[2]')
    time.sleep(5)
    time_taken= '//*[@id="tab_pubtrans_directions"]/ul/li[1]/div/div/div/em/span[1]'
    print(f" 소요시간 : {test.driver_find_element(By.XPATH, time_taken).get_attribute('innerText')} 분")