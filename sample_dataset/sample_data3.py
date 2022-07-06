from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import threading

def get_chrome_driver():
    
    chromedriver_autoinstaller.install(False)
    
    # 1. 크롬 옵션 세팅
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 시크릿모드로 접속
    chrome_options.add_argument("--no-sandbox")  # 대부분의 리소스에 대한 액세스 방지
    chrome_options.add_argument("--disable-setuid-sandbox")  # 크롬 드라이버에 setuid를 하지않음으로써 크롬의 충돌 방지
    chrome_options.add_argument('--disable-dev-shm-usage')  # 메모리 부족으로 인한 에러 방지
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 로그 숨기기

    # 2. driver 생성하기
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
   
    return driver

# 슬랙-웹훅으로 크롤링에 걸리는 시간 체크하기
def send_slack(text):
    import requests
    import json
    import datetime

    WEBHOOK_URL = "url"

    # 현재시간도 출력
    now = datetime.datetime.now()
    now = now.strftime("%Y/%m/%d, %H:%M:%S")
    
    # text와 현재시간을 같이 슬랙 메세지로 전송
    text = text + f', 시간: {now}'
    
    payload = {
        'username' : '크롤링봇',
        "text" : text
        }
    
    requests.post(WEBHOOK_URL, json.dumps(payload))
    
# 검색결과 크롤링 함수
def crawling(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml') 
       
    lst = soup.select('#resultData > tr')
    
    for a in lst:
        
        num = a.select('tr > td')[0].text
        name = a.select('tr > td')[1].text
        date = a.select('tr > td')[2].text
        he = a.select('tr > td')[3].text.strip()  # 실효습도
        
        data = [num, name, date, he]
        
        datas.append(data)
        
    print('for문 ok')  # 오류 확인
        
    return datas

# 다음일로 넘어가기
def next_date(driver,day):
    # 날짜 선택후 글자 다 지우기
    date = driver.find_element(By.XPATH, '//*[@id="startDt"]')
    # date.send_keys(Keys.CONTROL + "a")
    # date.send_keys(Keys.DELETE)
    date.clear()
    time.sleep(2)
    print('delete ok') #오류 확인
    
    date.send_keys(day)
    print('send date ok') #오류 확인
        
    # 검색 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="schForm"]/div[2]/button').click()
    time.sleep(2)
    
        
# 크롤링 시작
send_slack('크롤링 시작')

driver = get_chrome_driver()

# # 브라우저 창 한개 더 열기
# driver.execute_script('window.open("about:blank", "_blank");')

# # 브라우저 인덱스
# tabs = driver.window_handles

# # 첫번째 브라우저 -> 2013년 크롤링
# driver.switch_to.window(tabs[0])
driver.get('https://data.kma.go.kr/climate/ehum/selectEhumChart.do?pgmNo=110')

# 지점선택
driver.find_element(By.XPATH, '//*[@id="txtStnNm"]').click()
time.sleep(3)

# 전체 지점 다 선택
driver.find_element(By.XPATH, '//*[@id="ztree_1_check"]').click()
time.sleep(2)

# ASOS에 없는 지점들은 석택해제
# 116(관악산) 제외
driver.find_element(By.XPATH, '//*[@id="ztree_2_switch"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_3_check"]').click()  # 선택해제
time.sleep(2)

# 176(대구(기))
driver.find_element(By.XPATH, '//*[@id="ztree_7_switch"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_9_check"]').click()  # 선택해제
time.sleep(2)

# 214(삼척)
driver.find_element(By.XPATH, '//*[@id="ztree_26_switch"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_32_check"]').click()  # 선택해제
time.sleep(2)

# 전라남도 - 164(무안), 256(주암), 175(진도(첨찰산)) 제외
driver.find_element(By.XPATH, '//*[@id="ztree_66_switch"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_71_check"]').click()  # 164 선택해제
driver.find_element(By.XPATH, '//*[@id="ztree_78_check"]').click()  # 256 선택해제
driver.find_element(By.XPATH, '//*[@id="ztree_79_check"]').click()  # 175 선택해제
time.sleep(2)

# 제주도 - 187(성산), 265(성산포) 제외
driver.find_element(By.XPATH, '//*[@id="ztree_113_switch"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_117_check"]').click()  # 187 선택해제
driver.find_element(By.XPATH, '//*[@id="ztree_118_check"]').click()  # 265 선택해제
time.sleep(2)

# 선택완료 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="sidetreecontrol"]/a').click()
time.sleep(2)

# 데이터 수집    
datas = []
   
for day in range(20120201,20120502):
    
    if ((str(day)[-2:] < '32') & (str(day)[-2:] != '00')) & ((str(day)[4:6] < '13') & (str(day)[4:6] != '00')):
        try:
            next_date(driver,day)
            crawling(driver)
            time.sleep(3)
            print(day)
        except:
            try:
                # 시작일이 올바르지 않을경우
                driver.find_element(By.CSS_SELECTOR, '.buttonOK').click()
                time.sleep(2)    
            except:
                print('error!')
    else:
        pass    
        
# 드라이버 종료
driver.quit() 

send_slack('드라이버 종료')

# 저장
import pandas as pd

results_df = pd.DataFrame(datas)      
results_df.columns = ['지점', '지점명', '일시', '실효습도']
results_df.to_csv('실효습도_크롤링.csv', index=False) 

send_slack('결과 저장')