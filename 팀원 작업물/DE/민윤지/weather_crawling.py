import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#항목 parsing 함수작성하기
def parse():
    try:
        TM = item.find("tm").get_text()
        STNIDS = item.find("stnIds").get_text()
        STNNM = item.find("stnNm").get_text()
        WS = item.find("ws").get_text()
        HM = item.find("hm").get_text()
        TA = item.find("ta").get_text()
        RN = item.find("rn").get_text()
        WD = item.find("wd").get_text()
        return {
            "시간":TM,
            "지점번호":STNIDS,
            "지점명":STNNM,
            "기온":TA,
            "강수량":RN,
            "풍속":WS,
            "풍향":WD,
            "습도":HM
        }
    except AttributeError as e:
        return {
            "시간":None,
            "지점번호":None,
            "지점명":None,
            "기온":None,
            "강수량":None,
            "풍속":None,
            "풍향":None,
            "습도":None
        }


#parsing 하기
url="http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList?serviceKey=u0ML%2FzNCCB6MjYef2RKPwxGc9GUx%2BHweFSTbyNdoni1uS6ZMaLhDEALrihhdRaAGt%2Bfql3P%2FsWKN4%2FlLP%2FeKCQ%3D%3D&numOfRows=999&pageNo=1&dataCd=ASOS&dateCd=HR&stnIds=90&endDt=20000131&endHh=01&startHh=01&startDt=20000101"
result = requests.get(url)
soup = BeautifulSoup(result.text,'lxml-xml')
items = soup.find_all("item")
