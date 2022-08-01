from kafka import KafkaProducer
import requests
import pandas as pd
import time
import datetime
import pytz  
import json

# 브로커 생성시에는 브로커의 호스트들의 리스트를 준비한다.
# 한개만 알아도 상관없지만 모든 브로커들의 리스트를 입력하는것을 권장
BROKER_SERVER = ["localhost:2121"]
TOPIC_NAME = "climate_topic"

# 프로듀스 생성
producer = KafkaProducer(bootstrap_servers=BROKER_SERVER)

csv_datas = []
json_datas = []

def climate(local,start,start_time,end,end_time):
    API_KEY = "CJg6YBp/KNrl7YueJ48EwyvDpgka/lL0pUeuRvW84Aw+bDjTm0W1HVZSbhxk6mE4kU+jgLex72Up7mofH9hMUQ=="
    URL = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'

    params = {
      'serviceKey' : API_KEY,
      'pageNo' : '1', 
      'numOfRows' : '900', 
      'dataType' : 'json',
      'dataCd' : 'ASOS', 
      'dateCd' : 'HR',
      'startDt' : start, 
      'startHh' : start_time, 
      'endDt' : end, 
      'endHh' : end_time, 
      'stnIds' : local
    }

    response = requests.get(URL, params=params)
    datas = response.json()

    for a in datas['response']['body']['items']['item']:
        stnnm = a['stnNm']  # 지점명
        tm = a['tm']  # 일시
        ws = a['ws']  # 풍속
        wd = a['wd']  # 풍향
        hm = a['hm']  # 습도
        ta = a['ta']  # 기온

        # [[],[]] 형태로 저장
        csv_data = [tm, stnnm, local, ta, ws, wd, hm]
        csv_datas.append(csv_data)

        # json 형태로 저장 -> MySQL, kafka
        global json_data

        json_data = {
        'tm' : tm,
        'stnNm' : stnnm,
        'stnId': local,
        'ta' : ta,
        'ws' : ws,
        'wd' : wd,
        'hm' : hm
        }
        
        json_datas.append(json_data)

    return json_data

# 관측지점 뽑아오기
climate_point_df = pd.read_csv('data/climate_point.csv')
climate_point = list(climate_point_df['지점번호'])


# 현재 날짜 - 1일
def get_seoul_date():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    kst_now = utc_now.astimezone(pytz.timezone("Asia/Seoul")) + datetime.timedelta(days = -1)
    d = kst_now.strftime("%Y%m%d")  # 현재날짜 -1 (전날)
    # t = kst_now.strftime("%H:%M:%S")
    
    return d


date = get_seoul_date()

for a in climate_point:
    climate(a, date, '00', date, '23' )
    

# # 데이터 발생 및 스트리밍
# while True:
#     date = get_seoul_date()
#     # datas = ten(date)

#     # for b in datas:
#     #     tm = b[0]
#     #     stnnm = b[1]
#     #     local = b[2]
#     #     ta = b[3]
#     #     ws = b[4]

#     for a in climate_point:
#         tm, stnnm, local, ta, ws, wd, hm = climate(a, date, '01', date, '01' )


# 브로커에게 토픽에 맞는 데이터를 전송
producer.send(TOPIC_NAME, json.dumps(json_datas).encode("utf-8"))


# 버퍼 스트림 제거(안해도 상관없는데 권장함.)
producer.flush()