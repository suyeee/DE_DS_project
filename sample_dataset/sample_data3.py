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

# 강원도 선택
driver.find_element(By.XPATH, '//*[@id="ztree_26_switch"]').click()
time.sleep(2)

# 강릉, 동해, 속초, 태백 체크박스 선택
driver.find_element(By.XPATH, '//*[@id="ztree_27_check"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_29_check"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_33_check"]').click()
driver.find_element(By.XPATH, '//*[@id="ztree_40_check"]').click()
time.sleep(2)

# 선택완료 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="sidetreecontrol"]/a').click()
time.sleep(2)

# # 날짜 선택
# driver.find_element(By.XPATH, '//*[@id="startDt"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="datepicker_year"]/option[114]').click() # 2013년
# driver.find_element(By.XPATH, '//*[@id="datepicker_month"]/option[1]').click() # 1월 선택
# driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[3]/a').click() # 1일 선택

# # 검색 버튼 클릭
# driver.find_element(By.XPATH, '//*[@id="schForm"]/div[2]/button').click()
# time.sleep(2)

# 검색결과 크롤링 함수
datas = []

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

def crawling(soup):
        
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
    date = driver.find_element(By.XPATH, '//*[@id="startDt"]').click()
    date.send_keys(Keys.CONTROL + "a")
    date.send_keys(Keys.DELETE)
    time.sleep(2)
    print('delete ok') #오류 확인
    
    date.send_keys(day)
    print('send date ok') #오류 확인
        
    # 검색 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="schForm"]/div[2]/button').click()
    time.sleep(2)
    
for day in range(20130101,20130103):
    try:
        next_date(driver,day)
        crawling(driver)
        time.sleep(3)
        print(datas)
    except:
        # # 시작일이 올바르지 않을경우
        # driver.find_element(By.CSS_SELECTOR, '.buttonOK').click()
        # time.sleep(2)
        print('error!')
        pass
        # # 다시 날짜 입력
        # next_date(driver,day+1)
        
# 드라이버 종료
driver.quit()        
