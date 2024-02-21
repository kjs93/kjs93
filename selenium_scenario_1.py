import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#현재시간 구하기
now=time.strftime('%Y_%m_%d_%Hh_%Mm')
# 성공한 TC
result_pass_list=[]
# 실패한 TC
result_fail_list=[]
# 실패한 이유를 가지고 있는 TC
fail_reason_list=[]
# 전체 TC 개수
tc_count=3

if not os.path.exists('test_result'):
    os.makedirs('test_result')

f=open(f'test_result/{now}_test_result.txt','w')
f.write(f'테스트 수행 일자 - {now}\n')

#TC_001 CGV 홈페이지 접속
tc_id='TC_001'
driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)

cgv_url = driver.current_url
if cgv_url == 'https://www.cgv.co.kr/':
    print('cgv 접속 성공.')
    result_pass_list.append(tc_id)
else:
    print(cgv_url)
    print('cgv 접속 실패.')
    result_fail_list.append(tc_id)
    fail_reason_list.append('cgv 접속 실패.')

#TC_002 비유효한 영화 이름 검색
tc_id='TC_002'
elem = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
elem.click()
elem.send_keys('28tu9w8g')

driver.find_element(By.CSS_SELECTOR, '#btn_header_search').click()
driver.implicitly_wait(10)

elem = driver.find_element(By.CSS_SELECTOR, '#search_result')
origin_text = '\'28tu9w8g\' 검색결과가 없습니다.'
if origin_text == elem.text:
    print('비유효한 영화 이름 검색 성공.')
    result_pass_list.append(tc_id)
else:
    print('비유효한 영화 이름 검색 실패.')
    result_fail_list.append(tc_id)
    fail_reason_list.append('비유효한 영화 이름 검색 실패')

#TC_003 홈페이지로 되돌아가기
tc_id='TC_003'
driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > h1 > a > img').click()
driver.implicitly_wait(10)
elem = driver.find_element(By.CSS_SELECTOR, '#contaniner > div.noticeClient_wrap > div > div.noticeClient_container > div.qr_wrap > div > img')
if elem.is_displayed():
    print('홈페이지 이동 성공.')
    result_pass_list.append(tc_id)
else:
    print('홈페이지 이동 실패.')
    result_fail_list.append(tc_id)
    fail_reason_list.append('홈페이지 이동 실패.')

#PASS 테스트 결과 기록
f.write('\n[RESULT - PASS]\n')
for pass_cnt in range(len(result_pass_list)):
    f.write(f'{result_pass_list[pass_cnt]}:PASS\n')

#FAIL 테스트 결과 기록
f.write('\n[RESULT - FAIL]\n')
for fail_cnt in range(len(result_fail_list)):
    f.write(f'{result_fail_list[fail_cnt]}:FAIL\n')
    f.write(f'\t{fail_reason_list[fail_cnt]}\n')

# 테스트 결과 요약
f.write('\n[테스트 결과 요약]\n')
f.write(f'PASS TC COUNT:{len(result_pass_list)}\n')
f.write(f'FAIL TC COUNT:{len(result_fail_list)}\n')
f.write(f'COMPLETED TEST COUNT:{len(result_pass_list)+len(result_fail_list)/tc_count*100}%\n')
f.write(f'PASS RATE:{(len(result_pass_list)/tc_count)*100}\n')
f.close()
