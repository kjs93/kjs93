#1. CGV가 아닌 다른 웹 페이지를 대상으로 자동화 테스트 시나리오를 작성하기.
#2. 자동화 테스트 시나리오를 원하는 도구를 이용해 엑셀 등 파일에 TC화 하기.
#3. TC를 Selenium으로 자동화 하기.
#4. 작성한 시나리오와 TC파일, 자동화 코드 파일을 과제 진행 시 어려웠던 점과 함께 작성하여 제출하기.
import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By # 웹엘리먼트 찾아주는 기능

#현재시간 구하기
now = time.strftime('%Y_%m_%d_%Hh_%Mm')

#성공한 TC ID 넣는 리스트
result_pass_list = []
#실패한 TC ID 넣는 리스트
result_fail_list = []
#실패한 이유를 가지고 있는 리스트
fail_reason_list = []
#전체 TC 개수
tc_count = 6

if not os.path.exists('test_240119_result'):
    os.makedirs('test_240119_result')

f = open(f'test_240119_result/{now}_test_result.txt', 'w')
f.write(f'테스트 수행 일자 - {now}\n')

driver=None
try:
    driver=webdriver.Chrome()
    driver.get('https://www.skt-phone.co.kr/')
    driver.implicitly_wait(10)
    error_log=driver.get_log('browser')
    print(error_log)
    
#TC1 T전화 홈페이지 
    tc_id='tc_01'
    t_url=driver.current_url
    if t_url=='https://www.skt-phone.co.kr/':
        print('P:T홈페이지 접속 성공')
        result_pass_list.append(tc_id)
    else:
        print('F:T홈페이지 접속 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('T홈페이지 접속 실패')

#TC2 안심통화 센터 페이지 이동 
    tc_id='tc_02'
    driver.find_element(By.CSS_SELECTOR,'body > div.wrap > div.header > div > ul > li:nth-child(1) > a').click()
    t_ansim=driver.current_url
    if t_ansim=='https://www.skt-phone.co.kr/safecall/safecallInfo.do':
        print('P:안심통화센터 이동')
        result_pass_list.append(tc_id)
    else:
        print('F:안심통화센터 이동 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('안심통화센터 이동 실패')
    driver.implicitly_wait(10)
    time.sleep(1)

#TC3 T전화 홈 복귀 확인
    tc_id='tc_03'
    driver.find_element(By.CSS_SELECTOR,'body > div.wrap > div.header > div > h1 > a').click()
    t_home=driver.current_url
    if t_home=='https://www.skt-phone.co.kr/':
        print('P:T전화 홈 이동')
        result_pass_list.append(tc_id)
    else:
        print('F:T전화 홈이동 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('T전화 홈이동 실패')    
    driver.implicitly_wait(10)
    time.sleep(5)

#TC4 T전화 도움말 페이지 이동 확인
    tc_id='tc_04'
    pyautogui.click(221,804)
    pyautogui.scroll(-100000)
    pyautogui.click(221,804)
    driver.implicitly_wait(10)
    t_help=driver.current_url
    if t_help=='https://www.skt-phone.co.kr/faq/list.do':
        print('P:도움말 페이지 이동 성공')
        result_pass_list.append(tc_id)
    else:
        print('F:도움말 페이지 이동 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('도움말 페이지 이동 실패')
    driver.implicitly_wait(10)
    time.sleep(1)

#TC5 비효한 도움말 검색
    tc_id='tc_05'
    pyautogui.click(682,766)
    pyautogui.typewrite('##abcd^^&가나다')
    driver.find_element(By.CSS_SELECTOR,'#faq_Anchor > div.top > div.search-type00 > button:nth-child(2)').click()
    time.sleep(5)
    besearch=driver.find_element(By.CSS_SELECTOR,'#faq_Anchor > div.bottom > div.selectView.view0 > ul > li')
    origin_text='검색된 도움말이 없습니다'
    if besearch.text==origin_text:
        print('P:비유효한 도움말 검색 성공')
        result_pass_list.append(tc_id)
    else:
        print('F:비유효한 도움말 검색 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('비유효한 도움말 검색 실패')
    time.sleep(3)

#TC6 유효한 도움말 검색
    tc_id='tc_06'
    pyautogui.click(682,766)
    pyautogui.typewrite('전화')
    driver.find_element(By.CSS_SELECTOR,'#faq_Anchor > div.top > div.search-type00 > button:nth-child(2)').click()
    search=driver.find_element(By.CSS_SELECTOR,'#faq_Anchor > div.bottom > div.selectView.view0 > p')
    test='검색결과에 대한 도움말 N개'
    if search.text==test:
        print('P:유효한 도움말 검색 성공')
        result_pass_list.append(tc_id)
    else:
        print('F:유효한 도움말 검색 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append(tc_id)
except Exception as e:
    print(f'웹 에러 발생 : {e}')
finally:
    if driver:
        driver.quit()
#PASS 결과 기록
f.write('\n[RESULT_PASS]\n')
for pass_cnt in range(len(result_pass_list)):
    f.write(f'{result_pass_list[pass_cnt]} : PASS\n')

#FAIL 결과 기록
f.write('\n[RESULT_FAIL]\n')
for fail_cnt in range(len(result_fail_list)):
    f.write(f'{result_fail_list[fail_cnt]} : FAIL\n')

#테스트 결과 요약
f.write('\n[테스트 결과 요약]\n')
f.write(f'PASS TC COUNT:{len(result_pass_list)}\n')
f.write(f'FAIL TC COUNT:{len(result_fail_list)}\n')
f.write(f'COMPLETE TEST COUNT:{len(result_pass_list)} + {len(result_fail_list)}\n')
f.write(f'PROGRESS OF TEST:{((len(result_pass_list) + len(result_fail_list))/tc_count)*100}\n')
f.write(f'PASS RATE:{(len(result_pass_list)/tc_count)*100}\n')
f.close()
