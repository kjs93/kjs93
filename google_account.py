import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By  # 웹엘리먼트 찾아주는 기능
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 구글 접속하기
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr")
driver.set_window_size(1920, 1080)

# 로그인 화면 진입
login_id_btn = "#gb > div > div.gb_Ud > a"
driver.find_element(By.CSS_SELECTOR, login_id_btn).click()
time.sleep(1)

# 계정만들기 화면으로 이동하기
make_id_btn = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span'
driver.find_element(By.XPATH, make_id_btn).click()
personal_btn = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[2]'
driver.find_element(By.XPATH, personal_btn).click()
time.sleep(1)

# 이름 입력하는 화면
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys("김")
driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys("준수")
time.sleep(3)

# 다음 버튼이 클릭 가능할 때까지 기다린 후 클릭
next_btn_locator = '//*[@id="collectNameNext"]/div/button'
next_btn_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_btn_locator)))
next_btn_element.click()
time.sleep(3)

# 생년월일 입력하는 화면
driver.find_element(By.CSS_SELECTOR,'#year').send_keys('1993')
driver.find_element(By.CSS_SELECTOR,'#month').click()
option_5_btn='#month > option:nth-child(6)'
driver.find_element(By.CSS_SELECTOR, option_5_btn).click()
driver.find_element(By.CSS_SELECTOR,'#day').send_keys('27')
driver.find_element(By.CSS_SELECTOR,'#gender').click()
option_male_btn='#gender > option:nth-child(3)'
driver.find_element(By.CSS_SELECTOR, option_male_btn).click()
time.sleep(3)
# 다음 버튼이 클릭 가능할 때까지 기다린 후 클릭
next_btn2_locater='//*[@id="birthdaygenderNext"]/div/button'
next_btn2_element=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_btn2_locater)))
next_btn2_element.click()
time.sleep(5)

# 첫번째 이메일 라디오 버튼 클릭 후 비밀번호 입력하는 화면으로 넘어가기 (입력필드가 나올땐 어떻게 해야할까)
radio_btn='#yDmH0d > c-wiz > div.aDGQwe > div.eKnrVb > div > div.j663ec > div > form > span > section > div > div > div.IhH7Wd.hdGwMb.V9RXW > div.ci67pc > div > span > div:nth-child(1) > div > div.enBDyd > div'
driver.find_element(By.CSS_SELECTOR, radio_btn).click()
next_btn3_locater='//*[@id="next"]/div/button'
next_btn3_element=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_btn3_locater)))
next_btn3_element.click()
time.sleep(5)

# 비밀번호 입력하는 화면
password_field='#passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
driver.find_element(By.CSS_SELECTOR, password_field).send_keys('wsws13579')
password_verify='#confirm-passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
driver.find_element(By.CSS_SELECTOR, password_verify).send_keys('wsws13579')
next_btn4_locater='//*[@id="createpasswordNext"]/div/button'
next_btn4_element=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_btn4_locater)))
next_btn4_element.click()
time.sleep(5)
# '죄송합니다 계정을 만들수가 없습니다.' 오류 화면 노출

#복구 이메일 추가 화면에서 건너뛰기 버튼 클릭하기
pass_btn='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/button'
driver.find_element(By.XPATH, pass_btn).click()
time.sleep(5)





