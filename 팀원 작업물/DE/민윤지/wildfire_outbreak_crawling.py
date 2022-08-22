import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://openapi.forest.go.kr/openapi/service/forestDisasterService/frstFireOpenAPI?searchStDt=19000101&searchEdDt=20220101&ServiceKey=u0ML%2FzNCCB6MjYef2RKPwxGc9GUx%2BHweFSTbyNdoni1uS6ZMaLhDEALrihhdRaAGt%2Bfql3P%2FsWKN4%2FlLP%2FeKCQ%3D%3D"
numOfRows="&numOfRows=100000"

#항목 parsing 함수작성하기
def parse():
    try:
        OCURDT = item.find("ocurdt").get_text()
        OCURYOIL = item.find("ocuryoil").get_text()
        EXTINGDT = item.find("extingdt").get_text()
        EXTINGTM = item.find("exintgtm").get_text()
        OCURGM = item.find("ocurgm").get_text()
        OCURDO = item.find("ocurdo").get_text()
        OCURSGG = item.find("ocursgg").get_text()
        OCUREMD = item.find("ocuremd").get_text()
        OCURRI = item.find("ocurri").get_text()
        OCURJIBUN = item.find("ocurjibun").get_text()
        OWNERSEC = item.find("ownersec").get_text()
        OCURCAUSE = item.find("ocurcause").get_text()
        DMGAREA = item.find("dmgarea").get_text()
        DMGMONEY = item.find("dmgmoney").get_text()
        RISKAVG = item.find("riskavg").get_text()
        RISKMAX = item.find("riskmax").get_text()
        TEMPAVG = item.find("tempavg").get_text()
        HUMIDCURR = item.find("humidcurr").get_text()
        HUMIDREL = item.find("humidrel").get_text()
        HUMIDMIN = item.find("humidmin").get_text()
        WINDMAX = item.find("windmax").get_text()
        WINDAVG = item.find("windavg").get_text()
        DIRMAX = item.find("dirmax").get_text()
        DIRAVG = item.find("diravg").get_text()
        RAINDAYS = item.find("raindays").get_text()
        RAINAMOUNT = item.find("rainamount").get_text()
        return {
            "발생일시":OCURDT,
            "발생일시(요일)":OCURYOIL,
            "진화일시(년월일시분)":EXTINGDT,
            "진화소요시간(분)":EXTINGTM,
            "발생장소(관서)":OCURGM,
            "발생장소(시도)":OCURDO,
            "발생장소(시군구)":OCURSGG,
            "발생장소(읍면동)":OCUREMD,
            "발생장소(리)":OCURRI,
            "발생장소(지번)":OCURJIBUN,
            "소유구분":OWNERSEC,
            "발생세부원인":OCURCAUSE,
            "피해면적":DMGAREA,
            "피해액":DMGMONEY,
            "산불위험지수(평균)":RISKAVG,
            "산불위험지수(최대)":RISKMAX,
            "평균기온":TEMPAVG,
            "실효습도":HUMIDCURR,
            "상대습도":HUMIDREL,
            "최소습도":HUMIDMIN,
            "최대풍속":WINDMAX,
            "평균풍속":WINDAVG,
            "최대풍향":DIRMAX,
            "평균풍향":DIRAVG,
            "강우결과일수":RAINDAYS,
            "최종강우량":RAINAMOUNT
        }
    except AttributeError as e:
        return {
            "발생일시":None,
            "발생일시(요일)":None,
            "진화일시(년월일시분)":None,
            "진화소요시간(분)":None,
            "발생장소(관서)":None,
            "발생장소(시도)":None,
            "발생장소(시군구)":None,
            "발생장소(읍면동)":None,
            "발생장소(리)":None,
            "발생장소(지번)":None,
            "소유구분":None,
            "발생세부원인":None,
            "피해면적":None,
            "피해액":None,
            "산불위험지수(평균)":None,
            "산불위험지수(최대)":None,
            "평균기온":None,
            "실효습도":None,
            "상대습도":None,
            "최소습도":None,
            "최대풍속":None,
            "평균풍속":None,
            "최대풍향":None,
            "평균풍향":None,
            "강우결과일수":None,
            "최종강우량":None
        }
 
#parsing 하기
result = requests.get(url+numOfRows)
soup = BeautifulSoup(result.text,'lxml-xml')
items = soup.find_all("item")
 
row = []
for item in items:
    row.append(parse())
 
#pandas 데이터프레임에 넣기
df = pd.DataFrame(row)
df.head()


#csv 파일로 저장하기
data = df.to_csv('wildfire_outbreak_19841201-20140619.csv', mode='w')
